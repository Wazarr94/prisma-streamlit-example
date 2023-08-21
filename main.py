import streamlit as st

from data import init_connection
from generated.prisma import Prisma


def delete_user(db: Prisma, user_id: str):
    db.user.delete(where={"id": user_id})


def main():
    st.title("Prisma Streamlit Demo")

    db = init_connection()

    st.write("## Users")
    users = db.user.find_many()
    col1, col2 = st.columns([5, 1])
    for user in users:
        col1.write(user.name)
        col2.button(
            "Delete",
            key=user.id,
            on_click=delete_user,
            kwargs={"db": db, "user_id": user.id},
        )

    st.write("## Create User")
    name = st.text_input("Name")
    if st.button("Create"):
        db.user.create({"name": name})
        name = ""
        st.experimental_rerun()


if __name__ == "__main__":
    main()
