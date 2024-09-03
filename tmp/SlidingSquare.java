public class SlidingSquare {
	public static void main(String[] args) {
		double xCenter = .1;
		PennDraw.enableAnimation(30);
		while(true) {
			PennDraw.clear();
			PennDraw.filledSquare(xCenter, 0.5, 0.1);
			xCenter += 0.01;
			if (xCenter - 0.1 > 1.0) {
				xCenter = -0.1;
			}
			PennDraw.advance();
		}
	}
}
