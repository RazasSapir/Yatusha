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
        
        document.getElementById("lname").value = '';
        document.getElementById("id").value = '';
        document.getElementById("location").value = '';
    }

    // FormQuestion({field_id, field_text, field_type}){
    //     return(
    //         <>
    //             <label htmlFor={field_id}>{field_text}:</label>
    //             <input type={field_type} id={field_id}
    //             onChange={e=> this.updateField({field_id}, e.target.value)}/>
    //         </>
    //     )
    // }

    render(){
      return (
        <div className="form">
{/* 
            <this.FormQuestion field_id="fname" field_text={"שם פרטי"} field_type="text" />
            <this.FormQuestion field_id="lname" field_text={"שם משפחה"} field_type="text" />
            <this.FormQuestion field_id="id" field_text={"ת\"ז"} field_type="number" />
            <this.FormQuestion field_id="location" field_text={"מיקום"} field_type="text" /> */}

            <label htmlFor="fname">שם פרטי:</label>
            <input type="text" id="fname" name="fname"
            onChange={e=> this.updateField("first_name", e.target.value)}/>

            <label htmlFor="lname">שם משפחה:</label>
            <input type="text" id="lname" name="lname"
            onChange={e=> this.updateField("last_name", e.target.value)}/>

            <label htmlFor="lname">ת"ז:</label>
            <input type="number" id="id" name="lname"
            onChange={e=> this.updateField("id", e.target.value)}/>

            <label htmlFor="lname">מיקום:</label>
            <input type="text" id="location" name="lname"
            onChange={e=> this.updateField("location", e.target.value)}/>

            <button className="submit_btn" onClick={this.handleSubmit.bind(this)}>sub</button>
            <br/>
            <p>First name: {this.state.first_name}</p>
            <p>Last name: {this.state.last_name}</p>
            <p>Id: {this.state.id}</p>
            <p>Location: {this.state.location}</p>
        </div>
      );
    }
    
  }