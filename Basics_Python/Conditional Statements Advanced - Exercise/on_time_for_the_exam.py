hour_exam = int(input())
min_exam = int(input())
hour_arrive = int(input())
min_arrive = int(input())

time_exam = hour_exam * 60 + min_exam
time_arrive = hour_arrive * 60 + min_arrive

hh = abs(time_arrive - time_exam) // 60
mm = abs(time_arrive - time_exam) % 60

status = ""

if 0 <= time_exam - time_arrive <= 30:
    status = "On time"
    print(status)
elif time_arrive > time_exam:
    status = "Late"
    print(status)
else:
    status = "Early"
    print(status)

if status == "On time":
    if 0 <= time_exam - time_arrive < 60:
        print(f"{time_exam - time_arrive} minutes before the start")


elif status == "Late":

    if 10 <= abs(time_arrive - time_exam) < 60:
        print(f"{mm} minutes after the start")
        if 0 <= abs(time_arrive - time_exam) < 10:
            print(f"0{mm} minutes after the start")
    if time_arrive - time_exam >= 60:
        if mm < 10:
            print(f"{hh}:0{mm} hours after the start")
        else:
            print(f"{hh}:{mm} hours after the start")

elif status == "Early":

    if hh < 1 and 10 <= mm < 60:
        print(f"{mm} minutes before the start")
    elif hh >= 1 and 0 <= mm < 10:
        print(f"{hh}:0{mm} hours before the start")
    else:
        print(f"{hh}:{mm} hours before the start")



