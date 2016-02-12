#strings
s = 'furry dog'
s.rstrip() #remove whitespace

s.split(' ') # split into list where space is

s.isdigit() #check for whether or not it is an integer

s.endswith('y') # check last letter of string

s.lower()
s.upper() # lower/uppercase letter


multiLineString = '''This string will
extend multiple
lines in the
code''' # Use triple quotes to make multiline text

#slicing
s[:] #copy all elements
s[1:] #all elements past the first
s[:-1] #everything but last element
s[::2] #every other element