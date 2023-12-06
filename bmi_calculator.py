import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height / 100)**2
    return round(bmi, 2)

def main():
    st.title("BMI Calculator")
    st.subheader("Enter your details below:")

    name = st.text_input("Name:")
    gender = st.radio("Gender:", ("Male", "Female", "Other"))
    age = st.number_input("Age:", min_value=0, max_value=120, step=1)
    address = st.text_area("Address:")
    hobbies = st.multiselect(
        "Hobbies:", ("Reading", "Swimming", "Travelling", "Watching movies"))
    weight = st.number_input("Weight (in kg):",
                             value=0.0,
                             min_value=0.0,
                             max_value=500.0)
    height = st.number_input("Height (in cm):",
                             value=0.0,
                             min_value=0.0,
                             max_value=300.0)

    if st.button("Calculate BMI", key="calculate_button"):
        bmi = calculate_bmi(weight, height)

        # Colorful output
        if bmi < 18.5:
            st.warning(f"Hello {name}, your BMI is {bmi}. You are underweight. Please consider consulting a healthcare professional.")
        elif 18.5 <= bmi < 25:
            st.success(f"Hello {name}, your BMI is {bmi}. Congratulations! You have a healthy weight.")
        elif 25 <= bmi < 30:
            st.error(f"Hello {name}, your BMI is {bmi}. You are overweight. Please consider consulting a healthcare professional.")
        else:
            st.error(f"Hello {name}, your BMI is {bmi}. You are obese. Please consider consulting a healthcare professional.")

if __name__ == '__main__':
    main()
