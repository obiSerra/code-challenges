(ns codewars.consecutive_k_primes)

(defn prime? [n]
  (if (< n 2) true
      (loop [kn 2]
        (cond 
          (> kn (/ n 2)) true
          (= 0 (rem n kn)) false
          :else (recur (inc kn))))))


(defn next-prime [p]
  (loop [k (inc p)]
    (if (prime? k) 
      k
      (recur (inc k)))))

(defn primes 
  ([] (primes 1))
  ([n] (lazy-seq (cons n (primes (next-prime n))))))

(defn count-factors [n]
  (loop [f 2
         v n
         cnt 0]
    (cond (> f v) cnt
          (= 0 (rem v f)) (recur f (/ v f) (inc cnt))
          :else (recur (inc f) v cnt))))

(defn consec-kprimes [k xs]
  (loop [pts 0
         v nil
         sc xs]
    (if (empty? sc) pts
        (let [nv (count-factors (first sc))]
          (if (= nv k v) 
            (recur (inc pts) v (rest sc))
            (recur pts nv (rest sc)))))))

(comment
  (consec-kprimes 4 [10175, 10185, 10180, 10197])
  (fooo)
)
