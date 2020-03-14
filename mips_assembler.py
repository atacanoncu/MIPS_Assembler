#            Atacan Deniz Öncü
#            2243566
#            CNG 331 Term Project

import numpy as np

def type_finder(instr): #FUNCTION THAT FINDS THE TYPE OF THE INSTRUCTION
    checker=0
    while(checker < len(typeFinder)): #LOOPS THE ARRAY UNTIL IT FINDS THE TYPE
        if(instr == typeFinder[checker][0]):
            return typeFinder[checker][1]
        checker=checker+1
    
def upon_type_call(instype): #FUNCTION THAT FINDS THE HEX VALUE AFTER FINDING THE TYPE OF THE INSTRUCTION
    if(instype == "j"): #IF IT IS A J TYPE INSTRUCTION     
        opcode = get_opcode_j() #GET OPCODE
        instrAddress = get_instrAddress() #GET ADDRESS/LABEL
        result = opcode + instrAddress #COMBINE OPCODE+ADDRESS INTO 32 BITS
        hex_result = hex(int(result,2)) #CONVERT RESULT TO HEX 
        
    elif(instype == "i"): #IF IT IS AN I TYPE INSTRUCTION
        opcode = get_opcode_i()
        if(interactiveInstr[0] == "sw"): 
            #sw rt, imm(rs)
            
            rt = get_rtsd_value_5bits(interactiveInstr[1])
            rs = get_rtsd_value_5bits(interactiveInstr[3])
            immediate = immediate_value(interactiveInstr[2])
            
        elif(interactiveInstr[0] == "lw"): 
            #lw rt, imm(rs)

            rt = get_rtsd_value_5bits(interactiveInstr[1])
            rs = get_rtsd_value_5bits(interactiveInstr[3])
            immediate = immediate_value(interactiveInstr[2]) 
            
        elif(interactiveInstr[0] == "addi"):
            # addi rs rt imm
            
            rt = get_rtsd_value_5bits(interactiveInstr[2])
            rs = get_rtsd_value_5bits(interactiveInstr[1])
            immediate = immediate_value(interactiveInstr[3])
            
        elif(interactiveInstr[0] == "slti"):
            
            rt = get_rtsd_value_5bits(interactiveInstr[2])
            rs = get_rtsd_value_5bits(interactiveInstr[1])
            immediate = immediate_value(interactiveInstr[3])
            
        elif(interactiveInstr[0] == "beq"):

            rs = get_rtsd_value_5bits(interactiveInstr[1])
            rt = get_rtsd_value_5bits(interactiveInstr[2])
            immediate = immediate_value(interactiveInstr[3])
            
        elif(interactiveInstr[0] == "bne"):

            rs = get_rtsd_value_5bits(interactiveInstr[1])
            rt = get_rtsd_value_5bits(interactiveInstr[2])
            immediate = immediate_value(interactiveInstr[3])

            
        bin_result = opcode+rs
        bin_result = bin_result+rt
        bin_result = bin_result+immediate
        hex_result = hex(int(bin_result,2))


    
    elif(instype == "r"): # IF IT IS AN R TYPE INSTRUCTION
        opcode = "000000"
        if(interactiveInstr[0] == "add"): 
            
            rd = get_rtsd_value_5bits(interactiveInstr[1])
            rs = get_rtsd_value_5bits(interactiveInstr[2])
            rt = get_rtsd_value_5bits(interactiveInstr[3])
            sa = "00000"
            funct = get_funct()
            
        elif(interactiveInstr[0] == "move"):
            #move $1 $2 = add $1 $2 $0
            rd = get_rtsd_value_5bits(interactiveInstr[1])
            rs = get_rtsd_value_5bits(interactiveInstr[2])
            rt = "00000"
            sa = "00000"
            funct = get_funct()
            
        elif(interactiveInstr[0] == "jr"):
            # jr $rs
            rd = "00000"
            rs = get_rtsd_value_5bits(interactiveInstr[1])
            rt = "00000"
            sa = "00000"
            funct = get_funct()
        
        elif(interactiveInstr[0] == "sll"):
            # sll $rd $rt $shamt
            rd = get_rtsd_value_5bits(interactiveInstr[1])
            rs = "00000"
            rt = get_rtsd_value_5bits(interactiveInstr[2])
            sa = five_bits(int(interactiveInstr[3]))
            funct = get_funct()
           
        elif(interactiveInstr[0] == "slt"):
           #slt $rd $rs $rt
           rd = get_rtsd_value_5bits(interactiveInstr[1])
           rs = get_rtsd_value_5bits(interactiveInstr[2])
           rt = get_rtsd_value_5bits(interactiveInstr[3])
           sa = "00000"
           funct = get_funct()

        result = opcode+rs
        result = result+rt
        result = result+rd
        result = result+sa
        result = result+funct
        hex_result = hex(int(result,2))
    return hex_result
        


