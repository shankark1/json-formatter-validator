import json

def format_json():
    print("=== JSON Formatter & Validator ===")
    print("Paste your JSON below (press Enter twice to finish):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    json_text = "\n".join(lines)

    try:
        parsed = json.loads(json_text)

        print("\n Valid JSON!\n")
        print("Formatted JSON:\n")
        print(json.dumps(parsed, indent=4))

    except json.JSONDecodeError as e:
        print("\n Invalid JSON")
        print(f"Error: {e}")

if __name__ == "__main__":
    format_json()