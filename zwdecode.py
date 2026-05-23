#!/usr/bin/env python3

import argparse


def extract_hidden_chars(file_path):
    """
    Read file and extract supported invisible Unicode characters.

    Supported:
    U+200B = Zero Width Space
    U+200C = Zero Width Non-Joiner
    """

    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    hidden = []

    for char in data:
        unicode_value = ord(char)

        if unicode_value in [0x200B, 0x200C]:
            hidden.append(char)

    return hidden


def decode_hidden(hidden_chars, zwsp_bit="0"):
    """
    Convert invisible characters into binary
    and decode into text.
    """

    bits = ""

    for char in hidden_chars:

        # ZWSP (U+200B)
        if ord(char) == 0x200B:
            bits += zwsp_bit

        # ZWNJ (U+200C)
        else:
            bits += "1" if zwsp_bit == "0" else "0"

    decoded_text = ""

    for i in range(0, len(bits), 8):

        byte = bits[i:i+8]

        if len(byte) == 8:
            try:
                decoded_text += chr(int(byte, 2))
            except:
                pass

    return bits, decoded_text


def main():

    parser = argparse.ArgumentParser(
        description="Zero-Width Unicode Steganography Decoder"
    )

    parser.add_argument(
        "file",
        help="Target text file"
    )

    args = parser.parse_args()

    print("\n===================================")
    print(" Zero-Width Steganography Decoder")
    print("===================================")

    hidden = extract_hidden_chars(args.file)

    print(f"\n[+] Hidden Unicode characters found: {len(hidden)}")

    if len(hidden) == 0:
        print("\n[-] No supported hidden Unicode characters detected")
        return

    bits1, decoded1 = decode_hidden(hidden, "0")

    print("\n--- Mapping 1 ---")
    print("ZWSP = 0")
    print("ZWNJ = 1\n")

    print("Decoded message:")
    print(decoded1)

    bits2, decoded2 = decode_hidden(hidden, "1")

    print("\n--- Mapping 2 ---")
    print("ZWSP = 1")
    print("ZWNJ = 0\n")

    print("Decoded message:")
    print(decoded2)

    print("\nDone.\n")


if __name__ == "__main__":
    main()