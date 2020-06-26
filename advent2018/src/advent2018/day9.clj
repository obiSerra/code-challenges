(ns advent2018.day9
  (:require [advent2018.utils :as utils]))

(def players 413)
(def last-marble 71082)
(def p-obj (into [] (map (fn [p] {:id p :p 0}) (range players))))

(def players-pts (atom p-obj))

(defn clockwise [list position step]
  (let [p (mod (+ position step) (count list))]
    (if (= 0 p)
      (count list)
      p)))
(defn counter-clock [list position step]
  (let [p (mod (- position step) (count list))]
    (if (= 0 p)
      (count list)
      p)))

(defn append-el [list current-pos n]
  (let [new-pos (clockwise list current-pos 2)
        parts (split-at new-pos list)]
    (concat (first parts) [n] (last parts))))

(defn remove-el [list current-pos n]
  (let [new-pos (counter-clock list current-pos 7)
        parts (split-at new-pos list)]
    (concat (first parts) (drop 1 (last parts)))))

(defn after-remove-pos [list current-pos n]
  (counter-clock list current-pos 7))

(defn add-pebble [max]
  (loop [list [0]
         current-pos 0
         n 1]
    (if (= 0 (mod n 1000)) (println n))
    (if (> n max)
      list
      (cond 
        (= 0 (mod n 23)) (do 
                           ;; (println (- (mod n players) 1))
                           (swap! players-pts #(update-in % [(mod n players)] (fn [v] (assoc v :p (+ (:p v) n (nth list (counter-clock list current-pos 7)))))))
                           (recur (remove-el list current-pos n) (after-remove-pos list current-pos n) (inc n)))
        (= n 1) (recur [0 1] 1 2)
        :else (recur (append-el list current-pos n) (clockwise list current-pos 2) (inc n))))))


(defn solve [] 
  (add-pebble last-marble)
  (println (:p (last (sort-by :p @players-pts)))))


;; 416424
