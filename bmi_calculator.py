import streamlit as st

# Define a function to calculate BMI
def calculate_bmi(height, weight):
    bmi = weight / (height/100)**2
    return bmi

# Define a function to compare BMI to average BMI
def compare_to_average_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "healthy weight"
    elif bmi >= 25 and bmi < 30:
        return "overweight"
    else:
        return "obese"

# Create a streamlit app
def main():
    # Set app title
    st.title("BMI Calculator")

    # Add inputs for height and weight
    height = st.number_input("Enter your height (in cm)", min_value=0, max_value=300, step=1)
    weight = st.number_input("Enter your weight (in kg)", min_value=0, max_value=500, step=1)


    # Calculate BMI and compare to average BMI
    if height != 0 and weight != 0:
        bmi = calculate_bmi(height, weight)
        bmi_status = compare_to_average_bmi(bmi)

        # Display BMI and comparison to average BMI
        st.write("Your BMI is {:.2f}".format(bmi))
        st.write("You are {} compared to the average person.".format(bmi_status))

if __name__ == "__main__":
    main()
