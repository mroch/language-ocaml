// SYNTAX TEST "source.ocaml"
(* test *)
// ^ comment.block.ocaml
begin fun x -> y end
// <- keyword.control.begin-end.ocaml
//    ^^^^^^^^^^ meta.function.anonymous.ocaml
//               ^^^ !meta.function.anonymous.ocaml
//        ^ variable.parameter.ocaml
//          ^^ punctuation.separator.function-definition.ocaml
//               ^^^ keyword.control.begin-end.ocaml
