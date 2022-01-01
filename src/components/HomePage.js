import React from "react"
import yatushaLogo from "../images/logoYatusha.jfif"
import "../style/HomePage.css"
import { useNavigate } from "react-router-dom"

export default function HomePage(){
    const about = "לורם איפסום דולור סיט אמט, קונסקטורר אדיפיסינג אלית צש בליא, מנסוטו צמלח לביקו ננבי, צמוקו בלוקריה שיצמה ברורק. קולהע צופעט למרקוח איבן איף, ברומץ כלרשט מיחוצים. קלאצי קולהע צופעט למרקוח איבן איף, ברומץ כלרשט מיחוצים. קלאצי גולר מונפרר סוברט לורם שבצק יהול, לכנוץ בעריר גק ליץ, גולר מונפרר סוברט לורם שבצק יהול, לכנוץ בעריר גק ליץ, ושבעגט ליבם סולגק. בראיט ולחת צורק מונחף, בגורמי מגמש. תרבנך וסתעד לכנו סתשם השמה - לתכי מורגם בורק? לתיג ישבעס."
    let navigate = useNavigate();
    return(
            <div className="mainPage">
                <img className ="imgYatusha" src = {yatushaLogo} alt = ""/>
                <nav className = "navbar">
                    <p>האזור האישי</p>
                    <p onClick={() => navigate("/form")}>רישום הדברה</p>
                    <p>תמיכה טכנית</p>
                </nav>
                <p className="about">{about}</p>
            </div>
    )
}