move(state(middle,onbox,middle,hasnot),
   grasp,
   state(middle,onbox,middle,has)).
move(state(P,onfloor,P,H),
   climb,
   state(P,onbox,P,H)).
move(state(P1,onfloor,P1,H),
   drag(P1,P2),
   state(P2,onfloor,P2,H)).
move(state(P1,onfloor,B,H),
   walk(P1,P2),
   state(P2,onfloor,B,H)).
canget(state(_,_,_,has)).
canget(State1) :-
   move(State1,_,State2),
   canget(State2).


# | ?- [monkey_banana].
# compiling D:/TP Prolog/Sample_Codes/monkey_banana.pl for byte code...
# D:/TP Prolog/Sample_Codes/monkey_banana.pl compiled, 17 lines read - 2167 bytes written, 19 ms

# (31 ms) yes
# | ?- canget(state(atdoor, onfloor, atwindow, hasnot)).

# true ?

# yes
# | ?- trace
# .
# The debugger will first creep -- showing everything (trace)

# yes
# {trace}
# | ?- canget(state(atdoor, onfloor, atwindow, hasnot)).
#       1 1 Call: canget(state(atdoor,onfloor,atwindow,hasnot)) ?
#       2 2 Call: move(state(atdoor,onfloor,atwindow,hasnot),_52,_92) ?
#       2 2 Exit:move(state(atdoor,onfloor,atwindow,hasnot),walk(atdoor,_80),state(_80,onfloor,atwindow,hasnot)) ?
#       3 2 Call: canget(state(_80,onfloor,atwindow,hasnot)) ?
#       4 3 Call: move(state(_80,onfloor,atwindow,hasnot),_110,_150) ?
#       4 3 Exit: move(state(atwindow,onfloor,atwindow,hasnot),climb,state(atwindow,onbox,atwindow,hasnot)) ?
#       5 3 Call: canget(state(atwindow,onbox,atwindow,hasnot)) ?
#       6 4 Call: move(state(atwindow,onbox,atwindow,hasnot),_165,_205) ?
#       6 4 Fail: move(state(atwindow,onbox,atwindow,hasnot),_165,_193) ?
#       5 3 Fail: canget(state(atwindow,onbox,atwindow,hasnot)) ?
#       4 3 Redo: move(state(atwindow,onfloor,atwindow,hasnot),climb,state(atwindow,onbox,atwindow,hasnot)) ?
#       4 3 Exit: move(state(atwindow,onfloor,atwindow,hasnot),drag(atwindow,_138),state(_138,onfloor,_138,hasnot)) ?
#       5 3 Call: canget(state(_138,onfloor,_138,hasnot)) ?
#       6 4 Call: move(state(_138,onfloor,_138,hasnot),_168,_208) ?
#       6 4 Exit: move(state(_138,onfloor,_138,hasnot),climb,state(_138,onbox,_138,hasnot)) ?
#       7 4 Call: canget(state(_138,onbox,_138,hasnot)) ?
#       8 5 Call:   move(state(_138,onbox,_138,hasnot),_223,_263) ?
#       8 5 Exit: move(state(middle,onbox,middle,hasnot),grasp,state(middle,onbox,middle,has)) ?
#       9 5 Call: canget(state(middle,onbox,middle,has)) ?
#       9 5 Exit: canget(state(middle,onbox,middle,has)) ?
#       7 4 Exit: canget(state(middle,onbox,middle,hasnot)) ?
#       5 3 Exit: canget(state(middle,onfloor,middle,hasnot)) ?
#       3 2 Exit: canget(state(atwindow,onfloor,atwindow,hasnot)) ?
#       1 1 Exit: canget(state(atdoor,onfloor,atwindow,hasnot)) ?
      
# true ?

# (78 ms) yes