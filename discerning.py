def receive_data_with_length_field(sock, buffer_size=1024):
    header = sock.recv(6)
    if len(header) < 6:
        raise ValueError("Failed receive data")

    data_length = int.from_bytes(header[2:], byteorder='big')
    received_data = b''
    result = b''

    while len(received_data) < data_length:
        packet = sock.recv(min(buffer_size, data_length - len(received_data)))
        if not packet:
            break
        result += packet
        received_data = header + result

    return received_data

def process_response(recv_data, SOP_UID, success, fail, transfer, count, accept, output_file_op):
    hex_string = recv_data.hex()
    if hex_string[0] == '0' and hex_string[1] == '3':
        fail += 1
    elif hex_string[210] == '0' and hex_string[211] == '0':
        accept.append(SOP_UID)
        success += 1
        output_file_op.write(SOP_UID + '\n')
    else:
        fail += 1
    count += 1
    return success, fail, transfer, accept, count
