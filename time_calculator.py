days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def add_time(start_time, duration, *day_of_week):
    [long, meridian] = start_time.split(" ") #3:00, PM
    [hour, minute] = long.split(":")
    [dh, dm] = duration.split(":")

    future_days = 0

    output_mins = int(minute) + int(dm)
    output_hours = int(hour) + int(dh)
    if output_mins >= 60:
        # add an hour and subtract 60
        output_mins -= 60
        output_hours += 1
    if output_mins < 10:
        output_mins = f"{output_mins}".zfill(2) #zfill with the total amount of characters
    if output_hours >= 12:
        # divide by 12 to get the number of days
        days, rest_hours = divmod(output_hours, 12)
        #rest_hours = output_hours % 12
        #days = output_hours // 12
        output_hours = rest_hours if rest_hours else output_hours
        if output_hours > 12:
            #if the condition is only for cases where hours are exact multiples of 12;
            output_hours = output_hours - (days -1) * 12

        
        if meridian == "PM":
            future_days = ((days-1) // 2) +1
        else:
            future_days = days // 2

        if days > 0 and days % 2 != 0:
            meridian = "AM" if meridian == "PM" else "PM"

    new_time = str(output_hours) + ":"
    new_time += str(output_mins) + f" {meridian}"

    if day_of_week:
        day = day_of_week[0].title()
        if future_days > 0:
            # index of the list and find the index + future days, check if greater than end, reset the index
            index = days_of_week.index(day)
            index += future_days % 7
            if index > 6:
                index -= 7
            day = days_of_week[index]
        new_time += f", {day}"

    if future_days == 1:
        new_time += f" (next day)"
    elif future_days > 1:
        new_time += f" ({future_days} days later)"

    # 1:10:46 della livestream



    return new_time

#PDF a pag 14/46