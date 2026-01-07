total_class=float(input("Total Classes:"))
classes_attended=float(input("Classes Attended"))
percentage=(classes_attended/total_class)*100
minimum_req=int(0.75*total_class)
additional=minimum_req-classes_attended
print("Attendance Percentage=",percentage)
if(percentage>=75):
    print("Status:Eligible")
else:
    print("Status:Not Eligible")
    print("Additional Classes Required:",additional)
