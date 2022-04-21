def fun(s):
    # return True if s is a valid email, else return False
    username = s.split("@")[0] if "@" in s else ""
    website = s.split("@")[1] if "@" in s else ""
    extension = website.split(".")[1] if "." in website else ""
    website = website.split(".")[0] if "." in website else ""
    if not len(username) or not len(website) or \
        not len(extension) or len(extension)>3:
        return False
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    username = username.translate(str.maketrans("","",chars+digits+"_-"))
    website = website.translate(str.maketrans("","",chars+digits))
    extension = extension.translate(str.maketrans("","",chars))
    if len(username)+len(website)+len(extension) == 0:
        return True
    else:
        return False
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
