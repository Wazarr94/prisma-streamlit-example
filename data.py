import subprocess

import streamlit as st


def generate_prisma_client():
    print("GENERATING PRISMA CLIENT")
    subprocess.call(["prisma", "generate"])
    print("GENERATED PRISMA CLIENT")


generate_prisma_client()


try:
    from generated.prisma import Prisma
except RuntimeError:
    from prisma_cleanup import cleanup

    cleanup()
    print("GOT RUNTIME ERROR")
    generate_prisma_client()
    from generated.prisma import Prisma


@st.cache_resource
def init_connection() -> Prisma:
    db = Prisma()
    db.connect()
    return db
