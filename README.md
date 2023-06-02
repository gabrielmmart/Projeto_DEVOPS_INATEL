# App usado no seminário da matéria Engenharia de Software (C214)

### Instalação

1. Clone o repositório

   ```sh
   git clone https://github.com/gabrielmmart/supermercado_C214-S107.git
   ```
2. Instale pip como o gerenciador de dependências

   ```sh
   python -m pip install -U pip
   ```
3. Instale as dependências

   ```sh
   pip install -r requirements.txt
   ```
4. Execute com:

   ```sh
   python supermercadoMain.py 
   ```
### Usando docker
   
1. Na linha de comando:

   ```sh
   docker build -t python-jenkins . 
   ```
2. Próximo comando:

   ```sh
   docker run -p 8080:8080 python-jenkins
   ```
   
3: abra no browser:

   localhost:8080
   
### Autores

Gabriel Medeiros GES 97

Ramon Adonis GEC 1581
