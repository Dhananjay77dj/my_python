st = ('my name is {} and i am from {}')
name = 'dhananjay'
country = 'india'
print(st.format(name, country))          # is .format ne name ko {} big bracket me rakh diya ,{} this big bracket is necesarry
# you can also take ithe input for both name and coutnry , par jitne str hai un sabka unput lena hoga
print("my name is "+ name)

# now we are going to use f string 
print(f"hi me name is {name} and curently i am in {country}")  # this f string will automatically populate/ put the value of
#name and country in their places
txt = 'for only rs {rs:.3f}' # this will take value upto only 3 digits
print(txt.format(rs=44.7689))
print(type(f"{2 * 30}")) # its a string

print(type(2 * 30)) # its a integer
