# Test Cases
from TownCrier import crier

Crier = crier(True, True, True)

Crier.write_crier_exception("Testing Crier Exception")
Crier.write_message("This is a Message", 0)
Crier.write_message("This is a second Message With More Depth", 1)
Crier.write_message("This is a third message with a lot more depth", 13)
Crier.write_bland_message("This is a BLAND message", 0)
Crier.set_color("grEen");print(Crier.color + "Show me GREEN!" + Crier.reset_color())
Crier.set_color("red");print(Crier.color + "Show me RED!" + Crier.reset_color())
Crier.set_color("smash");print(Crier.color + "Show me ERROR!" + Crier.reset_color())
Crier.set_prefix(")))","@");print(Crier.write_message("Testing custom Prefixes", 3))
Crier.dump_object(Crier)
