# Avaliação Prática

Este projeto tem como objetivo criar uma API que possibilite a troca de dados em CSV entre um repositório local e um banco de dados SQL server.
O projeto contém dois componentes, respectivamente em C# e Python. O código em C# recebe as informações de um CSV, comunica com o Server e converte as informações em JSON. 
Enquanto o código em Python utiliza um ID informado pelo usuário para pesquisar informações deste arquivo e retorna-as de maneira organizada, junto à classificação etária referente àquele ID. 

Dentre as tecnologias utilizadas, destacam-se: C#, Python, ASP.NET Core Web API, MySQL e Swagger.  

## Rodando a API
1) Abra um terminal PowerShell em seu diretório local.
2) Rode o seguintes comando: dotnet run --project ./api-csharp/CsvImportApi.csproj
3) Acesse a interface pelo url: http://localhost:5226/
4) Nela é possível importar o CSV desejado ao server SQL.
5) Ao ser informado um ID, um novo arquivo em formato JSON será produzido.  

## Rodando o código Python Client
1) Abra um terminal PowerShell em seu diretório local.
2) Rode o seguinte comando: python .\client-python\age_classifier.py
3) Informe qual ID você deseja pesquisar.
4) O código retornará as informações compatíveis a este ID e a faixa etária a qual esta pessoa pertence.
