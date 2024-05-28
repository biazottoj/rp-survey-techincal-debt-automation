from spire.doc import *
from spire.doc.common import *

# Create an object of Document class and load a Word document
doc = Document()
doc.LoadFromFile("../data/s1_r2.docx")

# Find the text to comment on
text = doc.FindString("but I very much doubt it would be useful without extensive intelligent customization options.", True, True)

# Create a comment and set the content and author of the comment
comment = Comment(doc)
comment.Body.AddParagraph().Text = "1-customization options are necessary"
comment.Format.Author = "Joao Paulo"

# Get the found text as a text range and get the paragraph it belongs to
range = text.GetAsOneRange()
paragraph =  range.OwnerParagraph

# Add the comment to the paragraph
paragraph.ChildObjects.Insert(paragraph.ChildObjects.IndexOf(range) + 1, comment)

# Create a comment start mark and an end mark and set them as the start and end marks of the created comment
commentStart = CommentMark(doc, CommentMarkType.CommentStart)
commentEnd = CommentMark(doc, CommentMarkType.CommentEnd)
commentStart.CommentId = comment.Format.CommentId
commentEnd.CommentId = comment.Format.CommentId

# Insert the created comment start and end tags before and after the found text respectively
paragraph.ChildObjects.Insert(paragraph.ChildObjects.IndexOf(range), commentStart)
paragraph.ChildObjects.Insert(paragraph.ChildObjects.IndexOf(range) + 1, commentEnd)

# Save the document
doc.SaveToFile ("teste.docx")
doc.Close()