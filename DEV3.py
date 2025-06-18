import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 2, 3], [4, 2, 5]])

# Display various properties of the array
print("Array is of type:", type(arr))
print("Number of dimensions:", arr.ndim)
print("Shape of array:", arr.shape)
print("Size of array (total elements):", arr.size)
print("Array stores elements of type:", arr.dtype)



import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3]
y = [2, 4, 1]

# Plotting the graph
plt.plot(x, y)

# Adding labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My First Graph')

# Display the graph
plt.show()



import matplotlib.pyplot as plt

# Data
a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

# Plotting
plt.plot(a, label='a')
plt.plot(b, "or", label='b (red circles)')
plt.plot(list(range(0, 22, 3)), label='range 0-21 by 3')
plt.plot(c, label='4th Rep')

# Customizing axes
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

# Data
a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

# Create figure with 4 subplots
fig = plt.figure(figsize=(10, 10))

# Subplot 1
sub1 = plt.subplot(2, 2, 1)
sub1.plot(a, 'sb')  # square blue markers
sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st Rep')

# Subplot 2
sub2 = plt.subplot(2, 2, 2)
sub2.plot(b, 'or')  # circle red markers
sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd Rep')

# Subplot 3
sub3 = plt.subplot(2, 2, 3)
sub3.plot(list(range(0, 22, 3)), 'vg')  # triangle down green markers
sub3.set_xticks(list(range(0, 10, 1)))
sub3.set_title('3rd Rep')

# Subplot 4
sub4 = plt.subplot(2, 2, 4)
sub4.plot(c, 'Dm')  # diamond magenta markers
sub4.set_yticks(list(range(0, 24, 2)))
sub4.set_title('4th Rep')

plt.tight_layout()
plt.show()
