const char = `MSCode ::= SEQUENCE {
	type			SEQUENCE {
		contentType	ContentType,
		parameters	ANY
	},
	content			SEQUENCE {
		digestAlgorithm	DigestAlgorithmIdentifier,
		digest		OCTET STRING ({ mscode_note_digest })
	}
}

ContentType ::= OBJECT IDENTIFIER ({ mscode_note_content_type })

DigestAlgorithmIdentifier ::= SEQUENCE {
	algorithm   OBJECT IDENTIFIER ({ mscode_note_digest_algo }),
    parameters  ANY OPTIONAL
    #define pr_fmt(fmt) "ASYM: "fmt
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/err.h>
#include <crypto/public_key.h>
#include "asymmetric_keys.h"

static bool use_builtin_keys;
static struct asymmetric_key_id *ca_keyid;

#ifndef MODULE
static struct {
	struct asymmetric_key_id id;
	unsigned char data[10];
} cakey;

static int __init ca_keys_setup(char *str)
{
	if (!str)		/* default system keyring */
		return 1;

	if (strncmp(str, "id:", 3) == 0) {
		struct asymmetric_key_id *p = &cakey.id;
		size_t hexlen = (strlen(str) - 3) / 2;
		int ret;

		if (hexlen == 0 || hexlen > sizeof(cakey.data)) {
			pr_err("Missing or invalid ca_keys id\n");
			return 1;
		}

		ret = __asymmetric_key_hex_to_key_id(str + 3, p, hexlen);
		if (ret < 0)
			pr_err("Unparsable ca_keys id hex string\n");
		else
			ca_keyid = p;	/* owner key 'id:xxxxxx' */
	} else if (strcmp(str, "builtin") == 0) {
		use_builtin_keys = true;
	}

	return 1;
}
__setup("ca_keys=", ca_keys_setup);
#endif

/**
 * restrict_link_by_signature - Restrict additions to a ring of public keys
 PrivateKeyInfo ::= SEQUENCE {
	version			Version,
	privateKeyAlgorithm	PrivateKeyAlgorithmIdentifier,
	privateKey		PrivateKey,
	attributes		[0] IMPLICIT Attributes OPTIONAL
}

Version ::= INTEGER  ({ pkcs8_note_version })

PrivateKeyAlgorithmIdentifier ::= AlgorithmIdentifier ({ pkcs8_note_algo })

PrivateKey ::= OCTET STRING ({ pkcs8_note_key })

Attributes ::= SET OF Attribute

Attribute ::= ANY

AlgorithmIdentifier ::= SEQUENCE {
	algorithm   OBJECT IDENTIFIER ({ pkcs8_note_OID }),
	parameters  ANY OPTIONAL   
 `
// const char = `MSCode ::= SEQUENCE {
const code = document.querySelector('#code');
let i = 0;
code.addEventListener('keydown', function(event){
    event.preventDefault()
    console.log('yo')
    code.value += char.slice(i, i +3)
    i += 3;
    code.scrollTop = code.scrollHeight;

    
})
