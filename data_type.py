# Step 1: Create variables for each primitive data type
int_var = 10
float_var = 20.5
string_var = "Hello"
bool_var = True

# Step 2: Perform operations

# Arithmetic operations
int_sum = int_var + 5         
float_product = float_var * 2  

# String concatenation
greeting = string_var + ", World!" 

# Logical operations
bool_and = bool_var and False       
bool_or = bool_var or False      

# Step 3: Store variables in a dictionary by type
variables_dict = {
    "int": [int_var, int_sum],
    "float": [float_var, float_product],
    "string": [string_var, greeting],
    "bool": [bool_var, bool_and, bool_or]
}

# Step 4: Display the dictionary contents
for var_type, values in variables_dict.items():
    print(f"{var_type}: {values}")
