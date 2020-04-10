function log(){
    window.location='/login';
}
function head(head){
    let x=document.getElementById('head');
    // console.log(par);
    let arr=['Dance Acadmey','Sessional Restuarnt','Qutub Website'];
    if(head==arr[0]){
        x.innerHTML=arr[1];
    }
    else if(head==arr[1]){
        x.innerHTML=arr[2];
    }
    else{
        x.innerHTML=arr[0]
    }
}
// var param=document.getElementById('head');
// let par=document.getElementById('head').innerHTML;
function change(){
    var par=document.getElementById('head').innerHTML;
}

setInterval(() => {
    var par=document.getElementById('head').innerHTML;
}, 1900);
setInterval(head,2000,par);

function jaadmin(){
    window.location='/admin';
}
var para=document.getElementById('para');
para.addEventListener('mouseover',function run(){
    para.innerHTML='Gujrati Thali';
    console.log("hello");
})
para.addEventListener('mouseout',function run(){
    para.innerHTML='';
})
function signup(){
    window.location='/signup';
}
function signout(){
    window.location='/logout';
}
