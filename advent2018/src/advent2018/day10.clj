(ns advent2018.day10
  (:require [advent2018.utils :as utils]
            [clojure.string :as s]))

(def ex [

"position=< 9,  1> velocity=< 0,  2>"
"position=< 7,  0> velocity=<-1,  0>"
"position=< 3, -2> velocity=<-1,  1>"
"position=< 6, 10> velocity=<-2, -1>"
"position=< 2, -4> velocity=< 2,  2>"
"position=<-6, 10> velocity=< 2, -2>"
"position=< 1,  8> velocity=< 1, -1>"
"position=< 1,  7> velocity=< 1,  0>"
"position=<-3, 11> velocity=< 1, -2>"
"position=< 7,  6> velocity=<-1, -1>"
"position=<-2,  3> velocity=< 1,  0>"
"position=<-4,  3> velocity=< 2,  0>"
"position=<10, -3> velocity=<-1,  1>"
"position=< 5, 11> velocity=< 1, -2>"
"position=< 4,  7> velocity=< 0, -1>"
"position=< 8, -2> velocity=< 0,  1>"
"position=<15,  0> velocity=<-2,  0>"
"position=< 1,  6> velocity=< 1,  0>"
"position=< 8,  9> velocity=< 0, -1>"
"position=< 3,  3> velocity=<-1,  1>"
"position=< 0,  5> velocity=< 0, -1>"
"position=<-2,  2> velocity=< 2,  0>"
"position=< 5, -2> velocity=< 1,  2>"
"position=< 1,  4> velocity=< 2,  1>"
"position=<-2,  7> velocity=< 2, -2>"
"position=< 3,  6> velocity=<-1, -1>"
"position=< 5,  0> velocity=< 1,  0>"
"position=<-6,  0> velocity=< 2,  0>"
"position=< 5,  9> velocity=< 1, -2>"
"position=<14,  7> velocity=<-2,  0>"
"position=<-3,  6> velocity=< 2, -1>"
])


(defn row->lst [in]
  (-> in
      (s/replace #"position=<([ \-0-9]*), ([ \-0-9]*)> velocity=<([ \-0-9]*), ([ \-0-9]*)>" "$1|$2|$3|$4")
      (s/replace #" " "")
      (s/split #"\|")))


(defn lst->obj [in]
  (cond-> {}
    (< (second in) 0) (assoc :down (second in))
    (>= (second in) 0) (assoc :up (second in))
    (< (first in) 0) (assoc :left (first in))
    (>= (first in) 0) (assoc :right (first in))))

(defn row->obj [in]
  (->> in
       row->lst
       (map read-string)
       lst->obj))


(defn run-for-sec [pts sec]
  (loop [pos pts
         rem sec]

    (if (= 0 sec)
      pos
      (recur pos (dec rem)))))

(defn get-directions [pts d]
  (remove nil? (map d pts)))


(defn norm-pt [pt l u]
  (-> pt
      (update-in [:x] (fn [v] (if (nil? (:left pt))
                               (+ l
                                  (:right pt))
                               (+ l
                                  (:left pt)
                                  -1 ))))
      (update-in [:y] (fn [v] (if (nil? (:up pt))
                               (+ u
                                  (:down pt))
                               (+ u
                                  (:up pt)
                                  -1))))))

(defn there-is-point? [x y pts]
  (some #(and (= x (:x %))
              (= y (:y %))) pts))

(defn draw-grid [pts]
  (let [u (get-directions pts :up)
        d (get-directions pts :down)
        l (get-directions pts :left)
        r (get-directions pts :right)
        mr (apply max r)
        ml (apply min l)
        mu (apply max u)
        md (apply max d)

        w (- (apply max r) (apply min l))
        h (- (apply max u) (apply min d))
        norm (map #(norm-pt % (Math/abs ml) (Math/abs md)) pts)]

    (for [y (range h)]
      (println
       (for [x (range w)]
         (if (there-is-point? x y norm)
           "#"
           "."
           ))))))


(draw-grid (map row->obj ex))
