
SRC_DIR := .
OBJ_DIR := pdf
SRC_FILES := $(wildcard $(SRC_DIR)/*.html)
PDF_FILES := $(patsubst $(SRC_DIR)/%.html,$(OBJ_DIR)/%.pdf,$(SRC_FILES))
ARCHIVE := $(OBJ_DIR)/archive-cln.zip 

all: $(ARCHIVE)
	

pdf/%.pdf: %.html
	wkhtmltopdf $< $@

$(ARCHIVE): $(PDF_FILES)
	zip $@ $(PDF_FILES)
	
clean:
	rm -rf $(ARCHIVE) $(PDF_FILES)
