from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.gov.br/trabalho-e-emprego/pt-br/canais_atendimento/fale-conosco")

time.sleep(2)
driver.refresh()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Preenchendo o CPF
# primeira tentativa
driver.find_element(By.NAME, "cpf").send_keys("12345678909")  # Exemplo de CPF

# Preenchendo o Nome
driver.find_element(By.ID, "nome").send_keys("Nome Exemplo")

# Preenchendo o Email
driver.find_element(By.ID, "email").send_keys("email@exemplo.com")

# Preenchendo o Telefone
driver.find_element(By.ID, "telefone").send_keys("(85) 98765-4321")

# Selecionando a UF
uf_select = Select(driver.find_element(By.ID, "uf"))
uf_select.select_by_visible_text("Ceará")  

# Selecionando o Assunto
assunto_select = Select(driver.find_element(By.ID, "assunto"))
assunto_select.select_by_value("3")  

# Preenchendo a Mensagem
driver.find_element(By.ID, "mensagem").send_keys("Mensagem de teste para automação.")

# Preenchendo o campo de Captcha (intencionalmente incorreto)
driver.find_element(By.NAME, "captcha").send_keys("captcha_incorreto")

# Clicando no botão Enviar
driver.find_element(By.ID, "send-message").click()

time.sleep(100)

driver.quit()


# segunda tentativa
# input_cpf = WebDriverWait(driver, 5).until(
#   EC.presence_of_element_located((By.ID, "cpf"))
# );
# print(input_cpf)

# terceira tentativa
# input_cpf = driver.find_element(By.CSS_SELECTOR, "input[name='cpf']")

# quarta tentativa
# input_cpf = driver.find_element(By.XPATH, "//input[@name='cpf']")

# print(input_cpf)
