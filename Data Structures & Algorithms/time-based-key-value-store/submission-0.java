class TimeMap {
    class TimeVal{
        String val;
        int time;
        public TimeVal(String val, int time){
            this.val = val;
            this.time = time;
        }
    }

    HashMap <String, List<TimeVal>> map;

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if(!map.containsKey(key)){
            map.put(key, new ArrayList<>());
        }
        map.get(key).add(new TimeVal(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        List<TimeVal> list = map.get(key);
        if(list==null){
            return "";
        }
        int left = 0;
        int right = list.size() - 1;
        int target = timestamp;
        String res = "";
        
        while(left<=right){
            int mid = left + (right-left)/2;
            TimeVal midVal = list.get(mid);
            if(midVal.time == target){
                return midVal.val;
            }
            if (midVal.time < target) {
                res = midVal.val;
                left = mid + 1;
            }
            else {
                right = mid - 1;
            } 
        }
    return res;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */