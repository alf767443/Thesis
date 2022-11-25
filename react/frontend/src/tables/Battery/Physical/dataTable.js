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
        dataIndex: 'PhysicalId',
        key: 'id',
        sorter: {
            compare: (a, b) => a.PhysicalId - b.PhysicalId,
            multiple: 1
        },
        defaultSortOrder: 'descend'
    },
    {
        title: 'Voltage',
        dataIndex: 'PhysicalVoltage',
        key: 'voltage'
    },
    {
        title: 'Temperature',
        dataIndex: 'PhysicalTemperature',
        key: 'voltage'
    },
    {
        title: 'Current',
        dataIndex: 'PhysicalCurrent',
        key: 'current'
    }
];

const urls = 'battery/physical';

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
