import numpy as np


arr = np.array([[1, 2, 3], [4, 2, 5]])


print("Array is of type:", type(arr))
print("Number of dimensions:", arr.ndim)
print("Shape of array:", arr.shape)
print("Size of array (total elements):", arr.size)
print("Array stores elements of type:", arr.dtype)



import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 1]

plt.plot(x, y)


plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My First Graph')


plt.show()



import matplotlib.pyplot as plt
a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]


plt.plot(a, label='a')
plt.plot(b, "or", label='b (red circles)')
plt.plot(list(range(0, 22, 3)), label='range 0-21 by 3')
plt.plot(c, label='4th Rep')


plt.xlabel('Day->')
plt.ylabel('Temp->')
plt.legend()

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_bounds(3, 40)

plt.xticks(list(range(3, 10)))
plt.yticks(list(range(3, 20, 3)))

plt.title("Customized Line Plot")
plt.grid(True)
plt.show()



import matplotlib.pyplot as plt


a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]


fig = plt.figure(figsize=(10, 10))


sub1 = plt.subplot(2, 2, 1)
sub1.plot(a, 'sb')  
sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st Rep')


sub2 = plt.subplot(2, 2, 2)
sub2.plot(b, 'or')  
sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd Rep')


sub3 = plt.subplot(2, 2, 3)
sub3.plot(list(range(0, 22, 3)), 'vg')  
sub3.set_xticks(list(range(0, 10, 1)))
sub3.set_title('3rd Rep')

sub4 = plt.subplot(2, 2, 4)
sub4.plot(c, 'Dm')  
sub4.set_yticks(list(range(0, 24, 2)))
sub4.set_title('4th Rep')

plt.tight_layout()
plt.show()
