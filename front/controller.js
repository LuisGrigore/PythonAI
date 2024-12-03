import { updateResultText } from "./ui.js";

class Controller{
	constructor (client,view){
		this.client = client
		this.view = view
	}
	sendImage(image) {
		this.client.sendImage(image).then((result) => {
			updateResultText(result)
		}).catch((err) => {
			updateResultText(err)
		});
	}
}

export default Controller
 
