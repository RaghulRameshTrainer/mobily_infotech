import matplotlib.pyplot as plt

# plt.plot([1,2,3],[4,5,1], 'g',label="July Profit",linewidth=5)
# plt.plot([1,2,3],[5,2,4], 'm',label="August Profit",linewidth=5)
#
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Chart')
# plt.legend()
# plt.grid(True,color='k')
# plt.show()

plt.bar([1,3,5,7,9],[5,2,7,8,2],label='2021 sales')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='2022 sales',color='g')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sales Details')
plt.legend()
plt.show()