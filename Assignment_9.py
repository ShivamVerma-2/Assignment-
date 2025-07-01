import numpy as np

print("1️⃣ Combining 1D and 2D NumPy Arrays")
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
combined = np.vstack((b, a))
print("\n", combined)

print("\n2️⃣ Flatten a 2D array into 1D")
c = np.array([[1, 2], [3, 4]])
print("\n", c.flatten())

print("\n3️⃣ Reverse a NumPy array")
d = np.array([10, 20, 30, 40])
print("\n", d[::-1])

print("\n4️⃣ Practice Operations")

arr = np.array([[2, 5, 8], [1, 9, 4]])

print("\nMaximum value:", np.max(arr))
print("Minimum value:", np.min(arr))

print("\nShape (rows, columns):", arr.shape)

print("\nSelect all elements:")
for row in arr:
    for item in row:
        print(item, end=" ")

print("\n\nSelect specific element (row 1, col 2):", arr[1, 2])

print("\nSum of values using loop:")
total = 0
for row in arr:
    for item in row:
        total += item
print(total)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("\nAddition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
