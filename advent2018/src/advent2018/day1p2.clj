(ns advent2018.day1p2
  (:require [advent2018.utils :as utils]
            [advent2018.day1 :as d1]))


(def ex ["3" "3" "4" "-2" "-4"])
(def ex2 ["7" "7" "-2" "-7" "-4"])
(def ex3 ["-6" "3" "8" "5" "-6"])

(def input-data (utils/file->lines "day1.txt"))

(defn last-or-default
    ([vals] (last-or-default vals 0))
    ([vals def]
     (if (empty? vals) def (last vals)))
    )

(comment
  (def xf (map read-string))

  (defn add-val [vals from cnt]
    (conj (nthrest vals cnt)
          (+ (last-or-default vals)
             (->> from (take 1) first read-string))))

  (defn seen-frequency? [vals freq]
    (get (set vals) freq))

  (defn solve [data cnt]
    (loop [vals []
           from (utils/infinite-list data)]

      (println vals)
      (cond
        (seen-frequency? (butlast vals) (last-or-default vals)) (seen-frequency? (butlast vals) (last-or-default vals))
        :else (recur (add-val vals from cnt)
                     (next from))))))

(defn sum-list
  ([acc] acc)
  ([acc val]
   (conj acc (+ (last-or-default acc) val) )))

(comment
  (transduce xf sum-list [] ex)

  )
