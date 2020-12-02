(ns advent2020.day2
 (:require [advent2020.utils :as utils]))

(def test-input ["1-3 a: abcde" "1-3 b: cdefg" "2-9 c: ccccccccc"])

(defn match-line [line] (->> line
                             (re-matches #"(\d*)-(\d*) ([a-z]*): ([a-z]*)")
                             rest
                             (into [])))

(defn valid? [line-seq]
  (let [occ ((frequencies (last line-seq)) (.charAt (last (butlast line-seq)) 0)) ]
    (and (not (nil? occ))
         (>= occ (Integer/parseInt (first line-seq)))
         (<= occ (Integer/parseInt (first (rest line-seq)))))))


(defn solve [input]
    (->> input
       (map match-line)
       (filter valid?)
       count))


(defn get-chars [line-seq]
  (let [fc (dec (Integer/parseInt (first line-seq)))
        sc (dec (Integer/parseInt (first (rest line-seq))))
        ch (.charAt (last (butlast line-seq)) 0)]
    (bit-xor (if (= (get (last line-seq) fc) ch) 1 0) 
             (if (= (get (last line-seq) sc) ch) 1 0))))

(defn solve-gold [input]
    (->> input
       (map (comp get-chars match-line))
       (filter #(= 1 %))
       count))

(comment 
  (solve (utils/get-input 2))

  (solve-gold (utils/get-input 2))

)





