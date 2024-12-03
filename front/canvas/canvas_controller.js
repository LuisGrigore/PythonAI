export class CanvasController{
	constructor(canvas_view){
		this.canvas_view = canvas_view
	}
	startDrawing(e) {
		this.canvas_view.startDrawing(e)
	}

	draw(e) {
		this.canvas_view.draw(e)
	}

	stopDrawing() {
		this.canvas_view.stopDrawing()
	}
	
	reset(){
		this.canvas_view.reset()
	}

	touchStart(e) {
		this.canvas_view.touchStart(e)
	}
	touchMove(e){
		this.canvas_view.touchMove(e)
	}
}