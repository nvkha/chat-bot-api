import random

class GreetingSkills:
    
    @classmethod
    def greeting(cls, question):
        lst = ["Chào bạn, tôi có thể giúp gì được cho bạn ?", "Xin chào, rất vui được gặp bạn", "Chào bạn, chúc bạn một ngày tốt lành"] 
        return random.choice(lst)


    @classmethod
    def bye(cls, question):
        lst = ["Tạm biệt bạn", "Gặp lại bạn sau"] 
        text = random.choice(lst)
        return text