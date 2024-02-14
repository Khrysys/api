import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { AccountProvider } from "../general/AccountContext";
import { ThemeProvider } from "../general/ThemeContext";
import App from "./components/App";
import "../general/scss/main.scss";


const rootElement = document.createElement("div");
rootElement.classList.add("root");
document.body.appendChild(rootElement);

const root = createRoot(rootElement);
root.render(
	< StrictMode >
		<ThemeProvider>
			<AccountProvider>
				<App />
			</AccountProvider>
		</ThemeProvider>
	</ StrictMode >
);