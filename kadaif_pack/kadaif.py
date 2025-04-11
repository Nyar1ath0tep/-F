#!/usr/bin/env python3
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from kadaif_pack.kadaie_1 import kadaie_1


def main():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="課題F用の提出用関数",
    )
    parser.add_argument(
        "-i",
        "--input1",
        type=str,
        help="pdbファイルのパス",
        required=True,
    )
    parser.add_argument(
        "-l",
        "--input2",
        type=int,
        help="残基数の上限",
        required=True,
    )
    args = parser.parse_args()
    kadaie_1(args.input1, args.input2)


if __name__ == "__main__":
    main()
