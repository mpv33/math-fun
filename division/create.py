#for i in range(0,22):
#    print('<a id="l'+str((i+1))+'" onclick="tablefun('+str(i+1)+',3,'+str((i*5))+','+str(((i+1)*5))+',0)" class="dropdown-item l_s" href="#">3*['+str((i*5))+'...'+str(((i+1)*5))+']</a>')
#print('<a id="l'+str(i)+'" class="btn l_s" href="funtable/l'+str(i)+'.html">'+str(i)+"*[1...99]</a>")
b = '''
<!--Copyright 2020-2021 SUNIL KUMAR YADAV. (https://sunilkuyadav.github.io/MathFun/)-->
<!DOCTYPE html>
<html lang="">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="titlel"></title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="../cal.css">
    <script src="division.js"></script>
    <script defer src="cdown.js"></script>
</head>

<body>
    <div class="cantainer">
        <div class="main">
            <div class="operation">
                <nav class="navbar navbar-expand-md bg-dark navbar-dark">
                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="collapsibleNavbar">
                    <ul class="navbar-nav">
                      <li class="nav-item">
                        <a class="nav-link sp" href="../addition.html">Addition</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link sp" href="../substraction.html">Substraction</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link sp" href="../multiplication.html">Multiplication</a>
                      </li> 
                      <li class="nav-item">
                        <a class="nav-link sp" href="../division.html">Division</a>
                      </li>
                        <li class="nav-item">
                        <a class="nav-link sp" href="../tablefun.html">TableFun</a>
                      </li>
                    </ul>
                  </div>  
                </nav>
            </div>
             <div class="div">
            <div class="dropdown">
                <button type="button" class="btn dropdown-toggle btnl" data-toggle="dropdown">Level 1
    </button>
                <div id="qs" class="qs"></div>
                    <div class="text-center dropdown-menu">
                        <a id="l1" onclick="divt(1,10,0,0)" class="l_s dropdown-item" href="d1.html">Level 1</a>
                        <a id="l2" onclick="divt(2,2,0,0)" class="l_s dropdown-item" href="d2.html">Level 2</a>
                        <a id="l3" onclick="divt(3,3,0,0)" class="l_s dropdown-item" href="d3.html">Level 3</a>
                        <a id="l4" onclick="divt(4,4,0,0)" class="l_s dropdown-item" href="d4.html">Level 4</a>
                        <a id="l5" onclick="divt(5,5,0,0)" class="l_s dropdown-item" href="d5.html">Level 5</a>
                        <a id="l6" onclick="divt(6,6,0,0)" class="l_s dropdown-item" href="d6.html">Level 6</a>
                        <a id="l7" onclick="divt(7,7,0,0)" class="l_s dropdown-item" href="d7.html">Level 7</a>
                        <a id="l8" onclick="divt(8,8,0,0)" class="l_s dropdown-item" href="d8.html">Level 8</a>
                        <a id="l9" onclick="divt(9,9,0,0)" class="l_s dropdown-item" href="d9.html">Level 9</a>
                        <a id="l10" onclick="divt(10,10,0,0)" class="l_s dropdown-item" href="d10.html">Level 10</a>
                        <a id="l11" onclick="divt(11,11,0,0)" class="l_s dropdown-item" href="d11.html">Level 11</a>
                        <a id="l12" onclick="divt(12,12,0,0)" class="l_s dropdown-item" href="d12.html">Level 12</a>
                        <a id="l13" onclick="divt(13,13,0,0)" class="l_s dropdown-item" href="d13.html">Level 13</a>
                        <a id="l14" onclick="divt(14,14,0,0)" class="l_s dropdown-item" href="d14.html">Level 14</a>
                        <a id="l15" onclick="divt(14,15,0,0)" class="l_s dropdown-item" href="d15.html">Level 15</a>
                        <a id="l16" onclick="divt(15,16,0,0)" class="l_s dropdown-item" href="d16.html">Level 16</a>
                        <a id="l17" onclick="divt(16,17,0,0)" class="l_s dropdown-item" href="d17.html">Level 17</a>
                        <a id="l18" onclick="divt(18,18,0,0)" class="l_s dropdown-item" href="d18.html">Level 18</a>
                        <a id="l18" onclick="divt(18,18,0,0)" class="l_s dropdown-item" href="#">Level 18</a>
                        
                    </div>
                </div>
                <div id="quest">
                    <div class="question" id="question">start</div>
                    <div id="cd"><div id="app"></div></div>
                </div>
                <hr>
                <div class="input">
                    <div id="option-buttons" class="btn-grid">
                        <button id="btn1" class="btn btnc" href="">1</button>
                        <button id="btn2" class="btn btnc" href="#">2</button>
                        <button id="btn3" class="btn btnc" href="#">3</button>
                        <button id="btn4" class="btn btnc" href="#">4</button>
                    </div>
                </div>
                <hr>
                <div class="hint">
                    <button id="hintshow" class="hintshow btn" type="button">HINT</button>
                    <h1 id="hint">division</h1>
                </div>
            </div>           
            
        </div>
    </div>
    <footer>
            <div class="cpd">SUNIL KUMAR YADAV &copy; 2020-21</div>
    </footer>
</body>
    <script>
        $( document ).ready(function() {
        $('#l|').click();
    });
        $('.l_s').on('click',function(){
            $('.btnl').text(($(this).text()));
            $('#titlel').text(($(this).text())+" | Division");
        });
    </script>
</html>


'''
for i in range(1,19):
    x = b.replace('|',str(i))
    p = ('d'+str(i)+'.html')
    f = open(p,"w")
    f.write(x)
    f.close()
    