def dollar_sign_removal(instr):
    x=0
    while(x != len(instr)):
        temp = instr[x]
        if(temp[0] == "$"):
            temp = temp[1:]
            instr[x] = temp
        x=x+1
        
    return instr

#   Functions regarding J types  
    
def get_opcode_j():
    checker=0
    while(checker < len(jtype)): #WHILE LOOP RETURNS THE OPCODE
        if(interactiveInstr[0] == jtype[checker][0]):
            return jtype[checker][1]
        checker=checker+1
        
def get_instrAddress():
    decimal_form = int(interactiveInstr[1],16) #DECIMAL FORM OF THE HEX LABEL/ADDRESS
    binary_form = bin(int(decimal_form)) #BINARY FORM OF THE DECIMAL
    binary_form = binary_form[2:] #REMOVAL OF "0b" FROM THE START
    
    if(len(binary_form)!=32): #IF BINARY FORM IS NOT 32 BITS, ADD ZEROS TO THE START
        while(len(binary_form)!=32):
            binary_form = "0"+binary_form
        #print("\nAfter adding missing zeros:",binary_form)
        #print("Bit no:",len(binary_form))
        
    removed_binary_form = binary_form[4:-2] #REMOVAL OF FIRST 4 AND LAST 2 BITS
    return removed_binary_form

# Functions regarding I types

def get_opcode_i():
    checker=0
    while(checker < len(itype)): #WHILE LOOP RETURNS THE OPCODE
        if(interactiveInstr[0] == itype[checker][0]):
            return itype[checker][1]
        checker=checker+1
        
def get_rtsd_value_5bits(rtsd):
    checker=0
    # checks if the rtsd is inside the registerValue list
    while(checker < len(registerValue)):
        if(rtsd == registerValue[checker]):
            rtsd_five_bits = five_bits(checker)
            return rtsd_five_bits
        checker=checker+1
    
    #if the rtsd is an int value it will not be in the list so;
    #At the end of while loop, checker will be equal to registerValue length so if function will start working
    if(checker==len(registerValue)):
        rtsd_five_bits = five_bits(int(rtsd)) #Converting the number into 5 bits
        return rtsd_five_bits
    
def five_bits(checkno):
    binary_no = bin(checkno)
    binary_no = binary_no[2:]
    
    if(len(binary_no)<5): # If the length is less than 5
        while(len(binary_no) != 5):
            binary_no = "0"+binary_no
            
    elif(len(binary_no)>5): # If the length is more than 5
        x=len(binary_no)
        y=x-5
        binary_no = binary_no[y:]
        
    return binary_no


def immediate_value(imm):
    
    if(imm[0] == "-"): #If the value is NEGATIVE
        imm = imm[1:] # "-" is removed
        result = negative_binary(imm)
        
    else: #If the value is POSITIVE
        imm = bin(int(imm)) #convert to binary
        imm = imm[2:] #remove the "0b" from head
        x=len(imm) 
        if(x>16): #if the binary no is more than 16
            y=x-16
            imm = imm[y:] #throw away the extras
            result = imm
        elif(x<16): #if the binary no is less than 16
            while(x != 16):
                imm = "0"+imm #append 0s to the head
                x=x+1
            result = imm
            
    return result

