# Створіть клас Editor, який містить методи view_document та edit_document. 
# Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для безкоштовної версії. 
# Створіть підклас ProEditor, у якому цей метод буде перевизначено. 
# Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, 
# інакше Editor. Викликайте методи перегляду та редагування документів.
class Text:
    def __init__(self, title:str, body:str):
        self.title = title
        self.body = body
class Editor:
    def view_document(self, doc:Text):
        print(doc.title)
        print(doc.body)    
    def edit_document(self):
        print("Pедагування документів недоступне для безкоштовної версії")        
user1 = Editor()
class ProEditor(Editor):
    def edit_document(self,doc:Text):
        print(f"Тепер для вас відкрита опція редагування тексту  {doc.title}")
        print(f"Зміст документа: {doc.body}")

def check_pass(user_key:str)-> bool:   
    pass_key = '12345'
    return pass_key == user_key

user_key = input("Введіть ліцензійний ключ: ")


if check_pass(user_key):
    user = ProEditor()
    print("Ключ правильний! Ви отримали доступ до версії Pro.")
else:
    user = Editor()
    print("Ключ неправильний. Ви використовуєте безкоштовну версію.")
    

