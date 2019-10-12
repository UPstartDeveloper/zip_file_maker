import os
import zipfile


def zipdir(path, ziph):
    """ziph is zipfile handle"""
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


if __name__ == '__main__':
    file_name = input("Enter a name for your new ZIP folder " +
                      "(include extension): ")
    path = input("Enter the path to the directory you would like the ZIP " +
                 "to save to: ")
    zipf = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(path, zipf)
    zipf.close()
