import random, unittest, DLL_mod 

def random_number():
    i=random.randint(0,100)
    return i

def Node_create(i):
    Node=DLL_mod.Node(i)
    return Node


class Linked_List_2_Tests(unittest.TestCase):

#Тесты для метода add_in_tail

    def test_add_in_tail_in_empty_list(self):
        # Проверка add_in_tail при пустом списке
        LL_1=DLL_mod.LinkedList()
        i=random_number()
        Node=Node_create(i)
        if LL_1.len()==0:
            LL_1.add_in_tail(Node)
        Node_LL_1=LL_1.head
        self.assertEqual(Node_LL_1.value,i)

    def test_add_in_tail_with_one_element(self):
        # Проверка add_in_tail для списка с одним элементом
        LL_1=DLL_mod.LinkedList()
        data=[]
        for i in range(0,2):
            j=random_number()
            data.append(j)
            Node=Node_create(j)
            LL_1.add_in_tail(Node)
        Node_LL_1=LL_1.head
        for i in range(0,len(data)):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next

    def test_add_in_tail_in_random_len_ll(self):
        #Проверка add_in_tail для списка слючайной длины
        LL_1=DLL_mod.LinkedList()
        data=[]
        random_len=random.randint(5,10)
        random_number=random.randint(1,random_len-1)
        for i in range(0,random_len):
            data.append(random.randint(100,10**8))
        for j in range(0,len(data)):
            Node=Node_create(data[j])
            LL_1.add_in_tail(Node)  
        Node_LL_1=LL_1.head
        for i in range(0,len(data)):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next

#Конец теста для add_in_tail

#Тест для методов find и find_all 
    
    def test_find(self):
        # Тест метода find
        LL_1=DLL_mod.LinkedList()
        data=[]
        random_len=random.randint(5,10)
        random_number=random.randint(1,random_len-1)
        for i in range(0,random_len):
            data.append(random.randint(100,10**8))
        for j in range(0,len(data)):
            Node=Node_create(data[j])
            LL_1.add_in_tail(Node)
        value_for_find=data[random_number]
        found_value=LL_1.find(value_for_find)
        self.assertEqual(found_value.value,value_for_find)

    def test_find_all(self):
        # Тест метода find_all
        LL_1=DLL_mod.LinkedList()
        data=[]
        result=[]
        test_len=30
        value_for_find=random_number()
        for i in range(0,test_len):
            if i%5==0:
                data.append(value_for_find)
            else:
                data.append(random.randint(100,10**8))
        for i in range(0,len(data)):
            Node=Node_create(data[i])
            LL_1.add_in_tail(Node)
            if data[i]==value_for_find:
                result.append(data[i])
        founded_values=LL_1.find_all(value_for_find)
        for i in range(0,len(result)):
            founded_Node=founded_values[i]
            self.assertEqual(founded_Node.value,result[i])

#Конец тестов find и find_all

#Тесты delete
 
    def test_delete(self):
        #Удаление первого и последнего эл-тов
        LL_1=DLL_mod.LinkedList()
        data=[]
        test_len=10
        for i in range(0,test_len):
            data.append(random.randint(1,10**8))
        for i in range(0,len(data)):
            Node=Node_create(data[i])
            LL_1.add_in_tail(Node)
        LL_1.delete(data[0])
        data.remove(data[0])
        Node_LL_1=LL_1.head
        for i in range(0,len(data)):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next
        LL_1.delete(data[len(data)-1])
        data.remove(data[len(data)-1])
        Node_LL_1=LL_1.head
        for i in range(0,len(data)):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next

    def tast_random_delete(self):
        #Удаление случайного эл-та
        LL_1=DLL_mod.LinkedList()
        data=[]
        test_len=random.randint(5,10)
        number_for_delete=random.randint(1,len(test_len)-1)
        for i in range(0,test_len):
            data.append(random.randint(10,10**8))
        for i in range(0,test_len):
            Node=Node_create(data[i])
            LL_1.add_in_tail(Node)
        LL_1.delete(data[number_for_delete])
        data.remove(data[number_for_delete])
        Node_LL_1=LL_1.head
        for i in range(0,len(data)):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next

#Конец тестов delete

