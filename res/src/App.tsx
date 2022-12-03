import React, { useEffect, useMemo, useState } from 'react';
import phrases from "./phrases.json";
import _ from "lodash"
import "./app.scss";

export default function App() {
    const launchModded = () => void 0;
    const launchVanilla = () => void 0;

    const [mods, setMods] = useState("");

    // window.pywebview.api.getMods().then(setMods);

    return (
        <>
            <div className="contaienr w-[100vw] h-[100vh] flex justify-center items-center">
                <div className="top-0 left-0 background w-full h-full absolute z-[-100] bg-cover bg-center brightness-90 saturate-[.75]" style={{backgroundImage: "url(/bg.png)"}}></div>
                
                <div className="left w-1/4 h-full backdrop-blur-md backdrop-brightness-50 border-r border-[#FFFFFF40]">
                    {
                        mods.length < 1 ? 
                        <div className='w-full h-full grid place-items-center px-4'>
                            <h1 className='text-2xl text-center'>{_.sample(phrases)}</h1>
                        </div> :
                        <>
                            
                        </>
                    }
                    <div className='absolute bottom-0 left-0 right-0 h-[1/8] w-full py-3 bg-black'>
                        {
                            mods.length < 1 ? 
                            <p className='w-full px-3' >Head over to <a href='#' onClick={() => window.pywebview.api.open("https://www.gta5-mods.com/")}>gta5-mods.com</a> to download some mods and install them below {/**  or open <a href='#' onClick={() => window.pywebview.api.openOpenIV()}>OpenIV</a> to install them */}</p> : null
                        }
                    </div>
                </div>

                <div className="right w-3/4 h-full relative">
                    <div className="buttons absolute left-0 right-0 bottom-6 flex items-center justify-evenly">
                        <button className='launch-button' onClick={launchModded} >Launch Modded</button>
                        <button className='launch-button' onClick={launchVanilla} >Launch Vanilla</button>
                    </div>
                </div>
            </div>
        </>
    )
};