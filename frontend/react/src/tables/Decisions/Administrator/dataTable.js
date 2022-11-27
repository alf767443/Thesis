// Import from React
import React, { Component } from 'react';

// Import from Antd
import { Table } from 'antd';

// Import from project
import { url } from 'djangoAPI/url';

// Define columns
const columns = [
    {
        title: 'Id',
        dataIndex: 'AdministratorId',
        key: 'id',
        sorter: {
            compare: (a, b) => a.AdministratorId - b.AdministratorId,
            multiple: 1
        },
        defaultSortOrder: 'descend'
    },
    {
        title: 'Decision',
        dataIndex: 'AdministratorDecision',
        key: 'decision'
    },
    {
        title: 'Priority',
        dataIndex: 'AdministratorPriority',
        key: 'priority'
    }
];

const urls = 'decision/administrator';

// --------- table fiducialmark - datatable --------- \\
export class DataTable extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: []
        };
    }

    refreshList() {
        fetch(url.API + urls)
            .then((response) => response.json())
            .then((data) => {
                this.setState({ data: data });
            });
    }

    componentDidMount() {
        this.refreshList();
    }

    render() {
        console.log(this.state.data);

        return (
            <Table
                columns={columns}
                dataSource={this.state.data}
                pagination={this.state.pagination}
                loading={this.state.loading}
                onChange={this.handleTableChange}
                sx={this.props.sx}
            />
        );
    }
}
