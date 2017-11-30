Program Geron;
var a,b,c: Integer;
var P,S: Real;
Begin
  Write('A: ');
  ReadLn(a);
  Write('B: ');
  ReadLn(b);
  Write('C: ');
  ReadLn(c);
  P:= (a + b + c) / 2;
  S:= sqrt(P*(P-a)*(P-b)*(P-c));
  WriteLn('Площадь: ', S);
End.
