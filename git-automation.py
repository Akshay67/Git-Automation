import os
import subprocess

def run(*args):
    return subprocess.check_call(['git'] + list(args))

def add():
    run("status")
    choice = input("Do you want to add all file's y/n")
    choice = choice.lower()

    if choice == 'y':
        run("add",".")
    if choice == 'n':
        filename = input("Enter the file name to add")
        run("add",filename)
    else:
        print("\nInvalid command! Use y or n.\n")

def commit():
    message = input("Enter the Commit Message: ")
    commit_message = f'{message}'

    run("commit","-am",commit_message)

def branch():
    print("Following is your available branch/es")
    run("branch")

    br_choice = input("Do you want continue available branch: y/n ")
    br_choice = br_choice.lower()

    if br_choice == 'y':
        br = input("Enter the branch name: ")
        branch_nm = f'{br}'
        run("checkout",branch_nm)
        print("You successfully entered into {} ".format(branch_nm))
    elif br_choice == 'n':
        br = input("Enter the branch name which you want to create: ")
        run("checkout","-b",br)
    else:
        print("\nInvalid command! Use y or n.\n")

def push():
    br_name = input("Enter the branch name to push: ")
    print("Code is being pushed sit back!")
    run("push","origin",br_name)

def main():

    choices = 'branch, commit'
    print("ENter the command to use: " + choices)
    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == 'branch':
        branch()
    elif choose_command == 'commit':
        #branch()
        add()
        commit()
        push()

if __name__ == '__main__':
    main()