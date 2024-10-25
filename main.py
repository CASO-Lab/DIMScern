import socket
import time
import argparse
import os
import configparser
import sys
import datetime
from packet_generation import generate_packet, byte_split_send, byte_calc, string_to_ascii_hex, listToString
from discerning import process_response, receive_data_with_length_field

def main():
    parser = argparse.ArgumentParser(description='help description')
    parser.add_argument('-c', '--config_file', required=True, help='essential configuration file')
    args = parser.parse_args()

    local_ip = '0.0.0.0'
    local_port = 7878
    target_ip = ''
    target_port = ''
    print()
    output_file = ""

    using_date = datetime.datetime.now()
    using_date_format = using_date.strftime("%Y-%m-%d %p %I:%M")
    print("Defined Targets : ")
    print()
    show_target('sop_target.cfg') 
    print()

    user_input = input("Please enter the target : ")
    print()

    try:
        ip, port, Called_AET, output_file = get_config_values(user_input)  
    except ValueError as e:
        print(e)
    print(ip)
    target_ip = ip
    target_port = int(port)

    section = "DEFAULT"
    input_file = get_config_default(section)  

    with open(input_file, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
        line_count = len(lines)

    output_folder_path = "Outputs"
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    output_file_path = os.path.join(output_folder_path, output_file)

    if os.path.exists(output_file_path) == True:
        os.remove(output_file_path)
    try:
        output_file_op = open(output_file_path, 'w', encoding='UTF-8')
    except FileNotFoundError:
        print("I think you enter the not defined target.")

    calling_input = input("enter the Calling AE title (Default : DIMScern) : ")
    start_time = time.perf_counter()

    if calling_input == "":
        user_input_calling = string_to_ascii_hex("DIMScern")
        user_input_calling += "20" * 8
    else:
        user_input_calling = string_to_ascii_hex(calling_input)
        if (len(user_input_calling) / 2) < 16:
            space_count = int(16 - (len(user_input_calling) / 2))
            user_input_calling += "20" * space_count
        else:
            print("Calling AE Title length must smaller than 16 bytes")
            sys.exit(1)

    Calling_AE_title = user_input_calling
    space_count = 0

    convert_Called_AET = string_to_ascii_hex(Called_AET)
    if (len(convert_Called_AET) / 2) < 16:
        space_count = int(16 - (len(convert_Called_AET) / 2))
        convert_Called_AET += "20" * space_count
    Called_AE_Title = convert_Called_AET

    num = 0
    success = 0
    fail = 0
    transfer = 0
    accept = []
    move_cursor_up = "\033[6A"
    move_cursor_up_end = "\033[3A"
    second = 0
    minute = 0
    hour = 0
    count = 0

    for i in lines:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        num += 1

        #Packet generation Module
        message = generate_packet(Calling_AE_title, Called_AE_Title, i)
        print("==============================================")
        print("<A-ASSOCIATE>")
        sock.send(message)
        print(f"[Request to Target] :\t packet send success[{num}]!")

		#Discerning Module
        recv_data = receive_data_with_length_field(sock)
        print(f"[Response from Target] : packet recv success[{num}]!")

        success, fail, transfer, accept, count = process_response(recv_data, i, success, fail, transfer, count, accept, output_file_op)
        
        time.sleep(1)
        print(f"supported : {success}\t||   Unsupported : {fail}\t ( {count} / {line_count} )")
        print("==============================================")

        second += 1
        if second == 60:
            minute += 1
            second = 0
        if minute == 60:
            hour += 1
            minute = 0

        print(move_cursor_up, end='')

    print("                                                                                   ")
    print("                                                                                   ")
    print("                                                                                   ")
    print("                                                                                   ")
    print("                                                                                   ")
    print("                                                                                   ")
    print("                                                                                   ")

    print("---------------------END-----------------------")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print_clock(elapsed_time)
    print(f"packet count : {num}")
    print(f"supported : {success}\t||   Unsupported : {fail}\t    ( {count} / {line_count} )")

    log_dir = "Logs"
    log_file_path = os.path.join(log_dir, "DIMScern_log.txt")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    with open(log_file_path, "a") as file:
        file.write(f"Start DIMScern Time : {using_date_format}\n")
        file.write(f"Target : {user_input}\n")
        file.write(f"Supported UID : {success}  ||  Unsupported UID : {fail}  ( {count} / {line_count} )\n")
        file.write("\n")

    output_file_op.close()
    sock.close()

def show_target(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    sections = config.sections()
    for section in sections:
        print(f"[{section}]")

def get_config_values(target):
    config = configparser.ConfigParser()
    config.read('sop_target.cfg')

    if target not in config:
        raise ValueError(f"'{target}' is not defined in 'sop_target.cfg'. Please define the target.")

    ip = config[target]['ip']
    port = config[target]['port']
    Called_AE_Title = config[target].get('Called_AE_Title', '')  

    if not Called_AE_Title:  
        Called_AE_Title = "DIMSESCP" 

    output_file = config[target]['output_file']

    return ip, port, Called_AE_Title, output_file


def get_config_default(section):
    config = configparser.ConfigParser()
    config.read('sop_target.cfg')

    if section not in config:
        raise ValueError(f"'{section}' is not defined in 'sop_target.cfg'. Please define the {section}.")

    input_file = config[section]['input_file']

    return input_file

def print_clock(elapsed_time):
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"Elapsed Time : {minutes}m {seconds}s")

if __name__ == "__main__":
    main()
