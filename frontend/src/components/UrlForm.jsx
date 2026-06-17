import { useState } from "react";
import api from "../api/api";

function UrlForm({ onUrlCreated }) {

    const [url, setUrl] = useState("");

    const handleSubmit = async (e) => {

        e.preventDefault();

        if (!url.trim()) {
            alert("Please enter a URL");
            return;
        }

        try {

            const response = await api.post("/shorten", {
                url
            });

            onUrlCreated(response.data);

            setUrl("");

        } catch (error) {

            alert(
                error.response?.data?.error ||
                "Something went wrong"
            );

        }

    };

    return (

        <form onSubmit={handleSubmit}>

            <input
                type="url"
                placeholder="Paste your long URL here..."
                value={url}
                onChange={(e)=>setUrl(e.target.value)}
                required
            />

            <button type="submit">
                🚀 Shorten URL
            </button>

        </form>

    );

}

export default UrlForm;