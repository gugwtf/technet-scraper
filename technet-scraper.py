import requests, sys, urllib.request, os, time
from bs4 import BeautifulSoup

path = os.getcwd()

# Check if directory exist, if not try to create it
def directory_check(folder):
    full_path = path + "/" + folder
    try:
      if os.path.isdir(full_path) is False: os.makedirs(full_path)
    except OSError:
      print(f"[FAIL] Couldn't create folder \"{folder}\" (it might already exist)")
    else:
      print(f"[OK] Directory \"{folder}\" created")

def main():
  url='https://gallery.technet.microsoft.com'
  authorized_extensions=['ps1','psm1','psm','zip']

  for p in range(1, 1748):

    page_url= url + "/site/search?pageIndex=" + str(p)

    print("*********************")
    print(f"PAGE URL: {page_url}")
    print("*********************")

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
        script_file_name = script_full_link.rsplit('/', 1)[1].lower().replace(" ","_").replace("%20","_")
        script_file_extension = script_file_name.rsplit('.',1)[1]
        script_directory = script_category + "/" + script_sub_category
        script_file_directory = script_category + "/" + script_sub_category + "/" + script_file_name

        print(f"----------------------------")
        print(f"Article Link: {article_link}")
        print(f"Filename: {script_file_name}")
        print(f"Directory: {script_category}/{script_sub_category}")

        directory_check(script_directory)

        if script_file_extension in authorized_extensions: urllib.request.urlretrieve(script_full_link,script_file_directory)
        print(f"[OK] {script_file_name} downloaded!")
      except:
        print("[FAIL] The file {script_file_name} could not be downloaded")

if __name__ == '__main__':
    main()
    sys.exit(0)
