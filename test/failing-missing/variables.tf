variable "good_variable_with_description" {
  type        = string
  default     = "foo"
  description = "Some description which makes sense"
}


variable "bad_variable_without_description" {
  type    = string
  default = "bar"
  # description = "No description set here"
}
