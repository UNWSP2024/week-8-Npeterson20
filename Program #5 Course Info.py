# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.


def get_courses_by_subject():
    courses = {}
    while True:
        course_id = input("Enter course ID (or 'done' to finish): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter course name: ")
        courses[course_id] = course_name

    subject = input("Enter subject prefix to filter by (e.g., 'COS'): ").upper()
    print(f"\nCourses with subject '{subject}':")
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")

# Run the program
get_courses_by_subject()
