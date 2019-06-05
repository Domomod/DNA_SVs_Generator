
from random import randint


def main():
    def inser(pos_from, pos_to, size):
        pass

    def trans(pos_start, pos_end, size):
        nonlocal full_read, offset_to_ref, vs_ref, vs_new
        dupli(pos_start, pos_end, size)
        dele(pos_start, size)

    def dele(pos, size):
        nonlocal full_read, offset_to_ref, vs_ref, vs_new
        del full_read[pos:(pos+size)]
        vs_ref.append(("deletion", pos + offset_to_ref, pos + offset_to_ref + size))
        vs_new.append(("deletion", pos, pos + size))
        offset_to_ref += size

    def inver(pos, size):
        nonlocal full_read, offset_to_ref, vs_ref, vs_new
        for i in range(int(size / 2) + 1):
            full_read[i + pos], full_read[pos+size - i] = full_read[pos+size - i], full_read[i + pos]
        vs_ref.append(("inversion", pos + offset_to_ref, pos + offset_to_ref + size))
        vs_new.append(("inversion", pos, pos + size))

    def dupli(pos_start, pos_end, size):
        nonlocal full_read, offset_to_ref, vs_ref, vs_new
        for i in range(size):
            full_read.insert(pos_end+i, full_read[pos_start+i])
        # vs_ref.append(("dupl", pos + offset_to_ref, pos + offset_to_ref + size)) # ??
        # vs_new.append(("dupl", pos, pos + size)) # ??

    def dupli_t(pos, size):
        nonlocal full_read, offset_to_ref, vs_ref, vs_new
        for i in range(size):
            full_read.insert(pos+size+i, full_read[pos+i])
        vs_ref.append(("tandem_dupl", pos + offset_to_ref, pos + offset_to_ref + size)) # ??
        vs_new.append(("tandem_dupl", pos, pos + size)) # ??


    chromosome_file_path = "S288C_ref/"
    chromosome_names = []
    for i in range(1, 2):
        chromosome_names.append("chr{:02d}.fsa".format(i))
        chromosome_names.append("chrmt.fsa".format(i))

    test_file = open("test", "w")

    for current_chromosome_name in chromosome_names:
        current_chromosome_name = "chr{:02d}.fsa".format(i)
        chromosome_file = open(chromosome_file_path.strip() + current_chromosome_name.strip(), "r")
        next(chromosome_file)   # skip header
        full_read = list(chromosome_file.read())
        full_read = list("QWERTYUIOPASDFGHJKLZXCVBNMQWER1234567890")

        # start processing
        offset_to_ref = 0
        vs_ref = []
        vs_new = []
        current_pos = 0
        print(''.join(full_read[0:40]))
        dele(current_pos, 10)

        current_pos += 10
        dele(current_pos, 10)
        print(''.join(full_read[0:20]))

        print("ref: \t", vs_ref)
        print("new: \t", vs_new)


if __name__ == '__main__':
    main()
