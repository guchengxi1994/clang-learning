fn main() {

  let mut a = String::from("aaaaaaaaaaaaaaa");
  let mut c = &mut a;

  c = String::from("ss");
  println!("{}",c)
  
}