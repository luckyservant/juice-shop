import re

pattern = "^([abc]{1,3})*$"# pragma: allowlist secret
string = "abcabcabcbaaaccccccccccccc"
password = "mySuperSecretPswd"

if re.match(pattern, string):
    print(" The string '{}' matches the pattern.".format(password))
else:
    print("The string '{}' does not match the pattern.".format(string))

pattern = "^(.{1,3})+$"
string = "abcabcabc"

if re.match(pattern, string):
    print("The string '{}' matches the pattern.".format(string))
else:
    print("The string '{}' does not match the pattern.".format(string))
