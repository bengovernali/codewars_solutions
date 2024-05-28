def format_duration(seconds):
    result = ""
    
    time_dict = {
        'year': int(seconds / 31536000),
        'day': int((seconds % 31536000) / 86400),
        'hour': int(((seconds % 31536000) % 86400) / 3600),
        'minute': int((((seconds % 31536000) % 86400) % 3600) / 60),
        'second': int((((seconds % 31536000) % 86400) % 3600) % 60)
    }
    
    time_list = []
      
    for key in time_dict:
        if time_dict[key] != 0:
            time_list.append(f"{time_dict[key]} {key}{'s' if time_dict[key] > 1 else ''}")
    
    if len(time_list) == 0:
        return "now"
    else:
        for i in range(0, len(time_list)):
            if len(time_list) == 1:
                result += time_list[i]
            else:
                if i == len(time_list) - 1:
                    result += f" and {time_list[i]}"
                elif i == len(time_list) - 2:
                    result += f"{time_list[i]}"
                else:
                    result += f"{time_list[i]}, "
    
    return result