(ns advent2018.utils
  (:require [clojure.string :as string]))


(defn read-input [filename]
  (slurp (clojure.java.io/resource (str "input/" filename))))


(defn file->lines [filename]
  (-> filename
      read-input
      string/split-lines))



(defn counter [vals]
  (let [tick (atom -1)]
    #(do
       (swap! tick inc)
       (nth vals (mod @tick (count vals))))))


(defn infinite-list [vals]
  (repeatedly (counter vals)))

(comment
  (take 5 (repeatedly #(identity )))
  (take 5 (infinite-list))
  (take 20 (infinite-list ["1" "2" "3"])))
