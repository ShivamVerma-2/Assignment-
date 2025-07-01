import numpy as np

print("1️⃣ Create NumPy Arrays")

print("\nRandom 4x2 array:\n", np.random.rand(4, 2))
print("\nEmpty 4x2 array:\n", np.empty((4, 2)))
print("\nFull 4x2 array with 7:\n", np.full((4, 2), 7))
print("\n3x5 array with zeros:\n", np.zeros((3, 5)))
print("\n4x3x2 array with ones:\n", np.ones((4, 3, 2)))

print("\n2️⃣ 3x3 Matrix with Values 2 to 10")

print("\n", np.arange(2, 11).reshape(3, 3))

print("\n3️⃣ Null Vector of Size 10 with 6th Value = 11")

a = np.zeros(10)
a[5] = 11
print("\n", a)

print("\n4️⃣ Reverse an Array")

b = np.array([1, 2, 3, 4, 5])
print("\n", b[::-1])

print("\n5️⃣ Convert Array to Float")

c = np.array([1, 2, 3, 4])
print("\n", c.astype(float))
