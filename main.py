"""to use the entire application just call reader.inference()"""
""" boooi you must be proud now! u made a real chatbot! dudeee that took google forever to create."""
""" add the therapy part make it a func"""
"""you are working on two add_ons buffer and listen."""


"""
There are two tables in the sqlite db one called main containing regular keywords, the second is called short,   it
contains         keywords        of       3     or        less                words                       requests.
while adding records to the datebase make sure the key doesnt contain anything but keywords and    connecting words
were suitable. The application use the syntax '#KEY' for speciall commands. It is designed to be tought by the  end
users.  The application     doesnt have any      known bugs or     limitations and it   is relatively easy to edit.
"""

class sfile():

    flag1=True

    def add(data,tar):
        """complete"""
        import sqlite3
        cnct=sqlite3.connect('sfile.db')
        c=cnct.cursor()
        a=data[0]
        b=data[1]
        d=data[2]

        c.execute("""INSERT INTO  {} VALUES("{}","{}","{}")""".format(tar,a,b,d))
        print('request completed')
        cnct.commit()
        return

    def merge(source,s_table,tar):
        """update the main table using values from the targeted file. the first
        argument is the file name with the .db extension, the second is the
        targeted table in the targeted file, the third is the targeted table in
        the main file"""
        import sqlite3
        cnct=sqlite3.connect('sfile.db')
        c=cnct.cursor()


        new_cnct=sqlite3.connect("{}".format(source))
        new_c=new_cnct.cursor()

        no_rec=0
        for n_row in new_c.execute("SELECT * FROM {}".format(s_table)):
            copy= True
            n_key=n_row[0]
            for old_row in c.execute("SELECT * FROM {}".format(tar)):
                old_key=old_row[0]
                if n_key == old_key:
                    copy= False
            if copy == True:
                a=n_row[0]
                b=n_row[1]
                d=n_row[2]
                c.execute("""INSERT INTO  {} VALUES("{}","{}","{}")""".format(tar,a,b,d))
                no_rec += 1
        cnct.commit()
        print("Request completed {} items inserted.".format(no_rec))


    def get(request,tar):
        """complete"""

        import sqlite3
        cnct=sqlite3.connect('sfile.db')
        c=cnct.cursor()
        flag=True

        """selection criteria"""
        sure=[]
        for row in c.execute("SELECT * FROM {}".format(tar)):

            key=row[0]
            ksw=key.split()
            lend=0

            for word in ksw:

                if word in request:
                    lenk=len(ksw)

                    lend += 1
                    if lenk==lend:
                        sure.append(row)
                        flag= False
        if flag ==False:
            sfile.build_confidence(sure,request)
        return flag



    def build_confidence(sure,request):
        conflist=[]

        for possibility in sure:
            # postr=str(pos)
            confidence=0
            splitted_poskey=possibility[0]

            for word in request:
                if word in splitted_poskey:
                    confidence += 1
            conflist.append(confidence)
        ind=conflist.index(max(conflist))
        for_sure=sure[ind]


        if for_sure[1] != '' and for_sure[1] != None and for_sure[1] != 'None':
            print(for_sure[1])
        if for_sure[2] != '' and for_sure[2] != 'None' and for_sure[2] != None:
            try:
                exec(for_sure[2])
            except Exception as e:
                print(e)
                print('There was an error in the executable you assigned, please update it.')


    def update(key,tar):
        import sqlite3
        cnct=sqlite3.connect('sfile.db')
        c=cnct.cursor()

        okk= c.execute("SELECT * FROM {} WHERE key=='{}' ".format(tar,key))
        for data in okk:
            print(data )
        ok=input("Is this the record you want to update ? Answer in Y/N :   ")
        if ok=='Y':
            nkey=input('this is the new key value:    ')
            nanswer=input('this is the new answer to the key you entered:    ')
            nexec=input('enter any ecec if needed else leave empty:    ')
            if nexec==" " or nexec=="":
                nexec=None
            c.execute("""UPDATE {} SET key="{}",ans="{}" ,exec="{}" WHERE KEY=="{}"  """.format(tar,nkey,nanswer,nexec,key))
            print('request completed')
        cnct.commit()


    def delete(key,tar):
        import sqlite3
        cnct=sqlite3.connect('sfile.db')
        c=cnct.cursor()

        okk= c.execute("SELECT * FROM {} WHERE key=='{}' ".format(tar,key))
        for data in okk:
            print(data )
        ok=input("Is this the record you want to DELETE PERMANENTLY ? Answer in Y/N")
        if ok=='Y':
            c.execute("""DELETE FROM {} WHERE key ='{}'  """.format(tar,key)  )
            print('request completed')
        cnct.commit()

class add_ons:
    def listen():
        pass
        print('')
        bullshit=input(':))')
    class buffer:
        def __init__():
            pass


