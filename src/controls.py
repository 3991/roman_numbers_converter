import argparse

def command_line_arguments():
    parser = argparse.ArgumentParser(description = "Description for my parser")
    parser.add_argument("-a", "--arabic", help = "convert to arabic number", required = False)
    parser.add_argument("-r", "--roman", help = "convert to roman number", type=int, required = False)

    args = parser.parse_args()
    if args.arabic:
        print("Not implemented yet")
        sys.exit()

    return args.roman
