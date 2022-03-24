/*global kakao*/
import './App.css';
import Map from './Map'
import axios from 'axios'

const App = () => {
  const getStationData = async () => {
    try {
      return await axios.get('http://localhost:8080/station/all')
    } catch(error) {
      console.log(error)
      return null
    }
  }
  const mapHandler = async (map) => {
    var stationData = (await getStationData()).data
    stationData.forEach(data => {
      new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(data['latitude'], data['longitude'])
      })
    });
  }

  return (
    <div className="App">
      <Map mapHandler={mapHandler}/>
    </div>
  );
}

export default App;