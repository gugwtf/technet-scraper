# technet-scraper
*_Crappy_* but working technet scraper :)

**Technet**: https://gallery.technet.microsoft.com/

The technet is moving. A friend wanted all of the scripts of the Technet, so I made a web scraper.

/!\ The number page is static. (not enough time to make it dynamically at the moment)

The scrapper find all of the article on the first page, generate the arborescence like **./category/sub\_category**  and then download the script in the correct folder.

```bash
# Set-up a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Install required packages
pip install requirements.txt

# Scrap the scripts
python technet-scraper.py
```
