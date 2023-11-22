text = """
Today, Richard Rael and Tony Riggs tell the story of American astronomer edwin hubble. 
He changed our ideas about the universe and how it developed.
Edwin hubble made his most important discoveries in the nineteen twenties. Today, other 
astronomers continue the work he began. Many of them are using the Hubble space 
telescope that is named after him.
Edwin Hubble was born in eighteen eighty-nine in Marshfield, Missouri. He spent his early 
years in the state of Kentucky. Then he moved with his family to Chicago, Illinois. He 
attended the University of Chicago. He studied mathematics and astronomy.
"""


sentences_with_hubble = [sentence for sentence in text.split('.') if "edwin hubble" in sentence.lower()]
for sentence in sentences_with_hubble:
    print(sentence)


corrected_text = text.replace("edwin hubble", "Edwin Hubble").replace("Edwin hubble", "Edwin Hubble").replace("edwin Hubble", "Edwin Hubble")
print("\nCorrected Text:\n", corrected_text)

