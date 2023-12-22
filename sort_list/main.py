'''
https://edabit.com/challenge/NM8JbG5K2ajKjkqpj
In this solution, I used two different approach.
1. If conditionals to choose correct sort type.
2. dict data type instead of if conditionals.
You can find both below...

'''
#Approach 1 (If conditionals)
def sort_list_with_ifs(lst, sort_type='Asc'): #lst as list, sort_type as string(Default='Asc')
    if sort_type=='Asc':
        lst.sort()
    elif sort_type=='Des':
        lst.sort(reverse=True)
    return lst

def sort_list(lst, sort_type='Asc'): #lst as list, sort_type as string(Default='Asc')
    
    def sort_asc(lst):
        lst.sort()
        return lst
    
    def sort_des(lst):
        lst.sort(reverse=True)
        return lst
    
    def sort_none(lst):
        return lst
    
    dict_sort_type={
        'Asc': sort_asc,
        'Des': sort_des,
        'None': sort_none
    }

    return dict_sort_type[sort_type](lst)

lst=[1,5,3,4,7,2,9,6,8]
print(sort_list(lst, 'Asc'))
print(sort_list_with_ifs(lst, 'Des'))



