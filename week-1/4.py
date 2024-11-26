"""
Student helpers updates Linux on students computers. Initially, only one computer has installedthe latest version of Linux. 
Unfortunately, the eduroamhas broken down, so student helpers can now upload new versions of Linux to other computers only 
via cables. Student helpers can connect two computers with one cable at a time, and at most one cable can be connected to 
the computer at a time. Copying files of operating system between computers takes exactly one hour.Count how many hours it 
will take for student helpers to install the latest version of Linux on all students’computers, if there are n of them and 
student helpers brought k cables with them.

Input
The line containstwo integers n, k (1 ≤ k ≤ n ≤ 1018) -the number of computers 
and cables.

Output
Your program shouldwrite the minimum number of hours needed to implementinstalling Linux on all computers
"""

def time_to_install(n, k):
    