import React, {useEffect, useState} from 'react';
import axios from "axios";
import {CarModel} from "./models/CarModel";

function App() {
    const [cars, setCars] = useState<CarModel[]>([])

    useEffect(() => {
        axios.get('/api/cars')
            .then(({data}) => setCars(data.data))
    }, []);

    return (
        <div className="App">
            {cars.map(car => <div key={car.id}>
                {car.id} - {car.brand} - {car.price}$
            </div>)}
        </div>
    );
}

export default App;
