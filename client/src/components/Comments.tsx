import React, { Component } from 'react'

type CommentsProps = {}

type CommentState = {
  comments: Comment[];
  date: number;
}

type Comment = {
  author_id: string;  
  body: string;
  id: string;
  created_utc: number;
}

export default class Comments extends Component<CommentsProps, CommentState> {
  constructor(props: CommentsProps) {
    super(props)
    this.state = {
      comments : [],
      date: new Date().getTime()
    }
  }

  getComments = async () => {
    await fetch('/comments')
      .then((response: Response) => response.text())
      .then((data) => this.setState({...this.state, comments: JSON.parse(data), date: new Date().getTime()
      }))
  }

  componentDidMount() {
    this.getComments();
  }

  componentDidUpdate() {
    setTimeout(this.getComments, 5000); // wait for 5 seconds to not hit firebase read quota
  }

  render() {
    const comments = this.state.comments;
    const date = this.state.date;
    console.log(comments)
    comments.sort((a, b) => b.created_utc - a.created_utc)
    return (
      <div>
        <h1>{date}</h1>
      <table>
        <tr>
          <th>Created at</th>
          <th>Post ID</th>
          <th>Author ID</th>
          <th>Body</th>
        </tr>
        {comments.map((comment) => {
          return <tr id={comment.id}>
            <td>{comment.created_utc}</td>
            <td>{comment.id}</td>
            <td>{comment.author_id}</td>
            <td>{comment.body}</td>
          </tr>
        })}
      </table>
      </div>
    )
  }
}
