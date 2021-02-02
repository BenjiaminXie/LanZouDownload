import time
import os


# r'/home/zeus/Downloads/', 20
def download_wait_(directory, timeout, nfiles=None):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.
    timeout : int
        How many seconds to wait until timing out.
    nfiles : int, defaults to None
        If provided, also wait for the expected number of files.

    """
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True
                print("下载进行中————>等待ing")

        seconds += 1
    print('下载结束')
    return seconds


def download_wait(directory):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.
    """
    dl_wait = True
    while dl_wait:
        time.sleep(3)
        files = os.listdir(directory)
        for fname in files:
            if fname.endswith('.crdownload'):
                print("下载进行中————>等待下载结束ing")
            else:
                dl_wait = False
                print('下载结束')
                break
