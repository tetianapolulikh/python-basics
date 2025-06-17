def print_message(list_of_messages, printed_messages):
     while list_of_messages:
         current_list = list_of_messages.pop()
         print(f"Printing message: {current_list}")
         printed_messages.append(current_list)


def show_printed_messages(printed_messages):
     print('\nYour messages were printed: ')
     for printed_message in printed_messages:
          print(printed_message)

list_of_messages = ['You look great today!', 'You’ve got this!', 'Make it happen!', 'Believe in yourself!', 'Stay strong!']
printed_messages = []

print_message(list_of_messages, printed_messages)
show_printed_messages(printed_messages)