class Car {
    constructor(color, speed) {
        this.color = color;
        this.speed = speed;
    }
    turboOn(){
        console.log("The turbo is on");
    }
}
const car1 = new Car(red, 300)
car1.turboOn();
console.log(car1);
