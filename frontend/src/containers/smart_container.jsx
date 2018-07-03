import React from 'react';
import { connect } from 'react-redux';

import { fetchCards, annotateCard, passCard, popCard } from '../actions/classifier';
import { getHistory, changeLabel } from '../actions/history'

import Smart from '../components/Smart';

const PROJECT_ID = window.PROJECT_ID

const SmartContainer = (props) => <Smart {...props} />;

const mapStateToProps = (state) => {
    return {
        cards: state.classifier.cards,
        message: state.classifier.message,
        history_data: state.history.history_data,
        labels: state.history.labels
    };
};

const mapDispatchToProps = (dispatch) => {
    return {
        fetchCards: () => {
            dispatch(fetchCards(PROJECT_ID))
        },
        annotateCard: (dataID, labelID) => {
            dispatch(annotateCard(dataID, labelID, PROJECT_ID))
        },
        passCard: (dataID) => {
            dispatch(passCard(dataID))
        },
        popCard: () => {
            dispatch(popCard())
        },
        getHistory: () => {
            dispatch(getHistory(PROJECT_ID))
        },
        changeLabel: (dataID, oldLabelID ,labelID) => {
            dispatch(changeLabel(dataID, oldLabelID,labelID, PROJECT_ID))
        },
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(SmartContainer);
