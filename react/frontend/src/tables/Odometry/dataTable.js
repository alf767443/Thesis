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
        dataIndex: 'OdometryId',
        key: 'id',
        sorter: {
            compare: (a, b) => a.OdometryId - b.OdometryId,
            multiple: 1
        },
        defaultSortOrder: 'descend'
    },
    {
        title: 'Left',
        dataIndex: 'OdometryLeft',
        key: 'left'
    },
    {
        title: 'Right',
        dataIndex: 'OdometryRight',
        key: 'right'
    }
];

// --------- table odometry - datatable --------- \\
export class DataTable extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: []
        };
    }

    refreshList() {
        fetch(url.API + 'odometry')
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
