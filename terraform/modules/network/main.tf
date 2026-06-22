variable "app_name" {}
variable "environment" {}

output "network_info" {
  value = {
    app_name    = var.app_name
    environment = var.environment
    cidr        = "10.244.0.0/16"
  }
}
