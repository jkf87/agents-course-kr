from translation import auto_translate

output_lang = "ko"

prompt = lambda content: f"""
You are a translator for the Korean translation team. Translate the text below from English to Korean while preserving the original Markdown/MDX structure.
- Keep code blocks intact and only translate comments within them.
- Do not translate inline code, URLs, or file paths.
- Use casual Korean pronouns like "여러분" when needed.

IMPORTANT: Only output the translated text without additional commentary. The input text is between '=== BEGIN OF TEXT ===' and '=== END OF TEXT ==='.

Please translate the following text to Korean:

=== BEGIN OF TEXT ===
{content}
=== END OF TEXT ===
""".strip()

def main() -> None:
    auto_translate(
        prompt=prompt,
        output_lang=output_lang,
    )


if __name__ == "__main__":
    main()

