fn main() {
    let s = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_right().to_owned()
    };

    let a: usize = s.parse().unwrap();

    let s = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_right().to_owned()
    };

    let (b, c) = {
        let mut ws = s.split_whitespace();
        let b: usize = ws.next().unwrap().parse().unwrap();
        let c: usize = ws.next().unwrap().parse().unwrap();
        (b, c)
    };

    let s = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_right().to_owned()
    };
    let v: Vec<usize> = s.split_whitespace().map(|x| x.parse().unwrap()).collect();

    println!("{} {}", a + b + c, s);
}
