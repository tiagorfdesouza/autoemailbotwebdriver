from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import time
import random



class Botemail:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"./geckodriver")

    @staticmethod
    def type_like_a_person(setence,single_input_field):
        print("digitando...")
        for letter in setence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1,5) / 30)

    def login(self):
        driver = self.driver
        driver.get("https://webmail-seguro.com.br/")
        time.sleep(5)
        insertEmail = driver.find_element_by_xpath("//input[@name='_user']")
        insertEmail.clear()
        insertEmail.send_keys(self.username)
        print("login inserido")
        time.sleep(3)

        insertPassoword = driver.find_element_by_xpath("//input[@name='_pass']")
        insertPassoword.clear()
        print("inserindo senha")
        insertPassoword.send_keys(self.password)
        insertPassoword.send_keys(Keys.RETURN)
        time.sleep(6)
        driver.find_element_by_id('close-popover').click()
        time.sleep(2)

    def buttoncriarEmail(self):
        driver = self.driver
        print("clicando no botão criar email")
        driver.find_element_by_id('rcmbtn110').click()
        time.sleep(3)

    def prenchercampos(self):
        driver = self.driver
        to = driver.find_element_by_id('_to')
        print("inserindo destinatario")
        time.sleep(2)
        to.send_keys("tiagorfdesouza@gmail.com")
        time.sleep(3)
        subject = driver.find_element_by_xpath("//input[@name='_subject']")
        subject.click()
        print("inserindo assunto")
        time.sleep(1)
        subject.send_keys("SOLICITAÇÂO DE ARQUIVOS 07/2021")
        #subject.send_keys(Keys.TAB)
        time.sleep(3)
        body = driver.find_element_by_id('_rc_sig')
        body.click()
        body.send_keys("Testando envio de email automatizado")

    def Enviar(self):
        driver = self.driver
        enviar = driver.find_element_by_class_name('lm-compose-icosend')
        enviar.click()







jarvisemail = Botemail("usuario","senha")
jarvisemail.login()
jarvisemail.buttoncriarEmail()
jarvisemail.prenchercampos()
