#Reverse convert to seconds

# total_secs = int(input())
total_secs = int(input())
hours = int(total_secs / 3600)
new_total_secs = total_secs - (hours * 3600)
minutes = int((new_total_secs) / 60)
ntotal_secs = new_total_secs - (minutes * 60)
seconds = int((ntotal_secs))

print(f'Hours: {hours}')
print(f'Minutes: {minutes}')
print(f'Seconds: {seconds}')