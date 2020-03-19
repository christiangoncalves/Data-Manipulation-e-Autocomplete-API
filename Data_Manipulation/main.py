import requests
import json

# Função auxiliar da função sort() para ordenamento do Json pela Timestamp.
def timestampSort(e):
    return e["timestamp"]

# Função para Consumir os eventos e criar o Timelime.
def getEvent(data):
    comprou = []
    comprou_produto = []
    customData_comprou = []
    customData_comprou_produto = []
    timeline = []
   
    #Split de eventos do Json original.
    for i in data:
        if(i['event'] == 'comprou'):
            comprou.append(i)
        elif(i['event'] == 'comprou-produto'):
            comprou_produto.append(i)

    #Split dos Custom Data's dos eventos.
    for i in comprou:
        customData_comprou.append(i['custom_data'])

    for i in comprou_produto:
        customData_comprou_produto.append(i['custom_data'])

    # Recupera o numero da Transação para ser utilizado na busca dos produtos posteriormente.
    # também recupera o nome da loja para ser utilizado na formação da timeline, visto que a posição do "store_name" não é padrão.
    for i in range(len(customData_comprou)):
        for j in range(len(customData_comprou[i])):
            if(customData_comprou[i][j]["key"] == "transaction_id" ):
                transaction_id = customData_comprou[i][j]["value"]
            if(customData_comprou[i][j]["key"] == "store_name"):
                store_name = customData_comprou[i][j]["value"]
        
        produtos = []
        nome = ""
        preco = ""

        # Recupera o nome e o preço dos produtos para cada "transaction_id", e forma um Json com esses produtos.
        for j in range(len(customData_comprou_produto)):
            for k in range(len(customData_comprou_produto[j])):
                if(customData_comprou_produto[j][k]["value"] == transaction_id):
                    for l in range(len(customData_comprou_produto[j])):
                        if(customData_comprou_produto[j][l]["key"] == "product_name"):
                            nome = customData_comprou_produto[j][l]["value"]

                        if(customData_comprou_produto[j][l]["key"] == "product_price"):
                            preco = customData_comprou_produto[j][l]["value"]
                        
                    produtos.append({"name": nome, "price": preco})
        
        # Utiliza a lista de produtos criadas e injeta na timeline junto com as demais informaçoes.
        timeline.append( {"timestamp": comprou[i]['timestamp'], "revenue": comprou[i]['revenue'], "transaction_id": transaction_id, "store_name": store_name, "products": produtos})
       
        # Ordena a timeline pela Timestamp em modo decrescente utilizando a função auxiliar timestampSort().
        timeline.sort(reverse=True, key=timestampSort)

    return timeline     


if __name__ == "__main__":

    # Recupera todo o Json de eventos.
    request = requests.get('https://storage.googleapis.com/dito-questions/events.json').json()

    # Cria o corpo da Timeline passando o Json de eventos para a função getEvent().
    compras = getEvent(request['events'])

    # Cria toda a Timeline em si.
    json_t = {
      "timeline": compras
    }

    # Imprime a Timeline de maneira identada e utilizando "ensure_ascii" para resolver possiveis problemas de escrita ...
    # ... como por exemplo o "Ç".
    print(json.dumps(json_t, sort_keys=False, indent=2, ensure_ascii=False))