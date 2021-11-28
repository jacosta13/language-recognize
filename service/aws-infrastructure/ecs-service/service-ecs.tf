
resource "aws_ecs_task_definition" "langrec_def" {
  family                   = var.project
  execution_role_arn       = aws_iam_role.task_exec.arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  container_definitions = jsonencode([
    {
      name  = "${var.project}-service-run"
      image = "${data.terraform_remote_state.ecr_data.outputs.ecr_url}:${var.img_tag}"
      portMappings = [
        {
          hostPort      = "80"
          containerPort = "80"
        }
      ]
    }
  ])
  tags = {
    Name        = "language-recognize"
    Description = "Task definition for language recognize service."
    Project     = var.project
  }
}
