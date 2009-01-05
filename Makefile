DESTDIR  =
PREFIX   = /usr/local
EXEC_DIR = $(DESTDIR)$(PREFIX)/bin
PROGRAM  = scm-up-all.py

.PHONY: run
run:
	./$(PROGRAM)

.PHONY: clean
clean:
	rm $(PROGRAM)c

.PHONY: install
install:
	install -m 0755 $(PROGRAM) $(EXEC_DIR)

.PHONY: uninstall
uninstall:
	rm $(EXEC_DIR)/$(PROGRAM)
