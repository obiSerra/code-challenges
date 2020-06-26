(defproject advent2019 "1.0.0-SNAPSHOT" ; version "1.0.0-SNAPSHOT"
  ;; Beyond this point you may prepend a form with unquote, or ~, to eval it.

;;; Project Metadata
  ;; The description text is searchable from repositories like Clojars.
  :description "A sample project"
  :url "http://example.org/sample-clojure-project"

  :license {:name "Eclipse Public License - v 1.0"
            :url "http://www.eclipse.org/legal/epl-v10.html"
            :distribution :repo
            :comments "same as Clojure"}
  ;; Warns users of earlier versions of Leiningen. Set this if your project
  ;; relies on features only found in newer Leiningen versions.
  :min-lein-version "2.0.0"

 
  :dependencies [[org.clojure/clojure "1.10.1"]]

;;  :aot [org.example.sample]


  :source-paths ["src"]

  :target-path "target/%s/"
)
