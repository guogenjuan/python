#!python3
#randomQuizGenerator.py - Creates quizzes with questions and answers in
#random order ,along with the answer key.

import random
import os

#the quiz data.Keys are states and values are their capitals

capitals = {'Alibama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock',
        'Califonia':'Sacramento','Colorado':'Denver','Connecticut':'Hartford','Delawre':'Dover','Florida':'Tallahassee',
            'Groragia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','Illinois':'Spingfield','Indiana':'Indianapolis',
            'Iowa':'Des Moines','Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':'Augusta',
            'Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing','Minnesota':'Saint Paul','Mississippi':'Jackson',
            'Missouri':'Jefferson city','Montana':'Helena','Nebraska':'Loncpln','Nevada':'Carson city','New Hampshire':'Concord',
            'New Jersey':'Trenton','newMexico':'Santa Fe','New York':'Albany','North Carolina':'Raleigh','North Dakota':'Bismarck',
            'ohio':'Columbus','Oklahoma':'oklaoma City','South Carolin':'columbia','south Dakata':'pierre','tennessee':'Nashville',
            'Texas':'Austin','Utah':'Salt Lake vity','Vermont':'Montpelier','Virginia':'Richmond','Washington':'Olympia','West Virginia':'charleston',
            'Wisconsion':'Madison','Wyoming':'Cheyenne','ssss':'1111111','aaaaa':'222222','bbbbb':'333333'}

#Generate 35 quiz files
for quizNum in range (35):
    #TODO Create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt'%(quizNum+1),'w')  #s%就是%后面的变量
    answerKeyFile = open('capitalsquiz_answers%s.txt'%(quizNum+1),'w')
    
    
    #TODO Write out the header for the quiz
    
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')#写姓名，日期和年级
    quizFile.write(('' * 20)+'State Capitals Quiz (Form %s)' % (quizNum+1)) #标题
    quizFile.write('\n\n')
    
    #TODO Shuffle the order of the states
    states = list(capitals.keys())    #返回州名字列表
    random.shuffle(states)    #随机传递列表的值
    
    #TODO Loop through all 50 states,making a question for each

    for questionNum in range(50):
        #Get right and wrong answers.
      
        correctAnswer = capitals[states[questionNum]] #正常答案存储列表
        wrongAnswers= list(capitals.values())  #错误答案存储列表
        del wrongAnswers[wrongAnswers.index(correctAnswer)]#错误列表里剔除正确答案
        wrongAnswers = random.sample(wrongAnswers,3)  #错误列表里选取3个作为选项
        answerOptions = wrongAnswers + [correctAnswer]   #可选项
        random.shuffle(answerOptions)   #答案随机排列

        #TODO write the question and answer options to the quiz file
        quizFile.write('%s.what is the capital of %s?\n'%(questionNum+1,states[questionNum]))  #写入试卷问题

        for i in range(4): #可选项显示
            quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        
        #TODO write the answer key to a file
        answerKeyFile.write(' %s. %s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)])) #答案写入文件

    quizFile.close()
    answerKeyFile.close()
        
