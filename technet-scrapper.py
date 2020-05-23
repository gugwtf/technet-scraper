import requests, sys, urllib.request, os
from bs4 import BeautifulSoup

path = os.getcwd()

def directory_check(folder):
    print(f"folder: {folder}")
    full_path = path + "/" + folder
    print(f"FULL_PATH: {full_path}")
    try:
      os.makedirs(full_path)
    except OSError:
      print(f"[FAIL] Couldn't create folder \"{folder}\" (it might already exist)")
    else:
      print(f"[OK] Directory \"{folder}\" created")

def main():
  url='https://gallery.technet.microsoft.com'

  for p in range(1, 1736):
    page_url= url + "/site/search?pageIndex=" + str(p)
    print(f"PAGE URL: {page_url}")

    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find_all(class_='itemTitle')

   
    for article in articles:
      article_link = str(url) + str(article.find('a').get('href'))
      soup_article = BeautifulSoup(requests.get(article_link).content, 'html.parser')

      try:
        script_file = soup_article.find(id='Downloads').find('a').get('href')
        script_full_link = url + script_file
        script_category = (soup_article.find(id='sectionLeft').findAll(class_="itemBar"))[3].find('a').contents[0].lower().replace(" ","_")
        script_sub_category = (soup_article.find(id='sectionLeft').findAll(class_="itemBarLong"))[0].find('a').contents[0].lower().replace(" ","_")
        script_file = script_full_link.rsplit('/', 1)[1]
        script_directory = script_category + "/" + script_sub_category
        script_file_directory = script_category + "/" + script_sub_category + "/" + script_file
        print(f"ARTICLE LINK: {article_link}")
        print(f"FILENAME: {script_file}")
        print(f"CATEGORY: {script_category}")
        print(f"SUB_CATEGORY: {script_sub_category}")
        print(f"FULL LINK: {script_full_link}")
        directory_check(script_directory)
        urllib.request.urlretrieve(script_full_link,script_file_directory)
      except:
        print("No downloadable file")

if __name__ == '__main__':
    main()
    sys.exit(0)
