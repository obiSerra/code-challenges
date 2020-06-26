(ns advent2018.day5
  (:require [advent2018.utils :as utils]
            [clojure.string :as string]))

;; (def input-data (utils/file->lines "day1.txt"))

(def input "dabAcCaCBAcCcaDA")

(defn red-poly
  ([acc v] (if (and
                (and (last acc) v)
                (not (= v (last acc)))
                (= (string/lower-case v)
                       (string/lower-case (last acc))))
             (butlast acc)
             (flatten (conj [acc] v)))))

(defn react [poly]
  (apply str (reduce red-poly (string/split poly #""))))

(defn simplify [poly]
  (loop [i poly]
    (let [n-poly (react i)]
      (if (= (count n-poly) (count i))
          n-poly
          (recur n-poly)))))



(comment (count (react input)))

(println (count (react (utils/read-input "day5.txt"))))
