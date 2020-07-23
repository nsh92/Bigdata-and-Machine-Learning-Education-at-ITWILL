'''
step05 문제

문) price에는 과일 가게에 진열된 과일과 가격이 저장되어 있고, 
      buy에는 고객이 구매한 장바구니이다.
      
      list + for 형식1)을 적용하여 구매 상품 총 금액(tot_bill)을 계산하시오.      
'''

# 과일가게 진열 상품
price = {'사과':2000, '복숭아' : 3000, '딸기' : 2500}

# 구매 상품
buy = {'사과' : 3, '딸기' : 5}

# 구매 상품 총 금액 / 와꾸 : tot_bill = [실행문 for]

i=v=0

bill = []
for i1, v1 in price.items():
   for i2, v2 in buy.items():
       if i1 == i2:
           bill.append(v1*v2)
print(bill)
sum(bill)

tot_bill = [price[b] * buy[b] for b in buy]
print(tot_bill)
print('총 구매 금액 =', sum(tot_bill))