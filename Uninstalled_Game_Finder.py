import tkinter.filedialog
import tkinter as tk
import os


def Check_If_Exe(file):
    '''Gets file type from the given file name. It only uses the last period separating extension.'''
    file_type = ''
    split_string = file.split(".")
    file_type = f'.{split_string[-1]}'
    if file_type == '.exe':
        return True
    else:
        return False


def Run_Delete_Empty_Folders(watched_folder):
    empty_folders = []
    for folder in os.scandir(watched_folder):
        if os.path.exists(folder.path) and not os.path.isfile(folder.path):
            try:
                if len(os.listdir(folder)) == 0:
                    empty_folders.append(folder.path)
            except PermissionError:
                print(f'\nSkipped {folder} due to denied access.')
    if len(empty_folders) > 0:
        print(f'\n{empty_folders}')
        if input('\nDo you want to delete fully empty folders? (y/n)\n') == 'y':
            for folder in empty_folders:
                try:
                    os.rmdir(folder)
                except OSError:
                    print(f'Failed to delete {folder}\nIt is not empty.')


def Find_Uninstalled_Games():
    tk.Tk().withdraw()
    path = tk.filedialog.askdirectory(initialdir="C:/", title="Select Game Directory")
    print(f'Starting check in below path:\n{path}\n')
    delete_list = []
    for folder in os.scandir(path):
        print(f'Checking {folder.name}.')
        exe_total = 0
        for root, dirs, files in os.walk(folder.path):
            for name in files:
                if Check_If_Exe(name):
                    exe_total += 1
                    break
        if exe_total == 0:
            delete_list.append(folder.name)
    comma_delete_list = ', '.join(delete_list)
    print('\nCompleted search\nResults:')
    if len(delete_list) == 0:
        print('Nothing found.')
    else:
        print(comma_delete_list)
        Run_Delete_Empty_Folders(path)


if __name__ == "__main__":
    while True:
        Find_Uninstalled_Games()
        if input('\nRestart? (y/n)') != 'y':
            quit()
