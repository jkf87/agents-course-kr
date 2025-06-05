import argparse
import importlib
import os
import sys

# Ensure the scripts directory is on the path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)

from translation import auto_translate


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate all course MDX files.")
    parser.add_argument(
        "lang",
        default="ko",
        help="Target language code (e.g. ko, vi)",
    )
    parser.add_argument(
        "--input-dir",
        dest="input_dir",
        default=os.path.join(SCRIPT_DIR, "..", "units", "en"),
        help="Directory containing English MDX files",
    )
    args = parser.parse_args()

    lang_mod = importlib.import_module(args.lang)
    prompt = getattr(lang_mod, "prompt")

    auto_translate(prompt=prompt, output_lang=args.lang, inp_dir=args.input_dir)


if __name__ == "__main__":
    main()
