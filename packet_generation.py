def generate_packet(Calling_AE_title, Called_AE_Title, SOP_UID):
    packetheader = "01000000"
    length_of_pdu = "0000"
    protocol_version = "00010000"
    
    SOP_Class = "".join([hex(ord(j))[2:] for j in SOP_UID])
    null_bytes = "0000000000000000000000000000000000000000000000000000000000000000"
    App_Cont = "10000015312e322e3834302e31303030382e332e312e312e31"
    front = packetheader + length_of_pdu + protocol_version + Called_AE_Title + Calling_AE_title + null_bytes + App_Cont

    # Presentation Context(P=A+T)
    Item_type = "2000"
    padding_0 = "00"
    Context_ID = "0100"
    padding_1 = "ff00"

    # Abstract Syntax
    Abst_Item_Type = "3000"
    padding_2 = "00"
    sop_length = str(hex(int(len(SOP_Class) / 2)))
    Abstract_Syntax = Abst_Item_Type + padding_2 + sop_length[2:] + SOP_Class
    
    # Transfer Syntax
    Transfer_Syntax = "40000011312e322e3834302e31303030382e312e32"
    Item_length = str(hex(int(len(Abstract_Syntax) / 2) + int(len(Transfer_Syntax) / 2) + 4))[2:]

    Presentation_Context = Item_type + padding_0 + Item_length + Context_ID + padding_1

    byte = front + Presentation_Context + Abstract_Syntax + Transfer_Syntax
    Usr_Inf = "50000039510000040000400052000021312E322E3832362E302E312E333638303034332E31302E313531302E312E312E305500000844494D536365726E"
    byte += Usr_Inf

    length = byte_calc(byte)
    byte_list = list(byte)
    byte_list[11] = length[-1]
    byte_list[10] = length[-2]
    if length[-3] != 'x':
        byte_list[9] = length[-3]

    byte = listToString(byte_list)
    return byte_split_send(byte)

def byte_split_send(byte):
    data = []
    result = [byte[i:i + 2] for i in range(0, len(byte), 2)]
    for i in result:
        data.append(int(i, 16))
    return bytearray(data)

def byte_calc(byte):
    calc = len(byte) / 2
    return hex(int(calc) - 6)

def listToString(str_list):
    return "".join(str_list).strip()

def string_to_ascii_hex(string):
    return string.encode("utf-8").hex()
