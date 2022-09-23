import React, { Component } from "react";
import { Submission } from "../models";
import SubmissionItem from "./SubmissionItem";

export default class SubmissionPage extends Component {
  render() {
    const submission : Submission = {id: 1, title: "example title", text: "example text", url: "www.google.com", created_utc: "123"}
    return (
      <>
        <SubmissionItem submission={submission}/>
      </>
    );
  }
}
