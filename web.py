import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

# st.title("My todo App")
# st.subheader("This is my todo app.")
# st.write("This app ip")
st.title("Tareas Irene - Horno")
st.subheader("Claro, hay que hacer las cosa")
st.write("Listemos qué hay que hacer")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        print(todo)

value = st.text_input(label=" ", placeholder='Enter a todo',
                      on_change=add_todo, key='new_todo')
#
# st.session_state