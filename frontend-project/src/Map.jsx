import { useState } from "react";

const Map = () => {
    return (
        <div id="detail-box">
            <h1>Detail Box</h1>
            <div id="MapBox">
                {/* <iframe id= "mapp" src="https://api.maptiler.com/maps/streets-v2/?key=9KdwdPFWekWh407ASZUj#1.7/14.09521/19.47883" frameborder="0"></iframe> */}
            </div>
            <br />
            <button id="rBtn">Find Route</button>
        </div>
    )
}

export default Map;