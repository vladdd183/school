Program pascal3;
var a, b, c: Integer;
Begin
    Write('Input Number: ');
    ReadLn(a);
    b:= a div 10;
    c:= a mod 10;
    WriteLn('Sum: ', b+c);
    WriteLn('Multi: ', b*c);
    WriteLn('New Number: ', c*10+b);


End.
