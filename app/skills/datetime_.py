from datetime import datetime

class DateTimeSkills:  
    __current = datetime.now()

    @classmethod
    def get_time(cls, question):
        # Get current time
        time = cls.__current.strftime("%H:%M")
        return f"Bây giờ là {time}"

    @classmethod
    def get_date(cls, question):
        lst = ["Thứ 2", "Thứ 3", "Thứ tư", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]
        year = cls.__current.year
        month = cls.__current.month
        day = cls.__current.day
        weekday = cls.__current.today().weekday()

        if month == 4:
            month = "tư"
        text = f"Hôm nay là {lst[weekday]}, ngày {day} tháng {month} năm {year}" 
        return text
