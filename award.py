#These codes show how to read in minutes for swimming, cycling and running event
swimming_time = float(input("enter the time taken for swimming event (in minutes): "))
cycling_time = float(input("enter the time taken for cycling event (in minutes):  "))    
running_time = float(input("enter the time taken for running event (in minutes):  "))

#The line of code that shows total time taken to complete triathlon
total_time = swimming_time + cycling_time + running_time

#These line of codes that show if, elif and else statement conditions each participants must meet before an award can be given and print statement
if total_time <= 100:
    award = "Provicial colours"
elif total_time <= 105:
    award = "Provicial Half Colours"
    
elif total_time <= 110:
    award = "Provicial Scrolls"
else:
    award = "No award"
print("Award: ", award)
                          