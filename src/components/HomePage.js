import React from "react"
import yatushaLogo from "../images/logoYatusha.jfif"
import "../style/HomePage.css"

export default function HomePage(){
    const about = "לורם איפסום דולור סיט אמט, קונסקטורר אדיפיסינג אלית צש בליא, מנסוטו צמלח לביקו ננבי, צמוקו בלוקריה שיצמה ברורק. קולהע צופעט למרקוח איבן איף, ברומץ כלרשט מיחוצים. קלאצי קולהע צופעט למרקוח איבן איף, ברומץ כלרשט מיחוצים. קלאצי גולר מונפרר סוברט לורם שבצק יהול, לכנוץ בעריר גק ליץ, גולר מונפרר סוברט לורם שבצק יהול, לכנוץ בעריר גק ליץ, ושבעגט ליבם סולגק. בראיט ולחת צורק מונחף, בגורמי מגמש. תרבנך וסתעד לכנו סתשם השמה - לתכי מורגם בורק? לתיג ישבעס."
    return(
        <>
            <div className="mainPage">
                <img className ="imgYatusha" src = {yatushaLogo} alt = ""/>
                <nav className = "navbar">
                    <p>דף 2</p>
                    <p>דף 1</p>
                    <p>דף 3</p>
                </nav>
                <p className="about">{about}</p>
                <footer className="main_footer">
                <p> All rights reserved</p> 
                <a>ico1</a>
                <a>ico2</a>
                <a>ico3</a>
            </footer>
            </div>
        </>
    )
}