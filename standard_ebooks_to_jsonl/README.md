# standard-ebooks-to-jsonl
Python script to convert the .xml library from standardebooks.org to .jsonl.

The Python executable 'xml_to_jsonl' is set up to convert the contents of 'ebooks.xml' to 'converted_books.jsonl.' when run. To change the source or destination change the one reference to that file name in the executable.

The XML file was obtained on April 15 of 2020 from https://standardebooks.org/opds/all (thanks djreimer@gmail.com)and uses the formatting of that time. The one change I made to the XML file was removing "xmlns="http://www.w3.org/2005/Atom" since removing that line was easier than writing the code to ignore it.


