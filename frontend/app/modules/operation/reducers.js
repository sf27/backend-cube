import {EXECUTE_COMMAND_REQUEST, EXECUTE_COMMAND_SUCCESS, EXECUTE_COMMAND_FAILURE} from "./actions";

export const postExecuteCommandRequest = () => ({type: EXECUTE_COMMAND_REQUEST});
export const postExecuteCommandSuccess = (data) => ({type: EXECUTE_COMMAND_SUCCESS, data});
export const postExecuteCommandFailure = (error) => ({type: EXECUTE_COMMAND_FAILURE, error});


export function postExecuteCommand(command) {
    return dispatch => {
        dispatch(postExecuteCommandRequest());
        dispatch(postExecuteCommandSuccess());
        // todo: add post request
    }
}

const INITIAL_STATE = {
    executeCommand: {loading: false, success: false, error: '', data: ''}
};

const baseReducer = (state = INITIAL_STATE, action) => {
    let error;
    let data;
    switch (action.type) {
        case EXECUTE_COMMAND_REQUEST:
            return Object.assign({}, state, {
                executeCommand: {loading: true, success: false, error: '', data: []}
            });

        case EXECUTE_COMMAND_SUCCESS:
            data = action.data;
            return Object.assign({}, state, {
                executeCommand: {loading: false, success: true, error: '', data}
            });

        case EXECUTE_COMMAND_FAILURE:
            error = action.error;
            return Object.assign({}, state, {
                executeCommand: {loading: false, success: false, error, data: []}
            });

        default:
            return state;
    }
};

export default baseReducer;