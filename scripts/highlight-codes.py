from spire.doc import *
from spire.doc.common import *
from os import listdir
from pathlib import Path
from helpers import load_csv_dataset

data_dir = Path('../data')
quotations_dataset = load_csv_dataset(data_dir.joinpath('quotations.csv'), delimiter=';')

for file in listdir(data_dir.joinpath('answers')):
    doc = Document()
    path = data_dir.joinpath('answers').joinpath(file).resolve()
    doc.LoadFromFile(str(path))
    
    for quotation in quotations_dataset:
        if quotation['document'] != file.replace('.docx',''):
            continue    
        # Find the text to comment on
        text = doc.FindString(quotation['content'], True, True)

        # Create a comment and set the content and author of the comment
        comment = Comment(doc)
        comment.Body.AddParagraph().Text = quotation['codes']
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
    doc.SaveToFile(str(data_dir.joinpath('answers-highlighted').joinpath(file)))
    doc.Close()
