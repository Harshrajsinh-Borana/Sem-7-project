from MyQR import myqr
import os

# Open and read the file
with open(r"C:\Users\HARSHRAJSINH\OneDrive\Desktop\Project_7\Smart_Attendence_System\QR_Attendance\students.txt", 'r') as f:
    lines = f.read().split("\n")

# Print lines for debugging
print(lines)

# Process each line
for line in lines:
    if line.strip():  # Ensure the line is not empty
        data = line
        # Generate the filename by removing spaces and adding .png extension
        save_name = f"{line.split()[0]}.png"

        # Run the MyQR function
        version, level, qr = myqr.run(
            data,
            level='H',
            version=1,
            picture=r"C:\Users\HARSHRAJSINH\OneDrive\Desktop\Project_7\Smart_Attendence_System\QR_Attendance\malav1.jpg",
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name=save_name,
            save_dir=os.getcwd()
        )
