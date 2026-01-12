answer=""

   
while answer != "n":
    
  try:    

    num1 = float(input("1つ目の数値を入力してください: "))

    sign = input("演算子を入力してください (+, -, *, /): ")

    num2 = float(input("2つ目の数値を入力してください: "))
    
        
    if sign == "+":
      print("結果:" + str(num1) + "+" + str(num2) + "=" + str(num1+num2))
    elif sign == "-":
      print("結果:" + str(num1) + "-" + str(num2) + "=" + str(num1-num2))
    elif sign == "*":
      print("結果:" + str(num1) + "*" + str(num2) + "=" + str(num1*num2))
    elif  sign == "/": 
      print("結果:" + str(num1) + "/" + str(num2) + "=" + str(num1/num2))
      
    answer = input("計算を続けますか？(y/n)") 
    
  except ZeroDivisionError:
    print("0で割ることはできません")  
    answer = input("計算を続けますか？(y/n)")   
    
            
if answer == "n":
  print("プログラムを終了します。")
  
  
  
    





    
      