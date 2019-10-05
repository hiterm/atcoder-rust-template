use std::io::Write;

#[allow(unused)]
macro_rules! debug {
    ($($format:tt)*) => (write!(std::io::stderr(), $($format)*).unwrap());
}
#[allow(unused)]
macro_rules! debugln {
    ($($format:tt)*) => (writeln!(std::io::stderr(), $($format)*).unwrap());
}

fn main() {
    // 1つの数字
    let s = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_right().to_owned()
    };
    let a: usize = s.parse().unwrap();

    // 複数数字
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

    // 1行ベクトル
    let s = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_right().to_owned()
    };
    let v: Vec<usize> = s.split_whitespace().map(|x| x.parse().unwrap()).collect();

    // 複数行ベクトル
    let mut v: Vec<i64> = Vec::new();
    for _ in 0..a {
        let s = {
            let mut s = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            s.trim_right().to_owned()
        };
        let v_i: i64 = s.parse().unwrap();
        v.push(v_i)
    }
}
