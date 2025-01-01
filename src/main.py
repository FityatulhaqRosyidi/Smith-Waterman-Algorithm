import numpy as np

def smithWaterman(sequence1, sequence2, match=2, mismatch=-1, gap=-1):
    m, n = len(sequence1), len(sequence2)

    # Step 1: Inisialisasi matriks skor
    H = np.zeros((m + 1, n + 1))
    maxScore = 0
    maxPosition = (0, 0)

    # Step 2: Pengisian matriks skor
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            matchScore = match if sequence1[i - 1] == sequence2[j - 1] else mismatch
            H[i, j] = max(
                0,
                H[i - 1, j - 1] + matchScore,
                H[i - 1, j] + gap,
                H[i, j - 1] + gap
            )
            if H[i, j] > maxScore:
                maxScore = H[i, j]
                maxPosition = (i, j)


    # Step 3: Traceback
    alignment1, alignment2 = "", ""
    i, j = maxPosition

    while H[i, j] > 0:
        if sequence1[i - 1] == sequence2[j - 1]:
            alignment1 = sequence1[i - 1] + alignment1
            alignment2 = sequence2[j - 1] + alignment2
            i -= 1
            j -= 1
        elif H[i, j] == H[i - 1, j] + gap:
            alignment1 = sequence1[i - 1] + alignment1
            alignment2 = "-" + alignment2
            i -= 1
        else:
            alignment1 = "-" + alignment1
            alignment2 = sequence2[j - 1] + alignment2
            j -= 1

    return alignment1, alignment2, maxScore


def main():

    print("\nContoh input -> DNA-sample-1/seq-10.txt")
    filename1 = input("masukkan path dan file sample 1: ")
    filename2 = input("masukkan path dan file sample 2: ")

    with open(f'../test/{filename1}', 'r') as file:
        seq1 =  file.readline().strip()

    with open(f'../test/{filename2}', 'r') as file:
        seq2 =  file.readline().strip()

    alignment1, alignment2, maxScore = smithWaterman(seq1, seq2)

    print(100*'-')
    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)
    print("\nAlignment 1:", alignment1)
    print("Alignment 2:", alignment2)
    print("\nMax Score:", maxScore)
    print(100*'-')


if __name__ == "__main__":
    main()
