import React, {Component, PropTypes} from "react";
import CommandListC from "./CommandListC";

class ExecuteCommandC extends Component {
    constructor(props) {
        super(props);
        this.state = {
            message: "",
            commands: JSON.parse(localStorage.getItem('commands'))
        };
    }

    handleKeyPress = (event) => {
        if (event.charCode == 13) {
            this.handleSave();
        }
    };

    onSave = () => {
        this.handleSave();
    };

    onClearHistory = () => {
        this.setState({message: "", commands: []});
        localStorage.setItem('commands', JSON.stringify([]));
    };

    handleSave = () => {
        let message = this.state.message;
        if (message) {
            let commands = this.state.commands;
            commands.push(message);
            localStorage.setItem('commands', JSON.stringify(commands));
            this.setState({message: "", commands: commands});
        }
    };

    handleChange = (event) => {
        this.setState({message: event.target.value});
    };

    render() {
        return (
            <div className="box center-xs">
                <div className="row">
                    <div className="col-xs-12">
                        Ejecución de Script via WEB
                    </div>
                </div>
                <div className="row">
                    <div className="center-block">
                        <div className="form-group">
                            <input
                                type="text"
                                className="form-control"
                                value={this.state.message}
                                onChange={this.handleChange}
                                onKeyPress={this.handleKeyPress}
                            />
                            <button className="btn btn-default" onClick={this.onClearHistory}>
                                Clear history
                            </button>
                            <button className="btn btn-default" onClick={this.onSave}>
                                Execute
                            </button>
                        </div>
                    </div>
                </div>
                <CommandListC commandList={this.state.commands}/>
            </div>
        );
    }
}

export default ExecuteCommandC;
