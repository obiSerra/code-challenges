(ns advent2018.day4
  (:require [advent2018.utils :as utils]
            [clj-time.format :as f]
            [clj-time.core :as t]
            [clj-time.coerce :as tc]))

;; Solved

(def ex (shuffle ["[1518-11-01 00:00] Guard #10 begins shift"
                  "[1518-11-01 00:05] falls asleep"
                  "[1518-11-01 00:25] wakes up"
                  "[1518-11-01 00:30] falls asleep"
                  "[1518-11-01 00:55] wakes up"
                  "[1518-11-01 23:58] Guard #99 begins shift"
                  "[1518-11-02 00:40] falls asleep"
                  "[1518-11-02 00:50] wakes up"
                  "[1518-11-03 00:05] Guard #10 begins shift"
                  "[1518-11-03 00:24] falls asleep"
                  "[1518-11-03 00:29] wakes up"
                  "[1518-11-04 00:02] Guard #99 begins shift"
                  "[1518-11-04 00:36] falls asleep"
                  "[1518-11-04 00:46] wakes up"
                  "[1518-11-05 00:03] Guard #99 begins shift"
                  "[1518-11-05 00:45] falls asleep"
                  "[1518-11-05 00:55] wakes up"]))
(def formatter (f/formatter "yyyy MM dd HH mm"))

(defn parse-entry [entry]
  (let [str-parsed (-> entry
                       (clojure.string/replace #"\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\]" "$1 $2 $3 $4 $5|")
                       (clojure.string/split #"\|"))]
    [(tc/to-long (f/parse formatter (first str-parsed)))
     (last str-parsed)]
    )
  )

(defn current-id [entry current]
  (keyword (clojure.string/replace (or (re-find #"#[0-9]*" (last entry))
                                       (name current))
                                   #"#" "")))

(defn calc-hs [time-sl time-wk]

  (for [x (range (Math/abs (/ (- time-sl time-wk) (* 1000 60))))]
    (t/minute (tc/from-long (+ time-sl (* x 60 1000))))))


(defn get-diff [current-row last-row]
  (let [ac (last current-row)]
    (if (= " wakes up" ac) [(calc-hs (first last-row) (first current-row))] [])))

(defn calc-sleep [actions]
  (loop [to-check actions
         sleep {}
         current nil
         last nil]

    (if (empty? to-check)
      sleep
      (let [c (current-id (first to-check) current)
            h (get-diff (first to-check) last)]
        (recur (rest to-check)
               (if (get sleep c) (update-in sleep [c] #(flatten (concat h %))) (assoc sleep c h))
               c
               (first to-check)))
      )))

(defn maintain-max
  ([] nil)
  ([r1 r2]
                    (if (< (-> r1 last)
                           (-> r2 last))
                      r2 r1)))

(defn maintain-max-deep [r1 r2]
  (if (< (-> r1 last last)
         (-> r2 last last))
    r2 r1))

(def sorted-entries (->> "day4.txt"
                         utils/file->lines
                         (map parse-entry)
                         (sort-by #(first %))))

(comment (def sorted-entries (->> ex
                          (map parse-entry)
                          (sort-by #(first %)))))



(def sleep (calc-sleep sorted-entries))

(def winner (reduce maintain-max-deep (filter #(last %) (map
                                                         #(identity [(first %) (reduce maintain-max (into [] (frequencies (last %))))])
                                                         (into [] sleep)))))

(println (* (read-string (name (first winner)))
    (first (last winner))))
