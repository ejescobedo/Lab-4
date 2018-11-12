#*******************************************************************************************************************************
#Edgar Escobedo
#80502432
#Lab 4 option B
#*******************************************************************************************************************************
#For this program as a continuation of lab 3, we were to enter all the English words now into a hash table to have a faster accesing time
#In order to do so I would read the file containing all the english words, separate each word that would be inserted into the hash table
#to insert I would use the ascii values of each character of the word and multiply that number using the pow (some value,i) to account for
#the anagrams not causing extra collisions. At the end I would get the load factor by diving the number of elements by the length of the table


#Hash table node and initial setting of hash table that will be used throughout the code
class HashTableNode:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class HashTable:

    def __init__(self, table_size):
        self.table = [None] * table_size


#Next we will have 3 different hashes functions, which would take the ascii value of each character in the word, and multiply it
#using the pow function, the three method vary in the first parameter, second parameter would be the changing i, we do this to
#avoid the collisions of anagrams
    def hash_word1(self, word):
        hash = 0
        for i in range(len(word)):
            letter = ord(word[i])
            letter = letter * (pow(13, i))
            hash += letter
        return hash % len(self.table)


    def hash_word2(self, word):
        hash = 0
        for i in range(len(word)):
            letter = ord(word[i])
            letter = letter * (pow(2, i))
            hash += letter
        return hash % len(self.table)


    def hash_word3(self, word):
        hash = 0
        for i in range(len(word)):
            letter = ord(word[i])
            letter = letter * (pow(9, i))
            hash += letter
        return hash % len(self.table)


#Insert method will account for the 3 different hashes, we use the returned hash value to select the position of the table, then
#using this position we will insert the new word at the beginning of the list, either if it's empty or not
    def insert(self, k, hash):
        if hash == 1:
            position = self.hash_word1(k)
            self.table[position] = HashTableNode(k, self.table[position])
        if hash == 2:
            position = self.hash_word2(k)
            self.table[position] = HashTableNode(k, self.table[position])
        if hash == 3:
            position = self.hash_word3(k)
            self.table[position] = HashTableNode(k, self.table[position])
        if hash ==4:
            position = self.hash_word3(k)
            self.table[position] = HashTableNode(k, self.table[position])



#Search method that will return the node if it's found, if not it will return none
    def search(self, k):
        loc = self.hash(k)
        temp = self.table[loc]
        while temp is not None:
            if temp.item == k:
                return temp
            temp = temp.next
        return None


#In order to get the load factor we will count all the elements in the table and divide that number by the size of the table
    def get_load_factor(self):
        num_elements = 0
        for i in range(len(self.table)):
            temp = self.table[i]

            while temp is not None:
                num_elements += 1
                temp = temp.next
        return num_elements / len(self.table)


#The print table method will first find the list with the greatest length, using that information it will fill a list with the
#If the i of the first loop (the one that we will iterate as many times as the length of the greatest list) matches the length of
#the linked list at the moment, we will update a counter and do so for each index, each time appending the final count(once we iterate the
#hash table) to the list. Then we will sum all the values of the list to have the total sum of lengths and divide by the taken places
#in order to get the average comparisons
    def print_table(self):
        greatest = 0
        for i in range (len(self.table)):
            count = 0
            hashes = ""
            temp = self.table[i]
            while temp is not None:
                hashes += str(temp.item)+" "
                temp = temp.next
                count += 1

            greatest = max(greatest, count)
        print("The size of the longest list of words is: "+str(greatest))
        lst = []
        for x in range(greatest + 1):
            counter_list = 0
            for i in range(len(self.table)):
                count = 0
                temp = self.table[i]
                while temp is not None:
                    temp = temp.next
                    count += 1
                if count == x:
                    counter_list +=1
            lst.append(counter_list)
        total_sum = 0
        for i in range(1, greatest + 1):
            total_sum += lst[i]*i
        taken_indices = len(self.table) - lst[0]
        print("The sum of all the length of the lists sizes is: "+str(total_sum))
        print("The number of taken indices is: "+str(taken_indices))
        print("If we divide the sum of all the lengths of the lists by the total amount of taken places, we will find the average number ")
        print("of comparisons required to perform a successful retrieve operation, which is "+ str(total_sum/taken_indices)+" in this case.")


#Showing outputs
table1 = HashTable(443730)
table2 = HashTable(470000)
table3 = HashTable(400000)
table4 = HashTable(500000)
my_file = open("words_alpha.txt", "r")
passwords_list = my_file.readlines()
counter = 0
while (counter != len(passwords_list)):
    list_x = passwords_list[counter]
    wrds = list_x.split()
    table1.insert(wrds[0], 1)
    table2.insert(wrds[0], 2)
    table3.insert(wrds[0], 3)
    table4.insert(wrds[0], 4)
    counter = counter + 1

print("===============================================================================================================")
print("============================================Hash Table 1=======================================================")
print("                                  Please stand by while we load the table                                 ")
table1.print_table()
print("The load factor for first table is : "+str(table1.get_load_factor()))

print("===============================================================================================================")
print("============================================Hash Table 2=======================================================")
print("                                  Please stand by while we load the table                                 ")
table2.print_table()
print("The load factor for second table is : "+str(table2.get_load_factor()))

print("===============================================================================================================")
print("============================================Hash Table 3=======================================================")
print("                                  Please stand by while we load the table                                 ")
table3.print_table()
print("The load factor for third table is : "+str(table3.get_load_factor()))

print("===============================================================================================================")
print("============================================Hash Table 4=======================================================")
print("                                  Please stand by while we load the table                                 ")
table4.print_table()
print("The load factor for third table is : "+str(table4.get_load_factor()))
