def calculate_bmi(height,weight):
    print("Height = " +str(height))
    print("Weight = " +str(weight))
    bmi = weight /(height*2)
    print("BMI = " +str(bmi))
   
    if(bmi<18.5):
        classification = -1
    elif(bmi>= 18.5 and bmi<= 25):
        classification = 0
    else:
        classification = 1

    return bmi, classification

def classify_bmi(bmi):
    if(bmi<18.5):
        print ("Underweight")
    elif(bmi>= 18.5 and bmi<= 25):
        print("Normal Weight")
    else:
        print("Overweight,better exercise!!")
    return 

def main():
  bmi, class_value = calculate_bmi(1.7,60)
  classify_bmi(bmi)
  print("Classification value: ",class_value)
  return

if __name__=="__main__":
 main()


