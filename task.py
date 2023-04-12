input_text = input("Введите строку, состоящую из букв A-Z: ")

def rle(input_text):
   result_text = []
   input_text += ' '
   temp_symbol = input_text[0]
   symbol_count = 1
   
   for symbol in range(1, len(input_text)):
        if input_text[symbol_count] == temp_symbol:
            symbol_count += 1
        else:
            if symbol_count == 1:
                result_text.append(f'{temp_symbol}')
            else:
                result_text.append(f'{temp_symbol}{symbol_count}')
            symbol_count = 1
            temp_symbol = input_text[symbol]

    print(*result_text, sep='')
rle(input_text)


      