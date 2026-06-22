variable "namespace" {}
variable "app_name" {}
variable "replicas" {}
variable "docker_username" {}

output "deployment_info" {
  value = {
    namespace       = var.namespace
    app_name        = var.app_name
    replicas        = var.replicas
    docker_username = var.docker_username
  }
}
