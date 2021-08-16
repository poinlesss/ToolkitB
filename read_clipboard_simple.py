def read_from_clipboard():
    import subprocess

    current_clipboard_text = subprocess.check_output(['pbpaste'])
    return current_clipboard_text.decode('utf-8')


if __name__ == '__main__':
    clipboard_text = read_from_clipboard()
    print(clipboard_text)