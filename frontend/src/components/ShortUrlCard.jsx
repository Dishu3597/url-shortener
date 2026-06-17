import { useState } from "react";

function ShortUrlCard({ shortUrl }) {

    const [copied, setCopied] = useState(false);

    const copyToClipboard = () => {

        navigator.clipboard.writeText(shortUrl);

        setCopied(true);

        setTimeout(() => {

            setCopied(false);

        },2000);

    };

    return (

        <div className="card">

            <h2>✅ Short URL</h2>

            <a
                href={shortUrl}
                target="_blank"
                rel="noreferrer"
            >
                {shortUrl}
            </a>

            <button onClick={copyToClipboard}>

                {copied ? "✅ Copied!" : "📋 Copy"}

            </button>

        </div>

    );

}

export default ShortUrlCard;