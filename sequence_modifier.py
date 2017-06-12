from Bio.Seq import Seq


sequence = Seq(raw_input("Enter sequence: "))

def all_in_one(sequence):
    # type: (object) -> object
    reverse = sequence.reverse_complement()
    print(reverse)
    transcribed = sequence.transcribe()
    print(transcribed)
    translated = sequence.translate()
    print(translated)

all_in_one(sequence)

exit() 
