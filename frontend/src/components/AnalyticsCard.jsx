function AnalyticsCard({ analytics }) {

    return (

        <div className="card">

            <h2>📊 Analytics</h2>

            <div className="analytics-grid">

                <div className="analytics-box">

                    <h3>Visits</h3>

                    <span>{analytics.visitCount}</span>

                </div>

                <div className="analytics-box">

                    <h3>Created</h3>

                    <span>

                        {new Date(
                            analytics.createdAt
                        ).toLocaleDateString()}

                    </span>

                </div>

            </div>

        </div>

    );

}

export default AnalyticsCard;