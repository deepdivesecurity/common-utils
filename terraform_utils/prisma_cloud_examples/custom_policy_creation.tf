resource "prismacloud_policy" "Example_Policy" {
    name            = "Example Policy"
    policy_type     = "config"
    policy_subtypes = ["run"]
    cloud_type      = "all"
    severity        = "high"
    labels          = ["example_label"]
    description     = "Example description"
    enabled         = true

    compliance_metadata = [
        {name = "Example Compliance Standard"}
    ]

    rule {
        name        = "Example_Policy"
        rule_type   = "config"
        parameters  = {
            savedSearch = true
        }
        criteria = prismacloud_saved_search.Example_Policy_Saved_Search.search_id
    }
}

resource "prismacloud_saved_search" "Example_Policy_Saved_Search" {
    name        = "Example Policy"
    description = "Terraform saved RQL search"
    search_id   = prismacloud_rql_search.Example_Policy_rql.search_id
    query       = prismacloud_rql_search.Example_Policy_rql.query
}

resource "prismacloud_rql_search" "Example_Policy_rql" {
    search_type = "config"
    query       = "config from cloud.resource where cloud.type = ..."
}