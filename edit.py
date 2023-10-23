import argparse

def main(input_file, output_file):
    lines = []
    with open(input_file, 'r') as infile:
        for line in infile:
            if "=" in line:
                _, right_part = line.split("=", 1)
                lines.append(right_part)
            else:
                lines.append(line)

    lines.sort()

    with open(output_file, 'w') as outfile:
        for line in lines:
            outfile.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort lines in a text file with respect to lines containing an '='.")
    parser.add_argument("input_file", help="Input text file")
    parser.add_argument("output_file", help="Output text file")

    args = parser.parse_args()
    main(args.input_file, args.output_file)

