import os
import hcl2
import sys

missing_descriptions = []


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
                    if not v.get("description"):
                        missing_descriptions.append(
                            f"{block_type} '{k}' in {file_path}"
                        )


def process_tf_files(directory="."):
    for filename in os.listdir(directory):
        if filename.endswith(".tf"):
            file_path = os.path.join(directory, filename)
            parsed_hcl = parse_tf_file(file_path)
            check_descriptions(parsed_hcl, file_path)

    if missing_descriptions:
        print("Warning - Description missing in the following files:")
        for item in missing_descriptions:
            print(item)
        sys.exit(1)
    else:
        print("Done! All output and variable blocks have descriptions.")
        sys.exit(0)


if __name__ == "__main__":
    tf_path = sys.argv[1]
    print("\n\n Checking for missing descriptions in Terraform files...\n")
    process_tf_files(tf_path)
