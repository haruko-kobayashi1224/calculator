answer=""

while answer != "n":

  num1 = int(input("1つ目の数値を入力してください: "))

  sign = input("演算子を入力してください (+, -, *, /): ")

  num2 = int(input("2つ目の数値を入力してください: "))
  
  
  if sign == "+":
    print( num1 + num2 )
  elif sign == "-":
    print( num1 - num2 )
  elif sign == "*":
    print( num1 * num2 )
  elif  sign == "/":
    print( num1 / num2 ) 
   
  answer = input("計算を続けますか？(y/n)")
if answer == "n":
  print("終了しました")
  
    





    
      