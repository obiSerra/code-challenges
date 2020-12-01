(ns codewars.evaluate_math_exp_test
  (:require [clojure.test :refer :all]
            [codewars.evaluate_math_exp :refer :all]))


            
(deftest test-addition
  (is (= (calc "1+1") 2.0)))
  
(deftest test-subtraction
  (is (= (calc "3-1") 2.0)))
  
(deftest test-multiplication
  (is (= (calc "2*2") 4.0)))
  
(deftest test-division
  (is (= (calc "5/2") 2.5)))
  
(deftest test-negative
  (is (= (calc "1-2") -1.0)))
  
(deftest test-literal
  (is (= (calc "2") 2.0)))
  
(deftest test-expression
  (is (= (calc "2 /2+3 * 4.75- -6") 21.25)))
  
(deftest test-simple
  (is (= (calc "12 *123") 1476.0)))
  
(deftest test-complex
  (is (= (calc "2 / (2 + 3) * 4.33 - -6") 7.732)))
