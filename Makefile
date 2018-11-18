
SRC_DIR := .
OBJ_DIR := pdf
BLD_DIR := build
SRC_FILES := $(wildcard $(SRC_DIR)/*.html)
HTM_FILES := $(patsubst $(SRC_DIR)/%.html,$(BLD_DIR)/%.html,$(SRC_FILES))
PDF_FILES := $(patsubst $(SRC_DIR)/%.html,$(OBJ_DIR)/%.pdf,$(SRC_FILES))
DOC_FILES := $(wildcard docs/*.pdf)
ARCHIVE := $(OBJ_DIR)/archive-cln.zip 

all: $(ARCHIVE) $(HTM_FILES)
	
html: $(HTM_FILES)

pdf: $(PDF_FILES)

build/%.html: %.html structure.json
	if [ ! -d build ]; then mkdir build; fi
	./make-page.py $^ build/$< 
	
pdf/%.pdf: build/%.html
	if [ ! -L build/js ]; then ln -s ../js build/; fi
	if [ ! -L build/images ]; then ln -s ../images build/; fi
	if [ ! -L build/css ]; then ln -s ../css build/; fi
	wkhtmltopdf $< $@

$(ARCHIVE): $(PDF_FILES) $(DOC_FILES)
	zip $@ $(PDF_FILES) $(DOC_FILES)
	
clean:
	rm -rf $(ARCHIVE) pdf/*.pdf
