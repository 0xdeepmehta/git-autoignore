import sys

from gitignore.ignore import createModuleGitignore
 
def main():

    # If an module name is given, create the gitignore file 
    if len(sys.argv) > 1:
        createModuleGitignore(sys.argv[1])

    # If no module name is given, show a list of all modules
    else:
        print("Go and learn about .gitignore first ")

if __name__ == "__main__":
    main()