import React, {Component, PropTypes} from "react";

class CommandListC extends Component {
    render() {
        const commands = JSON.parse(localStorage.getItem('commands'));
        const {commandList} = this.props;
        return (
            <div className="row center-xs">
                <div className="col-xs-6">
                    <div className="box">
                        <div className="row">
                            <div className="col-xs-12 list-group">
                                {
                                    commandList.map((name, index) => {
                                        return <div className="box list-group-item"
                                                    type="button" key={ index }>
                                            {name}
                                        </div>
                                    })
                                }
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

CommandListC.propTypes = {
    commandList: PropTypes.array.isRequired
};

export default CommandListC;