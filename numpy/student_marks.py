import numpy as np
# data
hours = np.array([1,2,3,4,5,6,7,8])
marks = np.array([30,40,50,60,70,80,90,56])

# model
w = 10
b = 10
# prediction
prediction = w * hours + b
# error
error = prediction - marks
# loss
loss = np.mean(error **2)


print("prediction: ", prediction)
print("loss:", loss)

new_hours = 6
new_mark = w * new_hours + b

print("prediction marks: ", new_mark)
