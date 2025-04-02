import yaml
import glob

import os

print("Current Directory:", os.getcwd())  # Print current working directory

# List all YAML files to merge
yaml_files = glob.glob("*.yaml")  # Adjust path if needed

print("Found YAML files:", yaml_files)

# Initialize empty data structure
merged_data = {"tables": {}}

# Load and merge YAML files
for file in yaml_files:
    with open(file, "r") as f:
        data = yaml.safe_load(f)
        if "tables" in data:
            merged_data["tables"].update(data["tables"])

# Generate DOT graph
dot_file = "merged_model.dot"
dot_lines = ["digraph DatabaseSchema {", "  rankdir=LR;", "  node [shape=record];"]

# Generate table nodes
for table, details in merged_data["tables"].items():
    fields = "\\l".join([f"{col}: {dtype}" for col, dtype in details["columns"].items()]) + "\\l"
    dot_lines.append(f'  {table} [label="{{{table}|{fields}}}"];')

# Generate relationships
for table, details in merged_data["tables"].items():
    if "relationships" in details:
        for col, ref in details["relationships"].items():
            ref_table, ref_col = ref.split(".")
            dot_lines.append(f'  {table} -> {ref_table} [label="{col}"];')

dot_lines.append("}")

# Save DOT file
with open(dot_file, "w") as f:
    f.write("\n".join(dot_lines))

print(f"DOT file generated: {dot_file}")