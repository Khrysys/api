import "../css/masthead.css"

import { ImageContainer } from "./ImageContainer";

export function Masthead() {
	return <div className="masthead">
		<ImageContainer image={require("../img/Flaskinni.png")} alt={"Masthead Image"} />
	</div>;
}