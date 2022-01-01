import React from "react"
import "../style/Form.css"
import Post from "../FetchNPost"

export default class Form extends React.Component{
    fields = ["first_name", "last_name", "id", "location"];

    constructor(props){
      super(props);
       this.state={
         first_name: "",
         last_name: "",
         id: 0,
         location: ""
       }
    }
  
    updateField(key, value){
      //update react state
      this.setState({
        [key]: value
      });
    }

    handleSubmit(){
    //handles submit button click
        //sends personal data to db
        Post(this.state)
        console.log("posted")

        //initiates input fields
        this.fields.forEach(element => {
            document.getElementById("element").value = '';
        });
    }

    FormQuestion({context, field_id, field_text, field_type}){
      console.log(field_id);
      return(
          <div className="form__question">
              <input className="form__input" type={field_type} autoComplete="off" placeholder=" "
              onChange={(e)=> context.updateField("first_name", e.target.value)}/>              
              <label className="form__label" htmlFor={field_id}>{field_text}:</label>
          </div>
      );
    }

    render(){
      return (
        <div className="form">
          <h1>תיעוד אירוע הדברה:</h1>
          <div className="form__questions">
            <this.FormQuestion context = {this} field_id="first_name" field_text={"שם פרטי"} field_type="text" />
            <this.FormQuestion context = {this} field_id="last_name" field_text={"שם משפחה"} field_type="text" />
            <this.FormQuestion context = {this} field_id="license" field_text={"מספר רישיון"} field_type="number" />
            <this.FormQuestion context = {this} field_id="location" field_text={"מיקום"} field_type="text" />
            <this.FormQuestion context = {this} field_id="pest" field_text={"מזיק"} field_type="text" />
            <this.FormQuestion context = {this} field_id="substance" field_text={"תכשיר הדברה"} field_type="text" />
            <this.FormQuestion context = {this} field_id="amount" field_text={"ריכוז"} field_type="text" />
          </div>

          <button className="submit_btn" onClick={this.handleSubmit.bind(this)}>שליחה</button>
          {/* <br/>
          <p>First name: {this.state.first_name}</p>
          <p>Last name: {this.state.last_name}</p>
          <p>Id: {this.state.id}</p>
          <p>Location: {this.state.location}</p> */}
        </div>
      );
    }
    
  }
