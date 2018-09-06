dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)

    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb
=>dbfilename으로 되어있는 파일이 같은 경로내에 존재하면 이진수로 읽습니다. 하지만 존재하지 않는다면 예외처리를 통해 
  문제를 해결합니다. 언피클링을 통해 파일 내용을 객체로 변환시켜줍니다. 만약 비어있다면 예외처리를 통해 문제를 해결합니다.


def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()
=>피클링을 통해 변경된 내용을 파일로 저장합니다.



 inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
=>어떤 사건을 실행할지 입력하고 만약 아무것도 입력하지 않았다면 다시 입력합니다. 
그 후에 inputstr을 띄어쓰기 단위로 나누어 parse에 저장합니다.


        if parse[0] == 'add':
            if (len(parse) != 4):
                continue
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]
=>새로운 정보를 추가하는 부분으로 이름, 나이, 점수를 추가합니다.
  만약 이름, 나이, 점수 중에 무엇하나 빠졌으면 추가하지 않고 다시 어떤 사건을 실행할지 입력합니다.


        elif parse[0] == 'del':
            if(len(parse)!=2):
                continue
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
=>기존에 존재하던 정보를 삭제하는 부분으로, 입력한 이름과 같은 사람들의 정보는 모두 삭제합니다.
  만약 이름을 입력하지 않았다면 실행하지 않고, 다시 어떤 사건을 실행할지 입력합니다.


        elif parse[0] == 'show':
            if (len(parse) != 1):
                continue
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
=>현재 존재하는 정보를 모두 보여주기 위해서 sortKey값과 scdb를 함수 인자로 넘겨줍니. 
  만약 조건과 다르게 입력하였다면 실행하지 않고, 다시 어떤 사건을 실행할지 입력합니다.
 


        elif parse[0] == 'find':
            if (len(parse) != 2):
                continue
            for p in scdb:
                if p['Name'] == parse[1]:
                   for attr in sorted(p):
                       print(attr + "=" + p[attr], end=' ')
                   print()
=>입력한 이름을 통해 그에 해당하는 정보를 보여줍니다. 
  만약 이름 이외에 다른 정보를 입력했다면 실행하지 않고, 다시 어떤 사건을 실행할지 입력합니다.


        elif parse[0] == 'inc':
            if (len(parse) != 3):
                continue
            try:
               int(parse[2])
            except ValueError:
                continue

            for p in scdb:
                if p['Name'] == parse[1]:
                    a=int(parse[2])+int(p['Score'])
                    p['Score']=str(a)
=>입력한 이름에 해당하는 사람들의 점수를 입력한 만큼 증가시켜줍니다.
  만약 점수를 입력하지 않았거나 입력한 점수가 숫자가 아닌경우 실행하지 않고, 다시 어떤 사건을 실행할지 입력합니다.


        elif parse[0] == 'quit':
            break
=>quit을 입력했다면 while문을 종료합니다.


        else:
            print("Invalid command: " + parse[0])
=>이 외에 다른 사건을 입력하였다면, 경고문을 주고 다시 다른 사건을 입력합니다.


	def showScoreDB(scdb, keyname):
    	for p in sorted(scdb, key=lambda person: person[keyname]):
        	for attr in sorted(p):
            	print(attr + "=" + p[attr], end=' ')
        	print()
=>사람들의 이름을 알파벳기준으로 재정렬 하여 정보를 보여주는 함수입니다. 




