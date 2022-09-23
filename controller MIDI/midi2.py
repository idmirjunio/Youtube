

import mido
msg2 = mido.get_input_names()  #'DJControl Starlight 0'
msg = mido.get_output_names()  #'DJControl Starlight 1'
#print(type(msg))
print(msg)
#print(type(msg2))
print(msg2)

inport = mido.open_input('DJControl Starlight 0')
#outport = mido.open_output('DJControl Starlight 1')
msg = inport.receive()
print(msg)