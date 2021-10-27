# DATASCIENCE-NASA-CRAWLING
#### Solar Dynamics Observatory: SDO Crawling Python Code

[ALL DATA ARE FROM NASA]

![NASA](https://user-images.githubusercontent.com/87653966/139007517-2b2f5d61-b709-4100-a524-aee8f0d57a6b.png)
URL: https://sdo.gsfc.nasa.gov/
I am an artificial intelligence engineer who develops machine learning and deep learning models using SDO AIA-193 images. That's why I have to get the images needed for learning and crawl the data from NASA's SDO site.

#### We will access the Solar Dynamics Observatory website and crawl the data.
![maxresdefault](https://user-images.githubusercontent.com/87653966/139008775-0d884262-7de3-4cb0-9c1c-350cb4e1cf6c.jpg)
AIA 193 

This method is for making URL for accessing Data Assets

    def urlMaker(n):
        url = 'https://sdo.gsfc.nasa.gov/assets/img/browse/'
        today = date.today()
        yesterday = date.today() - timedelta(n)
        url = url + str(yesterday.strftime('%Y/%m/%d')) + "/"
        return [url, str(yesterday.strftime('%Y%m%d'))]

In the below method, 512_211193171 is a code of SDO image. 512 is the size of image, and 211193171 is the code number of SDO image.
There are a lot of SDO Image code.

    def fileprint(url):
        indexlst = []
        files = []
        number = 0
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
        else : 
            print(response.status_code)

        links = soup.find_all('a') 
        cell_line = []
        for i in links:
            href = i.attrs['href']
            cell_line.append(href)

        for i in range(5, len(cell_line)):
            if '512_211193171.jpg' in cell_line[i]:
                # print(cell_line[i][0:11])
                if cell_line[i][0:11] not in indexlst:
                    indexlst.append(cell_line[i][0:11])
                    files.append(cell_line[i])
                number += 1
        return files

From 0 to 3000 means downloading image data from today to 3,000 days ago.

      def main():
          for i in range(0, 3000):
              x = fileprint(urlMaker(i)[0])
              for j in range(0, len(x)):
                  print(urlMaker(i)[0] + x[j])
                  try:
                      download(urlMaker(i)[0] + x[j], x[j])
                      print('DONE --- ', x[j])
                  except:
                      print("ERROR")

