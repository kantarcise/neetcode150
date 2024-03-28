"""
Q: Design an algorithm to encode a list of strings 
to a string. The encoded string is then sent 
over the network and is decoded back to the 
original list of strings.

Please implement encode and decode.

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

"""

class Solution:
    def encode_(self, strs: list) -> str:
        # just join all elements in the given list
        return "~".join(strs)
    
    def decode_(self, string: str) -> list:
        # take the incoming string and split it based on 
        # your special character
        return string.split("~")

    def encode_stateless(self, strs: list) -> str:
        # how about we solve the question, stateless?
        
        # So we somehow need to 
        # clarify the word lenghts while we are trasporting them.

        # For that we can use the lenght of the words and 
        # sent them prior to the encoded words.

        # When we are decoding, we will know how many 
        # indexes we need to be 
        # looking for, simply using the length.
        
        result = ""

        for elem in strs:
            # this is not ideal because strings are 
            # immutable
            # we are making a lot of objects in this loop
            result += str(len(elem)) + "#" + elem

        return result

    def decode_stateless(self, input_string: str) -> list:
        # we will populate this result
        result = []

        # string starting index
        i = 0

        # until you are end of the string
        while i < len(input_string):
            # This index holds width for the length 
            # of the word
            j = i
            while input_string[j] != "#":
                j += 1

            length = int(input_string[i:j])
            result.append(input_string[j+1: j+1+length])
            
            # move index
            i = j + 1 + length
        return result

sol = Solution()

# this is simple and pretty cool
encoded_list = sol.encode_(["lint","code","love","you"])
print("Here is the simple version, decoded:")
print(sol.decode_(encoded_list))

# here is the stateless version
print("\n Stateless Version:")
another_encoded_list = \
    sol.encode_stateless(["lint","code","love","you"])

print(f"Here is encoded version: {another_encoded_list}")
print(f"And the result of decoding: \
            {sol.decode_stateless(another_encoded_list)}")