class learner:
    """to use the entire class just call learner.getter().
    it does not need any arguements"""
    data = []

    def getter():
        """make it easier to add multiple keys"""
        """gets the input"""
        ok='N'
        while ok=='N':
            global data
            key=input('this is the key value:    ')
            answer=input('this is the answer to the key you entered:    ')
            executable=input('enter any ecec if needed else leave empty:    ')
            if ',,' in answer:
                variant_answers = answer.split(',,')
                executable = "import random ; aiv = random.choice({}) ; print(aiv)".format(variant_answers)
                answer = None
            if answer==" " or answer=="":
                answer=None
            if executable==" " or executable=="":
                executable=None
            multi_key= False
            if ',,' in key:
                variant_keys = key.split(',,')
                for key in variant_keys:

                    data = [key , answer , executable]
                    ok=input("are you satisfied by this?{}  answer in 'Y'es or 'N'o :  ".format(data))
                    while ok != 'Y' and ok!='N':
                        print('you entered a wrong input try again')
                        ok=input("are you satisfied by this?{}    answer in 'Y'es or 'N'o:  ".format(data))


                    target=input('if the key is intended for a 3 or less words req type 1 else type 2 :   ')
                    while True:
                        if target == '2':
                            sfile.add(data,'main')

                            break
                        if target == '1':
                            sfile.add(data,'short')

                            break
                        else:
                            print('wrong choice')
                multi_key= True
            if multi_key == False:

                data = [key , answer , executable]
                ok=input("are you satisfied by this?{}  answer in 'Y'es or 'N'o :  ".format(data))
                while ok != 'Y' and ok!='N':
                    print('you entered a wrong input try again')
                    ok=input("are you satisfied by this?{}    answer in 'Y'es or 'N'o:  ".format(data))

                target=input('if the key is intended for a 3 or less words req type 1 else type 2 :   ')
                while True:
                    if target == '2':
                        sfile.add(data,'main')

                        break
                    if target == '1':
                        sfile.add(data,'short')

                        break
                    else:
                        print('wrong choice')
        return
    def auto_learn(reqw):
        useless=[0]
        for a in useless:
            print("to stop type'#'")
            answer=input('how do i answer that?    ')
            if answer =='#':
                break
            executable=input('enter any ecec if needed else leave empty:    ')

            if executable =='':
                executable= None
            reqword=""
            for word in reqw:
                reqword = reqword + word +' '

            data = [reqword.rstrip(' ') , answer , executable]
            pre_target= len(reqw)

            ok=input("are you satisfied by this?{}  answer in 'Y'es or 'N'o ".format(data))
            if ok == 'Y':
                if pre_target <=3:
                    sfile.add(data,'short')
                else:
                    sfile.add(data,'main')




class reader:
    """compares the database for match"""



    def inference():
        """this is the brain of the app"""
        print("hey i am Mo! am here to help you")
        print("if you want to stop chatting with me type '#EXIT' or type'#INFO' for more useful commands")
        #ADD ABILITY TO CALL THE USER BY HIS NAME IF U DONT FEEL LAZY LATER ON

        while True:
            reqw=reader.reader()


            if reqw[0].upper() == '#EXIT':
                print("cyaa m8")
                break
            elif reqw[0].upper() == "#TEACH":
                learner.getter()

            elif reqw[0].upper() == '#DELETE':
                while True:
                    tar=input("for seach in short db type'1', for search in main db type '2':  ")
                    if tar == '1':
                        tar= 'short'
                        break
                    elif tar =='2':
                        tar= 'main'
                        break
                    else:
                        print('wrong choice')
                key=input('what is the key for the record you want to delete?')
                sfile.delete(key,tar)

            elif reqw[0].upper() == '#UPDATE':
                while True:
                    tar=input("for seach in short db type'1', for search in main db type '2':  ")
                    if tar == '1':
                        tar= 'short'
                        break
                    elif tar =='2':
                        tar= 'main'
                        break
                    else:
                        print('wrong choice')

                key=input('what is the key for the record you want to update?')
                sfile.update(key,tar)
            elif reqw[0].upper() == '#MERGE':
                s_file = input('type the entire file path. make sure to use double slashes   ')
                s_table =input('type the table name   ')
                t_table= input("type the table name in the main file 'short' or 'main'  "   )
                sfile.merge(s_file,s_table,t_table)
            elif reqw[0].upper() =='#DB':
                import sqlite3
                cnct=sqlite3.connect('sfile.db')
                c=cnct.cursor()

                okk= c.execute("SELECT * FROM main")
                print('--------------------------------------------------------')
                print('table name: main')
                print('')
                print("columns are: key  , ans  , exec")
                print('')
                print('')
                for data in okk:
                    print(data )
                    print('')
                okk= c.execute("SELECT * FROM short")
                print('--------------------------------------------------------')
                print('table name: short')
                print('')
                print("columns are: key  , ans  , exec")
                print('')
                print('')
                for data in okk:
                    print('')
                    print(data )
                print('--------------------------------------------------------')
            elif reqw[0].upper() =='#INFO':
                print("""
                to add commands to the app :   #TEACH
                to update commands         :   #UPDATE
                to delete commands         :   #DELETE
                to view all db elements    :   #DB
                to leave the app           :   #EXIT

                """)
            elif reqw[0].upper() == '#LISTEN':
                add_ons.listen()

            elif len(reqw)<=3:
                lflag=(sfile.get(reqw,'short'))
                if lflag == True:
                    lflag=(sfile.get(reqw,'main'))
                    if lflag==True:
                        lastly=True
                        if lastly ==True:
                            # print("I have no idea how to answer you. If you want to teach me how to answer please type '#TEACH'")
                            learner.auto_learn(reqw)

            else:
                lflag=(sfile.get(reqw,'main'))
                if lflag == True:
                    # print("I have no idea how to answer you. If you want to teach me how to answer please type '#TEACH'")
                    learner.auto_learn(reqw)

    def reader():
        """done"""

        request=input(":)>>>  ")
        rqt= request.lower()
        rst=""
        for letter in rqt:
            if letter not in [',','.','!','?','*',';',':']:
                rst += letter
        rqb=rst.split()

        return rqb



reader.inference()
