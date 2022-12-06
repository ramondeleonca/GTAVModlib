import { useState } from "react";
import "./launch.scss";

export default function Launch() {
    const [progressText, setProgressText] = useState("Initializing Launch...");
    const [progress, setProgress] = useState(0);

    window["setProgressText"] = setProgressText;
    window["setProgress"] = setProgress;

    return (
        <>
            <div className="container pywebview-drag-region w-full h-full fixed bg-black flex justify-center items-center flex-col">
                <img className="w-2/5 aspect-square pointer-events-none" src="/logo.png" alt="" />

                <h1 className="text-xl font-semibold">{progressText}</h1>

                <div className="progress-container flex items-center justify-center w-full mt-2">
                    <div className="bar w-3/5 relative h-2 rounded-full overflow-hidden bg-gray-700 mx-2">
                        <div className="fill bg-[#fcaf17] h-full absolute top-0 left-0" style={{
                            width: `${progress * 100}%`
                        }}></div>
                    </div>
                    <h2>{progress * 100}%</h2>
                </div>
            </div>
        </>
    )
}