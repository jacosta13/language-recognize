variable "language_recognize_bucket" {
  type        = string
  description = "Bucket where project data (i.e. models and dataset) are stored."
}

variable "project" {
  type        = string
  description = "Name of the project resources are associated to."
  default     = "language-recognize"
}