def negative_binary(imm):
    #Convert the number into binary form
    binary_imm = bin(int(imm))
    
    #Since our immediate is 16 bits, we need to show the binary form here in 16 bits too
    #So we append 0's to the start
    
    binary_imm = binary_imm[2:] #Get rif of the "0b" in the head
    appended_binary_imm = binary_imm
    counter = len(binary_imm)
    while(counter != 16):
        appended_binary_imm = "0"+appended_binary_imm
        counter=counter+1
    
    #After appending 0 to complete into 16 bits, we need its 1's complement
    
    temp = appended_binary_imm
    checker = 0
    ones_comp = "0b"
    while(checker != 16):
        if(temp[checker] == "0"):
            ones_comp = ones_comp+"1"
        else:
            ones_comp = ones_comp+"0"
            
        checker=checker+1
    
    ones_comp = ones_comp[2:]

    #Now in order to get the 2's complement, we need to add 1 to the 1's complement
    
    add_one = "1"
    twos_comp = bin(int(ones_comp,2) + int(add_one,2))
    
    # We got our 2's complement
    twos_comp = twos_comp[2:] #remove "0b" from the head
    
    
    #We must check if there is any overflow
    if(len(twos_comp)>16): 
        twos_comp = twos_comp[1:]
        
    return twos_comp
    
    
# Functions regarding R types

def get_funct():
    checker=0
    while(checker < len(rtype)):
        if(interactiveInstr[0] == rtype[checker][0]):
            return rtype[checker][1]
        checker=checker+1    

#%%      
# Batch Mode functions
        
def send_line(line):
    print(line)
    line_head = line[0]
    print(line[0])
    print(line_head)
    line_head_type = check_line_head(line_head)
    #if it's not an instruction
    if(line_head_type == "address"):
        line = line[1:]
        work_on_each_line(line,"fail")
    else:
        work_on_each_line(line,line_head_type)
    
def work_on_each_line(line,instype):
    line = dollar_sign_removal(line)
    print(line)
    if(instype=="fail"):
        f = open("output.obj", "a+")
        f.write("failed")
        f.close()
    else:
        hex_result = upon_type_call_batch(instype,line)
        print(hex_result)
        f = open("output.obj", "a+")
        f.write(hex_result + "\n")
        f.close()

def check_line_head(checker):
    temp = 0
    while(temp<len(typeFinder)):
        if(checker == typeFinder[counter][0]):
            return type_finder(checker)
        temp=temp+1
    return "address"
    
