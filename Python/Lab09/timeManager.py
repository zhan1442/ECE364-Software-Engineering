from timeDuration import *

def getTotalEventSpan(ex):
    with open("Events.txt", 'r') as myfile:
        content = myfile.readlines()
        weeks = 0
        days = 0
        hours = 0
        for line in content[2:]:
            if line[4:11] == ex:
                if line[20] == "w":
                    weeks += int(line[18:20])*int(line[31])
                if line[20] == "d":
                    days += int(line[18:20])*int(line[31])
                if line[20] == "h":
                    hours += int(line[18:20])*int(line[31])
        return TimeSpan(weeks, days, hours)

def rankEventsBySpan(*argv):
    events = {}
    hours = []
    for ex in argv:
        tots = getTotalEventSpan(ex)
        toth = tots.getTotalHours()
        hours.append(toth)
        if toth in events.keys():
            events[toth].append(ex)
        else:
            events[toth] = []
            events[toth].append(ex)
    hours.sort(reverse=True)
    out = []
    for hour in hours:
        out.extend(events[hour])
    return out
