def write_to_clipboard(output):
    import subprocess
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode())


if __name__ == '__main__':
    write_to_clipboard("you have written to the clipboard.")