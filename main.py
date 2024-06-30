import streamlit as st
from expense import Expense
import pandas as pd

def main():
    st.title("Expense Tracker")  
    get_user_expense()
    total_expenses = display_expenses()
    if total_expenses is not None:
        amount_per_person = split_expenses(total_expense=total_expenses)

def get_user_expense():
    if 'expenses' not in st.session_state:
        st.session_state.expenses = []
          
    with st.form(key='expense_form'):
        expense_name = st.text_input(label='Enter expense name')
        expense_amount = st.number_input(label='Enter expense amount', min_value=0.0, format="%.2f")
        selected_expense_category = st.selectbox('Select a category', ["🍔 Food", "🏨 Accommodation", "🚕 Transport", "👽 Misc"], key=1)
        payer_name = st.text_input(label='Enter payer name')
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if expense_name and expense_amount > 0 and payer_name:
            new_expense = Expense(name=expense_name, amount=expense_amount, category=selected_expense_category, payer=payer_name)
            st.session_state.expenses.append(new_expense)
            st.success(f"Successfully added {expense_name}")
        else:
            st.error("Please enter all fields correctly.")

def display_expenses():
    if 'expenses' in st.session_state and st.session_state.expenses:
        expense_data = [{
            "Name": expense.name,
            "Category": expense.category,
            "Amount": expense.amount,
            "Payer": expense.payer
        } for expense in st.session_state.expenses]

        df = pd.DataFrame(expense_data)
        st.subheader("Expenses")
        st.dataframe(df)
        total_expenses = df['Amount'].sum()
        st.write(f"Total Expense: £{total_expenses:.2f}")
        return total_expenses

def split_expenses(total_expense):
    st.subheader("Split Expenses")
    number_of_people = st.slider("How many people should divide the expenses?", 2, 10, 4)
    
    if number_of_people > 0:
        amount_per_person = total_expense / number_of_people
        st.write(f"The total cost per person is £{amount_per_person:.2f} when divided among {number_of_people} people.")
        return amount_per_person
    else:
        st.error("Number of people must be greater than zero.")
        return None

if __name__ == "__main__":
    main()
