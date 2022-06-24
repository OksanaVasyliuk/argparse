import argparse

parser = argparse.ArgumentParser(description='argparse greeting')
parser.add_argument('-n', '--name', help='a name to repeat', required=True)
parser.add_argument("input_file", default=None, help=("Input file to read"))
parser.add_argument("output_file", default=None, help=("Output file to read"))

args = parser.parse_args()

def other_letter(string):
    string = string.replace("a", "@")
    return string

def task_encoding(input_file, output_file, name):
    task_file = open(input_file, encoding='utf-8')
    line1 = []
    for line in task_file:
        line1.append('Who are you? '+"\n"+name+"\n"+other_letter(line)+"\n")
    task_file.close()

    line2=line1[0]
    line3=line1[1]

    with open(output_file, mode='w', encoding='utf-8') as task_file_2:
        task_file_2.write(line2+"?????")
        task_file_2.write(line3)

task_encoding(args.output_file, args.input_file, args.name)