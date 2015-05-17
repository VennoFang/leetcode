package leetcode;

public class Count_and_Say {
	public String countAndSay(int n) {
        String result = "1";
        if (n ==1) return result;
        for(int i=2; i<=n; i++) {
            StringBuilder sb = new StringBuilder();
            char[] chars = result.toCharArray();
            char cur = chars[0];
            int count = 0;
            for(int j = 0; j< result.length(); j++) {
            	if(cur == chars[j]) count++;
            	else {
            		sb.append(count).append(cur);
            		cur = chars[j];
            		count = 1;
            	}
            	if(j==result.length()-1) {
            		sb.append(count).append(cur);
            	}
            }
            result = sb.toString();
        }
        return result;
    }
}
