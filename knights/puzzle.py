from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")



# Puzzle 0
# A says "I am both a knight and a knave."

implication1 = Implication(AKnight,And(AKnight, AKnave))#if A is Knight then what A said is true
implication2 = Implication(AKnave,Not(And(AKnight, AKnave)))
or1 = Or(AKnight, AKnave)#A can be Knight or Knave
not1 = Not(And(AKnight, AKnave))#But can not be both
knowledge0 = And(implication1, implication2, or1, not1)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.

implication1 = Implication(AKnight,And(AKnave, BKnave))#if A is Knight then what A said is true
implication2 = Implication(AKnave, Not(And(AKnave, BKnave)))#if A is not Knight then what A said is false
or1 = Or(AKnave, AKnight)
or2 = Or(BKnave, BKnight)
not1 = Not(And(AKnight, AKnave))#But can not be both
not2 = Not(And(BKnight, BKnave))
knowledge1 = And(implication1, implication2, or1, or2, not1, not2)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

implication1 = Implication(AKnight, Or(And(AKnight,BKnight), And(AKnave,BKnave)))#if A is Knight then what A said is true
implication2 = Implication(AKnave, Not(Or(And(AKnight,BKnight), And(AKnave,BKnave))))
implication3 = Implication(BKnight, Not(Or(And(AKnight,BKnight), And(AKnave,BKnave))))
implication4 = Implication(BKnave, Or(And(AKnight,BKnight), And(AKnave,BKnave)))
or1 = Or(AKnave, AKnight)
or2 = Or(BKnave, BKnight)
not1 = Not(And(AKnight, AKnave))#But can not be both
not2 = Not(And(BKnight, BKnave))
knowledge2 = And(implication1, implication2, implication3,implication4,or1,or2,not1,not2)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
implicationA1 = Implication(AKnight, Or(AKnight,AKnave))
implicationA2 = Implication(AKnave, Not(Or(AKnight,AKnave)))

implicationB1 = Implication(BKnight, Implication(AKnight, AKnave))
implicationB2 = Implication(BKnave, Not(Implication(AKnight, AKnave)))
implicationB3 = Implication(BKnight, CKnave)
implicationB4 = Implication(BKnave, Not(CKnave))

implicationC1 = Implication(CKnight, AKnight)
implicationC2 = Implication(CKnave, Not(AKnight))
or1 = Or(AKnave, AKnight)
or2 = Or(BKnave, BKnight)
or3 = Or(CKnave, CKnight)
not1 = Not(And(AKnight, AKnave))#But can not be both
not2 = Not(And(BKnight, BKnave))
not3 = Not(And(CKnight, CKnave))
knowledge3 = And(implicationA1, implicationA2, implicationB1,implicationB2,implicationB3,implicationB4,implicationC1,implicationC2,or1,or2,or3,not1,not2,not3
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
