import math
import numpy as np
import matplotlib.pyplot as plt
kernelized_list = []


file_path = "kmeans_data.txt"



try:
    with open(file_path, "r") as file:
        # Read the contents of the file
        file_contents = file.read()
        words = file_contents.split()
        # # temp_list = []
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
        # print(list_of_list)
        # print(lines)

        # kernelized_list.append()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# Now we have data in 1 dimensional
cluster1_mean = x_sq_plus_y_sq[0]
cluster2_mean = x_sq_plus_y_sq[1]

def k_means(cluster1_mean_arg,cluster2_mean_arg):
    for i in range(10):
        mean_1 = cluster1_mean_arg
        mean_2 = cluster2_mean_arg
        cluster1 = []
        cluster2 = []
        cluster1_index = []
        cluster2_index = []
        for index,i in enumerate(x_sq_plus_y_sq):
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






    # print(cluster1_mean)
    # print(cluster2_mean)

    color_values = ['red', 'green', 'blue', 'yellow', 'orange']

    # Scatter plot
    plt.scatter(cluster1_index_x1, cluster1_index_x2, marker='o', c='r')
    plt.scatter(cluster2_index_x1, cluster2_index_x2, marker='o', c='g')


    # Customize the plot
    plt.title('Scatter Plot with Four Lists')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')

    # Show the plot
    plt.show()



k_means(cluster1_mean,cluster2_mean)

