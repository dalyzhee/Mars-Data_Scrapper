from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from selenium import webdriver
from splinter import Browser


data_info= {}
def news_data():
     #news_url = 'https://redplanetscience.com/'
     # driver = webdriver.Chrome()
     # driver.get(news_url)
     # page_source = driver.page_source
     # soup = bs(page_source, 'html.parser')
     # data = soup.find("div", class_="content_title")
     news_url = 'https://redplanetscience.com/'
     browser = Browser('chrome')
     browser.visit(news_url)
     html = browser.html
     soup = bs(html, 'html.parser')
     data = soup.find("div", class_="content_title")
     data_p = soup.find("div", class_="article_teaser_body")
     data_info['nasa_news_title'] = data.text
     data_info['nasa_news_paragraph'] = data_p.text

     return data_info
     
def scrapping_images():
     # image_ul='https://spaceimages-mars.com/'
     # driver = webdriver.Chrome()
     # driver.get(image_ul)
     # page_source = driver.page_source
     # soup = bs(page_source, 'lxml')
     # data = soup.find("img", class_="headerimage")
     # img_src = data.get('src')
     # image_url = image_ul + img_src
     image_ul='https://spaceimages-mars.com/'
     browser = Browser('chrome')
     browser.visit(image_ul)
     html = browser.html
     soup = bs(html, 'html.parser')
     data = soup.find("img", class_="headerimage")
     img_src = data.get('src')
     image_url = image_ul + img_src
     data_info['full_image_url']= image_url

     return data_info

# def all_facts_mars():
#      all_mars='https://galaxyfacts-mars.com/'
#      data_mars=pd.read_html(all_mars)
#      df = data_mars[0]
#      earth_facts = 'https://galaxyfacts-mars.com/'
#      earth_facts_table = pd.read_html(earth_facts)

#      mars_df = data_mars[0] 
#      mars_df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
#      earth_df = earth_facts_table[0]
#      mars_df['Earth'] = earth_df[1]
#      mars_data = mars_df.to_html()
#      data_info['mars'] = mars_data
#      return data_info

def all_facts_mars():
     # Visit the Mars Facts webpage
     mars_facts_url='https://galaxyfacts-mars.com/'
     mars_fact_table=pd.read_html(mars_facts_url)

     #Create Dataframe to store table data
     df = mars_fact_table[0]
     df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
     mars_facts = df.to_html()
     data_info['mars_facts'] = mars_facts
     return data_info



def hemisperical():
     # hem_url="https://marshemispheres.com/"
     # browser = requests.get(hem_url)
     # html = browser.content
     # soup = bs(html, 'html.parser')
     # full_url = soup.find_all('div', class_='item')
     
     # hemisphere_img_urls=[]      
     # for x in full_url:
     #      title = x.find('h3').text
     #      url = x.find('a')['href']
     #      img_url= hem_url + url
     #      browser = requests.get(img_url)
     #      html = browser.content
     #      soup = bs(html, 'html.parser')
     #      original_img= soup.find('div',class_='downloads')
     #      hem_url=original_img.find('a')['href']
     #      img_data=dict({'title':title, 'img_url':hem_url})
     #      hemisphere_img_urls.append(img_data)
     hem_url="https://marshemispheres.com/"
     browser = requests.get(hem_url)
     html = browser.content
     soup = bs(html, 'html.parser')
     full_url = soup.find_all('div', class_='item')
     hemisphere_img_urls=[] 
     for x in full_url:
          title_a = x.find('h3').text
          urls = x.find('a')['href']
          img_url= hem_url+urls
          print(img_url)
          browser = requests.get(img_url)
          html = browser.content
          soup = bs(html, 'html.parser')
          original_img= soup.find('div',class_='downloads')
          hems_url=original_img.find('a')['href']
          hems_url = hem_url + hems_url
          print(hems_url)
          img_data=dict({'title':title_a, 'img_url':hems_url})
          hemisphere_img_urls.append(img_data)
     data_info['hemisphere_img_urls']=hemisphere_img_urls
     return data_info