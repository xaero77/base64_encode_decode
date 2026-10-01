#!/usr/bin/env python3

import argparse
import base64
from pathlib import Path


def encode_file(src: Path, dst: Path) -> None:
    data = src.read_bytes()
    encoded = base64.b64encode(data)
    dst.write_bytes(encoded)


def decode_file(src: Path, dst: Path) -> None:
    data = src.read_bytes()
    decoded = base64.b64decode(data)
    dst.write_bytes(decoded)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="파일을 Base64로 인코딩하거나 디코딩합니다."
    )

    parser.add_argument(
        "mode",
        choices=["encode", "decode"],
        help="encode 또는 decode",
    )

    parser.add_argument(
        "input",
        help="입력 파일",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="출력 파일. 생략하면 자동으로 파일명을 생성합니다.",
    )

    args = parser.parse_args()

    src = Path(args.input)

    if not src.is_file():
        raise FileNotFoundError(f"입력 파일을 찾을 수 없습니다: {src}")

    if args.output:
        dst = Path(args.output)

    elif args.mode == "encode":
        dst = src.with_name(src.name + ".b64")

    else:
        if src.suffix == ".b64":
            dst = src.with_suffix("")
        else:
            dst = src.with_name(src.name + ".decoded")

    if args.mode == "encode":
        encode_file(src, dst)
    else:
        decode_file(src, dst)

    print(f"{args.mode.upper()} 완료")
    print(f"입력 : {src}")
    print(f"출력 : {dst}")


if __name__ == "__main__":
    main()
