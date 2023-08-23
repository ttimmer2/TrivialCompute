import backend_interface
import dice # dice class
import board # board class



backend_prompt = \
"""
Update database:
    Create category: cc
    Create question: cq
    Back: b
    Help: h
"""

def run_update_backend_help():
    print(backend_prompt)

def create_question():
    c = ""
    q = ""
    a = ""
    c = input("Enter question category\n")
    bi = backend_interface.backend_interface()
    cats = bi.get_categories()
    if c not in cats:
        print(f"{c} is invalid category. Must be one of {cats}")
        return create_question()
    q = input("Enter question: ")
    i = input(f"y/n: is `{q}` the question you meant to enter?\n")
    if i.lower() == "n":
        return create_question()
    a = input("Enter answer: ")
    i = input(f"y/n: is `{a}` the answer you meant to enter?\n")
    if i.lower() == "n":
        return create_question()
    bi.add_question(c,q,a)
    print(f"Successfully added:\n\tcategory:{c}\n\tquestion:{q}\n\tanswer:{a}\n")

def create_category():
    c = input("Enter category:\n")
    while True:
        i = input(f"y/n: is {c} the category you meant to enter?")
        if i.lower() == "n":
            return create_category()
        elif i.lower() == 'y':
            break
    bi = backend_interface.backend_interface()
    bi.add_category(c)
    print(f"Category: `{c}` successfully added to backend\n")

def go_to_main_menu():
    pass

def run_update_backend():
    i = input(backend_prompt)
    match i:
        case "cc":
            create_category()
        case "cq":
            create_question()
        case "b":
            go_to_main_menu()
        case "h":
            run_update_backend_help()
        case _ :
            print(f"{i}: is invalid input.")


def run_game():
    pass


if __name__ == "__main__":
    while True:
        run_update_backend()


