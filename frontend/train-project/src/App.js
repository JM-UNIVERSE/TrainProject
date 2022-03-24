/*global kakao*/
import './App.css';
import Map from './Map'

const App = () => {
  const mapHandler = (map) => {
    var geocoder = new kakao.maps.services.Geocoder();
    geocoder.addressSearch('')
  }

  return (
    <div className="App">
      <Map mapHandler={mapHandler}/>
    </div>
  );
}

export default App;