# **PDF to Excel Data Extractor**

## **Descrição**
O **PDF to Excel Data Extractor** é uma ferramenta que extrai automaticamente valores de exames laboratoriais de arquivos PDF e os organiza em um arquivo Excel. Ele facilita a coleta de dados de PDFs e apresenta os resultados em um formato organizado, pronto para ser usado.

---

## **Requisitos**
- **Sistema Operacional:** Windows
- Arquivos PDF localizados em uma pasta, todos com resultados laboratoriais que seguem a mesma estrutura.

---

## **Como Usar**

1. **Abra o programa:**
   - Execute o arquivo `.exe` gerado. Uma janela do console será aberta, solicitando o caminho da pasta com os arquivos PDF.

2. **Insira o caminho da pasta:**
   - No campo de entrada do console, insira o caminho completo da pasta onde estão localizados os arquivos PDF.
   - **Exemplo:**  
     `C:\Users\Usuario\Documents\ExamesPDF`
   
3. **Processamento dos arquivos:**
   - O programa irá automaticamente acessar todos os PDFs dentro da pasta especificada, extrair os valores de interesse e organizá-los no formato necessário.

4. **Resultado do processamento:**
   - O programa criará um arquivo Excel (`.xlsx`) com o nome da pasta que contém os arquivos PDF.
   - O arquivo Excel terá os seguintes campos:
     - **Coluna A:** Lista de parâmetros de exames (ex.: ERITROCITOS, HEMOGLOBINA, etc.).
     - **Colunas subsequentes:** Para cada PDF processado, uma nova coluna será gerada, contendo os valores extraídos daquele arquivo PDF.
   
   - A célula A1 será chamada de **"PARÂMETROS"** e todas as colunas subsequentes trarão o nome dos arquivos PDF processados (ex.: 12.pdf, 13.pdf, etc.).

5. **Largura da Coluna A:**
   - A coluna A será automaticamente ajustada para ter 187 pixels de largura, garantindo que os nomes dos parâmetros fiquem bem visíveis.

6. **Finalização:**
   - Após o processamento, uma mensagem de sucesso será exibida no console:
     - **Exemplo:** `"Arquivo Excel 'NomeDaPasta.xlsx' gerado com sucesso!"`

7. **Localização do arquivo Excel:**
   - O arquivo Excel será salvo na mesma pasta onde estão os arquivos PDF processados, com o nome da pasta que você especificou.

---

## **Erros Comuns**

1. **Caminho inválido:**
   - Se o caminho fornecido para a pasta estiver incorreto ou não for encontrado, o programa exibirá a seguinte mensagem:  
     `"O caminho fornecido 'caminho_da_pasta' não é válido."`  
   - Verifique se o caminho está correto e tente novamente.

2. **PDFs fora do padrão:**
   - Se os arquivos PDF não seguirem o formato esperado, alguns parâmetros podem não ser corretamente identificados. Verifique se os PDFs têm a estrutura correta antes de processá-los.

---

## **Apoio Técnico**
Se houver qualquer dúvida ou problema com o programa, entre em contato com o suporte técnico através do e-mail **suporte@exemplo.com**.

---

### **Autor**
Leonardo Miguel dos Santos



### **DISCLAIMER** 
Devido ao modelo de pdf usado como modelo de análise e teste, a ordem dos parâmetros DEVE ser "ERITROCITOS", "HEMOGLOBINA", "HEMATÓCRITO", "V.C.M", "H.C.M", "C.H.C.M", "PLAQUETAS", "LEUCÓCITOS TOTAIS", "BASTONETES", "SEGMENTADOS", "LINFÓCITOS", "MONÓCITOS", "EOSINÓFILOS", "BASÓFILOS", "ALBUMINA", "BILIRRUBINA DIRETA", "BILIRRUBINA TOTAL", "CK", "CREATININA", "FOSFATASE ALCALINA", "GGT", "PROTEINA TOTAL", "AST", "ALT", "UREIA", "BILIRRUBINA INDIRETA"
(Requer mais testes para saber se foi resolvido)
