output "app_name" {
  description = "Application name"
  value       = var.app_name
}

output "environment" {
  description = "Current environment"
  value       = var.environment
}

output "api_image" {
  description = "API Docker image"
  value       = "${var.docker_username}/taskmaster-api:latest"
}

output "frontend_image" {
  description = "Frontend Docker image"
  value       = "${var.docker_username}/taskmaster-frontend:latest"
}
