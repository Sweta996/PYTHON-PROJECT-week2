# def is_palindrome(word):
 #   reversed_word = word[::-1]
 #   if word == reversed_word:
  #      return True
  #  else:
  #      return False

# print(is_palindrome("naman"))
# print(is_palindrome("horse"))

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False
print(is_palindrome("naman"))
print(is_palindrome("horse"))