#Тест clean

    def test_clean(self):
        #Очистка 
        LL_1=DLL_mod.LinkedList()
        data=[]
        test_len=random.randint(5,10)
        for i in range(0,test_len):
            data.append(random.randint(10,10**8))
        for i in range(0,test_len):
            Node=Node_create(data[i])
            LL_1.add_in_tail(Node)
        data.clear()
        LL_1.clean()
        self.assertEqual(LL_1.len(),len(data))

#Конец теста clean

#Тесты для метода insert  

    def test_insert_in_empty_list(self):
        # Проверка ф-ции insert при пустом списке
        LL_1=DLL_mod.LinkedList()
        i=random_number()
        Node=Node_create(i)
        if LL_1.len()==0:
            LL_1.insert(None,Node)
        Node_LL_1=LL_1.head
        self.assertEqual(LL_1.head.value,i)
        for j in range (0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,i)

    def test_insert_with_one_element(self):
        #Проверка ф-ции insert для списка с 1 элементом. Вставка э-та после первого
        #э-та, далее вставка после предварительно вставленного эл-та. 
        LL_1=DLL_mod.LinkedList()
        Q_ty=3
        data=[]
        for i in range (0,Q_ty):
            j=random_number()
            data.append(j)
        LL_1.add_in_tail(Node_create(data[0]))
        LL_1.insert(Node_create(data[0]),Node_create(data[1]))
        LL_1.insert(Node_create(data[1]),Node_create(data[2]))
        Node_LL_1=LL_1.head
        for i in range (0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next


    def test_insert_in_last_position(self):
        #Вставка в конец списка
        LL_1=DLL_mod.LinkedList()
        data=[]
        for i in range(0,10):
            data.append(random_number())
        for i in range(0,10):
            RN=random_number()
            if i==9:
                LL_1.insert(Node_create(data[i]),Node_create(RN))
                data.append(i)
            else:
                LL_1.add_in_tail(Node_create(data[i]))
        Node_LL_1=LL_1.head
        for i in range(0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next

    def test_insert_in_random_position(self):
       #Вставка в случайную позицию, случайного значения
        LL_1=DLL_mod.LinkedList()
        data=[]
        random_len=random.randint(5,10)
        random_number=random.randint(1,random_len-1)
        insert_value=random.randint(1,99)
        for i in range(0,random_len):
            data.append(random.randint(100,10**8))
        for j in range(0,len(data)):
            Node=Node_create(data[j])
            if j == random_number:
                after_Node=Node
            LL_1.add_in_tail(Node)  
        data.insert(random_number+1,insert_value)
        new_Node=Node_create(insert_value)
        LL_1.insert(after_Node,new_Node)
        Node_LL_1=LL_1.head
        for i in range(0,len(data)):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next
    
    #Конец тестов insert    

    #Тесты add_in_head
        
    def test_add_in_head_in_empty_list(self):
        #Тест на добавление в пустой список
        LL_1=DLL_mod.LinkedList()
        i=random_number()
        Node=Node_create(i)
        LL_1.add_in_head(Node)
        Node_LL_1=LL_1.head
        self.assertEqual(Node_LL_1.value,i)

    def test_add_in_head_with_one_element(self):
        #Тест на добавление э-та в список с уже существующим одним э-том
        LL_1=DLL_mod.LinkedList()
        i=random_number()
        j=random_number()
        data=[]
        data.append(j)
        data.append(i)
        Node_0=Node_create(i)
        Node_1=Node_create(j)
        LL_1.add_in_tail(Node_0)
        LL_1.add_in_head(Node_1)
        Node_LL_1=LL_1.head
        for k in range(0,len(data)):
            self.assertEqual(Node_LL_1.value,data[k])
            Node_LL_1=Node_LL_1.next

    def test_add_in_head_with_random_len(self):
        #Тест на вставку э-та на первую позицию при случайной длине списка
        LL_1=DLL_mod.LinkedList()
        data=[]
        random_len=random.randint(5,10)
        insert_value=random.randint(1,99)
        for i in range(0,random_len):
            data.append(random.randint(100,10**8))
        for j in range(0,len(data)):
            Node=Node_create(data[j])
            LL_1.add_in_tail(Node)  
        data.insert(0,insert_value)
        new_Node=Node_create(insert_value)
        LL_1.add_in_head(new_Node)
        Node_LL_1=LL_1.head
        for i in range(0,len(data)):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next

    


    #Конец тестов add_in_head

        

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()