(ns advent2020.utils
  (:require [clojure.string :as string]))


(defn get-input 
  ([day] (get-input day false))
  ([day test?]
   (-> (str "resources/input/day" day (if test? "-test" "") ".txt")
       slurp
       (string/split-lines))))

(defn get-input-int [day]
  (->> day
       get-input       
       (map #(Integer/parseInt %))))


(comment
  (get-input 1)
  )
