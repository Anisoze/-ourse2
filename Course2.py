
def ask(num1,num2):
    while(True):
        f=(input())
        if(len(f)==0 or ord(f)<ord(str(num1)) or ord(f)>ord(str(num2))):
            print("\nwrong input\n")
        else:
            return int(f)




def open_image():
    print("\nchoose Image:\n1 - white_and_black_bin.png\n2 - grayscale.jpeg\n3 - color.jpeg\n4 - RAW\n5 - other\n")
    im = ask(1,5)
        
    if (im==1):
        filename="white_and_black_bin.png"
    elif(im==2):
        filename="grayscale.jpeg"
    elif(im==3):
        filename="color.jpeg"
            
    elif(im==4):
        img=RAW(0, 2)
            
    elif(im==5):
        print("\ninput name\n")
        filename = input()
        
    if(im!=4):
        with Image.open(filename) as img:
            img.load()

    img.show() 



def open_data():

    print("\nchoose data:\n1 - text_small.txt\n2 - text_rus.txt\n3 - w_and_b_raw\n4 - grayscale_raw\n5 - color_raw\n6 - pride_and_prejudice.txt\n7 - other\n")       #open data
    f=ask(1,7)
    if(f==1):
        name="text_small.txt"

    elif(f==2):
        name="text_rus.txt"
    
    elif(f==3):
        name="w_and_b_raw"
   
    elif(f==4):
        name="grayscale_raw"
    
    elif(f==5):
        name="color_raw"

    elif(f==6):
        name="pride_and_prejudice.txt"

    elif(f==7):
        print("\nenter name\n")
        name=input()
    
    #if(f==1 or f==2):
        #file = open(name, "r", encoding="utf-8")
    #else:
    file=open(name, "rb")
    data = file.read()
    #file2 = open("out", "wb")
    return data, name











def RAW(img, num):               #work with RAW of image
               
    f = num
                
    if (f==1):      #save raw
        print("\nchoose out:\n1 - saved_raw\n2 - other\n")        
        f2=ask(1,2)
        if(f2==1):
            name="saved_raw"
        else:
            print("\nenter name\n")
            name=input()
            
        print("\nchoose mode:\n1 - RGB\n2 - L\n")
        f2=ask(1,2)
        if(f2==1):
            rgb=True
        else:
            rgb=False
            
                        #save raw as array
        if(rgb):    #rgb
            obj=img.load()
            B=np.zeros([img.height,img.width, 3], dtype=np.uint8)
            #data2=bytearray()                
            for i in range(img.height):
                for j in range(img.width):
                    for c in range (3):
                        B[i,j, c]=obj[j, i][c]
                        #data2.append(obj[j, i][c])
            file=open(name,"wb")
            np.save(file, B)
            file.close()
                

        else:   #not rgb
            obj=img.load()
            B=np.zeros([img.height,img.width], dtype=np.uint8)
            for i in range(img.height):
                for j in range(img.width):
                    B[i,j]=obj[j, i]
            file=open(name,"wb")
            np.save(file, B)
            file.close()
                
        return img
                    
                    

    else:           #open raw
        
        while(True):
            print("\nchoose open:\n1 - w_and_b_raw\n2 - grayscale_raw\n3 - color_raw\n4 - re_out.txt\n5 - other\n")
            f2=ask(1,5)
            if(f2==1):
                name="w_and_b_raw"  
            
            elif(f2==2):
                name="grayscale_raw"  
                
            elif(f2==3):
                name="color_raw"  
                
            elif(f2==4):
                name="re_out.txt" 
                
            elif(f2==5):
                print("\nenter name\n")
                name=input()
                    
            file=open(name,"rb")
            A=np.load(file)
            file.close()
                
            if(f2==4):
                print("\nchoose mode:\n1 - RGB\n2 - L\n")
                f2=ask(1,2)
                if(f2==1):
                    mod="RGB"
                else:
                    mod="L"
         
            elif(f2==3):
                mod="L"
                mod="RGB"

            else:
                mod="L"

            img=Image.fromarray(A, mode=mod)
            return img












def LL_code_for_len(L):                     #get symbols for length and extra bits from LL table from RFC 1951
    
    if(L<11):           #no extra bits
        return 254+L

    elif(L==258):       
        return 285

    else:               #with extra bits
        k=11
        for i in range(5):
            if(L < k + (2**(3+i)) ):
                a=(L-k)//(2**(1+i))
                b=L-(k+(2**(1+i))*a)
                return 265+(i*4)+a, b
               
            else:
                k+=(2**(3+i))
                




def len_from_LL_code(val, extra):                     #get length from symbols and extra bits  from LL table from RFC 1951          #reverse
    
    if(val<265):           #no extra bits
        return val-257+3

    elif(val==285):       
        return 258

    else:               #with extra bits
        k=(val-265)//4
        pos=(val-265)%4
        L=11
        for i in range(k):
            L+=(2**(3+i))
        for i in range(pos):
            L+=2**(1+k)
            
        return L+extra
            








def LL_code_for_dist(Dist):             #get symbols for distance and extra bits from LL table from RFC 1951
    
    if(Dist<5):           #no extra bits
        return Dist-1


    else:               #with extra bits
        
        k=5
        for i in range(13):
            if(Dist < k + (2**(2+i)) ):
                a=(Dist-k)//(2**(1+i))
                b=Dist-(k+(2**(1+i))*a)
                return 4+(i*2)+a, b
               
            else:
                k+=(2**(2+i))










