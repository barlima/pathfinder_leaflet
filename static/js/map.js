// Display route data on the left hand side from the map
function setTimeAndDistance(point_A, point_B, distance, time) {
    var paragraph = document.createElement('p');
    var node = document.createTextNode(
                            '(' + point_A + ', ' + point_B + ')' +
                            '\nDistance: ' + distance +
                            ', \n' + time);

    paragraph.appendChild(node);

    var element = document.getElementById('routeData');
    element.appendChild(paragraph)
}

// Add middle point in routing
function addMiddlePoint() {
    var input = document.createElement('input');

    var element = document.getElementById('forms');

    element.appendChild(input)
}
