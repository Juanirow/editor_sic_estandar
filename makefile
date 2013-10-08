EJECUTABLE=python main.py
clean:
	@rm -rf *.pyc
	@rm -rf *.o{x,s} *.t{x,s}
	@rm -rf parsetab.py
	@rm -rf *.out
run:
	$(EJECUTABLE)
