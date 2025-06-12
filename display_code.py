import streamlit as st

st.code("""def hello():
        print("Hello Streamlit!")""", language="python")

st.code("""public class Main {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}""", language="java")

st.json({
    "name": "Disha",
    "age": 21,
    "skills": ["Python", "ML", "AI"]
})