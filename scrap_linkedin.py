
from selenium import webdriver

if __name__ =='__main__':
    driver = webdriver.Chrome()
    
    driver.get('https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0')
    resultados = driver.find_elements_by_class_name('base-card')
    
    listadescricoes = []
    for r in resultados:
        r.click
        descricao1 = driver.find_element_by_class_name('description')
        listadescricoes.append(descricao1.text)

    print(listadescricoes)
