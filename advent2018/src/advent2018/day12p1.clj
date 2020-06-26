(ns advent2018.day12p1
  (:require [advent2018.utils :as utils]
            [clojure.string :as s]))

(def initial-state-ex "#..#.#..##......###...###")

(def initial-state "..##.#######...##.###...#..#.#.#..#.##.#.##....####..........#..#.######..####.#.#..###.##..##..#..#")

(def ex-notes ["...## => #"
               "..#.. => #"
               ".#... => #"
               ".#.#. => #"
               ".#.## => #"
               ".##.. => #"
               ".#### => #"
               "#.#.# => #"
               "#.### => #"
               "##.#. => #"
               "##.## => #"
               "###.. => #"
               "###.# => #"
               "####. => #"])


(def notes [
"#..#. => ."
"..#.. => ."
"..#.# => #"
"##.#. => ."
".#... => #"
"#.... => ."
"##### => #"
".#.## => ."
"#.#.. => ."
"#.### => #"
".##.. => #"
"##... => ."
"#...# => #"
"####. => #"
"#.#.# => ."
"#..## => ."
".#### => ."
"...## => ."
"..### => #"
".#..# => ."
"##..# => #"
".#.#. => ."
"..##. => ."
"###.. => ."
"###.# => #"
"#.##. => #"
"..... => ."
".##.# => #"
"....# => ."
"##.## => #"
"...#. => #"
".###. => ."])


(def current-left (atom 0))

(defn parse-notes [n]
  (map #(conj (s/split %1 #" => ") %2) n (range)))


(defn change-plant [piece rule]
  (if (= piece (first rule)) (second rule) false))

(defn sub-part [gen i]
  (str
   (nth gen (- i 2) ".")
   (nth gen (- i 1) ".")
   (nth gen i)
   (nth gen (+ i 1) ".")
   (nth gen (+ i 2) ".")))



(defn new-gen [gen rules]
  (let [ng (for [x (range (count gen))]
              (or
               (some #(change-plant (sub-part gen x) %) rules)
               "."))
        lng (cond (= "#"(first ng)) (do
                                      (swap! current-left #(- % 2))
                                      (concat ["." "."] ng))
                  (= "#"(second ng)) (do
                                       (swap! current-left #(- % 1))
                                       (concat ["."] ng))
                  :else ng)

        lngr (cond (= "#"(last lng)) (concat lng ["." "."])
                  (= "#" (butlast (last ng))) (concat lng [ "."])
                  :else lng)]
    lngr))


(defn grow [gen rules max-g]
  (loop [g gen
         n 0]

    (if (= n max-g)
      g
      (recur (new-gen g rules) (inc n)))))

(defn count-plants [gen]
  (count (filter #(= "#" %) gen)))

(let [res (grow (s/split initial-state #"") (parse-notes notes) 20)]
  (apply + (map first
                (filter
                 #(= (last %) "#")
                 (map
                  #(identity [%2 %1])
                  res
                  (range @current-left (count res)))))))