def dist_from_LL_code(val, extra):             #get distance from symbols and extra bits from LL table from RFC 1951            #reverse
    
    if(val<4):           #no extra bits
        return val+1


    else:               #with extra bits
        k=(val-4)//2
        pos=(val-4)%2
        Dist=5
        for i in range(k):
            Dist+=(2**(2+i))
        for i in range(pos):
            Dist+=2**(1+k)
            
        return Dist+extra














def LZSS(data, type_, frequencies, buffer):                                         #LZSS
    

    #process
    #put end of block after the data (256)
    #use LZSS on data
    #back reference only of len >= 3
    




    #print("\nchoose type:\n1 - quick\n2 - medium\n3 - long\n")
    #type_=ask(1,3)
    #if(type_==2):
        #print("\nenter time search\n")
        #max_time=int(input())
    max_time=100
 
    data2=[]

    buff_size=32767
    buff=buffer

    list_of_turples=[]
    i=0
    k=0
    q=0
    
    if(frequencies):
        frequencies_LL=[0 for j in range(286)]
        frequencies_Distance=[0 for j in range(30)]

    i=len(buff)
    data=buff+data

    while(i<len(data)):
        buff=data[max(i-buff_size,0):i]
        L=0
        start=0      
        l_buff=len(buff)
        if(type_==1):       #quick
            while(True):
                s=data[i:i+L+1]               
                while(len(s)>len(buff) and len(buff)!=0 and 2*len(buff)<buff_size):
                    buff+=buff
                if(buff.find(s)>=0 and i+L < len(data) and L<258):
                    start=buff.find(s)
                    L+=1
                else:
                    break
                    

        elif(type_==2):         #medium
            time=0
            while(True):
                s=data[i:i+L+1]
                while(len(s)>len(buff) and len(buff)!=0 and 2*len(buff)<buff_size):
                    buff+=buff
                if(buff.find(s)>=0 and i+L < len(data) and L<258):
                    start=buff.find(s)                   
                    L+=1
                else:
                    if(i+L < len(data) and L<258):
                        s=s[:-1]
                    new_start=start                   
                    while(time<max_time and len(s)!=0):
                        new=buff.find(s,new_start+1)
                        if(new>=0 and i+L < len(data) and new<l_buff):
                            start=new
                            new_start=start
                            t+=1
                        else:
                            break
                    break
                     
                        
        elif(type_==3):         #long
            while(True):
                s=data[i:i+L+1]
                while(len(s)>len(buff) and len(buff)!=0 and 2*len(buff)<buff_size):
                    buff=buff+buff
                if(buff.find(s)>=0 and i+L < len(data) and L<258):
                    start=buff.find(s)
                    L+=1
                else:
                    if(i+L < len(data) and L<258):
                        s=s[:-1]
                    new_start=start
                    while(len(s)!=0):
                        new=buff.find(s,new_start+1)
                        if(new>=0 and i+L < len(data) and new<l_buff):                          
                            start=new
                            new_start=start
                        else:
                            break
                    break

        if(L>=3):        #turple

            if(L<11 or L==258):
                one=LL_code_for_len(L)
                data2.append(one)
                if(frequencies):
                    frequencies_LL[one]+=1
            else:
                one, two=LL_code_for_len(L)
                data2.append(one)
                data2.append(two)
                if(frequencies):
                    frequencies_LL[one]+=1
                
            if(l_buff-start < 5):
                one=LL_code_for_dist(l_buff-start)
                data2.append(one)
                if(frequencies):
                    frequencies_Distance[one]+=1
            else:
                one, two=LL_code_for_dist(l_buff-start)
                data2.append(one)
                data2.append(two)
                if(frequencies):
                    frequencies_Distance[one]+=1
                
            i+=L-1

            


        else:       #single
            if(L==2):
                data2.append(data[i])
                data2.append(data[i+1])
                if(frequencies):
                    frequencies_LL[data[i]]+=1
                    frequencies_LL[data[i+1]]+=1
                i+=1
                
            else:
                data2.append(data[i])      
                if(frequencies):
                    frequencies_LL[data[i]]+=1
   
        i+=1
            

        

       
    data2.append(256)           #end of block
    buff=data[max(len(data)-1-buff_size,0):]
    if(frequencies):
        frequencies_LL[256]+=1
        return data2, frequencies_LL, frequencies_Distance, buff
    else:
        return data2, buff


















def decode_LZSS(data, data2):                  #decode LZSS                    

    i=0
    while(i<len(data)):
        
        if(data[i]>256):        #length
            
            if(data[i]<265 or data[i]==285):        #no extra bits
                a=len_from_LL_code(data[i], 0)
                
            else:                   #with extra bits
                a=len_from_LL_code(data[i], data[i+1])
                i+=1
            i+=1
            if(data[i]<4):      #distance
                b=dist_from_LL_code(data[i], 0)
            else:               #with extra bits
                b=dist_from_LL_code(data[i], data[i+1])
                i+=1
                
            dt=data2
            ln=len(dt)
            for j in range(a):
                #s=chr(dt[(ln - b + j)%ln])
                data2.append(dt[(ln - b + j)%ln])
            

        else:                   #literal
            s=chr(data[i])
            data2.append(data[i])
        
        i+=1
            
    return data2





















def bytes_to_bits(data, reverse):            #turn bytes to bits
    data2=""
    for i in data:
        d=bin(i)[2:]
        if(len(d)<8):
            d="0"*(8-len(d))+d
        if(reverse):
            d=d[::-1]
        data2+=d      
    return data2






