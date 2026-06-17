import { useState, useEffect } from "react";
import "./App.css";

import api from "./api/api";
import UrlForm from "./components/UrlForm";
import ShortUrlCard from "./components/ShortUrlCard";
import AnalyticsCard from "./components/AnalyticsCard";

function App() {
    const [urlData, setUrlData] = useState(null);
    const [analytics, setAnalytics] = useState(null);

    const fetchAnalytics = async (shortCode) => {
        try {
            const response = await api.get(`/analytics/${shortCode}`);
            setAnalytics(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    const handleUrlCreated = (data) => {
        setUrlData(data);
        fetchAnalytics(data.shortCode);
    };

    useEffect(() => {
        if (!urlData) return;

        const interval = setInterval(() => {
            fetchAnalytics(urlData.shortCode);
        }, 3000);

        return () => clearInterval(interval);
    }, [urlData]);

    return (
        <div className="container">

            <h1>🔗 URL Shortener</h1>

            <p>Fast • Secure • Simple URL Shortening</p>

            <UrlForm onUrlCreated={handleUrlCreated} />

            {urlData && (
                <ShortUrlCard shortUrl={urlData.shortUrl} />
            )}

            {analytics && (
                <AnalyticsCard analytics={analytics} />
            )}

        </div>
    );
}

export default App;
