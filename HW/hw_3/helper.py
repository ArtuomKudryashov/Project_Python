def task(a):
    print("Task " + str(a))


def count_family_numbers (f,sc):
    membersFam_1 = f.split(',')
    membersFam_2= sc.split(',')

    countFam_1=len(membersFam_1)
    countFam_2=len(membersFam_2)

    if countFam_1> countFam_2:
        return ("The First Family is bigger. " +f )
    elif countFam_1<countFam_2:
        return ("The Second Family is bigger. "+ sc)
    else:
        return ("Both families are equal")



def list_to_set (T_list):
    my_set = set(T_list)
    return my_set

