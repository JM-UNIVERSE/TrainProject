/*global kakao*/
import { useEffect } from 'react';

const Map = (props) => {
    useEffect(() => {
        var container = document.getElementById('map');
        var options = {
          center: new kakao.maps.LatLng(36.38, 127.51),
          level: 14
        };
        props.mapHandler(new kakao.maps.Map(container, options));
      }, []);

    return (
        <div id="map"></div>
    )
}
export default Map;