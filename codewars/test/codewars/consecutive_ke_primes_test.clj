(ns codewars.consecutive_k_primes_test
  (:require [clojure.test :refer :all]
            [codewars.consecutive_k_primes :refer :all]))


(defn do-test [k xs ans]
  (is (= (consec-kprimes k xs) ans)))

(deftest a-test1
  (testing "Basic Tests consec-kprimes"  
    (do-test 1 [10054, 10039, 10053, 10051, 10047, 10043, 10037, 10034] 0)
    (do-test 3 [10158, 10182, 10184, 10172, 10179, 10168, 10156, 10165, 10155, 10161, 10178, 10170] 5)
    (do-test 2 [10123, 10122, 10132, 10129, 10145, 10148, 10147, 10135, 10146, 10134] 2)
    (do-test 4 [10140, 10122, 10132, 10134, 10120, 10115, 10128] 2)
    (do-test 6 [10098] 0)))
