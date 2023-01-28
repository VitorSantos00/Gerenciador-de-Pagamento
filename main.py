print("{:/^50}".format(' LOJAS GUARÁ '))
compra = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
  total = compra - (compra * 10 / 100)
elif opcao == 2:
  total = compra - (compra * 5 / 100)
elif opcao == 3:
  parcela = compra / 2
  total = compra
  print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
  total = compra + (compra * 20 / 100)
  meses = int(input('Quantas parcelas? '))
  parcelas = total / meses
  print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(meses, parcelas))
else:
  total = 0
  print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, total))