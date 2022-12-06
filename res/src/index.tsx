import ReactDOM from 'react-dom/client';
import "./global.scss";
import App from "./App";
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Launch from './Launch';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);

function Index() {
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path='/' element={<App></App>}></Route>
                    <Route path='/launch' element={<Launch></Launch>}></Route>
                </Routes>
            </BrowserRouter>
        </>
    )
};

root.render(<Index></Index>);