#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：叶福
日期：2022年5月9日
"""


# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数





    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


    #编写执行代码,代码完成后将pass删除





    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

    #编写执行代码,代码完成后将pass删除
print("欢迎使用RPSLS游戏")
import random
def rpsls():
   dict1={'石头':0,'史波克':1,'纸':2,'蜥蜴':3,'剪刀':4}
   dict2={0:'石头',1:'史波克', 2:'布',3:'蜥蜴',4:'剪刀'}
   a=eval(input("您的选择为："))
   b=random.randrange(0,4)
   if(a in dict1):
      c=dict1[a]
      d=dict2[b]
      if c==0:
          if b-c>=3:
              print ("电脑的选择为%s,您赢了"%(d))
          elif b==c:
              print("电脑的选择为%s,平局"%(d))
          else:
              print("电脑的选择为%s,电脑赢了" % (d))
      elif 0<c<5:
          if b-c>=1:
              print("电脑的选择为%s,电脑赢了" % (d))
          elif b==c:
              print("电脑的选择为%s,平局" % (d))
          else:
              print("电脑的选择为%s,您赢了" % (d))
   elif(a not in dict1):
       print("Error:No Correct Name")

rpsls()








 # 输出"-------- "进行分割
 # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

 # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

# 在屏幕上显示计算机选择的随机对象

# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
 # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
 #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试


