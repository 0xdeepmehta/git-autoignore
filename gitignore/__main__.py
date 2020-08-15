import sys
import argparse
from gitignore.ignore import createModuleGitignore
 

def usage():
	print("usage: git-autoignore <module Name>")
	print("Example: git-autoignore python")
	print("Available subcommands are:")
	print("    usage                    Show this help message and exit")
	print("    version                  Show version and exit")
	print("https://github.com/Imdeepmehta/git-autoignore")
	print("git-autoignore, copyright Imdeepmehta <itsdeepmehta25@gmail.com>")

def main():
	parser = argparse.ArgumentParser(prog='git-autoignore',usage='%(prog)s [options] Module Name',description="Example: git-autoignore python",epilog='Enjoy the program! :)')
	parser.add_argument('module',
                       metavar='module',
                       type=str,
                       help='Single Module Name for which you wanna genrate .gitignore')

	parser.add_argument("-V", "--version", help="show program version", action="store_true")
	args = parser.parse_args()

	if args.version:
		print("git-autoignore, version 1.0.3")
		print("https://github.com/Imdeepmehta/git-autoignore")
		print("git-autoignore, copyright Imdeepmehta <itsdeepmehta25@gmail.com>")
	elif args.module:
		createModuleGitignore(args.module)

if __name__ == "__main__":
    main()