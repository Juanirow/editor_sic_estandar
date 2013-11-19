EJECUTABLE=python main.py
clean:
	@rm -rf *.pyc
	@rm -rf *.o[x,s] *.t[x,s]
	@rm -rf parsetab.py
	@rm -rf *.out && clear
	@rm -rf salidas/*.o[x,s] salidas/*.t[x,s]
	@rm -rf ply/*.pyc
run:
	$(EJECUTABLE)
