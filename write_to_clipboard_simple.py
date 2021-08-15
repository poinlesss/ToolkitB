def write_to_clipboard(new_clipboard_text):
    import subprocess
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(new_clipboard_text.encode())


if __name__ == '__main__':
    write_to_clipboard("you have written to the clipboard")