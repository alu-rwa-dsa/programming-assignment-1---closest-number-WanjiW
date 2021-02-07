# make a closest number function to find out which two pairs have the smallest difference
# Author: Wanjiru Wang'ondu

# first, we create an array

arrA = [-20, -40, 3, 4, 6, 77, 89, 90]


def finding_differences(arr):
    arr.sort()
    diff_list = {}
    array_a = []
    for i in arr:
        for j in arr:
            if i != j:
                # because of smallest absolute difference
                # 1, 2 = difference of 1
                # 2, 3 = 1
                # 3, 4 = 1
                difference = abs(i - j)

                # we do this because for 1, 1234, we have done all the combos for 1 so we don't need one to be done
                # again continue means just go ahead if we've already checked the number
                # if not, proceed
                if j in array_a:
                    continue
                array_a.append(i)
                if difference in diff_list:
                    diff_list[difference].append(i)
                    diff_list[difference].append(j)

                #     here, we do this because if the difference hasn't been added yet, just add as the value
                #  the one up means append to the already existing value
                else:
                    diff_list[difference] = [i, j]
    diff_keys = list(diff_list.keys())
    diff_keys.sort()
    return diff_list[diff_keys[0]]

    # sorts from smallest to largest
    # print(diff_list[0])


print(finding_differences(arrA))
