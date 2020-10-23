(ns codewars.strip_comments_test
  (:require [clojure.test :refer :all]
            [codewars.consecutive_k_primes :refer :all]
            [codewars.strip_comments :refer :all]
            ))

(deftest strip-comments-tests
  (are [text symbols expected] (= (strip-comments text symbols) expected)
    "apples, pears # and bananas\ngrapes\nbananas !apples"
    '("#" "!")
    "apples, pears\ngrapes\nbananas"
    
    "a #b\nc\nd $e f g"
    '("#" "$")
    "a\nc\nd"))
