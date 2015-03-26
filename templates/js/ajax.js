/*----------*/
function objectAjax() {
    var xmlhttp = false;
    try {
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
        try {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e) {
            xmlhttp = false;
        }
    }
    if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
        xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}

function searchFiltered(Pag, objId, objIdEmpty) {
    divEmpty = document.getElementById(objIdEmpty);
    if (document.form.q.value == "") {
        divEmpty.innerHTML = "<div class='msg' align='justify'>Complete la informacion</div>"
    }
    else {
        divResult = document.getElementById(objId);
        value = document.form.q.value;
        ajax = objectAjax();
        ajax.open("GET", Pag + "?q=" + valor);
        ajax.onreadysstatechange = function () {
            if (ajax.readyState == 4) {
                divResult.innerHTML = ajax.responseText
                divEmpty.innerHTML = ""
            }
        }
        ajax.send(null)
    }
}

function create(Pag, objId, objIdEmpty) {
    divEmpty = document.getElementById(objIdEmpty);
    if (document.form.name.value == "") {
        divEmpty.innerHTML = "<div class='msg' align='justify'>Complete la informacion</div>"
    }
    else {
        divResult = document.getElementById(objId);
        name = document.form.name.value;
        ajax = objectAjax();
        ajax.open("GET", Pag + "?name=" + name, true);
        ajax.onreadystatechange = function () {
            if (ajax.readyState == 4) {
                divResult.innerHTML = ajax.responseText
                divEmpty.innerHTML = ""
            }
        }
        ajax.send(null)
    }

}

function deleteRegister(Pag, objId) {
    divEmpty = document.getElementById(objId);
    var agree = confirm('¿Esta seguro de eliminar el registro?');
    if (agree) {
        ajax = objectAjax();
        ajax.open("GET", Pag, true);
        ajax.onreadystatechange = function () {
            if (ajax.readyState == 4) {
                divEmpty.innerHTML = ajax.responseText
            }
        }
        ajax.send(null)
    }
}

function details(Pag, objId) {
    divResult = document.getElementById(objId);
    var agree = confirm('¿Actualizar el registro?');
    if (agree) {
        ajax = objectAjax();
        ajax.open("GET", Pag, true);
        ajax.onreadystatechange = function () {
            if (ajax.readyState == 4) {
                divResultado.innerHTML = ajax.responseText
            }
        }
        ajax.send(null)
    }

}
/*____________________________________________________________________*/
function update(Pag, objId, objIdVacio) {
    divEmpty = document.getElementById(objIdVacio);
    if (document.form.name.value == "") {
        divEmpty.innerHTML = "<div class='mensaje' align='justify'>Complete la informacion</div>"
    }
    else {
        divResult = document.getElementById(objId);
        id = document.form.id.value;
        name = document.form.name.value;
        ajax = objectAjax();
        ajax.open("GET", Pag + "?id=" + id + "&name=" + name, true);
        ajax.onreadystatechange = function () {
            if (ajax.readyState == 4) {
                divResultado.innerHTML = ajax.responseText
                divVacios.innerHTML = ""
            }
        }
        ajax.send(null)
    }
}

function loginUser(event){

    if (document.form.login.value == "" || document.form.pass.value == "") {
        divEmpty.innerHTML = "<div class='mensaje' align='justify'>Complete la informacion</div>"
    }
    else {

         loginName = document.form.login.value;
         pass = document.form.pass.value;
         event.preventDefault();
         window.location.replace("http://localhost:8000/menu/?login=" + loginName + "&pass=" + pass);
    }
}