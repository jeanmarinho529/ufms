def ler_produtos():
    produtos = []
    n = int(input())
    for _ in range(n):
        produto = input().strip()
        preco = float(input().strip())
        
        if any(p == produto for p, _ in produtos):
            print("Produto já cadastrado")
        else:
            produtos.append((produto, preco))
    
    return produtos

def buscar_precos(produtos):
    while True:
        nome = input().strip()
        if nome == "Fim":
            break
        encontrado = False
        for produto, preco in produtos:
            if produto == nome:
                print(f"{preco:.2f}")
                encontrado = True
                break
        if not encontrado:
            print("Produto nao cadastrado")

produtos = ler_produtos()
buscar_precos(produtos)