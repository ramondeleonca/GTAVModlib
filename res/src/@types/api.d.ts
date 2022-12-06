export interface pywebview {
    token: string;
    platform: string;
    domJSON: {
        toDOM: (obj: {}, opts: {}) => HTMLElement;
        toJSON: (node: HTMLElement, opts: {}) => {};
    };
    api: {
        [apiFunctionName: string]: (...args) => Promise<any>;
    }
}

declare global {
    interface Window {
        pywebview: pywebview;
        [customProps: string]: any;
    }
    
    interface WindowEventMap {
        "pywebviewready": Event;
    }
}