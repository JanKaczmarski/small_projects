

string_for_reverse = "aaaaaa"
string_numbers = "This is 500 plus 300 700  "


def reverse_string(string):
    final_string = ''
    for i in range(1,len(string)+1):
        final_string += string[-i]
    return final_string

def is_pallidrome(string):
    if reverse_string(string) == string:
        return "Pallidrome"
    else:
        return " Not pallidrome"

def count_int_in_str(string):
    """Functions take string and search for integers inside of it and sum them up

    Args:
        string (str): string with numbers

    Returns:
        int: int of summed ints from string 
        int: how many ints where inside string
    """
    result = 0
    number = ''
    int_found = 0
    last_integer = False
    for i in string:
        try:
            if int(i) or int(i) == 0:
                print(i)
                if last_integer:
                    number += i
                else:
                    number += i
                    last_integer = True
                
        except ValueError :
            last_integer = False
            if number:
                int_found += 1
                result += int(number)
                number = ''
            continue
    if type(string[-1]) is int:
        result += int(number)
    return result, int_found

def star_triangle(number):
    """creates star triangle with height of the argument

    Args:
        number (int): height of triangle
    """

    for i in range(number):
        for j in range(i, number):
            print('*', end=' ')
        print()

def sum_of_two(x,y,z):
    for i in x:
        for j in y:
            if i+j == z:
                return True
    return False

def fizzBuzz(number):
    for i in range(1,number+1):
        if i%4==0 and i%6 == 0:
            print('FizzBuzz')
        elif i%6==0:
            print('Buzz')
        elif i%4 == 0:
            print('Fuzz')
        else:
            print(i)
        

def dopelnienie(n):
    return 8999 - n

def czy_k(n,A,B):
    a1 = []
    b1 = []
    a2 = []
    b2 = []
    for k in range(n):
        for i in range(k):
            a1.append(A[i])
        for i in range(n-k,n):
            b1.append(B[i])
        for i in range(k,n):
            a2.append(A[i])
        for i in range(n-k):
            b2.append(B[i])
        if a1==b1 and a2==b2:
            return 'Prawda', k
        else:
            return "Fałsz"
    


def is_first_number(n):
    """ Ex 4.1 from matura 2020"""
    if n>4 and n%2 == 0:
        first_numbers = []
        possible_solutions = []
        dividers = []
        definite_solution = ()
        for liczba in range(2,n):
            if liczba % 2 != 0:
                ilosc_roznych_dzielnikow = 0
                for dzielnik in range(2,liczba):
                    if liczba % dzielnik == 0:
                        ilosc_roznych_dzielnikow += 1
                if ilosc_roznych_dzielnikow == 0:
                    first_numbers.append(liczba)
        
        
        for number in first_numbers:
            for second_number in first_numbers:
                if n == number + second_number:
                    possible_solutions.append((number,second_number,second_number-number))


        if len(possible_solutions) > 1:
            biggest_difference = 0
            for solution in possible_solutions:
                if solution[2] > biggest_difference:
                    biggest_difference = solution[2]    

            for solution in possible_solutions:
                if biggest_difference == solution[2]:
                    return n, solution[0], solution[1]    
                    
        else:
            if len(first_numbers) == 2:
                return n, possible_solutions[0], possible_solutions[1]
            elif len(first_numbers) == 1:
                return n, possible_solutions[0], possible_solutions[0]


def couples(string):
    last_letter = string[0]
    length = 0
    word = ''
    list_of_words = []
    final_list_of_words = []
    i = 0
    biggest_length = 0
    for letter in string:
        if letter == last_letter and i != 1:
            length += 1
            word += letter
        else:
            last_letter = letter
            list_of_words.append((word,length))
            word = last_letter
            length = 1

    list_of_words.append((word,length))        
    
    for word in list_of_words:
        if word[1] > biggest_length:
            biggest_length = word[1]

    for word in list_of_words:
        if word[1] == biggest_length:
            final_list_of_words.append(word)

    if len(final_list_of_words) > 1:
        final_list_of_words.remove(final_list_of_words[1])

    return final_list_of_words[0][0],final_list_of_words[0][1]

    
def jas_malogisa(numbers):
    for number in numbers:
        if number%2 == 0:
            return number

def power_of_three(numbers):
    powers_of_three = []
    for number in numbers:
        if number%3 == 0:
            for i in range(10):
                if 3**i == number:
                    powers_of_three.append(number)
    return len(powers_of_three)

def coma_separated_string_to_list(string):
    last_word = ''
    list_of_words = []
    for letter in string:
        if letter != ';':
            if letter != ',':
                last_word += letter
            else:
                last_word += '.'
        else:
            list_of_words.append(last_word)
            last_word = ''
    if last_word:
        list_of_words.append(last_word)
    return list_of_words

data = ['1;19;0;0;0','1;18;0;0;0','2;22;1;C;1','3;23,6;4;C;1','2;24;1;C;1','1;19;0;0;0']

def exercise_5_1(data):
    gt_eq_20 = 0
    for line in data:
        line_list = coma_separated_string_to_list(line)
        if float(line_list[1]) >= 20:
            gt_eq_20 += 1
    return gt_eq_20

import requests
import json

def does_site_exist(file_path):
    working_sites = []
    not_working_sites = []
    with open(file_path, "r") as file:
        for line in file:
            if requests.get(line[0:-1]).status_code == 200:
                working_sites.append(line[0:-1])
            else:
                not_working_sites.append(line[0:-1])
    return working_sites, not_working_sites

#working_sites, not_working_sites = does_site_exist('C:/Users/janek/Desktop/html vscode/web_sites.txt')



def change_list_into_conj_of_params(my_list, key="id"):
    conj_params = ''
    for param in my_list:
        if my_list.index(param) != len(my_list)-1:
            conj_params += f"{key}={param}&"
        else:
            conj_params += f"{key}={param}"
    return conj_params


