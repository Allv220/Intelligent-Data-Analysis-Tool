
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDORleftMASMENOSleftPORDIVrightUMENOSrightNOTAND CADENA CORDER CORIZQ DECIMAL DIV ENTERO MAS MENOS NOT OR PARDER PARIZQ POR PTCOMA REVALUARinstrucciones    : instruccion instrucciones\n                        | instruccion instruccion : CORIZQ expresion CORDERexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIV expresion\n                  | expresion AND expresion\n                  | expresion OR expresionexpresion : MENOS expresion %prec UMENOS\n                  | NOT expresion %prec NOTexpresion : PARIZQ expresion PARDERexpresion    : ENTERO\n                    | DECIMAL\n                    | CADENA'
    
_lr_action_items = {'CORIZQ':([0,2,12,],[3,3,-3,]),'$end':([1,2,4,12,],[0,-2,-1,-3,]),'MENOS':([3,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,],[6,14,6,6,6,-13,-14,-15,6,6,6,6,6,6,-10,-11,14,-4,-5,-6,-7,14,14,-12,]),'NOT':([3,6,7,8,13,14,15,16,17,18,],[7,7,7,7,7,7,7,7,7,7,]),'PARIZQ':([3,6,7,8,13,14,15,16,17,18,],[8,8,8,8,8,8,8,8,8,8,]),'ENTERO':([3,6,7,8,13,14,15,16,17,18,],[9,9,9,9,9,9,9,9,9,9,]),'DECIMAL':([3,6,7,8,13,14,15,16,17,18,],[10,10,10,10,10,10,10,10,10,10,]),'CADENA':([3,6,7,8,13,14,15,16,17,18,],[11,11,11,11,11,11,11,11,11,11,]),'CORDER':([5,9,10,11,19,20,22,23,24,25,26,27,28,],[12,-13,-14,-15,-10,-11,-4,-5,-6,-7,-8,-9,-12,]),'MAS':([5,9,10,11,19,20,21,22,23,24,25,26,27,28,],[13,-13,-14,-15,-10,-11,13,-4,-5,-6,-7,13,13,-12,]),'POR':([5,9,10,11,19,20,21,22,23,24,25,26,27,28,],[15,-13,-14,-15,-10,-11,15,15,15,-6,-7,15,15,-12,]),'DIV':([5,9,10,11,19,20,21,22,23,24,25,26,27,28,],[16,-13,-14,-15,-10,-11,16,16,16,-6,-7,16,16,-12,]),'AND':([5,9,10,11,19,20,21,22,23,24,25,26,27,28,],[17,-13,-14,-15,-10,-11,17,-4,-5,-6,-7,-8,-9,-12,]),'OR':([5,9,10,11,19,20,21,22,23,24,25,26,27,28,],[18,-13,-14,-15,-10,-11,18,-4,-5,-6,-7,-8,-9,-12,]),'PARDER':([9,10,11,19,20,21,22,23,24,25,26,27,28,],[-13,-14,-15,-10,-11,28,-4,-5,-6,-7,-8,-9,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,2,],[1,4,]),'instruccion':([0,2,],[2,2,]),'expresion':([3,6,7,8,13,14,15,16,17,18,],[5,19,20,21,22,23,24,25,26,27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones_lista','gramatica.py',88),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','gramatica.py',89),
  ('instruccion -> CORIZQ expresion CORDER','instruccion',3,'p_instrucciones_evaluar','gramatica.py',92),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','gramatica.py',96),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','gramatica.py',97),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','gramatica.py',98),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','gramatica.py',99),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','gramatica.py',100),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','gramatica.py',101),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','gramatica.py',178),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','gramatica.py',179),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','gramatica.py',193),
  ('expresion -> ENTERO','expresion',1,'p_expresion_number','gramatica.py',197),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_number','gramatica.py',198),
  ('expresion -> CADENA','expresion',1,'p_expresion_number','gramatica.py',199),
]
