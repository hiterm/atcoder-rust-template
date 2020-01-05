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
    let a: usize = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        let s = s.trim_right().to_owned();
        s.parse().unwrap()
    };

    // 複数数字
    let (a, b): (usize, usize) = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        let s = s.trim_right().to_owned();
        let mut ws = s.split_whitespace();
        let a = ws.next().unwrap().parse().unwrap();
        let b = ws.next().unwrap().parse().unwrap();
        (a, b)
    };

    // 1行ベクトル
    let v: Vec<usize> = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        let s = s.trim_right().to_owned();
        s.split_whitespace().map(|x| x.parse().unwrap()).collect()
    };

    // 複数行ベクトル
    let v: Vec<usize> = {
        let mut v: Vec<usize> = Vec::new();
        for _ in 0..a {
            let v_i = {
                let mut s = String::new();
                std::io::stdin().read_line(&mut s).unwrap();
                let s = s.trim_right().to_owned();
                s.parse().unwrap()
            };
            v.push(v_i)
        }
        v
    };
}
