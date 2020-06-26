(ns advent2018.day11
  (:require [advent2018.utils :as utils]))

;; RackID = x + 10
;;

(def serial 18)

(defn get-power [cell]
  (let [rack-ID (+ 10 (first cell))]

    (println (-> rack-ID
         (* (last cell))
         (+ serial)
         (* rack-ID)
         (mod 10)
         ))


    (-> rack-ID
        (* (last cell))
        (+ serial)
        (* rack-ID)
        (mod 10)
        (- 5))))

(defn get-power-mask [cell]
  (for [x (range 3)
        y (range 3)]

    {:cell [(+ (first cell) x) (+ (last cell) y)]
     :power (get-power [(+ (first cell) x) (+ (last cell) y)])}

))

;;

;;; (get-power-mask [33 45])

(get-power [33 47])
