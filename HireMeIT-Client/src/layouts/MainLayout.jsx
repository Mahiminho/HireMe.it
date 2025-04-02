import { Outlet } from "react-router-dom"
import Navbar from "../components/Navbar"
import 'react-toastify/ReactToastify.min.css'
import { ToastContainer } from "react-toastify"

const MainLayout = () => {
    return (
        <>
            <Navbar />
            <Outlet />
            <ToastContainer />
        </>
    )
}

export default MainLayout