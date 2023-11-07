# Localstack Server Side

Here's how to set up S3 buckets locally using Localstack.

For information on the dvc client, view the `main` branch for an example project.

## Quick Start 

To run localstack with our configuration above run the following.  Continue reading for more information.

```bash
localstack --profile=network start -d
```

## Installing Dependencies

This following dependencies are required by Localstack:
- Python 3.7 or later
- Pip
- Docker

With these installed, localstack can be installed by running:

```bash
python3 -m pip install --upgrade localstack
```

Verify localstack is installed correctly with:

```bash
localstack --version
```

Finally start localstack with:

```bash
locakstack start -d
```

By default localstack uses port 4566 as its endpoint.  To ensure this is accessible run:

```bash
curl http://localhost:4566
```

## Adding Remote Access

Under its default configuration, localstack only allows connections from localhost.  It, however, can be easily configured to allow remote connections.

To view the current configuration run:

```bash
localstack config show
```

For remote access we need to modify the `GATEWAY_LISTEN` option.  By default it is set to `127.0.0.1:4566`.  This only allows connections from localhost and should be changed to `0.0.0.0:4566`.

To change this we'll add a profile.  This should be a `.env` file within the `~/.localstack` config directory.  Add `GATEWAY_LISTEN=0.0.0.0:4566` to `~/.localstack/network.env` as seen above.  

Finally we can stop and restart localstack with the appropirate profile:

```bash
localstack stop
localstack --profile=network start -d
```

To ensure remote access run the following command from another machine with the corresponding IP address:

```bash
curl http://44.*****:4566/health
```

For more information, please refer to [this article](https://medium.com/@esarat/installing-and-setting-up-localstack-on-a-remote-computer-a848e44b2838).
