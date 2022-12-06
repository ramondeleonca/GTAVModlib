import { useState } from 'react';
import _ from "lodash"
import "./app.scss";
// import phrases from "./phrases.json";


export default function App() {
    const launchModded = () => window.pywebview.api.launch("modded", true);
    const launchVanilla = () => window.pywebview.api.launch("vanilla", true);
    
    const [bg, setBg] = useState("");

    window.addEventListener("pywebviewready", () => {
        window.pywebview.api.listDir("./../public/bg").then(bgs => setBg(_.sample(bgs)));
    });

    return (
        <>
            <div className='container w-[100vw] h-[100vh]'>

                <div className={`screen home w-full h-full flex justify-center items-center fixed`}>
                    <div className="top-0 left-0 background w-full h-full absolute z-[-100] bg-cover bg-center brightness-90 saturate-[.75]" style={{backgroundImage: `url(/bg/${bg})`}}></div>

                    {/* Will be used in the future */}
                    {/* <div className="left w-1/4 h-full backdrop-blur-md backdrop-brightness-50 border-r border-[#FFFFFF40]">
                        <div className='absolute bottom-0 left-0 right-0 h-fit w-full py-3 bg-black'>
                            {
                                mods.length < 1 ? 
                                <p className='w-full px-3 mb-2' >Head over to <a href='#' onClick={() => window.pywebview.api.open("https://www.gta5-mods.com/")}>gta5-mods.com</a> to download some mods and install them below</p> : null
                            }
                            <div className="buttons z-10 relative flex items-center justify-evenly">
                                <button className='themed-button text-xs font-normal w-[45%] h-8' onClick={installMod}>Install mod</button>
                                <button className='themed-button text-xs font-normal w-[45%] h-8' onClick={importFiles}>Import files</button>
                            </div>
                        </div>
                    </div> */}

                    <div className="right w-full h-full relative">
                        <img src="/logo.png" alt="" className='w-36 left-4 absolute aspect-square pointer-events-none z-10' />
                        <div className="buttons absolute left-0 right-0 bottom-8 flex items-center justify-evenly">
                            <div className="modded-container relative w-fit">
                                <button className='themed-button w-60 h-16' onClick={launchModded} >Launch Modded</button>
                            </div>
                            <div className="vanilla-container relative w-fit">
                                <button className='themed-button w-60 h-16' onClick={launchVanilla} >Launch Vanilla</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
};