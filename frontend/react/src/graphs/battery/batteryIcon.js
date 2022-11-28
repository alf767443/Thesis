import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import { Liquid } from "@ant-design/plots";
import { SvgIcon } from "@mui/material";
import { BoltIcon } from "@mui/icons-material/Bolt";

export default class BatteryIcon extends React.Component {
	constructor(props) {
		super(props);
	}

	pallet = ["#12B33A", "#97F218", "#F5F518", "#FF860D", "#D91616"];

	config = {
		shape: function (x, y, width, height) {
			const lr = height * 0.06;
			const r = height * 0.07;
			const lh = width * 0.03;
			const h = height * (0.5 - 0.06 - 0.03);
			const lw = width * 0.11;
			const w = width * 0.3;
			return [
				["M", x - w, y + h + lh + r],
				["L", x - w, y - h + lh + r],
				["A", r, r, 0, 0, 1, x - w + r, y - h + lh],
				["L", x - lw, y - h + lh],
				["L", x - lw, y - h],
				["A", lr, lr, 0, 0, 1, x - lw + lr, y - h - lr],
				["L", x + lw - lr, y - h - lr],
				["A", lr, lr, 0, 0, 1, x + lw, y - h],
				["L", x + lw, y - h + lh],
				["L", x + w - r, y - h + lh],
				["A", r, r, 0, 0, 1, x + w, y - h + lh + r],
				["L", x + w, y + h + lh + r],
				["Z"],
			];
		},
		outline: {
			border: 1,
			distance: 0,
		},
	};

	statistic = [null];

	color() {
		if (this.props.percent < 0.2) {
			return this.pallet[4];
		} else if (this.props.percent < 0.4) {
			return this.pallet[3];
		} else if (this.props.percent < 0.6) {
			return this.pallet[2];
		} else if (this.props.percent < 0.8) {
			return this.pallet[1];
		} else if (this.props.percent < 1) {
			return this.pallet[0];
		} else {
			return "#B3B3B3";
		}
	}

	render() {
		return (
			<div>
				<Liquid
					{...this.config}
					color={this.color()}
					percent={this.props.percent}
					width={this.props.width}
					height={this.props.height}
					statistic={this.statistic}
				/>
			</div>
		);
	}
}
