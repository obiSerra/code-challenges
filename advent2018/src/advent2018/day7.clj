(ns advent2018.day7
  (:require [advent2018.utils :as utils]))

;; (def input-data (utils/file->lines "day1.txt"))

(def ex ["Step C must be finished before step A can begin."
         "Step C must be finished before step F can begin."
         "Step A must be finished before step B can begin."
         "Step A must be finished before step D can begin."
         "Step B must be finished before step E can begin."
         "Step D must be finished before step E can begin."
         "Step F must be finished before step E can begin."])

(defn str->data [s]
  (-> s
      (clojure.string/replace #"Step ([A-Z]) must be finished before step ([A-Z]) can begin\." "$1,$2")
      (clojure.string/split #",")))

(comment


  (map str->data ex)

)
