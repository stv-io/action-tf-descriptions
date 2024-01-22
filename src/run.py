import os
import hcl2
import sys

missing_descriptions = []
duplicate_descriptions = []
descriptions_found = {}
descriptions_found["variable"] = []
descriptions_found["output"] = []


def parse_tf_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        parsed_hcl = hcl2.loads(content)
        return parsed_hcl


def check_descriptions(parsed_hcl, file_path):
    for block_type, blocks in parsed_hcl.items():
        for block in blocks:
            if block_type in ["output", "variable"]:
                for k, v in block.items():
                    print(f"Checking {block_type} '{k}' from {file_path}")
                    description = v.get("description")
                    if not description:
                        missing_descriptions.append(
                            {"type": block_type, "name": k, "file": file_path}
                        )
                    else:
                        descriptions_found[block_type].append(description)
    return descriptions_found, missing_descriptions


def validate_descriptions(descriptions_found, missing_descriptions):
    failing = False
    for block_type, descriptions in descriptions_found.items():
        unique_descriptions = set()
        duplicate_descriptions = set()

        for description in descriptions:
            if description in unique_descriptions:
                duplicate_descriptions.add(description)
            else:
                unique_descriptions.add(description)

        if duplicate_descriptions:
            print(f"Error - Duplicate descriptions found in {block_type} block:")
            for description in duplicate_descriptions:
                print(f"  - '{description}'")
            failing = True
    if missing_descriptions:
        print("Error - Missing descriptions:")
        for missing_description in missing_descriptions:
            print(
                f"  - Type: {missing_description['type']}, Name: {missing_description['name']}, File: {missing_description['file']}"
            )
        failing = True

    if not failing:
        print("Done! All output and variable blocks have unique descriptions.")
        sys.exit(0)
    else:
        sys.exit(1)


def process_tf_files(directory):
    descriptions_found = {}
    missing_descriptions = []
    for filename in os.listdir(directory):
        if filename.endswith(".tf"):
            file_path = os.path.join(directory, filename)
            parsed_hcl = parse_tf_file(file_path)
            descriptions_found, missing_descriptions = check_descriptions(
                parsed_hcl, file_path
            )
    validate_descriptions(descriptions_found, missing_descriptions)


if __name__ == "__main__":
    tf_path = sys.argv[1]
    print(
        f"\nChecking for missing and duplicate descriptions in Terraform files in '{tf_path}' ..\n"
    )
    process_tf_files(tf_path)
