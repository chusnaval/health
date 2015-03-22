/*----------*/
function objetoAjax(){
	var xmlhttp=false;
	try{
		xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
	}catch(e) {
		try{
			xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
		}catch (e){
			xmlhttp = false;
		}
	}
	if(!xmlhttp && typeof XMLHttpRequest!='undefined') {
		xmlhttp = new XMLHttpRequest();
	}
	return xmlhttp;
}

function searchFiltered(Pag, objId, objIdEmpty){
	divEmpty = document.getElementById(objIdEmpty);
	if(document.form.q.value=="")
	{
		divEmpty.innerHTML = "<div class='msg' align='justify'>Complete la informacion</div>"
	}
	else {
		divResult = document.getElementById(objId);
		value = document.form.q.value
		ajax = objetoAjax();
		ajax.open("GET", Pag+ "?q=" + valor);
		ajax.onreadysstatechange=function() {
			if(ajax.readyState==4){
				divResult.innerHTML = ajax.responseText
				divEmpty.innerHTML = ""
			}
		}
		ajax.send(null)
	}
}