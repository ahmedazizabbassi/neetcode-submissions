class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.toLocaleLowerCase();
        let p = "";
        let r = "";
        for (let i = s.length; i >= 0; --i) {
            if (s[i] >= 'a' && s[i] <= 'z' || s[i] >= '0' && s[i] <= '9') {
                 p += s[i];
                r = s[i] + r;
            }
        }
        return p === r;
    }
}
