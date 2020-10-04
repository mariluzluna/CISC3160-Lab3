// Add a checked symbol when clicking on an item onlist item
var check = document.querySelector('ul');
check.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('check-out');
  }
}, false);

// Create a new list item when user press Add buttin
function add_list() {
  var li = document.createElement("li");
  var input = document.getElementById("items").value;
  var t = document.createTextNode(input);
  li.appendChild(t);
  if (input === '') {
    alert("Enter an item to the list!"); 
  } else {
    document.getElementById("list").appendChild(li);
  }
  document.getElementById("items").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("X");
  span.className = "erase";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}
// Create a delete button andd add on item list
var drop = document.getElementsByTagName("LI");
var i;
for (i = 0; i < drop.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("X");
  span.className = "erase";
  span.appendChild(txt);
  drop[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("erase");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

