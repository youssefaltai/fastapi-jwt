# FastAPI + JWT

A minimal starter FastAPI project with JWT authentication
set up and ready.

## How to use

As you can see in ```example.py```,
the endpoint ```create_token(username)```
uses the method ```sign_jwt(data)```
to generate a JWT token from a payload.

```
@router.post("/")
async def create_token(username: str):
    return sign_jwt({"username": username})
```

The endpoint ```get_secret()```
is an example of a protected endpoints
that requires JWT token authorization.
The way you create protected endpoints is by
adding ```Depends(JWTBearer())``` to the endpoint's
```dependencies```  list.

```
@router.get("/", dependencies=[Depends(JWTBearer())])
async def get_secret():
    return {"secret": "im potato"}
```

Now, the only thing left is the JWT token verification,
which you can easily fully customize by modifying the
method ```verify_jwt(jwt_token)``` in ```auth/verify.py```

```
from auth.auth_handler import decode_jwt


def verify_jwt(jwt_token: str) -> bool:
    # data: The previously encoded payload
    data = decode_jwt(jwt_token)

    # Put token verification logic here
    ...
```

Also, do not forget to include these environment variables
in a ```.env``` in your project:

#### ```JWT_SECRET```

A string that you should NOT expose in public, used in
creating the JWT from the payload.

#### ```JWT_ALGORITHM```

The name of the algorithm to be used
in creating the JWT token.

[See all possible values for ```JWT_ALGORITHM```](https://pyjwt.readthedocs.io/en/latest/algorithms.html?highlight=algorithm#digital-signature-algorithms)

#### ```JWT_EXPIRES```

An integer number of seconds that the JWT expires after
from the time of its creation.
