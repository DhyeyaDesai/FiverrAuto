# %%
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# %%
data = {'Modelo': [], 'Year': [], 'Images': [], 'City': [], 'Distance': [], 'Negotiable': [], 'Price': [], 'Marca': [], 'Subtipo': [], 'Vidrios': [], 'Tracción': [], 'Transmisión': [], 'Dirección': [], 'Sistema_de_climatización': [], 'Placa': [], 'Tapizado': [], 'Combustible': [], 'Description': []}

df = pd.DataFrame(data)

# %%
driver = webdriver.Firefox(executable_path="C:\\Python38\\geckodriver.exe")
driver.get("https://peru.todoautos.com.pe/usados/-/autos/-/bmw?type_autos_brand=toyota&type_autos_brand=byd&type_autos_brand=kia&type_autos_brand=hyundai&type_autos_brand=jeep&type_autos_brand=jac&type_autos_brand=volvo&type_autos_brand=land+rover&type_autos_brand=lexus&type_autos_brand=mahindra&type_autos_brand=mazda&type_autos_brand=mercedes+benz&type_autos_brand=mg&type_autos_brand=mini&type_autos_brand=mitsubishi&type_autos_brand=nissan&type_autos_brand=peugeot&type_autos_brand=porsche&type_autos_brand=renault&type_autos_brand=seat&type_autos_brand=smart&type_autos_brand=ssangyong&type_autos_brand=subaru&type_autos_brand=suzuki&type_autos_brand=volkswagen")

# %%
driver2 = webdriver.Firefox(executable_path="C:\\Python38\\geckodriver.exe")

# %%
for i in range(1,16):
    try:
        searchBar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='row m-b-none']"))
        )
        cars = driver.find_elements_by_id("featuredUsed")
    except Exception as e:
        print(e)
        
    for car in driver.find_elements_by_xpath("//*[@class='card-info card-content']"):
        
        price = ""
        Marca = ""
        Subtipo = ""
        Vidrios = ""
        Tracción = ""
        Transmisión = ""
        Dirección = ""
        Sistema_de_climatización = ""
        Placa = ""
        Tapizado = ""
        Combustible = ""
        description = ""

        images = []
        link = car.find_element_by_css_selector('a').get_attribute("href")
        driver2.get(link)
        
        try:
            image_list = driver2.find_element_by_xpath("/html/body/article/div/div[1]/div[1]/div[2]/div/div[3]/div[2]/div[1]/div/ul")
        except NoSuchElementException:
            continue
            

        try:
            for image in image_list.find_elements_by_css_selector('img'):
                images.append(image.get_attribute('data-src').replace("x80", "990x540xC"))
        except:
            print(link)
            continue

        try:
            year = (driver2.find_element_by_xpath("/html/body/article/div/div[1]/div[2]/div/div/div[3]/section[1]/div[2]/div[1]").text).replace("Año\n", "")
        except:
            pass
        try:
            city = driver2.find_element_by_xpath("/html/body/article/div/div[1]/div[2]/div/div/div[3]/section[1]/div[2]/div[2]").text.replace("Ciudad\n", "")
        except:
            pass
        try:
            distance = driver2.find_element_by_xpath("/html/body/article/div/div[1]/div[2]/div/div/div[3]/section[1]/div[2]/div[3]").text.replace("Recorrido\n", "")
        except:
            pass
        try:
            negotiable = driver2.find_element_by_xpath("/html/body/article/div/div[1]/div[2]/div/div/div[3]/section[1]/div[2]/div[4]").text.replace("Tipo de pago\n", "")
        except:
            pass
        try:
            price = driver2.find_element_by_xpath("/html/body/article/div/div[1]/div[2]/div/div/div[3]/section[1]/div[2]/div[5]").text.replace("Precio Contado\n", "")
        except:
            pass

        try:
            technicalData = driver2.find_element_by_id("technicalData")
        except:
            pass
        try:
            Marca = technicalData.find_element_by_xpath(".//*[contains(text(), 'Marca')]/following-sibling::*").text
        except:
            pass
        try:
            Modelo = technicalData.find_element_by_xpath(".//*[contains(text(), 'Modelo')]/following-sibling::*").text
        except:
            pass
        try:
            Subtipo = technicalData.find_element_by_xpath(".//*[contains(text(), 'Subtipo')]/following-sibling::*").text
        except:
            pass
        try:
            Vidrios = technicalData.find_element_by_xpath(".//*[contains(text(), 'Vidrios')]/following-sibling::*").text
        except:
            pass
        try:
            Tracción = technicalData.find_element_by_xpath(".//*[contains(text(), 'Tracción')]/following-sibling::*").text
        except:
            pass
        try:
            Transmisión = technicalData.find_element_by_xpath(".//*[contains(text(), 'Transmisión')]/following-sibling::*").text
        except:
            pass
        try:
            Dirección = technicalData.find_element_by_xpath(".//*[contains(text(), 'Dirección')]/following-sibling::*").text
        except:
            pass
        try:
            Sistema_de_climatización = technicalData.find_element_by_xpath(".//*[contains(text(), 'Sistema de climatización')]/following-sibling::*").text
        except:
            pass
        try:
            Placa = technicalData.find_element_by_xpath(".//*[contains(text(), 'Placa')]/following-sibling::*").text
        except:
            pass
        try:
            Tapizado = technicalData.find_element_by_xpath(".//*[contains(text(), 'Tapizado')]/following-sibling::*").text
        except:
            pass
        try:
            Combustible = technicalData.find_element_by_xpath(".//*[contains(text(), 'Combustible')]/following-sibling::*").text
        except:
            pass
        try: 
            description = driver2.find_element_by_xpath(".//*[contains(text(), 'Descripción')]/following-sibling::*/following-sibling::*").text.replace("\n", ". ")
        except:
            pass
        
        row = {'Modelo': Modelo, 'Year': year, 'Images': images, 'City': city, 'Distance': distance, 'Negotiable': negotiable, 'Price': price, 'Marca': Marca, 'Subtipo': Subtipo, 'Vidrios': Vidrios, 'Tracción': Tracción, 'Transmisión': Transmisión, 'Dirección': Dirección, 'Sistema_de_climatización': Sistema_de_climatización, 'Placa': Placa, 'Tapizado': Tapizado, 'Combustible': Combustible, 'Description': description}
        df = df.append(row, ignore_index=True)
        
    try:
        next_len = len(driver.find_elements_by_xpath("//*[@class='waves-effect active']"))
        driver.find_elements_by_xpath("//*[@class='waves-effect active']")[next_len-1].click()
    except:
        break

# %%
df1 = df 

# %%
df1 = df1.drop_duplicates(subset=["Description", "Modelo", "Year", "City", "Distance","Negotiable","Price","Marca","Subtipo","Vidrios","Tracción","Transmisión","Dirección","Sistema_de_climatización", "Placa","Tapizado","Combustible","Description"]).reset_index(drop=True)

# %%
df1.to_excel("AutoData.xlsx")