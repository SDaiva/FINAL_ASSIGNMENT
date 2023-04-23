variable "region" {
  description = "The AWS region to create resources in"
  default     = "us-east-1"
}

variable "ami_id" {
  description = "The ID of the AMI to use for instance"
  default     = "ami-007855ac798b5175e"
}

variable "instance_type" {
  description = "The type of the instance"
  default = "t3.micro"
}

variable "key_name" {
  description = "The name of the key pair"
}

variable "public_key_path" {
  description = "The path to the public key"
}

variable "private_key_path" {
  description = "The path to the private key"
}

variable "security_group_name" {
  description = "The name of the security group"
  default = "team2_security_group"
}

variable "aws_instance_user_id" {
  description = "AWS instance user ID"
  default = "ubuntu"
}
variable "inventory_filename" {
  description = "Name of the inventory file"
  default = "inventory"
}