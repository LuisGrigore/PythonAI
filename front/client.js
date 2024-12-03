class Client{
	async sendImage(image){
		const formData = new FormData();
        formData.append('image', image, 'canvas_image.png');
		const response = await fetch('https://example.com/upload', {
			method: 'POST',
			body: formData,
		});
		return response
	}
}
export default Client