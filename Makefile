
SRC_DIR := .
OBJ_DIR := pdf
SRC_FILES := $(wildcard $(SRC_DIR)/*.html)
PDF_FILES := $(patsubst $(SRC_DIR)/%.html,$(OBJ_DIR)/%.pdf,$(SRC_FILES))
DOC_FILES := $(wildcard docs/*.pdf)
ARCHIVE := $(OBJ_DIR)/archive-cln.zip 

all: $(ARCHIVE)
	

pdf/%.pdf: %.html
	wkhtmltopdf $< $@

$(ARCHIVE): $(PDF_FILES) $(DOC_FILES)
	zip $@ $(PDF_FILES) $(DOC_FILES)
	
clean:
	rm -rf $(ARCHIVE) pdf/*.pdf
