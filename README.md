# automacao_com_selenium
Automação de testes com Selenium Webdriver no Python
Inicialmente fiz o teste pelo Selenium IDE, exportei os comandos de testes em um arquivo de Python.
Depois transformei cada formulário do site utilizado para o teste em um objeto, uma classe, e cada elemento de interação em um método.
Inicialmente criei o arquivo WebDriver.py, onde tem uma classe de geração de objetos com webdriver do Selenium, para poder gerar todos os testes até para outros projetos.
Depois criei o arquivo sampleTricentisCadastro.py, que contém uma classe filha da classe do arquivo WebDriver.py.
A classe sampleTricentisCadastro representa o começo do projeto, nela tem o link do site.
Depois gerei as classes para os formulários e o arquivo Teste_cadastro_dos_formularios.py para iniciar os testes em todos os formulários.

Dependências:
Instalação do pacote do Selenium.
ChromeDriver, última versão, só baixar e apontar o caminho no arquivo WebDriver.py em webdriver.Chrome().
