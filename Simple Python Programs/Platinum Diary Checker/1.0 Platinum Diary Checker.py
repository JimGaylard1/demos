"""
This program compares the current band diary on the internet (saved in 
diarycompare.txt) with the website as it was at the time of the last check
(saved in diarymaster.txt) and reports any changes.

1.0 tidies up the code in 0.2 without losing any of the function.
"""
import requests
import webbrowser
import time
from bs4 import BeautifulSoup


def get_website_diary():
    r = requests.get('https://www.platinumtheband.co/platinumtours')
    soup = BeautifulSoup(r.text, "html5lib")
    website_html = soup.find_all("div", id="PAGES_CONTAINERinlineContent")

    global website_text
    website_text = []
    for elem in website_html:
        if '<span class="backcolor_14">' or '<span class="color_15">' in elem:
            website_text.append(elem.text.strip())


def write_to_compare():
    with open("diarycompare.txt", "w", encoding="utf-8") as f:
        f.writelines(website_text)


def write_to_master():
    with open("diarymaster.txt", "w", encoding="utf-8") as f:
        f.writelines(website_text)


def check_for_changes():
    with open("diarymaster.txt", "r", encoding="utf-8") as f:
        master_text = f.readlines()
    with open("diarycompare.txt", "r", encoding="utf-8") as f:
        compare_text = f.readlines()

    print("==================================================================")
    if compare_text == master_text:
        print("No update necessary!")
        time.sleep(1)
        webbrowser.open_new('launcher://homescreen')
    else:
        print("Update diary with the following:")

        months = (
            "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
            "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
        )
        years = [str(elem) for elem in range(2020, 2100)]
        years = tuple(years)

        def convert_to_list(list_var, text1, text2):
            # adds lines present in text1 and missing from text2 to list_var
            for line in text1:
                if "{" not in line and "}" not in line and ";" not in line:
                    if line.strip() in years:
                        list_var.append(line.strip())
                    elif line.strip() in months:
                        list_var.append(line.strip())
                    elif line not in text2:
                        list_var.append(line.strip())
        new_dates = []
        convert_to_list(new_dates, compare_text, master_text)
        old_dates = []
        convert_to_list(old_dates, master_text, compare_text)

        def print_result(list):
            for pos, elem in enumerate(list):
                if elem in months:
                    next_pos = pos + 1
                    if next_pos != len(list):
                        if (list[next_pos] not in months and
                            list[next_pos] not in years and
                                list[next_pos] != "\u200b"):
                            print(elem)
                elif elem in years:
                    next_pos = pos + 1
                    if next_pos != len(list):
                        if list[next_pos] not in years:
                            print(elem)
                elif "{" not in elem and "}" not in elem and ";" not in elem:
                    print(elem)

        def debug(list):
            print("[========        DEBUG        ========]")
            print(list)
            print("[========      END DEBUG      ========]")

        print("\n\n\nREMOVE\n\n")
        print_result(old_dates)
        # debug(old_dates)
        print("\n\nADD\n\n")
        print_result(new_dates)
        # debug(new_dates)
        write_to_master()
        time.sleep(3)
        webbrowser.open_new('calshow://')

get_website_diary()
write_to_compare()
check_for_changes()
