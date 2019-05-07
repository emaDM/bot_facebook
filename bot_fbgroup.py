from myselenium import *
from selenium.webdriver.common.keys import Keys

path_driver = './chromedriver'

fb_home = "http://www.facebook.com"
grupo_venta = "https://www.facebook.com/groups/485025718211121/"

field_email = 'email'
email = "micorreo@gmail.com"

field_password = 'pass'
password = "micontraseña"

photo1 = 'mipath/aloe.jpg'
photo2 = 'mipath/aloe2.png'

titulo='Aloe Vera Gel Forever'
precio='505'
descripcion='''*Desintoxica, Colon Limpio, Elimina Acidez y Estreñimiento
Reduce Grasas, Controla El Peso, Energizante, Normaliza Colesterol.
* + Info - WhatsApp: 9999999999 - 999999999'''


try:
    vstr = MySelenium(path_driver)
    vstr.driver.maximize_window()
    vstr.visit(fb_home)
    vstr.input_by_name(field_email, email)
    vstr.input_by_name(field_password, password + Keys.RETURN)
    vstr.visit(grupo_venta)
    vstr.click_by_class('_3ixn') #quitar la pantalla obscura
    vstr.input_by_class("_58al", titulo, 3)
    vstr.input_by_xpath('//*[@id="rc.u_0_1y"]/div[2]/div/div[1]/div[2]/div[2]/label/input', precio, 3)
    vstr.input_unknow_xpath('//*[@id="rc.u_0_1y"]/div[2]/div/div[1]/div[4]/div[1]/div/div/div/div[2]/div/div/div/div', descripcion, 3)
    vstr.upload_by_name("composer_photo","mipath/aloe.jpg", 1) #adjuntar foto 1
    vstr.upload_by_name("composer_photo", "mipath/aloe2.png", 3) #adjuntar foto 2
    vstr.click_by_xpath('//*[@id="rc.u_0_1y"]/div[2]/div/div[2]/div/div[2]/div/div/span/span/button') #boton confirmar aviso
    vstr.click_all_by_class('_4ofr', 0.2)  # seleccionar todos los grupos
    vstr.click_by_xpath('//*[@id="rc.u_0_1y"]/div[2]/div/div[2]/div/div[2]/div/div/span/span/button') #boton publicar aviso
except Exception as e:
    print("Exception in main(): ", e)
#driver.close()