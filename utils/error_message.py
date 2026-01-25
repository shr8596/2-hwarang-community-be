# 실패 메시지
# 400
missing_required_field = "missing_required_field"

def invalid_input(field_name: str) -> str:
    return f"invalid_{field_name}"

# 401
authentication_required = "authentication_required"
unauthorized = "unauthorized"
invalid_credentials = "invalid_credentials"

# 403
permission_denied = "permission_denied"
def permission_denied_to(action: str) -> str:
    return f"permission_denied_to_{action}"

# 404
user_not_found = "user_not_found"
def not_found(field_name: str) -> str:
    return f"{field_name}_not_found"

# 405
http_method_not_supported = "http_method_not_supported"

# 409
duplicate_email = "duplicate_email"
duplicate_nickname = "duplicate_nickname"
def is_already_in_use(field_name: str) -> str:
    return f"{field_name}_is_already_in_use"

# 413
request_body_too_large = "request_body_too_large"

# 422
def invalid_input_format(field_name: str) -> str:
    return f"invalid_{field_name}_format"

# 429
rate_limit_exceeded = "rate_limit_exceeded"

# 500
internal_server_error = "internal_server_error"