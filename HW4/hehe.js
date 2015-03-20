var a = 1;
function f1(){
	console.log(a+1);
}
function f2(a){
	var b = a+0;
	return function(){
		console.log(a+1);
	}
}

setTimeout(f2(a), 200);

a+=1;
