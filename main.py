import easygui as eg
import subprocess


def main():
    file_dir = ''

    try:
        file = open('config.txt', 'r')
        file_dir = file.readline()
    except FileNotFoundError:
        file = open('config.txt', 'w')

    if '.txt' in file_dir:
        option = eg.choicebox(msg='Open previous file?', title='Open options', choices=[file_dir, file_dir])
        if option is None:
            update_process(file=file)
        subprocess.Popen('notepad.exe ' + file_dir)
        file.close()
        exit(0)
    else:
        update_process(file=file)


def update_process(file):
        file_to_edit = eg.fileopenbox("Select TXT file", default="*.txt", filetypes="*.txt")
        file.close()
        file = open('config.txt', 'w')
        file.write(file_to_edit)
        subprocess.Popen('notepad.exe ' + file_to_edit)
        file.close()
        exit(0)


if __name__ == '__main__':
    main()
