(ns advent2019.day9
  (:require [advent2019.utils :as utils]
            [advent2019.day5 :as d5]
            [advent2019.day5gold :as d5gold]
            [advent2019.intcodeParser :as parser]))

;; Url
;; https://adventofcode.com/2019/day/9


(def input "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")
;;(def input "104,1125899906842624,99")

;;(def input "1102,34915192,34915192,7,4,7,99,0")

(def input-data (into [] (map #(bigint %) (clojure.string/split input #","))))

(defn parse-operation [prog pos]
  (let [full (map utils/to-int (clojure.string/split (format "%05d" (int (nth prog pos))) #""))
        v (utils/to-int (apply str (drop 3 full)))]
    [(nth full 2) (second full) (first full) v]))

(defn mode-select [program pos rel-pos mode]
  (println mode)
  (cond (= 0 mode) (parser/get-val program pos)
        (= 1 mode) (parser/get-cell program pos)
        (= 2 mode) (do
                     (println ["relative pos" pos rel-pos (parser/get-cell program (+ rel-pos (parser/get-cell program pos)))] )
                     (parser/get-cell program (+ rel-pos (parser/get-cell program pos))) )))

(defn do-operation [op-fn program pos rel-pos modes]
  (let [m-sel (partial mode-select program)
        p1 (m-sel (+ 1 pos) (+ 1 rel-pos) (nth modes 0))
        p2 (m-sel (+ 2 pos) (+ 1 rel-pos) (nth modes 1))
        p3 (parser/get-cell program (+ 3 pos))]
    (update-in program [p3] (fn [_] (op-fn p1 p2)))))

(def sum-op (partial do-operation +))
(def mult-op (partial do-operation *))

(defn input-op [program pos value]
  (assoc-in program [(parser/get-cell program (+ 1 pos))] value))

(defn output-op [mode program pos rel-pos]
  (mode-select program (+ 1 pos) rel-pos mode))

(defn jump-if [pred program pos rel-pos modes]
  (if (pred 0 (mode-select program (+ 1 pos) rel-pos (first modes)))
    (mode-select program (+ 2 pos) rel-pos (second modes))
    (+ 3 pos)))

(def jump-if-true (partial jump-if not=))
(def jump-if-false (partial jump-if =))

(defn compare-op [pred program pos rel-pos modes]
  (let [sel (partial mode-select program)
        p1 (sel (+ 1 pos) rel-pos (first modes))
        p2 (sel (+ 2 pos) rel-pos (second modes))
        p3 (parser/get-cell program (+ 3 pos))
        v (if (pred p1 p2) 1 0)]
    (assoc-in program [p3] v)))

(def less-than (partial compare-op <))
(def equals-op (partial compare-op =))


;;Opcode 9 adjusts the relative base by the value of its only parameter.
;; The relative base increases (or decreases, if the value is negative) by the value of the parameter.

(defn adjust-rel-pos [program pos rel-pos modes]
  (let [p1 (mode-select program (+ 1 pos) rel-pos (first modes))]
    (+ p1 rel-pos)))

(defn run-program [program & inputs]
  (loop [prg program
         pos 0
         rel-pos 0
         out nil
         in inputs]
    (let [[m1 m2 m3 op] (parse-operation prg pos)
          modes [m1 m2 m3]]
      (println ["Op" op])
      (cond (= 1 op) (recur (sum-op prg pos rel-pos modes) (+ 4 pos) rel-pos out in)
            (= 2 op) (recur (mult-op prg pos rel-pos modes) (+ 4 pos) rel-pos out in)
            (= 3 op) (recur (input-op prg pos (first in)) (+ 2 pos) rel-pos out (rest in))
            (= 4 op) (recur prg (+ pos 2) rel-pos (output-op m1 prg pos rel-pos) in)
            (= 5 op) (recur prg (jump-if-true prg pos rel-pos modes) rel-pos out in)
            (= 6 op) (recur prg (jump-if-false rel-pos prg pos modes) rel-pos out in)
            (= 7 op) (recur (less-than prg pos rel-pos modes) (+ pos 4) rel-pos out in)
            (= 8 op) (recur (equals-op prg pos rel-pos modes) (+ pos 4) rel-pos out in)
            (= 9 op) (recur prg (+ 2 pos) (adjust-rel-pos prg pos rel-pos modes) out in)
            (= 99 op) out
            :else ["error" op]))))


(comment

  )

(println  (run-program input-data))
