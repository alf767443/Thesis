import React from "react";
import parse from "html-react-parser";

class App extends React.Component {

    constructor() {
        super();
        this.state = {
          description: '<h1 style="color:red;">something</h1>'
        }
      }

      forloop () {
        let text = ''
        for(let i = 0; i < 10; i++){
            text += '<h1 style="color:red;">something</h1> *'
            console.log(text)
        }
        return text
      }

      render() {
        this.forloop();
        return (
          <div>{parse(this.forloop())}</div>
        );
      }
    }
    
export default App;