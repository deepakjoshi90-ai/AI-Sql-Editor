import streamlit as st

import mysql.connector



# -----------------------------

# Database Connection

# -----------------------------

connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="Password",      # Replace with your MySQL password

    database="DB Name"

)



cursor = connection.cursor()



# -----------------------------

# Page Title

# -----------------------------

st.title("AI SQL Query Auditor")



st.write("Write your SQL query and click Run Query.")



# -----------------------------

# Business Question

# -----------------------------

business_question = st.text_input(

    "Business Question"

)



# -----------------------------

# SQL Query

# -----------------------------

query = st.text_area(

    "Write SQL Query",

    height=200

)



# -----------------------------

# Run Button

# -----------------------------

run = st.button("Run Query")



# -----------------------------

# Execute Query

# -----------------------------

if run:



    if query.strip() == "":

        st.warning("Please enter a SQL query.")



    else:



        try:



            cursor.execute(query)



            if query.strip().lower().startswith("select"):



                result = cursor.fetchall()



                column_names = []



                for column in cursor.description:

                    column_names.append(column[0])



                st.success("Query Executed Successfully")



                st.dataframe(

                    result,

                    column_config=None,

                    use_container_width=True

                )



                st.write("Columns Returned")



                st.write(column_names)



            else:



                connection.commit()



                st.success("Query Executed Successfully")



        except Exception as e:



            st.error("Query Execution Failed")



            st.write(e)

            
