import lexer
import interpreter
import time

# Added efficiency with print statements

while True:
  command = input(">>> ")
  #try:
  if command[:4] == "run ":
    try:
      command = open(f"{command[4:]}.qball").read()
    except FileNotFoundError:
      raise Exception("File not found to run")
  if command == "debug":
    interpreter.debug = True
  else:
    result = lexer.lexer(command).generate_tokens()
    interpret = interpreter.interpreter(result)
    interpret.interpret()
  #except Exception as e:
  #  try:
  #    print(f"\033[91mError at section {interpret.section}: {e}#\033[00m", flush=True)
  #  except NameError:
  #    print(f"\033[91mLexer error: {e}\033[00m", flush=True)
  try: command.close();
  except AttributeError: pass
  except Exception as e: print(e)
