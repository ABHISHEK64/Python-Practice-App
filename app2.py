import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image=Image.open('./Images/LogoApp2.png')
st.image(image,use_column_width=False
st.write(""" # DNA Nucleotide Count Web App
\n
This apps counts the nucleotide composition of query DNA!
""")

#Import Text Box
st.header('Enter DNA Sequence')
sequence_input=">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAAGAACT"
sequence=st.text_area("Sequence input",sequence_input,height=25)
sequence=sequence.splitlines()#split into new in form of list
sequence=sequence[1:]
sequence=''.join(sequence)

st.write("""
****
""")

st.header('INPUT (DNA Query)')
## print drictnary
def DNA_nucleotide_count(seq):
    d=dict([
       ('A',seq.count('A')),
       ('T',seq.count('T')),
       ('G',seq.count('G')),
       ('C',seq.count('C')),    
    ])
    return d
X=DNA_nucleotide_count(sequence)
x_label=list(X)
x_Values=list(X.values())
X
 ###2.print text
st.subheader('2.Print Text')
st.write('There are' +str(X['A'])+'adenine (A)')
st.write('There are' +str(X['T'])+'thymine (T)')
st.write('There are' +str(X['G'])+'adenine (G)')
st.write('There are' +str(X['C'])+'adenine (C)')
##3.data frame
st.subheader('3. Display Data Frame')
df=pd.DataFrame.from_dict(X,orient='index')
df=df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide'})
st.write(df)
## 4. Display Bar Chart Using Altair
st.subheader('4. Display Bar Chart')
p=alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p=p.properties(
    width=alt.Step(60) #Controls width of bar
)
st.write(p)