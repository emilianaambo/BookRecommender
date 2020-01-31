
import zipfile, urllib.request, shutil
import requests, io

def main():

    url = 'http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip'
    file_name = 'BX-CSV-Dump.zip'
    r = requests.get(url, stream =True)
    check = zipfile.is_zipfile(io.BytesIO(r.content))
    while not check:
        r = requests.get(url, stream =True)
        check = zipfile.is_zipfile(io.BytesIO(r.content))
    else:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()


if __name__ == '__main__': main()