# %%
# Same of upon_type_call function used in INTERACTION MOde, only with provided instrAddress locally
def upon_type_call_batch(instype,instrAddress): 

    #FUNCTION THAT FINDS THE HEX VALUE AFTER FINDING THE TYPE OF THE INSTRUCTION
    if(instype == "j"): #IF IT IS A J TYPE INSTRUCTION     
        opcode = get_opcode_j_batch(instrAddress) #GET OPCODE
        instr_Address = get_instrAddress_batch(instrAddress) #GET ADDRESS/LABEL
        result = opcode + instr_Address #COMBINE OPCODE+ADDRESS INTO 32 BITS
        hex_result_batch = hex(int(result,2)) #CONVERT RESULT TO HEX 
        hex_result = hex_result_batch
        
    elif(instype == "i"): #IF IT IS AN I TYPE INSTRUCTION
        opcode = get_opcode_i_batch(instrAddress)
        if(instrAddress[0] == "sw"): 
            #sw rt, imm(rs)
            
            rt = get_rtsd_value_5bits(instrAddress[1])
            rs = get_rtsd_value_5bits(instrAddress[3])
            immediate = immediate_value(instrAddress[2])
            
        elif(instrAddress[0] == "lw"): 
            #lw rt, imm(rs)

            rt = get_rtsd_value_5bits(instrAddress[1])
            rs = get_rtsd_value_5bits(instrAddress[3])
            immediate = immediate_value(instrAddress[2]) 
            
        elif(instrAddress[0] == "addi"):
            # addi rs rt imm
            rt = get_rtsd_value_5bits(instrAddress[2])
            rs = get_rtsd_value_5bits(instrAddress[1])
            immediate = immediate_value(instrAddress[3])
            
        elif(instrAddress[0] == "slti"):
            
            rt = get_rtsd_value_5bits(instrAddress[2])
            rs = get_rtsd_value_5bits(instrAddress[1])
            immediate = immediate_value(instrAddress[3])
            
        elif(instrAddress[0] == "beq"):

            rs = get_rtsd_value_5bits(instrAddress[1])
            rt = get_rtsd_value_5bits(instrAddress[2])
            immediate = immediate_value(instrAddress[3])
            
        elif(instrAddress[0] == "bne"):

            rs = get_rtsd_value_5bits(instrAddress[1])
            rt = get_rtsd_value_5bits(instrAddress[2])
            immediate = immediate_value(instrAddress[3])

            
        bin_result = opcode+rs
        bin_result = bin_result+rt
        bin_result = bin_result+immediate
        hex_result_batch = hex(int(bin_result,2))
        hex_result = hex_result_batch
    
    elif(instype == "r"): # IF IT IS AN R TYPE INSTRUCTION
        opcode = "000000"
        if(instrAddress[0] == "add"): 
            
            rd = get_rtsd_value_5bits(instrAddress[1])
            rs = get_rtsd_value_5bits(instrAddress[2])
            rt = get_rtsd_value_5bits(instrAddress[3])
            sa = "00000"
            funct = get_funct_batch(instrAddress)
            
        elif(instrAddress[0] == "move"):
            #move $1 $2 = add $1 $2 $0
            rd = get_rtsd_value_5bits(instrAddress[1])
            rs = get_rtsd_value_5bits(instrAddress[2])
            rt = "00000"
            sa = "00000"
            funct = get_funct_batch(instrAddress)
            
        elif(instrAddress[0] == "jr"):
            # jr $rs
            rd = "00000"
            rs = get_rtsd_value_5bits(instrAddress[1])
            rt = "00000"
            sa = "00000"
            funct = get_funct_batch(instrAddress)
        
        elif(instrAddress[0] == "sll"):
            # sll $rd $rt $shamt
            rd = get_rtsd_value_5bits(instrAddress[1])
            rs = "00000"
            rt = get_rtsd_value_5bits(instrAddress[2])
            sa = five_bits(int(instrAddress[3]))
            funct = get_funct_batch(instrAddress)
           
        elif(instrAddress[0] == "slt"):
           #slt $rd $rs $rt
           rd = get_rtsd_value_5bits(instrAddress[1])
           rs = get_rtsd_value_5bits(instrAddress[2])
           rt = get_rtsd_value_5bits(instrAddress[3])
           sa = "00000"
           funct = get_funct_batch(instrAddress)

        result = opcode+rs
        result = result+rt
        result = result+rd
        result = result+sa
        result = result+funct
        hex_result_batch = hex(int(result,2))
        hex_result = hex_result_batch
        
    return hex_result

def get_opcode_j_batch(instrAddress):
    checker=0
    while(checker < len(jtype)): #WHILE LOOP RETURNS THE OPCODE
        if(instrAddress[0] == jtype[checker][0]):
            return jtype[checker][1]
        checker=checker+1
        
def get_instrAddress_batch(instrAddress):
    decimal_form = int(instrAddress[1],16) #DECIMAL FORM OF THE HEX LABEL/ADDRESS
    binary_form = bin(int(decimal_form)) #BINARY FORM OF THE DECIMAL
    binary_form = binary_form[2:] #REMOVAL OF "0b" FROM THE START
    
    if(len(binary_form)!=32): #IF BINARY FORM IS NOT 32 BITS, ADD ZEROS TO THE START
        while(len(binary_form)!=32):
            binary_form = "0"+binary_form
        #print("\nAfter adding missing zeros:",binary_form)
        #print("Bit no:",len(binary_form))
        
    removed_binary_form = binary_form[4:-2] #REMOVAL OF FIRST 4 AND LAST 2 BITS
    return removed_binary_form


