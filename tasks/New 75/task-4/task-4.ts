function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let length = flowerbed.length;
    let i = 0;

    while (i < length && n > 0) {
        if (flowerbed[i] === 0 && (i === 0 || flowerbed[i - 1] === 0) && (i === length - 1 || flowerbed[i + 1] === 0)) {
            flowerbed[i] = 1;
            n -= 1;
            i += 2;
        } else {
            i += 1;
        }
    }

    return n === 0;
};

console.log(canPlaceFlowers([1, 0, 0, 0, 1], 1));
