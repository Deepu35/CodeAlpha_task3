import os
import shutil
import re
import requests

def move_jpgs():
    src = input("Enter source folder: ")
    dst = input("Enter destination folder: ")

    os.makedirs(dst, exist_ok=True)

    for f in os.listdir(src):
        if f.endswith(".jpg"):
            shutil.move(os.path.join(src, f), os.path.join(dst, f))

    print("Moved all JPG files.\n")


def extract_emails():
    filename = input("Enter text file name: ")

    text = open(filename).read()
    emails = re.findall(r"\S+@\S+\.\S+", text)

    with open("emails.txt", "w") as f:
        for e in emails:
            f.write(e + "\n")

    print("Emails saved to emails.txt\n")


def scrape_title():
    url = input("Enter website URL: ")

    html = requests.get(url).text
    start = html.find("<title>")
    end = html.find("</title>")

    if start != -1 and end != -1:
        title = html[start+7:end]
    else:
        title = "No title found"

    open("title.txt", "w").write(title)
    print("Title saved to title.txt\n")


def main():
    while True:
        print("Choose a task:")
        print("1) Move JPG files")
        print("2) Extract emails from text file")
        print("3) Scrape website title")
        print("4) Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            move_jpgs()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_title()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if _name_ == "_main_":
    main()
