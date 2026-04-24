import math
secs = int(input('Enter how many seconds: '))
days = secs / 86400
remainingSeconds = secs % 86400
hours = remainingSeconds / 3600
remainingSeconds %= 3600
minutes = remainingSeconds / 60
remainingSeconds %= 60
filtereddays = math.floor(days)
filteredhours = math.floor(hours)
filteredminutes = math.floor(minutes)
filteredseconds = math.floor(remainingSeconds)
print(f"{filtereddays:02d}:{filteredhours:02d}:{filteredminutes:02d}:{filteredseconds:02d}")