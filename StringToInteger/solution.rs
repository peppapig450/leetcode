impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let s = s.trim_start();
        if s.is_empty() {
            return 0;
        }

        let mut chars = s.chars();
        let mut sign = 1;
        let mut result: i64 = 0;

        if let Some(first_char) = chars.next() {
            match first_char {
                '-' => sign = -1,
                '+' => sign = 1,
                '0'..='9' => result = (first_char as i64 - '0' as i64),
                _ => return 0,
            }
        }

        for c in chars {
            if let Some(digit) = c.to_digit(10) {
                result = result * 10 + digit as i64;
                if sign * result > i32::MAX as i64 {
                    return i32::MAX;
                }
                if sign * result < i32::MIN as i64 {
                    return i32::MIN;
                }
            } else {
                break;
            }
        }

        (sign * result) as i32
    }
}