def pack_bit_to_byte(data):            #pack 8 bits to byte
    data2=data[::-1]
    data2=int('0b'+data2,2)

    return data2






def num_to_bit_from_least(num):        #make a number to bitstream putting from least significant bit  (using rule #1)
    bitstream=bin(num)[2:]      
    return bitstream[::-1]
        
    



def bit_to_num_from_least(bit):
    bit=bit[::-1]
    return int("0b"+bit,2)




def data_to_save(data):                 #at the end of Deflate
    data2=bytearray()
    b=len(data)%8
    if(b>0):
        a=1
    else:
        a=0
    data2.append(b)
    for i in range((len(data)//8) + a):
        data2.append(pack_bit_to_byte(data[8*i:8*i+8]))
    
    return data2








def data_from_save(data):                 #at the start of reverse Deflate
    if(data[0]!=0):
        a=True
        b=8-data[0]
    else:
        a=False
    data=bytes_to_bits(data[1:], True)
    if(a):
        data=data[:-b]

    return data








def block_zero(data, last):           #make a block type 0       - not compressed
    
    #parts:
    #is_last        1 - last ; 0 - not last     1 bit
    #btype (type of block)    (00)              2 bits
    #padding - 00000  to make full byte         5 bits
    #len - number of bytes of data              16 bits       max len 65 535
    #bitstream    - the data, length of len     ... bits



    data2=""
    
    if(last):           #is last
        data2+="1"
    else:
        data2+="0"
        
    data2+="00"          #type
    
    data2+="00000"      #padding
    
    ln=num_to_bit_from_least(len(data))     #len
    data2+=ln
    data2+="0"*(16-len(ln))
    
    data2+=bytes_to_bits(data, False)     #bitstream
    
    return data2
    



















def make_fixed_codes():                         #fixed codes for block type 1
    fixed_codes_LL=[0 for i in range(288)]
    
        
    base=48                                 #0-143
    for i in range(144):
        a=bin(base+i)[2:]
        fixed_codes_LL[i]="0"*(8-len(a))+a
        

    place=144                               #144-255
    base=400                            
    for i in range(112):
        a=bin(base+i)[2:]
        fixed_codes_LL[place+i]=a
    

                                       
    place=256                               #256-279
    for i in range(24):
        a=bin(i)[2:]
        fixed_codes_LL[place+i]="0"*(7-len(a))+a


    place=280                               #280-287
    base=192                           
    for i in range(8):
        a=bin(base+i)[2:]
        fixed_codes_LL[place+i]=a


    fixed_codes_Distance=[]                  #Distance 0-31
    for i in range(32):
        a=bin(i)[2:]
        fixed_codes_Distance.append("0"*(5-len(a))+a)
    

    return fixed_codes_LL, fixed_codes_Distance












def block_one(data, last, fixed_codes_LL, fixed_codes_Distance, buffer):            #make a block type 1       - compressed with fixed Huffman codes
    
    #parts:
    #is_last        1 - last ; 0 - not last     1 bit
    #btype (type of block)    (10)              2 bits
    #bitstream    - the data                    ... bits

    #Huffman codes for literal and lengths are from table in RFC 1951
    #0-143 - 8 bits
    #144-255 - 9 bits
    #256-279 - 7 bits
    #280-287 - 8 bits

    #Huffman codes for distance are all 5 bits



    data2=""
    
    if(last):           #is last
        data2+="1"
    else:
        data2+="0"
        
    data2+="10"          #type
    
    data, buffer=LZSS(data, 3, False, buffer)      #using the LZSS on data
    
    #print(data)
    
    i=0                                 #fixed Huffman codes
    while(i<len(data)):
        data2+=fixed_codes_LL[data[i]]
        
        if(data[i]>256):                                  #Length
            
            if(data[i]>264 and data[i]<285):             #with exta bits
                b=data[i]
                i+=1
                a=num_to_bit_from_least(data[i])
                data2+=a 
                data2+="0"*((((b-265)//4) +1) - len(a))
                
            i+=1
            data2+=fixed_codes_Distance[data[i]]        #Distance
            
            if(data[i]>3):                          #with extra bits
                b=data[i]
                i+=1
                a=num_to_bit_from_least(data[i])
                data2+=a
                data2+="0"*((((b-4)//2) +1) - len(a))
        i+=1
            

    
    return data2















def form_inner_nodes(A, n):                                #part one of getting lengths from frequencies
    #формирование внутренних узлов

    s=0
    r=0
    for t in range(n-1):
        #выбираем первый узел потомок
        if((s>n-1) or (r<t and A[r]<A[s])):
            #выбираем внутренний узел
            A[t]=A[r]
            A[r]=t+1
            r+=1
        else:
            #выбираем лист
            A[t]=A[s]
            s+=1
            
        #выбираем втором потомок
        if((s>n-1) or (r<t and A[r]<A[s])):
            #внутренний
            A[t]=A[t]+A[r]
            A[r]=t+1
            r+=1
        else:
            #лист
            A[t]=A[t]+A[s]
            s+=1

    return A






def form_lens(A, n):                                                                       #part two of getting lengths from frequencies
    
    #преобразование индексов родительских узлов в значения глубин каждого узла
    A[n-1]=-1
    A[n-2]=0
    t=n-2
    while(t>-1):
        A[t]=A[A[t]-1]+1
        t-=1
        
    #преобразование значения глубины внутренних узлов в значения глубины листьев (длин кодов)
    a=0
    u=0
    d=0
    t=n-2
    x=n-1
    while(True):
        #определяем количество узлов с глубиной d
        while(t>=0 and A[t]==d):
            u+=1
            t-=1
        #назначаем листьями узлы, которые не являются внутренними
        while(a>u):
            A[x]=d
            x-=1
            a-=1
        #переходми к следующему значению глубины
        a=2*u
        d+=1
        u=0
        if(a<=0):
            break
        
    return A






def get_lengths_from_frequencies(table):                #make table of frequencies to the table of lengths for codes 
    
    non_zero=[]
    for i in range(len(table)):                      #выбор ненулевых частот
        if(table[i]!=0):
            non_zero.append((i, table[i]))
            
    non_zero.sort(key=lambda x: (x[1], x[0]))
    
    A=list(list(zip(*non_zero))[1])                   #взять частоты    
    n=len(A)       
    if(n==1):
        table[non_zero[0][0]]=A[0]
    else:
        A=form_inner_nodes(A,n)                        #формирование внутренних узлов  
        A=form_lens(A, n)                              #формирование длин

        for i in range(n):                       #назначение длин
            table[non_zero[i][0]]=A[i]
   
    return table









def num_of_code_len(A):                                #get number of entries for each length
    B=[]
    m=max(A)
    A=''.join([str(A[i]) for i in range(len(A))])
    for i in range(m+1):
        if(i==0):
            B.append(0)             #zero to not make unnecessary values
        else:
            B.append(A.count(str(i)))
    return B





def get_numerical_value(max_bits, bl_count):                #get base value of each length for a table
    next_code=[]
    code=0
    bits=1
    next_code.append(0)
    while(bits<=max_bits):
        code=(code+bl_count[bits-1])<<1
        next_code.append(code);
        bits+=1

    return next_code



def assign_numerical_value(table, next_code):               #make a dictionary for table of lengths
    n=0
    dictionary={}
    for i in range(len(table)):
        if(table[i]!=0):
            a=bin(next_code[table[i]])[2:]
            a="0"*(table[i]-len(a))+a
            dictionary[i]=a
            next_code[table[i]]+=1
    return dictionary
            













def final_table_LL_and_Distance(table_LL, table_Distance, no_Distance):                          #use functons to get final tables for LL and Distance
    print("\n\n")
    print(table_LL)
    
    
    table_LL=get_lengths_from_frequencies(table_LL)                  #get table of lengths from frequencies         LL
    print("\n\ntable_LL")
    print(table_LL)


    bl_count_LL=num_of_code_len(table_LL)                   #find number of codes of given each length          LL
    print("\n\nbl_count_LL")
    print(bl_count_LL)
    
    next_code_LL=get_numerical_value(max(table_LL), bl_count_LL)                  #find base values for each length         LL
    print("\n\nnext_code_LL")
    print(next_code_LL)

    
    codes_LL=assign_numerical_value(table_LL, next_code_LL)                                     #make prefix codes          LL
    print("\n\ncodes_LL")
    print(codes_LL)
    
    a=0
    DIST=0
    for i in range(len(table_LL)):
        if(table_LL[i]!=0):
            a=i
            


    if(no_Distance==False):     #if Distance not empty
        print("\n\n")
        print(table_Distance)
        
        table_Distance=get_lengths_from_frequencies(table_Distance)                 #get table of lengths from frequencies      Distance
        print("\n\ntable_Distance")
        print(table_Distance)
        
        bl_count_Distance=num_of_code_len(table_Distance)                       #find number of codes of given each length   Distance
        print("\n\nbl_count_Distance")
        print(bl_count_Distance)
        
        next_code_Distance=get_numerical_value(max(table_Distance), bl_count_Distance)      #find base values for each length    Distance
        print("\n\nnext_code_Distance")
        print(next_code_Distance)
        
        codes_Distance=assign_numerical_value(table_Distance, next_code_Distance)           #make prefix codes              Distance
        print("\n\ncodes_Distance")
        print(codes_Distance)


        for i in range(len(table_Distance)):
            if(table_Distance[i]!=0):
                DIST=i
    else:
        codes_Distance=0
            
    HLIT=a+1-257
    
    return table_LL, table_Distance, codes_LL, codes_Distance, HLIT, DIST











def make_CL_stream(table):                          #making of CL stream
    CL_stream=[]
    k_of_symbol=0
    k_of_zero=0
    for i in range(len(table)):       
        if(table[i]==0):            #found zero      
            if(k_of_symbol!=0):                             #left symbols            
                while(k_of_symbol>2):                       #>=3 symbols
                    CL_stream.append(16)                 
                    if(k_of_symbol>6):                      #more than can put
                        CL_stream.append(3)
                        k_of_symbol-=6                    
                    else:                                   #put all
                        CL_stream.append(k_of_symbol-3)
                        k_of_symbol=0
                        
                for j in range(k_of_symbol):                #<=2 symbols
                    CL_stream.append(last_sym)
                    
                k_of_symbol=0
                        
            k_of_zero+=1
            


            
        elif(table[i]<16):           #found symbol       
            if(k_of_zero!=0):                                #left zeros               
                while(k_of_zero>10):                         #>=11 zeros
                    CL_stream.append(18)                  
                    if(k_of_zero>138):                       #more that can put
                        CL_stream.append(127)
                        k_of_zero-=138                       
                    else:                                    #put all
                        CL_stream.append(k_of_zero-11)      
                        k_of_zero=0
                    
                while(k_of_zero>2):                          #>=3 zeros
                    CL_stream.append(17)                   
                    if(k_of_zero>6):                         #more than can put
                        CL_stream.append(3)
                        k_of_zero-=6                        
                    else:                                    #put all
                        CL_stream.append(k_of_zero-3)
                        k_of_zero=0
                                
                for j in range(k_of_zero):                   #<=2 zero
                    CL_stream.append(0)
                    
                k_of_zero=0
                     
            if(i!=0 and table[i]==table[i-1]):               #repeat of symbol
                k_of_symbol+=1
                last_sym=table[i]
            else:                                            #no repeat
                if(k_of_symbol!=0):
                    while(k_of_symbol>2):                       #>=3 symbols
                        CL_stream.append(16)                 
                        if(k_of_symbol>6):                      #more than can put
                            CL_stream.append(3)
                            k_of_symbol-=6                    
                        else:                                   #put all
                            CL_stream.append(k_of_symbol-3)
                            k_of_symbol=0
                        
                    for j in range(k_of_symbol):                #<=2 symbols
                        CL_stream.append(last_sym)
                    
                    k_of_symbol=0
                    
                CL_stream.append(table[i])
                last_sym=table[i]
            
        else:
            print("\nproblem - length in table >15\n")
            return


    if(k_of_symbol>0):                              #left symbols
        while(k_of_symbol>2):                       #>=3 symbols
            CL_stream.append(16)                 
            if(k_of_symbol>6):                      #more than can put
                CL_stream.append(3)
                k_of_symbol-=6                    
            else:                                   #put all
                CL_stream.append(k_of_symbol-3)
                k_of_symbol=0
                        
        for j in range(k_of_symbol):                #<=2 symbols
            CL_stream.append(last_sym)                   
        k_of_symbol=0

    if(k_of_zero>0):
        while(k_of_zero>10):                         #>=11 zeros
            CL_stream.append(18)                  
            if(k_of_zero>138):                       #more that can put
                CL_stream.append(127)
                k_of_zero-=138                       
            else:                                    #put all
                CL_stream.append(k_of_zero-11)      
                k_of_zero=0
                    
        while(k_of_zero>2):                          #>=3 zeros
            CL_stream.append(17)                   
            if(k_of_zero>6):                         #more than can put
                CL_stream.append(3)
                k_of_zero-=6                        
            else:                                    #put all
                CL_stream.append(k_of_zero-3)
                k_of_zero=0
                                
        for j in range(k_of_zero):                   #<=2 zero
            CL_stream.append(0)                  
        k_of_zero=0

    return CL_stream









def rearrange_table_CL(table):                      #rearrange the table for CL
    table_CL=[]
    for i in range(3):
        table_CL.append(table[16+i])
    table_CL.append(table[0])
    
    k=8
    for i in range(15):
        if(i%2==0):
            k+=i
        else:
            k-=i
        table_CL.append(table[k])
        
    return table_CL
    

def rearrange_table_CL_back(table):                      #return table for CL to normal
    table_CL=[]

    table_CL.append(table[3])
    for i in range(7):
        table_CL.append(table[17-2*i])
        
    for i in range(8):
        table_CL.append(table[4+2*i])
    
    for i in range(3):
        table_CL.append(table[i])
        
    return table_CL







def final_table_CL(CL_LL, CL_Distance):              #use functons to get final tables for LL and Distance
    print("\n\nCL_LL")
    print(CL_LL)
    print("\n\nCL_Distance")
    print(CL_Distance)


    table_CL=[0 for i in range(19)]                 #make frequencies for CL
    i=0
    while(i<len(CL_LL)):
        if(CL_LL[i]>15):
            table_CL[CL_LL[i]]+=1
            i+=1
        else:
            table_CL[CL_LL[i]]+=1
        i+=1
        
    i=0
    while(i<len(CL_Distance)):
        if(CL_Distance[i]>15):
            table_CL[CL_Distance[i]]+=1
            i+=1
        else:
            table_CL[CL_Distance[i]]+=1
        i+=1
    print("\n\n")
    print(table_CL)



    table_CL=get_lengths_from_frequencies(table_CL)         #get table of lengths from frequencies      CL
    print("\n\ntable_CL")
    print(table_CL)
    

    bl_count_CL=num_of_code_len(table_CL)                   #find number of codes of given each length       CL
    print("\n\nbl_count_CL")
    print(bl_count_CL)

    
    next_code_CL=get_numerical_value(max(table_CL), bl_count_CL)           #find base values for each length      CL
    print("\n\nnext_code_CL")
    print(next_code_CL)

    
    codes_CL=assign_numerical_value(table_CL, next_code_CL)                   #make prefix codes      CL
    print("\n\ncodes_CL")
    print(codes_CL)


    table_CL=rearrange_table_CL(table_CL)                   #rearrange table                CL
    print("\n\ntable_CL")
    print(table_CL)
    

    for i in range(len(table_CL)):                          #get HCLEN
        if(table_CL[i]!=0):
            HCLEN=i
            
    HCLEN=HCLEN + 1 - 4
    

    table_CL=table_CL[0:HCLEN+4]                             #cut the table          CL
    print("\n\ntable_CL")
    print(table_CL)

    return table_CL, codes_CL, HCLEN










def use_CL_codes_on_stream(CL_stream, codes):                   #use CL codes on CL stream of LL or Distance
    data2=""
    
    i=0
    while(i<len(CL_stream)):
        data2+=codes[CL_stream[i]]    
        
        if(CL_stream[i]>15):
            a=CL_stream[i]
            i+=1
            b=num_to_bit_from_least(CL_stream[i])
            
            if(a==16):
                n=(2-len(b))           
            elif(a==17):
                n=(3-len(b))      
            else:
                n=(7-len(b))
                
            b+="0"*n
            data2+=b
        
        i+=1

    return data2







def block_two(data, last, buffer):                                         #make a block type 2       - compressed with dynamic Huffman codes
    
    #process:
    #use LZSS
    #construct the LL codes and the Distance codes  (with frequencies of LL symbols and frequencies of Distances using Huffman)         LL and Distance codes are limited to 15 bit lengths
    #encode tables for dynamic LL and Distance into the streams of CL  - [] like output of LZSS, using the CL table
    #create a prefix code for CL symbols    -    using symbols frequencies
    #use the codes on turned tables of LL and Distance - store in the header
    #use dynamic codes on LZSS symbols to make bitstream
    

    #each block can have different prefix codes, encoded in the block header
    #LL and Distance codes encoded using third prefix code - 'code length' - CL   - turn tables in [] like output of LZSS, then make codes using frequencies

    #table for CL:
    #0-15 - lengths 0-15
    #16 - repeat previous length x+3 time (followed by 2 bit value x)
    #17 - repeat a zero length y+3 time (followed by 3 bit value y)
    #18 - repeat a zero length z+11 time (followed by 7 bit value z)
    #x, y and z - offset values -> rule #1
    #same CL prefix code is used for LL and Distance tables - frequencies are summed from LL and Distance
    #code lengths for CL symbols are limited to 7 bits
    #each code can be stored in 3 bits


    #parts of header:
    #is_last                                                             1 - last ; 0 - not last     1 bit
    #btype (type of block)      (01)                                     2 bits
    #HLIT - (number of LL code entries present) minus 257                5 bits            - cut out the rest table
    #DIST - (number of Distance code entries present) minus 1            5 bits            - cut out the rest table
    #HCLEN - (number of CL code entries present) minus 4                 4 bits            - cut out the rest table, but table in order: 16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15
    #CL length    - the table for CL   - numbers -> rule #1              3*HCLEN + 4 bits
    #LL and Distance lengths - table using the CL codes                  .. bits
    #bitstream    - the data                                             ... bits

    data2=""

    if(last):           #is last
        data2+="1"
    else:
        data2+="0"
        
    data2+="01"          #type
    
    data, table_LL, table_Distance, buffer=LZSS(data, 3, True, buffer)      #using the LZSS on data     and get the frequencies
     
    #print(data)
    if(max(table_Distance)>0):
        no_Distance=False
    else:
        no_Distance=True
    
    table_LL, table_Distance, codes_LL, codes_Distance, HLIT, DIST = final_table_LL_and_Distance(table_LL, table_Distance, no_Distance)      #find tables and codes for LL and Distance
      
    table_LL=table_LL[0:HLIT+257]                   #cut tables
    table_Distance=table_Distance[0:DIST+1]
    print("\n\ntable_LL")
    print(table_LL)
    print("\n\ntable_Distance")
    print(table_Distance)

    HLIT=num_to_bit_from_least(HLIT)        #use rule #1 on HLIT and DIST
    HLIT+="0"*(5-len(HLIT))
    DIST=num_to_bit_from_least(DIST)
    DIST+="0"*(5-len(DIST))
    data2+=HLIT
    data2+=DIST
    
    #print(HLIT)
    #print(DIST)



    CL_LL=make_CL_stream(table_LL)                                          #make the stream of CL
    if(CL_LL==None):
        print("\n\nthe reading block is too long\n\n")
        return
    CL_Distance=make_CL_stream(table_Distance)

    

    table_CL, codes_CL, HCLEN = final_table_CL(CL_LL,CL_Distance)           #find table and codes for CL
    
    HCLEN=num_to_bit_from_least(HCLEN)        #use rule #1 on HCLEN
    HCLEN+="0"*(4-len(HLIT))
    data2+=HCLEN
    
    #print(HCLEN)


    CL_LL=use_CL_codes_on_stream(CL_LL, codes_CL)                       #use CL codes on CL streams
    CL_Distance=use_CL_codes_on_stream(CL_Distance, codes_CL)

    
    for i in table_CL:                      #put CL table in the header
        a=num_to_bit_from_least(i)
        a+="0"*(3-len(a))
        data2+=a
            
    data2+=CL_LL                #put coded tables of LL and Distance in the header
    data2+=CL_Distance
    



    i=0
    while(i<len(data)):                                 #code the data with dynamic LL and Distance
        data2+=codes_LL[data[i]]
        
        if(data[i]>256):                                  #Length
            
            if(data[i]>264 and data[i]<285):             #with exta bits
                b=data[i]
                i+=1
                a=num_to_bit_from_least(data[i])
                data2+=a 
                data2+="0"*((((b-265)//4) +1) - len(a))
                
            i+=1
            data2+=codes_Distance[data[i]]        #Distance
            
            if(data[i]>3):                          #with extra bits
                b=data[i]
                i+=1
                a=num_to_bit_from_least(data[i])
                data2+=a
                data2+="0"*((((b-4)//2) +1) - len(a))
        i+=1
   
    return data2, buffer












def get_CL_stream(data, H, codes, i):               #get the CL stream for tables of LL or Distance
    j=0
    table=[]
    while(j<H):                   
        sr=""
        while(True):
            sr+=data[i]
            if(sr in codes):                   #found a code
                table.append(codes[sr])
                        
                if(codes[sr]>15):              #with extra bits
                    i+=1
                    if(codes[sr]==16):         
                        a=data[i:i+2]
                        i+=1
                        j+=3
                    elif(codes[sr]==17):
                        a=data[i:i+3]
                        i+=2
                        j+=3        
                    elif(codes[sr]==18):
                        a=data[i:i+7]
                        i+=6
                        j+=11
                    a=bit_to_num_from_least(a)
                    table.append(a)
                    j+=a
                else:
                    j+=1
                break
                    
            else:                                 #no code found
                i+=1
        i+=1

    return table, i








def get_table_from_CL_stream(stream, ln):            #get table for LL or Distance from CL stream
    i=0
    table=[]
    while(i<len(stream)):
        if(stream[i]<16):       #literal
            table.append(stream[i])          
        else:
            if(stream[i]==16):
                a=table[-1]     
                i+=1
                for j in range(stream[i]+3):
                    table.append(a)               
            elif(stream[i]==17):  
                i+=1
                for j in range(stream[i]+3):
                    table.append(0)  
            elif(stream[i]==18):
                i+=1
                for j in range(stream[i]+11):
                    table.append(0)  
        i+=1
            
    for i in range(ln-len(stream)):
        table.append(0)
        
    return table











def turn_dictionary(table, next_code):                              #change place of keys and values in dictionary
    codes_tmp=assign_numerical_value(table, next_code)                   #make prefix codes  
    codes_tmp=codes_tmp.items()
    codes={}
    for j in codes_tmp:
        codes[j[1]]=j[0]
    print("\n\ncodes")
    print(codes)
    
    return codes











def decode_Deflate(data, data2):                   #decode Deflate
    i=0
    not_last=True
    #data2=bytearray()
    o=1
    print("")
    while(not_last):
        print(o)
        o+=1
        tmp=data[i]
        if(tmp=="1"):
            not_last=False
        tmp=data[i+1:i+3]
        if(tmp=="00"):
            block_type=0
        elif(tmp=="10"):
            block_type=1
        else:
            block_type=2
        i+=3
        


        if(block_type==0):                                                  #decode block type 0
            i+=5
            ln=data[i:i+16]
            ln=ln[::-1]
            ln=int('0b'+ln,2)
            i+=16
            for j in range(ln):
                a=data[i+8*j:i+8+8*j]
                a=int('0b'+a,2)
                data2.append(a)
            i+=ln
            






            
        elif(block_type==1):                                                    #decode block type 1      
            fixed_codes_LL, fixed_codes_Distance=make_fixed_codes() 
            val=0
            sr=""
            dt=[]
            while(val!=256):      
                sr+=data[i]
                
                if(sr in fixed_codes_LL):           #have found a code
                    val=fixed_codes_LL.index(sr)
                    dt.append(val)
                    #print(sr)
                    sr=""
                    i+=1
                    if(val>256):                    #length                       
                        if(val>264 and val<285):                #with exta bits        
                            k=((val-265)//4)+1
                            for j in range(k):
                                sr+=data[i+j]
                            sr=sr[::-1]
                            sr=int("0b"+sr,2)
                            dt.append(sr)
                            sr=""
                            i+=k
                          
                        sr=data[i:i+5]
                        sr=int("0b"+sr,2)      #Distance
                        i+=5
                        dt.append(sr)
                        if(sr>3):                       #with extra bits
                            k=((sr-4)//2)+1
                            sr=""
                            for j in range(k):
                                sr+=data[i+j]
                            sr=sr[::-1]
                            sr=int("0b"+sr,2)
                            dt.append(sr)
                            sr=""
                            i+=k
                        else:
                            sr=""
                else:                               #haven't found a code
                    i+=1
            
            dt.pop(-1)
            #print(dt)
            data2=decode_LZSS(dt, data2)










        else:                                                                             #decode block type 2
            
            HLIT=data[i:i+5]        #number of LL code entries present
            HLIT=bit_to_num_from_least(HLIT) + 257
            #print(HLIT)           
            i+=5
            
            HDIST=data[i:i+5]       #number of Distance code entries present
            HDIST=bit_to_num_from_least(HDIST) + 1
            #print(HDIST)  
            i+=5
            
            HCLEN=data[i:i+4]       #number of CL code entries present
            HCLEN=bit_to_num_from_least(HCLEN) + 4
            #print(HCLEN)  
            i+=4
            
            table_CL=[]                     #get table CL from header
            for j in range(HCLEN):
                tmp=data[i:i+3]
                table_CL.append(bit_to_num_from_least(tmp))
                i+=3
            
            for j in range(19-HCLEN):       #place missing part of CL table
                table_CL.append(0)
               
                    
            print("\n\ntable_CL")
            print(table_CL)

            table_CL=rearrange_table_CL_back(table_CL)      #rearrange table of CL
            
            print("\n\ntable_CL")
            print(table_CL)
            
            bl_count_CL=num_of_code_len(table_CL)                   #find number of codes of given each length       CL
            print("\n\nbl_count_CL")
            print(bl_count_CL)

    
            next_code_CL=get_numerical_value(max(table_CL), bl_count_CL)           #find base values for each length      CL
            print("\n\nnext_code_CL")
            print(next_code_CL)

    
            codes_CL=turn_dictionary(table_CL, next_code_CL)                 #get prefix codes      CL
            
            
            
            table_LL, i=get_CL_stream(data, HLIT, codes_CL, i)             #get stream CL for LL
            print("\n\nstream_LL")
            print(table_LL)
        
            
            table_Distance, i = get_CL_stream(data, HDIST, codes_CL, i)    #get stream CL for Distance
            print("\n\nstream_Distance")
            print(table_Distance)
            

            table_LL=get_table_from_CL_stream(table_LL, 286)               #get table for LL from CL stream
            print("\n\ntable_LL")
            print(table_LL)
            
            table_Distance=get_table_from_CL_stream(table_Distance, 30)   #get table for Distance from CL stream
            print("\n\ntable_Distance")
            print(table_Distance)
            
            
            bl_count_LL=num_of_code_len(table_LL)                   #find number of codes of given each length
            bl_count_Distance=num_of_code_len(table_Distance)
            print("\n\nbl_count_LL")
            print(bl_count_LL)
            print("\n\nbl_count_Distance")
            print(bl_count_Distance)
    
            next_code_LL=get_numerical_value(max(table_LL), bl_count_LL)                              #find base values for each length
            next_code_Distance=get_numerical_value(max(table_Distance), bl_count_Distance)
            print("\n\nnext_code_LL")
            print(next_code_LL)
            print("\n\nnext_code_Distance")
            print(next_code_Distance)
            
            codes_LL=turn_dictionary(table_LL, next_code_LL)                                #make prefix codes
            codes_Distance=turn_dictionary(table_Distance, next_code_Distance)   

            

            sr=""
            val=0
            dt=[]
            while(val!=256):        #decode main data
                sr+=data[i]
                
                if(sr in codes_LL):           #have found a code
                    val=codes_LL[sr]
                    dt.append(val)
                    #print(sr)
                    sr=""
                    i+=1
                    if(val>256):                    #length                       
                        if(val>264 and val<285):                #with exta bits        
                            k=((val-265)//4)+1
                            for j in range(k):
                                sr+=data[i+j]
                            sr=bit_to_num_from_least(sr)
                            dt.append(sr)
                            sr=""
                            i+=k
                          
                        while(True):       #Distance
                            sr+=data[i]
                            if(sr in codes_Distance):                               
                                break
                            else:
                                i+=1     
                        i+=1
                        sr=codes_Distance[sr]
                        dt.append(sr)
                        if(sr>3):                       #with extra bits
                            k=((sr-4)//2)+1
                            sr=""
                            for j in range(k):
                                sr+=data[i+j]
                            sr=bit_to_num_from_least(sr)
                            dt.append(sr)
                            sr=""
                            i+=k
                        else:
                            sr=""
                else:                               #haven't found a code
                    i+=1
            
            dt.pop(-1)
            #print("\n\n")
            #print(dt)
            data2=decode_LZSS(dt, data2)              #decode LZSS stream

            





    return data2
        

















   











    






#rule #1
#числа добавляются в стек с менее значимого бита
#хаффман с более значимого
#при формировании байта происходит разворот, так числа оказываются в обычном представлении, а хаффман в реверсивном


                #### Начало ###


from PIL import Image           
from io import BytesIO
import numpy as np
import math


    

                            

tmp=0


            
while(True):
    print("\nchoose action:\n1 - use Deflate\n2 - decode Deflate\n3 - open image\n4 - exit\n")
    f=ask(1,4)
    
        

    if(f==1):          #Deflate
        print("\nchoose:\n1 - auto\n2 - manual\n")
        f2=ask(1,2)
        data, name=open_data() 
        if(f2==2):
            print("\nchoose block:\n1 - type 0\n2 - type 1\n3 - type 2\n")
            f2=ask(1,3)
        else:
            if(name=="grayscale_raw" or name=="color_raw" or len(data)<1000):
                f2=2
            else:
                f2=3
            
        if(f2==1):
            #print(data)                         #block type 0
            data=block_zero(data,True) 
            #print(data)
        
        elif(f2==2):                            #block type 1
            
            fixed_codes_LL, fixed_codes_Distance=make_fixed_codes()         #generate fixed codes
            #print(data)
            buffer=bytearray()
            data=block_one(data,True,fixed_codes_LL, fixed_codes_Distance, buffer)          #use block one
            #print(data)
        
        elif(f2==3):
            print("\n\nenter size of block 2\n")
            size=int(input())
            times=len(data)//size
            the_data=[]
            buffer=bytearray()
            if(len(data)%size!=0):
                times+=1
                
            print("")
            #dt2=bytearray()
            for i in range(times):   
                print(i+1)
                if(i==times-1):
                    dt, buffer=block_two(data[i*size:i*size+size],True, buffer)
                else:
                    dt, buffer=block_two(data[i*size:i*size+size],False, buffer)

                #dt2=decode_Deflate(dt, dt2)
                #file=open("re_out.txt", "wb")
                #file.write(dt2)
                #file.close()
                
                the_data.append(dt)
            data=""
            for i in range(len(the_data)):
                data+=the_data[i]
            #print(data)

        if(data!=None):
            data=data_to_save(data)         #put in form for saving   - turn bitstream to bytes           

        #print(data)
        if(data!=None):
            file=open("out.txt", "wb")
            file.write(data)
            file.close()






        
    elif(f==2):                                 #decode Deflate
        file=open("out.txt", "rb")
        data=file.read()
        file.close()
        
        #print("\n\n")
        #print(data)
        
        data=data_from_save(data)     

        #print("\n\n")
        #print(data)
        
        
        data=decode_Deflate(data, bytearray())
        
        #print("\n\n")
        #print(data)

        file=open("re_out.txt", "wb")
        file.write(data)
        file.close()



    elif(f==3):             #open image
        open_image()
        



    elif(f==4):         #exit
        break