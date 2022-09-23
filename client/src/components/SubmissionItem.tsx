import React, { Component } from "react";
import { Submission } from "../models"
import "./SubmissionItem.css"

type SubmissionProps = {
  submission: Submission;
}

type SubmissionState = {};

export default class SubmissionItem extends Component<
  SubmissionProps,
  SubmissionState
> {
  constructor(props: SubmissionProps) {
    super(props);
    this.state = {};
  }

  render() {
    const { title, text, url } = this.props.submission
    return <>
    <div className="submission-container">
      <a href={url}>{title}</a>
      <p>{text}</p>
    </div>
    </>;
  }
}
