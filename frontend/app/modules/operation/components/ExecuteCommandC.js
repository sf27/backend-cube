import React, {Component, PropTypes} from "react";
import {connect} from "react-redux";
import CommandListC from "./CommandListC";
import {postExecuteCommand} from "../reducers";

class ExecuteCommandC extends Component {
    constructor(props) {
        super(props);
        this.state = {
            command: "",
            commands: JSON.parse(localStorage.getItem('commands')) || []
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
        this.setState({command: "", commands: []});
        localStorage.setItem('commands', JSON.stringify([]));
    };

    handleSave = () => {
        let command = this.state.command;
        if (command) {
            let commands = this.state.commands;
            commands.push(command);
            localStorage.setItem('commands', JSON.stringify(commands));
            this.setState({command: "", commands: commands});
            this.props.onPostExecuteCommand(command)
        }
    };

    handleChange = (event) => {
        this.setState({command: event.target.value});
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
                                value={this.state.command}
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

const mapStateToProps = state => (
{
    executeCommand: state.executeCommand
}
);

const mapDispatchToProps = dispatch => (
{
    onPostExecuteCommand: (command) => {
        dispatch(postExecuteCommand(command));
    }
}
);

ExecuteCommandC.propTypes = {
    onPostExecuteCommand: React.PropTypes.func.isRequired,
    executeCommand: React.PropTypes.object.isRequired,
};

const ExecuteCommand = connect(mapStateToProps, mapDispatchToProps)(ExecuteCommandC);

export default ExecuteCommand;
