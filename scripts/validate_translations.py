from __future__ import annotations

from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
ENGLISH_ROOT = REPOSITORY_ROOT / "translations" / "en"
IGNORED_PARTS = {".git", ".github"}


def is_source_markdown(path: Path) -> bool:
    if path.suffix.lower() != ".md":
        return False
    relative_path = path.relative_to(REPOSITORY_ROOT)
    if "translations" in relative_path.parts:
        return False
    return not any(part in IGNORED_PARTS for part in relative_path.parts)


def has_language_switcher(content: str, expected_labels: tuple[str, str]) -> bool:
    return all(label in content for label in expected_labels)


def main() -> int:
    errors: list[str] = []

    source_files = sorted(path for path in REPOSITORY_ROOT.rglob("*.md") if is_source_markdown(path))
    english_files = sorted(path for path in ENGLISH_ROOT.rglob("*.md")) if ENGLISH_ROOT.exists() else []

    if not source_files:
        errors.append("No Portuguese source Markdown files were found outside translations/.")

    for source_file in source_files:
        relative_source = source_file.relative_to(REPOSITORY_ROOT)
        expected_english_file = ENGLISH_ROOT / relative_source

        if not expected_english_file.exists():
            errors.append(
                f"Missing English mirror for '{relative_source.as_posix()}'. Expected '{expected_english_file.relative_to(REPOSITORY_ROOT).as_posix()}'."
            )
            continue

        source_content = source_file.read_text(encoding="utf-8")
        english_content = expected_english_file.read_text(encoding="utf-8")

        if not has_language_switcher(source_content, ("English", "Português (Brasil)")):
            errors.append(
                f"Missing language switcher labels in Portuguese file '{relative_source.as_posix()}'."
            )

        if not has_language_switcher(english_content, ("English", "Português (Brasil)")):
            errors.append(
                f"Missing language switcher labels in English file '{expected_english_file.relative_to(REPOSITORY_ROOT).as_posix()}'."
            )

    for english_file in english_files:
        relative_english = english_file.relative_to(ENGLISH_ROOT)
        expected_source_file = REPOSITORY_ROOT / relative_english

        if not expected_source_file.exists():
            errors.append(
                f"English file without Portuguese source: '{english_file.relative_to(REPOSITORY_ROOT).as_posix()}'. Expected source '{relative_english.as_posix()}'."
            )

    if errors:
        print("Translation structure validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Translation structure validation passed.")
    print(f"Portuguese files checked: {len(source_files)}")
    print(f"English files checked: {len(english_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())