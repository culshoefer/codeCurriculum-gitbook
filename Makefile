SOURCES = README.md chapter1.md chapter2.md chapter3.md chapter4.md

name = "Introduction to Python and PyGame"

all: html pdf

html : $(SOURCES)
	pandoc --toc --toc-depth=3 --self-contained --standalone -t html5 -f markdown -o $(name).html $(SOURCES)

pdf : $(SOURCES)
	pandoc --toc --toc-depth=3 --self-contained --standalone -f markdown -o $(name).pdf $(SOURCES)


