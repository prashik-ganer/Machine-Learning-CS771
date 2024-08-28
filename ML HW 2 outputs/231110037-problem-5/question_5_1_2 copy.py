import math
import numpy as np
import matplotlib.pyplot as plt
import random

# ridgetest = "ridgetest.txt"
# ridgetrain = "ridgetrain.txt"

ridgetest = "ridgetest.txt"
ridgetrain = "ridgetrain.txt"
try:
    with open(ridgetrain, "r") as file:
        # Read the contents of the file
        ridgetrain_content = file.read()
        words = ridgetrain_content.split()
        # print(words)
        # print("entered!!!!")
        x = []
        y = []
        ridgetrain_x = []
        ridgetrain_y = []
        for j in range(0, len(words), 2):
            for i in range(2):
                if i ==0:
                    ridgetrain_x.append(float(words[j+i]))
                if i ==1:
                    ridgetrain_y.append(float(words[j+i]))
        # print(x)
        # print(y)
        # print("ridgetrain_y")
        # print(ridgetrain_y)
        list_of_list = []
        for i,j in zip(ridgetrain_x,ridgetrain_y):
            # print(i,j)
            temp = []
            i_int = float(i)
            j_int = float(j)
            temp.append(i_int)
            temp.append(j_int)
            list_of_list.append(temp)
        # print(list_of_list)
        # print(y)




except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")



# x_n = list_of_list[0][0]
# x_m = list_of_list[1][0]
def rbf_kernel(x_n,x_m):
    gamma = 0.1
    rbf = math.exp(-1*gamma*(np.linalg.norm(float(x_n)-float(x_m))**2))
    return rbf
# print(np.linalg.norm(x_n-x_m)**2)


Ls = [2, 5, 20, 50, 100]


for L in Ls:
    lamda=0.1
    landmarks=[]
    for i in range(L):
        random_number = random.randint(0, len(ridgetrain_y)-1)
        landmarks.append(random_number)
    transformed_data = []
    for i in range(len(ridgetrain_x)):
        temp=[]
        for j in range(L):
            temp.append(rbf_kernel(ridgetrain_x[landmarks[j]],ridgetrain_x[i]))
        transformed_data.append(temp)
    Identity_matrix=np.identity(L)
    W=np.dot(np.transpose(transformed_data),transformed_data)
    W=W+lamda*Identity_matrix
    W=np.linalg.inv(W)
    XTY=np.dot(np.transpose(transformed_data),ridgetrain_y)
    W=np.dot(W,XTY)
    try:
        with open(ridgetest, "r") as file:
            # Read the contents of the file
            ridgetrain_content = file.read()
            words = ridgetrain_content.split()

            ridgetest_x = []
            ridgetest_y = []
            for j in range(0, len(words), 2):
                for i in range(2):
                    if i ==0:
                        ridgetest_x.append(float(words[j+i]))
                    if i ==1:
                        ridgetest_y.append(float(words[j+i]))
            # print(x)
            # print(y)
            # print("ridgetest_x")
            # print(ridgetrain_y)
            list_of_list_test = []
            for i,j in zip(ridgetest_x,ridgetest_y):
                # print(i,j)
                temp = []
                i_int = float(i)
                j_int = float(j)
                temp.append(i_int)
                temp.append(j_int)
                list_of_list_test.append(temp)
            transformed_test_data = []
            for i in range(len(list_of_list_test)):
                temp=[]
                for j in range(L):
                    temp.append(rbf_kernel(ridgetrain_x[landmarks[j]],ridgetest_x[i]))
                transformed_test_data.append(temp)

        # print(ridgetest_x)
        # print(ridgetest_y)

    except FileNotFoundError:
        print(f"The file {ridgetest} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")







    pred=[]
    print(W)
    for i in range(len(list_of_list_test)):
        pred.append(np.dot(W,np.transpose(transformed_test_data[i])))
    # print(pred)
    # print("pred!")
    # print(ridgetest_x)
    # print(ridgetest_y)
    # print(len(pred))
    # print(len(ridgetest_y))
    # print(pred)

    # RMS
    sum =0
    for i in range(0,len(pred)):
        sum += (list_of_list_test[i][1]-pred[i])**2
    MSE = sum/len(pred)
    RSME = math.sqrt(MSE)

    print("ROOT MEAN SQUARE VALUE FOR LAMBDA", L," is: ", RSME)


    plt.scatter(ridgetest_x,ridgetest_y, marker='o', c='blue')
    plt.scatter(ridgetest_x,pred, marker='o', c='red')
    # Customize the plot
    # plt.title('For lamda ='+str(index))
    plt.xlabel('X-axis ')
    plt.ylabel('Y-axis ')
    # Show the plot
    plt.show()





