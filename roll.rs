use rand::Rng;
use std::collections::HashSet;

fn roll(sides: usize) -> usize {
    let mut rng = rand::thread_rng();
    let roll = rng.gen_range(0..sides) + 1;
    return roll;
}

fn main() {
    let sides: usize = 6;
    let mut n = 1;
    let mut rolls = HashSet::new();
    while rolls.len() < sides {
        let roll = roll(sides);
        println!("{} rolled", roll);
        if !rolls.contains(&roll) {
            rolls.insert(roll);
        }
        n += 1;
    }
    println!("{} unique rolls in {} total rolls.", rolls.len(), n);
}
