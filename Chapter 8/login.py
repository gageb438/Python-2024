def get_login_name(first, last, idnumber): #8-3
    # login accepts arguments for first, last, and id number.
    # it createss seperate substrings of the first 3 letters of both
    # the first name and last and last 3 characters of the id number.
    # it concatenates the strings in order of first, last, id
    # and it returns the newly generated login.

    first_slice = first[0:3]
    last_slice = last[-3:]
    last_id = idnumber[-3:]

    new_login = first_slice + last_slice + last_id
    return new_login