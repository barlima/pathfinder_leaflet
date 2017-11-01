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
    var container = document.getElementById("extra-points");

    var text = document.createElement("SMALL");
    text.appendChild(document.createTextNode("Extra points " + id));
    text.id = "extra_points_text_" + id;
    container.appendChild(text);

    container.appendChild(document.createElement("br"));

    var input = document.createElement("input");
                input.type = "text";
                input.name = "extra_points_" + id;
                input.id = "id_extra_points_" + id;
                if (value) {
                    input.value = value;
                }

    container.appendChild(input);
    container.appendChild(document.createElement("br"));
}


function countDistances(A, B) {

    var routes = {};

    var routingControl = L.Routing.control({
        serviceUrl: 'http://127.0.0.1:5000/route/v1',
        waypoints: [
            L.latLng([selectedPoints[A][0], selectedPoints[A][1]]),
            L.latLng([selectedPoints[B][0], selectedPoints[B][1]])
        ],
        routeWhileDragging: true,
        show: false
    });

    routingControl.on('routesfound', function (e) {
        var total_route = e.routes[0];
        var total_distance = total_route.summary.totalDistance;
        var total_time = total_route.summary.totalTime;

        var value = A + "/" + B + "/" + total_distance + ":";

        // $("[id=distances]").val($("[id=distances]").val() + total_distance + ', ');
        $("[id=distance]").val($("[id=distance]").val() + value);
    });
}
