import {useState} from 'react'
const Dashboard = () =>{

    return (
        <div id="dash-board" >
            <h1>Dash-board</h1>
            <form className='m-3'>
                <label id="lbl">Vehicle Id:</label>
                <input type="text" placeholder='vehicle Id'/>
            </form>
            <form className='m-3'>
                <label id="lbl" >Date:</label>
                <input type="date" placeholder='date'/>
            </form>
            <form className='m-3' >
                <label id="lbl" >Destination:</label>
                <input type="text" placeholder='destination'/>
            </form>
            <form className='m-3' >
                <label  id="lbl">VehicleType:</label>
                <input type="text" placeholder='vehicletype eg. 2 wheeler, 4 wheeler '/>
            </form>
            <button className='pmrBtn'>Plan My Route</button>
        </div>
    )
}

export default Dashboard;