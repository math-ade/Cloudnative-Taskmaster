terraform {
  required_version = ">= 1.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}

# Local provider - no cloud costs!
provider "local" {}

# Create project directories
resource "local_file" "dev_config" {
  content  = jsonencode({
    environment = "development"
    namespace   = "taskmaster-dev"
    replicas    = 2
    images = {
      api      = "mathade/taskmaster-api:latest"
      frontend = "mathade/taskmaster-frontend:latest"
      worker   = "mathade/taskmaster-worker:latest"
    }
  })
  filename = "${path.module}/environments/dev/config.json"
}

resource "local_file" "prod_config" {
  content  = jsonencode({
    environment = "production"
    namespace   = "taskmaster-prod"
    replicas    = 3
    images = {
      api      = "mathade/taskmaster-api:latest"
      frontend = "mathade/taskmaster-frontend:latest"
      worker   = "mathade/taskmaster-worker:latest"
    }
  })
  filename = "${path.module}/environments/prod/config.json"
}
