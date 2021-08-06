from selenium import webdriver
import pandas as pd
from time import sleep

# #Abre o navegador e acessa o site
navegador = webdriver.Chrome()
navegador.get('http://www.rpachallenge.com/')

#Abre arquivo excel
arquivo = pd.read_excel('input_forms.xlsx')

navegador.find_element_by_xpath('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()
for i in range(0, len(arquivo.index)):
    nome = arquivo.loc[i, 'First Name']
    sobrenome = arquivo.loc[i, 'Last Name']
    email = arquivo.loc[i, 'Email']
    endereco = arquivo.loc[i, 'Address']
    telefone = str(arquivo.loc[i, 'Phone'])
    empresa = arquivo.loc[i, 'Company']
    funcao = arquivo.loc[i, 'Role']
    
    navegador.find_element_by_xpath('//input[@ng-reflect-name="labelFirstName"]').send_keys(nome)
    navegador.find_element_by_xpath('//input[@ng-reflect-name="labelLastName"]').send_keys(sobrenome)
    navegador.find_element_by_xpath('//input[@ng-reflect-name="labelEmail"]').send_keys(email)
    navegador.find_element_by_xpath('//input[@ng-reflect-name="labelAddress"]').send_keys(endereco)
    navegador.find_element_by_xpath('//*[@ng-reflect-name="labelPhone"]').send_keys(telefone)
    navegador.find_element_by_xpath('//input[@ng-reflect-name="labelCompanyName"]').send_keys(empresa)
    navegador.find_element_by_xpath('//input[@ng-reflect-name="labelRole"]').send_keys(funcao)
    navegador.find_element_by_xpath('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
