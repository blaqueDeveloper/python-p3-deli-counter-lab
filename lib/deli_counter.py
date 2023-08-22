def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        text = "The line is currently:"
        for i in range(len(katz_deli)):
            text += f' {i + 1}. {katz_deli[i]}'
        print(text)

  
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")



