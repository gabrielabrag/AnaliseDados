import pandas as pd
import plotly.express as px

#importar base de dados
tabela = pd.read_csv(R"C:\Users\gabir\Downloads\telecom_users.csv")

#tratamento dos dados
#coluna com formato errado texto -> numero
tabela["TotalGasto"] =pd.to_numeric(tabela["TotalGasto"],errors="coerce")
#excluir coluna inutil
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela = tabela.drop("IDCliente", axis=1)
#excluir coluna completamente vazia
tabela = tabela.dropna(how="all", axis=1)
#excluir linha alguma celula vazia
tabela = tabela.dropna(how="any" , axis=0)

#print(tabela.info()) -> confirmar se esta ok

#analise inicial dos dados
print(tabela["Churn"].value_counts())
#porcentagem
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#grafico p/ comparacao, rodar todas as colunas comparando com churn
for todex in tabela.columns:
    #criar grafico
    grafico = px.histogram(tabela,x=todex,color="Churn",text_auto=True)
    #exibir grafico
    grafico.show()

#Considerações:
#serviço de fibra cancela mais,
#cliente menos meses cancela mais,
#tipo contrato mensal cancela mais,
#clientes pagam boleto eletronico cancelam mais
#clientes gastam menos cancelam mais