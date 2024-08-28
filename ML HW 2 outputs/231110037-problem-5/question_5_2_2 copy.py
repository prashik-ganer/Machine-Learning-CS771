import math
import numpy as np
import matplotlib.pyplot as plt
import random

# ridgetest = "ridgetest.txt"
# ridgetrain = "ridgetrain.txt"

file_path = "kmeans_data.txt"


try:
    with open(file_path, "r") as file:
        # Read the contents of the file
        file_contents = file.read()
        words = file_contents.split()
        # print(words)

        x = []
        y = []


        for j in range(0, len(words), 2):
            for i in range(2):
                if i ==0:
                    x.append(words[j+i])
                if i ==1:
                    y.append(words[j+i])
                # print(words[j+i])

            # print("\n")

            # for j in range(len(words)):
            #     # x.append(file_contents)
            #     print(i).
        x_sq_plus_y_sq = []
        print("x",x)
        print("y",y)

        list_of_list = []
        for i,j in zip(x,y):
            # print(i,j)
            temp = []
            i_int = float(i)
            j_int = float(j)
            temp.append(i_int)
            temp.append(j_int)
            list_of_list.append(temp)
            temp = i_int*i_int+j_int*j_int
            x_sq_plus_y_sq.append(temp)

        # print(x_sq_plus_y_sq)
        print(list_of_list)

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")





def rbf_kernel_temp(x_n,x_m):
    gamma = 0.1
    # rbf_kernel_value = math.exp(-1*gamma*math.sqrt(abs(x_n-x_m)))

    transformed_list = []
    for i1,i2 in zip(x_n,x_m):
        temp = math.exp(-1*gamma*((abs(float(i1)-float(i2)))**2))
        transformed_list.append(temp)
    # print("transformed_list: ", transformed_list)

    x = np.array(x_n)
    y = np.array(x_m)
    l2_norm = np.linalg.norm(x - y)
    return math.exp(-1*gamma*(l2_norm))
    # print("final: ",math.exp(-1*gamma*(l2_norm)))

# def kernel(x,y):
#   x = np.array(x)
#   y = np.array(y)
#   l2_norm = np.linalg.norm(x - y)
#   return math.exp(-1*gamma(l2_norm))



for i in range(10):
    final_list= []
    random_number = random.randint(1, len(list_of_list))

    for index,i in enumerate(list_of_list):

        final_list.append(rbf_kernel_temp(list_of_list[index],list_of_list[random_number]))

    cluster1_mean = final_list[0]
    cluster2_mean = final_list[1]


    for i in range(10):
        mean_1 = cluster1_mean
        mean_2 = cluster2_mean
        cluster1 = []
        cluster2 = []
        cluster1_index = []
        cluster2_index = []
        for index,i in enumerate(final_list):
            distance_1 = abs(i-mean_1)
            distance_2 = abs(i-mean_2)
            if distance_1 < distance_2:
                cluster1.append(i)
                cluster1_index.append(index)
            else:
                cluster2.append(i)
                cluster2_index.append(index)

        # cluster means updated


        cluster1_mean = np.mean(cluster1)
        cluster2_mean = np.mean(cluster2)

        cluster1_index_x1 = []
        cluster1_index_x2 = []
        cluster2_index_x1 = []
        cluster2_index_x2 = []
        # for i in range(len(list_of_list)):
        for i in cluster1_index:
            cluster1_index_x1.append(list_of_list[i][0])
            cluster1_index_x2.append(list_of_list[i][1])

        for i in cluster2_index:
            cluster2_index_x1.append(list_of_list[i][0])
            cluster2_index_x2.append(list_of_list[i][1])



    color_values = ['red', 'green', 'blue', 'yellow', 'orange']

    # Scatter plot
    plt.scatter(cluster1_index_x1, cluster1_index_x2, marker='o', c='r')
    plt.scatter(cluster2_index_x1, cluster2_index_x2, marker='o', c='g')
    plt.scatter(list_of_list[random_number][0], list_of_list[random_number][1], marker='o', c='b')



    # Customize the plot
    plt.title('Scatter Plot with Four Lists')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')

    # Show the plot
    plt.show()
