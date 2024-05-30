import subprocess, os, platform


# https://stackoverflow.com/a/435669
def open_file(filepath):
    """
    Otwiera plik domyślnym programem  na danym systemie (np. pdf adobe readerem)
    :param filepath: ścieżka do pliku
    """
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(filepath)
    else:  # linux variants
        subprocess.call(('xdg-open', filepath))
