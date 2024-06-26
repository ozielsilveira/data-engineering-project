provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "grupo_assinatura" {
  name     = "myresourcegroup"
  location = "Brazil South"
}

resource "azurerm_storage_account" "storage_account" {
  name                     = "datalakeengdados2"
  resource_group_name      = azurerm_resource_group.grupo_assinatura.name
  location                 = azurerm_resource_group.grupo_assinatura.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  blob_properties {
    delete_retention_policy {
      days = 7
    }
  }
}

resource "azurerm_storage_container" "landing_zone" {
  name                  = "landing-zone"
  storage_account_name  = azurerm_storage_account.storage_account.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "bronze" {
  name                  = "bronze"
  storage_account_name  = azurerm_storage_account.storage_account.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "silver" {
  name                  = "silver"
  storage_account_name  = azurerm_storage_account.storage_account.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "gold" {
  name                  = "gold"
  storage_account_name  = azurerm_storage_account.storage_account.name
  container_access_type = "private"
}

output "storage_account_name" {
  value = azurerm_storage_account.storage_account.name
}

output "storage_container_names" {
  value = [
    azurerm_storage_container.landing_zone.name,
    azurerm_storage_container.bronze.name,
    azurerm_storage_container.silver.name,
    azurerm_storage_container.gold.name
  ]
}