def get_opcode_i_batch(instrAddress):
    checker=0
    while(checker < len(itype)): #WHILE LOOP RETURNS THE OPCODE
        if(instrAddress[0] == itype[checker][0]):
            return itype[checker][1]
        checker=checker+1
        
def get_funct_batch(instrAddress):
    checker=0
    while(checker < len(rtype)):
        if(instrAddress[0] == rtype[checker][0]):
            return rtype[checker][1]
        checker=checker+1  
            
    
# %%
# Global variable, array definitions

counter = 1
jtype = np.array((("j","000010"),("jal","000011")))
itype = np.array((("addi","001000"),("beq","000100"),("bne","000101"),("lw","100011"),("slti","001010"),("sw","101011")))
rtype = np.array((("add","100000"),("move","100000"),("jr","001000"),("sll","000000"),("slt","101010"))) #opcode is 000000
typeFinder = np.array((("j","j"),("jal","j"),("add","r"),("move","r"),("jr","r"),("sll","r"),("slt","r"),("addi","i"),("beq","i"),("bne","i"),("lw","i"),("slti","i"),("sw","i")))
registerValue = np.array(("zero","at","v0","v1","a0","a1","a2","a3","t0","t1","t2","t3","t4","t5","t6","t7","s0","s1","s2","s3","s4","s5","s6","s7","t8","t9","k0","k1","gp","sp","fp","ra"))
        
# %%
# USER MENU

while(counter!=0):
    print("\nPlease select the mode that you would like to work on:\n\n1-Interactive Mode\n2-Batch Mode\n3-Exit")
    print("\nEnter your selection:")
        
    selection = input()
        
# %%
#Interactive mode
    if (selection == "1"):
        print("\n**********\nYou have selected the INTERACTIVE MODE\n1) Use spaces to seperate values instead of commas.\n[i.e: addi $s1 $s1 -17 instead of addi $s1, $s1, -17]\n2)You can either put $ signs or not, it’s up to you\n3)For lw and sw, do not use paranthesis, instead write all with spaces\n[i.e: sw/lw $s1 0 $s1 instead of sw/lw $s1,0($s1)]\n**********")
        print("\nEnter your instruction:")
        user_input = input()
        interactiveInstr = user_input.split(" ") #Store my instruction in a list
        interactiveInstr = dollar_sign_removal(interactiveInstr) #Remove the dollar signs
        instructionType = type_finder(interactiveInstr[0]) #Find the type of the instruction
        hex_code = upon_type_call(instructionType) #After finding the type, do the operations to find its HEX code
        print("\nHEX:",hex_code)
# %%          
#Batch Mode
    elif (selection == "2"):
        print("\n**********\nYou have selected the BATCH MODE\nIn order to assemble a source file, enter the name of your source code which should be inside your assembler folder such as 'source.src'\n**********\n")
        
        fileName = input()        
        f = open(fileName,"r")
        if(f.mode == "r"):
            f1 = f.readlines() # f1 is instructions list
            totalInstrNumber = len(f1) # holds the length of file

            for i in range(totalInstrNumber):
                f2 = f1[i].split() # list of all elements in a line
                lengthOfLine = len(f2)
                send_line(f2)
                for j in range(lengthOfLine):
                    f3 = f2[j].split() # list of single elements
                    lengthOfInstr = len(f3)
        
# %%        
#Exit Mode
    elif (selection == "3"):
        counter = 0
        print("\nGoodbye!")

# %%            
#Error Mode
    else:
        print("\nYou did something wrong. Choose again!\n")
        print("******************************\n")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    