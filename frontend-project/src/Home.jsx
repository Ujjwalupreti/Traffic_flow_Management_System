import { useState } from 'react'
const Home = ()=>{
    return(
    <div id="home" className="mt-3">
        <h1>Home</h1>
        <div>
            <p>
            Kachi Dham Traffic Congestion Management System is an intelligent, software-driven solution developed to address the persistent issue of traffic congestion in the Kachi Dham area. This system is designed to assist both travelers and local authorities by providing real-time, dynamic route planning based on current and historical traffic patterns. When a user enters their destination and intended travel date, the system analyzes live traffic data from map APIs and compares it with previously recorded data from similar time periods, such as weekends or festivals. By detecting potential congestion ahead of time, it suggests alternate routes and optimal entry schedules to ensure smoother traffic flow and reduced delays. Unlike traditional systems, our platform requires no external hardware or infrastructure upgrades—it operates entirely through intelligent software algorithms and user input. With an easy-to-use interface and an interactive map, the system not only helps visitors plan their trips efficiently but also empowers authorities with insights and tools to manage traffic more effectively. Whether it's a regular day or a peak event, this system ensures a smarter, safer, and more organized travel experience in Kachi Dham.
            </p>
        </div>
    </div>
    )
}

export default Home;