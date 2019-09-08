import os,subprocess,sys

color = {
   "LBLUE" : '\033[94m',
   "LGREEN" : '\033[92m',
   "LYELLOW" : '\033[93m',
   "LRED" : '\033[91m',
   "BLUE" : '\033[34m',
   "YELLOW" : '\033[33m',
   "RED" : '\033[31m',
   "GREEN" : '\033[32m',
   "PURPLE" : '\033[35m',
   "ENDC" : '\033[0m'
}

commit_type = [
    ('feat:' , "A new feature"),
    ('fix:' , "A bug fix"),
    ('docs:' , "Documentation only chanes"),
    ('style:' , "Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)"),
    ('refactor:' , "A code change that neither fixes a bug nor adds a feature"),
    ('perf:' , "A change that improves performance"),
    ('test:' , "Adding missing tests"),
    ('chore:' , "Changes to the build process or auxiliary tools and libraries such as documentation generation")
]

message = ""
path = os.getcwd()

try:
    line = 1
    while True:
        os.system('clear')
        print(color['BLUE'] + "Line:" + color['ENDC'] + " " + str(line))
        line += 1
        print("Select the type of change that you're commiting:\n")
        i = 1
        for pair in commit_type:
            print(str(i) + "." + color['LBLUE'] + pair[0] + color['ENDC'] + " " + pair[1])
            i += 1
        while True:
            try:
                choice = int(input(color['LGREEN'] + ">" + color['ENDC']))
                if choice > len(commit_type) or choice < 1:
                    raise Exception("Number Out Of Menu Range")
            except ValueError:
                print(color['LRED'] + 'Please Enter A Valid Number' + color['ENDC'])
            except Exception as e:
                print(color['LRED'] + 'Number Out Of Menu Range, Please Enter A Valid Number' + color['ENDC'])
            else:
                break
        os.system('clear')
        print("Selected Type:" + color['LBLUE'] + commit_type[choice - 1][0] + color['ENDC'] + '\n')
        print("Please Enter The Commit Message (All commit message lines will be cropped at 100 characters.)")
        message += commit_type[choice - 1][0] + input("[" + color['LBLUE'] + commit_type[choice - 1][0] + color['ENDC'] + "]" + color['LGREEN'] + ">" + color['ENDC']) + '\n'
        print(color['LYELLOW'] + "Line Added" + color['ENDC'] + '\n')
        print("1.Add Another Line")
        print("2.Finish And Write Output To File")
        print("3.Run git commit With Current Message")
        print("4.Abort")
        menu = input(color['LGREEN'] + ">" + color['ENDC'])
        if menu == '1':
            continue
        elif menu == '2':
            print('\n' + color['PURPLE'] + 'Final Commit Message:' + color['ENDC'])
            print(message + '\n')
            print("Please Provide A File Name (default: message.txt)")
            filename = input(path + "/" + color['LGREEN'] + ">" + color['ENDC'])
            if filename:
                file = open(path + "/" + filename, 'w')
            else:
                file = open(path + "/" + "message.txt", 'w')
                filename = "message.txt"
            file.write(message)
            file.close()
            print(color['LYELLOW'] + "Written To File." + color['ENDC'] + '\n' + "You Should Run git commit --file " + filename)
            break
        elif menu == '3':
            print('\n' + color['PURPLE'] + 'Final Commit Message:' + color['ENDC'])
            print(message + '\n')
            subprocess.Popen("git commit -m '" + message + "'", shell=True, stderr=sys.stderr, stdout=sys.stdout)
            print(color['LYELLOW'] + "Changes Commited." + color['ENDC'])
            break
        elif menu == '4':
            print('\n' + color['LRED'] + 'Aborting Commit.' + color['ENDC'])
            break
except KeyboardInterrupt:
    print('\n' + color['LRED'] + 'Keyboard Interrupt, Aborting Commit.' + color['ENDC'])




