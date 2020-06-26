(ns advent2019.day4
  (:require [advent2019.utils :as utils]))

;; Url
;; https://adventofcode.com/2019/day/4

(def input (->> (clojure.string/split "256310-732736" #"-") (map utils/to-int)))

(defn length? [s]
  (= (count s) 6))

(defn incr? [s]
  (loop [rem (rest s)
         cur (first s)] 
    (cond (empty? rem) true
          (< (utils/to-int (first rem))(utils/to-int cur)) false 
          :else (recur (rest rem) (first rem)))))

(defn repeat? [s]
  (not= (count s) (count (into #{} s))))

(defn validate [validators num]
  (let [s (clojure.string/split (str num) #"")]
    ((apply every-pred validators) s)))

(defn solve [validate-fn start end]
  (loop [n start
         cnt 0]
    (if (> n end)
      cnt
      (recur (inc n) (if (validate-fn n) (inc cnt) cnt)))))

(def d4-validate (partial validate [length? incr? repeat?]))
(def d4-solve (partial solve d4-validate))

(comment 
  (println (d4-solve (first input) (last input)))
)


