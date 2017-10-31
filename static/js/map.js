// Display route data on the left hand side from the map
function getTimeAndDistance(distance, time) {
    var paragraph = document.createElement('p');
    var node = document.createTextNode('Distance: ' + distance + 'm in ' +
                                        parseInt(time/3600) + ':' +
                                        parseInt(time/60%60) + ',' +
                                        parseInt(time%60));

    paragraph.appendChild(node);

    var element = document.getElementById('routeData');
    element.appendChild(paragraph)
}

// Add middle point by clicking on button
function addMiddlePoint(id, value) {
    var container = document.getElementById("points-form");
                container.appendChild(document.createTextNode("Extra points " + id));
                container.appendChild(document.createElement("br"));

    var input = document.createElement("input");
                input.type = "text";
                input.name = "extra_points_" + id;
                input.id = "id_extra_points_" + id;
                input.value = value;

    container.appendChild(input);
    container.appendChild(document.createElement("br"));
}

function countDistances(json) {
    debugger;
}
