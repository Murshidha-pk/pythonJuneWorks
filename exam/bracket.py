input="{ [] }"

symbol_table={
             
             "< : >"
             "{ : }"
             "( : )"
             "[ : ]"

    }

top=-1

is_valid=True

symbol_stack=[]

for symbol in input:

    if symbol in symbol_table:

        top+=1

        symbol_stack.append(symbol)

    else:
        
        current_symbol=symbol_stack[top]
        current_symbol_closing=symbol_table[current_symbol]

        if symbol==current_symbol_closing:

            symbol_stack.pop()

            top-=1
        else:
            is_valid=False
            break
print(is_valid)
    