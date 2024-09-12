faturamento = 1000 # tipo: int -> numero inteiro
custo = 300.0 # tipo: float -> numero com casa decimal
novas_vendas = 100
faturamento = faturamento + novas_vendas
lucro = faturamento - custo 
imposto = faturamento * 0.1
margem_lucro = lucro / faturamento
mensagem = "o faturamento da loja foi de tanto"
email = "casadodentista@gmail.com" # tipo string -> texto




print("o faturamento foi de",faturamento)
print("o custo foi de",custo)
print("o lucro foi de",lucro)
print("a margem de lucro foi de", round(margem_lucro, 2)) # round= aredonda casa decimais