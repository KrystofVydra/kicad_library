import os

OLD = "${EASYEDA2KICAD}/easyeda2kicad.3dshapes/"
NEW = "${EASYEDA2KICAD}/easyeda2kicad.3dshapes/"

for filename in os.listdir("."):
    if not os.path.isfile(filename):
        continue

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        # Skip binary or non-text files
        continue

    modified = False
    new_lines = []

    for line in lines:
        if OLD in line:
            print(f"\nFile: {filename}")
            print("Original:", line.rstrip())
            replaced = line.replace(OLD, NEW)
            print("Modified:", replaced.rstrip())
            new_lines.append(replaced)
            modified = True
        else:
            new_lines.append(line)

    if modified:
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
