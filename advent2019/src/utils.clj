(ns advent2019.utils)

(defn read-input-file [filename]
  (slurp (str "input/" filename)))

(def read-input (comp clojure.string/split-lines read-input-file))

(defn to-int [s]
  (Integer. s))

