import React, {Component, PropTypes} from "react";
import {connect} from "react-redux";
import CommandListC from "./CommandListC";
import {postExecuteCommand} from "../reducers";

class ExecuteCommandC extends Component {
    constructor(props) {
        super(props);
        localStorage.setItem('commands', JSON.stringify([]));
        this.state = {
            command: "",
            commands: [],
            results: []
        };
    }

    handleKeyPress = (event) => {
        let enter_key = 13;
        if (event.charCode == enter_key) {
            this.handleSave();
        }
    };

    onSave = () => {
        this.handleSave();
    };

    onClearHistory = () => {
        this.setState({command: "", results: [], commands: []});
        localStorage.setItem('commands', JSON.stringify([]));
    };

    handleSave = () => {
        let command = this.state.command;
        if (command) {
            this.props.onPostExecuteCommand(command)
        }
    };

    handleChange = (event) => {
        this.setState({command: event.target.value});
    };

    componentWillReceiveProps = (props) => {
        if (props.executeCommand.success) {
            let command = this.state.command;
            let commands = this.state.commands;
            commands.push(command);
            localStorage.setItem('commands', JSON.stringify(commands));
            this.setState({command: "", commands});
            if (props.executeCommand.data.result) {
                let results = this.state.results;
                results.push(props.executeCommand.data.value);
                this.setState({results});
            }
        }
    };

    render() {
        const {executeCommand} = this.props;
        return (
            <div className="box center-xs">
                <div className="row">
                    <div className="col-xs-12">
                        {executeCommand.error &&
                        <div className="alert alert-danger alert-dismissable fade in">
                            <a href="#" className="close" data-dismiss="alert" aria-label="close">&times;</a>
                            <strong>Error!</strong> {executeCommand.error}
                        </div>
                        }
                    </div>
                </div>
                <div className="row">
                    <div className="col-xs-12">
                        <p>
                            Script execution via web
                            <a href="https://www.hackerrank.com/challenges/cube-summation" target="_blank">
                                <h2>Cube Summation</h2>
                            </a>
                            <h4><b>Nota:</b> Por favor ingrese la entrada de prueba, linea por linea. No toda al mismo tiempo.</h4>
                        </p>
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

                        {executeCommand.success &&
                        <div className="alert alert-success alert-dismissable fade in">
                            <p>
                                {executeCommand.data.message}
                            </p>
                        </div>
                        }
                    </div>
                </div>
                <div className="row">
                    <div className="col-xs-6">
                        <h3>Comandos:</h3>
                        <CommandListC commandList={this.state.commands}/>
                    </div>
                    <div className="col-xs-6">
                        <h3>Resultados:</h3>
                        <CommandListC commandList={this.state.results}/>
                    </div>
                </div>
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
