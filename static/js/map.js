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

// Add middle point in routing
function addMiddlePoint() {
    var input = document.createElement('input');

    var element = document.getElementById('forms');

    element.appendChild(input)
}
