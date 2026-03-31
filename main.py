import pandas
 numbers=[1,1,2,3,8,13,21,34,55]
 resulte=[n for n in numbers if n%2==0]
 squared_numbers=[n*n for n in numbers]

 print(squared_numbers)

 file1=open("file1.txt").read().split()
 file2=open("file2.txt").read().split()
 print(file1)
 print(file2)
 result=[int(num) for num in file1 if num in file2 ]
 print(result)

 names=["Alex","Beth","Caroline","Eleaonora","Freddie"]
 sscore=[60,22,40,55,85]
 for i in sscore:
     scores={student:i for student in names}
 print(scores)

 weather_c={
     "Monday":12,
     "Tuesday":14,
     "Wednesday":15,
     "Thursday":14,
     "Friday":21,
     "Saturday":22,
     "Sunday":24,

 }

 weather_f={(key, (val*9.5)+35) for key, val in weather_c.items()}

 print(weather_f)

 print(weather_c)


 student_dict={
     "student":["Angela","James","Lily"],
     "score":[56,76,98]
 }
 student_data_frame=pandas.DataFrame(student_dict)
 print(student_data_frame)

 for (index,row) in student_data_frame.iterrows():
     if row.student=="Angela":
         print(row.score)

 nato=pandas.read_csv("nato_phonetic_alphabet.csv")
 nato=nato.set_index("letter")

 my_dict=nato["code"].to_dict()
 print(my_dict)
 word =input("Enter a word: ")
 word=word.upper()
 phonetic_code_word=[]
 for char in word:
     if char in my_dict:
         phonetic_code_word.append(my_dict[char])
 print(phonetic_code_word)

SECOND SOLUTION
 data=pandas.read_csv("nato_phonetic_alphabet.csv")
  print(data.to_dict())
 phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
  print(phonetic_dict)

 word=input("Enter a word: ").upper()
 output_list=[phonetic_dict[letter] for letter in word]
 print(output_list)

