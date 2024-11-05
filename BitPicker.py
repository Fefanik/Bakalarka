def extract_specific_bit(byte, position):
    return (byte >> position) & 1


def check(byte_array):
    with open("SpecificBits.bin", 'rb') as f:
        load = f.read()
        for i in range(len(load)):
            if load[i] != byte_array[i]:
                print("NOT GOOD")


def extract_byte(new_bits, block, byte_index):
    for j in range(7, -1, -1):
        new_bits.append(extract_specific_bit(block[byte_index], j))


def read_file(file_path, block_size):
    new_bits = []
    with open(file_path, "rb") as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            new_bits.append(extract_specific_bit(block[3], 7))
    return new_bits


def create_bytearray(new_bits):
    number_of_added_bits = 0
    byte_array = bytearray()
    for bit in new_bits:
        if number_of_added_bits == 8 or len(byte_array) == 0:
            number_of_added_bits = 0
            byte_array.append(0)
        byte_array[-1] = (byte_array[-1] << 1) | bit
        number_of_added_bits += 1
    return byte_array


def main():
    file_path = "rand_numbers.bin"
    block_size = 4
    new_bits = read_file(file_path, block_size)
    byte_array = create_bytearray(new_bits)
    with open("4thByte7thBit.bin", 'wb') as f:
        f.write(byte_array)
    #check(byte_array)


if __name__ == "__main__":
    main()
