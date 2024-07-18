impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows <= 1 {
            return s;
        }

        let num_rows = num_rows as usize;

        let mut levels: Vec<String> = vec![String::new(); num_rows];
        let mut step = 1;
        let mut current_level = 0;

        for c in s.chars() {
            levels[current_level].push(c);
            current_level = (current_level as i32 + step) as usize;
            if current_level == 0 {
                step = 1;
            } else if current_level == num_rows - 1 {
                step = -1;
            }
        }

        levels.concat()
    }
}
