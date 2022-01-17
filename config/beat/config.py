SETTING = {
    "ROPSTEN_URL": "https://rinkeby.arbitrum.io/rpc",
    "WALLET_PRIVATE_KEY": "0x5921059e276bae2e61d8e5ade6d6a026cce953344d3b9f0df218ef9ecd90ac58", # WALLET_PRIVATE_KEY 加0x
    "WALLET_ADDRESS": "0x6014F6D866F3EeC7463c7D74639185265a98C91D"
}

MARGIN_CONTRACT_INFO = {
    "CONTRACT_ADDRESS": "0x0ee4ad6Cb756D1a548E359BB8a6dF86d4798df89",
    "CONTRACT_ABI":"""[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "depositAmount",
				"type": "uint256"
			},
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "AddMargin",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "BeforeAddMargin",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "BeforeClosePosition",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "BeforeLiquidate",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "BeforeOpenPosition",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "BeforeRemoveMargin",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "int256",
				"name": "fundingFee",
				"type": "int256"
			},
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "ClosePosition",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "liquidator",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "bonus",
				"type": "uint256"
			},
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "Liquidate",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint8",
				"name": "side",
				"type": "uint8"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "OpenPosition",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "withdrawAmount",
				"type": "uint256"
			},
			{
				"components": [
					{
						"internalType": "int256",
						"name": "quoteSize",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "baseSize",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "tradeSize",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct IMargin.Position",
				"name": "position",
				"type": "tuple"
			}
		],
		"name": "RemoveMargin",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "timeStamp",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "int256",
				"name": "cpf",
				"type": "int256"
			}
		],
		"name": "UpdateCPF",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "depositAmount",
				"type": "uint256"
			}
		],
		"name": "addMargin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "amm",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "baseToken",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			}
		],
		"name": "calDebtRatio",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "debtRatio",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			}
		],
		"name": "calFundingFee",
		"outputs": [
			{
				"internalType": "int256",
				"name": "fundingFee",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			}
		],
		"name": "canLiquidate",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			}
		],
		"name": "closePosition",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "config",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "factory",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			}
		],
		"name": "getPosition",
		"outputs": [
			{
				"internalType": "int256",
				"name": "baseSize",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "quoteSize",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "tradeSize",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			}
		],
		"name": "getWithdrawable",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "baseToken_",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken_",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "amm_",
				"type": "address"
			}
		],
		"name": "initialize",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			}
		],
		"name": "liquidate",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "bonus",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "netPosition",
		"outputs": [
			{
				"internalType": "int256",
				"name": "netBasePosition",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"internalType": "uint8",
				"name": "side",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			}
		],
		"name": "openPosition",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "quoteToken",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "trader",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "withdrawAmount",
				"type": "uint256"
			}
		],
		"name": "removeMargin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""
    }

