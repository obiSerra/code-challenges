(ns codewars.strip_comments)

(defn remove-comments [comment-symbols str]
  (loop [s str
         sy comment-symbols]   
    (if (empty? sy) (clojure.string/trimr s)
        (let [f (.indexOf s (first sy))
              ns (if (> f -1) (subs s 0 f) s)]
          (recur ns (rest sy))))))

(defn strip-comments [text comment-symbols]
  (clojure.string/join "\n" (map #(remove-comments comment-symbols %)
        (clojure.string/split-lines text))))


(comment

  (strip-comments"apples, pears # and bananas\ngrapes\nbananas !apples" '("#" "!"))


  (.indexOf "foo" "o")
) 


