#dictionaries
knowlege = {
    "h_emotion": [
        'love','like','happy','nice','giggling','joy','smile','laugh','excited','delight','cheerful'
    ],
    "s_emotion": [
        'sad','cry','crying','unhappy','depressed','lonely','upset','hurt','tears','miserable','hate'
    ],
    "sport": [
        'play','playing','sport','sports','football','soccer','ball','basketball','score',
        'tennis','cricket','volleyball','swimming','running','gym','training','match','tournament'
    ],
    "study": [
        'education','score','marks','english','nepali','math','science','computer','physics',
        'physic','chemistry','biology','history','geography','exam','test','assignment','homework','lecture','class','teacher','student'
    ],
    "calculation": [
        '+','-','/','*','mathematics','math','algebra','geometry','trigonometry','equation',
        'formula','addition','subtraction','multiplication','division','numbers','arithmetic'
    ],
    "technology": [
        'computer','laptop','mobile','phone','internet','software','hardware','programming',
        'python','java','database','AI','robotics','coding','application','website'
    ],
    "food": [
        'food','eat','meal','breakfast','lunch','dinner','snack','fruit','vegetable','rice','bread',
        'meat','chicken','pizza','burger','coffee','tea','water','drink','juice'
    ],
    "travel": [
        'trip','journey','travel','tour','holiday','vacation','flight','airport','bus','train',
        'hotel','ticket','passport','visa','explore','adventure','map','destination'
    ]
}
type = ['happy', 'sad', 'sports', 'study', 'math', 'tech', 'food', 'travel']




#functions
def context(n1):
    happy=sad=sports=study=math=tech=food=travel=0
    for i in n1:
        if i in knowlege['h_emotion']:
            happy+=1
        elif i in knowlege['s_emotion']:
            sad+=1   
        elif i in knowlege['sport']:
            sports+=1
        elif i in knowlege['study']:
            study+=1
        elif i in knowlege['calculation']:
            math+=1
        elif i in knowlege['technology']:
            tech+=1
        elif i in knowlege['food']:
            food+=1
        elif i in knowlege['travel']:
            travel+=1
    return happy, sad, sports, study, math, tech, food, travel 

def classify(k):
    if k[0]>k[1]:
        emo = 'happy'
    elif k[0]<k[1]:
        emo = 'sad'
    else:
        emo = 'neutral'

    # Check if any category has a count > 0
    if all(k[count] == 0 for count in range(2, 8)):
        return {'emo': emo, 'about': 'unknown'}
    
    ab = 2
    for i in range(2,8):
        if k[ab] < k[i]:
            ab = i
    return {'emo': emo , 'about': ab}




#main:
intp = input("Enter a phrase : ")
a = len(intp)
x = 1
nl =[]
if intp[0] != " ":
    word = intp[0]
else:
    word = intp[1]
    x = 2

for i in range(x,a):
    if i == a-1:
       word = word + intp[i]
       nl.append(word) 
    elif intp[i] != " " and intp[i] != ".":
        word = word + intp[i]
    elif intp[i] == " " or intp[i] == ".":
        nl.append(word)
        word = ""
for y in nl:
    print(y)

print(context(nl))
know = context(nl)
about = classify(know)
if about['about'] == 'unknown':
    print(f'The user is {about['emo']} and is talking about unknown')
else:
    print(f'The user is {about['emo']} and is talking about {type[about['about']]}')