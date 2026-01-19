# 실패 메시지
# 400
missing_required_field = "missing_required_field"

def invalid_input(field_name: str) -> str:
    return f"invalid_{field_name}"

# 401
authentication_required = "authentication_required"

# 403
def permission_denied(action: str) -> str:
    return f"permission_denied_to_{action}"

# 404
def not_found(field_name: str) -> str:
    return f"{field_name}_not_found"

# 405
http_method_not_supported = "http_method_not_supported"

# 409
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