# Phishing_Stuffer
The program is designed to inflate a phishing page's logs and captured credentials.

- Reasons:
Prevent validation of possible captured credentials
Inflate the number of captured credentials, buying time for IRT to mitigate and disable affected credentials.
Allows fast and slow credential sending with realistic logins based on current corporate formats.
Allows IRT to identify Threat Actors IP and User-agent for further mitigation and investigation via Microsoft logs (requires manual input of a real account)

- Support:
Chrome Version Impersonation? - Yes

Proxy Support? - Yes

Custom Corporate Email Format Support? - Yes

Cloudflare Support? - Yes

Cloudflare Turnstile Support? - No

Custom User-agent Generation? - Yes

Unique Email and Name Generation? - Yes

- Two versions:
Non-Protected Domains
Cloudflare protected Domains


- Supported Email Formats (you can build your own)
Format 1 - jess smith = jess.smith@domain.com
Format 2 - jess smith = j.smith@domain.com
Format 3 - jess smith = jess.s@domain.com
Format 4 - jess smith = jesssmith@domain.com
Format 5 - jess smith = jsmith@domain.com
Format 6 - jess smith = jesss@domain.com
Format 7 - jess smith = jess_smith@domain.com
Format 8 - jess smith = j_smith@domain.com
Format 9 - jess smith = jess_s@domain.com
Format 10 - Build Your Own
