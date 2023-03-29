A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the special attribute of that object.
### Syntax - 
a docstring is defined by three "qoutation marks" in the first line of the function, e.g.:
``` python
def format_name(f_name,l_name):
	"""Take a first and last name and format it to return the title case of version of a name """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    formated_full_name = f"{formated_f_name} {formated_l_name}"
    return formated_full_name

```


