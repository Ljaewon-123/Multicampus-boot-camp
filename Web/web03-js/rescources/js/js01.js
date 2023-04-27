function fileFunction(){
    window.alert('외부 js file 에서 실행됨');   // window 생략가능
}

window.onload = function(){
    alert('윈도우 로딩 됨! (로딩 후)');
}