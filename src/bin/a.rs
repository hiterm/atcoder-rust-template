//{{{
#[allow(unused_macros)]
macro_rules! getl {
    ( $( $t:ty ),* ) => {
        {
            let mut s = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            let s = s.trim_right();
            let mut ws = s.split_whitespace();
            ($(ws.next().unwrap().parse::<$t>().unwrap()),*)
        }
    };
}

#[allow(unused_macros)]
macro_rules! getl_vec {
    ( $t:ty ) => {{
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        let s = s.trim_right();
        s.split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect::<Vec<$t>>()
    }};
}
//}}}

fn main() {}
