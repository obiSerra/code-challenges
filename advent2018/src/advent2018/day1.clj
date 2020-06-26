(ns advent2018.day1
  (:require [advent2018.utils :as utils]))

(def input-data (utils/file->lines "day1.txt"))

(def xf (map read-string))

(defn solve [data]
  (transduce xf + 0 data))

(comment 
  (solve input-data))

