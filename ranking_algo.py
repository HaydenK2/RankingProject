import csv
import numpy as np
import matplotlib.pyplot as plt

#   [0,0,0]: idx 0 = first choice, idx 1 = 2nd choice, idx 2 = 3rd choice
# data_umpressed = {"Design #1": [0,0,0], "Design #2": [0,0,0], "Design #3": [0,0,0], "Design #4": [0,0,0], "Design #5": [0,0,0], "Design #6": [0,0,0]}
data_umpressed = [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]



with open('data\DesignMerchHouseVote.csv', mode = 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for lines in reader:
        choice1 = int(lines[1][-1]) - 1
        choice2 = int(lines[2][-1]) - 1
        choice3 = int(lines[3][-1]) - 1

        data_umpressed[choice1][0] += 1
        data_umpressed[choice2][1] += 1
        data_umpressed[choice3][2] += 1


            
        # data = lines.split(',')
        # print(lines)
    
print(data_umpressed)

#  All First Choices
choice1All = [data_umpressed[i][0] for i in range(len(data_umpressed))]
# print(choice1All)
#  All Second Choices
choice2All = [data_umpressed[i][1] for i in range(len(data_umpressed))]
print(choice2All)
#  All Third Choices
choice3All = [data_umpressed[i][2] for i in range(len(data_umpressed))]
print(choice3All)

#   graphs

barWidth = 0.25
fig = plt.subplots(figsize =(12, 8)) 


br1 = np.arange(len(choice1All)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

plt.bar(br1, choice1All, color ='b', width = barWidth, 
        edgecolor ='grey', label ='1st Choice') 
plt.bar(br2, choice2All, color ='r', width = barWidth, 
        edgecolor ='grey', label ='2nd Choice') 
plt.bar(br3, choice3All, color ='g', width = barWidth, 
        edgecolor ='grey', label ='3rd Choice') 

plt.xlabel('Designs', fontweight ='bold', fontsize = 15) 
plt.ylabel('Votes', fontweight ='bold', fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(choice1All))], 
        ['Design #1', 'Design #2', 'Design #3', 'Design #4', 'Design #5', 'Design #6'])

plt.legend()
plt.show() 



