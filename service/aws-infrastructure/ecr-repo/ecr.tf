
resource "aws_ecr_repository" "language_recognize" {
  name                 = "language-recognize"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}
