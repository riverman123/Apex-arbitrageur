SETTING = {
    "URL": "https://rinkeby.arbitrum.io/rpc",
    "PRIVATE_KEY_ROBOT":"0xf072d6e5deacdc39f916f38123beddf63cd2934bb7863a5c2e62949d1bac5bee", # WALLET_PRIVATE_KEY 加0x
    "ADDRESS_ROBOT":"0x4c3C90d25c93d08853b61c81cFd95d58c3B0C073",
    "PRIVATE_KEY_USER":"0x5921059e276bae2e61d8e5ade6d6a026cce953344d3b9f0df218ef9ecd90ac58",
    "ADDRESS_USER":"0x6014F6D866F3EeC7463c7D74639185265a98C91D",
}

TOKEN_INFO = {
    "mockWETH": "0x655e2b2244934Aea3457E3C56a7438C271778D44",
    "mockWBTC": "0x3F12C33BDe6dE5B66F88D7a5d3CE8dE3C98b5FA7",
    "mockUSDC": "0x79dCF515aA18399CF8fAda58720FAfBB1043c526",
    "BBB":"0x8d5de6ac3732b8fbfc6d4843ac182eb725f3f741"
}

MARGIN_CONTRACT_INFO = {
    "CONTRACT_ADDRESS": "0x0eD607e927a4C5f5CA304da171e6e6F3E8887920",
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
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "withdrawAmount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "int256",
				"name": "fundingFee",
				"type": "int256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "withdrawAmountFromMargin",
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
		"name": "calUnrealizedPnl",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
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
		"inputs": [],
		"name": "getNewLatestCPF",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
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
		"inputs": [
			{
				"internalType": "bool",
				"name": "isLong",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			}
		],
		"name": "querySwapBaseWithAmm",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
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
				"internalType": "address",
				"name": "to",
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
	},
	{
		"inputs": [],
		"name": "updateCPF",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""
}

ROUTER_CONTRACT_INFO = {
    "CONTRACT_ADDRESS": "0x39d3a0F25D94D9c13E552b9E81eF9b03550A9783",
    "CONTRACT_ABI":"""[
	{
		"inputs": [],
		"name": "WETH",
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
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmountMin",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "pcv",
				"type": "bool"
			}
		],
		"name": "addLiquidity",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "liquidity",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmountMin",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "pcv",
				"type": "bool"
			}
		],
		"name": "addLiquidityETH",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "ethAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "liquidity",
				"type": "uint256"
			}
		],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "autoWithdraw",
				"type": "bool"
			}
		],
		"name": "closePosition",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "withdrawAmount",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			}
		],
		"name": "closePositionETH",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "withdrawAmount",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "holder",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "deposit",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "holder",
				"type": "address"
			}
		],
		"name": "depositETH",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "holder",
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
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint8",
				"name": "side",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			}
		],
		"name": "getQuoteAmount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quoteAmount",
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
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			}
		],
		"name": "getReserves",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "reserveBase",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "reserveQuote",
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
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "holder",
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
				"name": "quoteToken",
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
			},
			{
				"internalType": "uint256",
				"name": "baseAmountLimit",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			}
		],
		"name": "openPositionETHWithWallet",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			}
		],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
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
			},
			{
				"internalType": "uint256",
				"name": "baseAmountLimit",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			}
		],
		"name": "openPositionWithMargin",
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
		"inputs": [
			{
				"internalType": "address",
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint8",
				"name": "side",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "marginAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "baseAmountLimit",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			}
		],
		"name": "openPositionWithWallet",
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
		"name": "pairFactory",
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
		"name": "pcvTreasury",
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
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "liquidity",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "baseAmountMin",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			}
		],
		"name": "removeLiquidity",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "liquidity",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "ethAmountMin",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			}
		],
		"name": "removeLiquidityETH",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "ethAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "withdraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "withdrawETH",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""
}

PRICEORACLE_CONTRACT_INFO = {
    "CONTRACT_ADDRESS": "0xB89280BA3c2057c68458b6f462Fc81b9a632bB21",
    "CONTRACT_ABI":"""[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "amm",
				"type": "address"
			}
		],
		"name": "getIndexPrice",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
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
				"name": "amm",
				"type": "address"
			}
		],
		"name": "getMarkPrice",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "price",
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
				"name": "amm",
				"type": "address"
			},
			{
				"internalType": "uint8",
				"name": "beta",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "negative",
				"type": "bool"
			}
		],
		"name": "getMarkPriceAcc",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
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
				"name": "amm",
				"type": "address"
			}
		],
		"name": "getPremiumFraction",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
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
				"name": "baseToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "quoteToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			}
		],
		"name": "quote",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint8",
				"name": "source",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "amm",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			}
		],
		"name": "quoteFromAmmTwap",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quoteAmount",
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
				"name": "amm",
				"type": "address"
			}
		],
		"name": "setupTwap",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "pair",
				"type": "address"
			}
		],
		"name": "updateAmmTwap",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""
}

AMM_CONTRACT_INFO = {
    "CONTRACT_ADDRESS": "0x357B185F7D472b0bC7b9a8dE3A26d3404b26acCa",
    "CONTRACT_ABI":"""[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
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
				"indexed": false,
				"internalType": "uint256",
				"name": "liquidity",
				"type": "uint256"
			}
		],
		"name": "Burn",
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
				"indexed": true,
				"internalType": "address",
				"name": "inputToken",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "outputToken",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "inputAmount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "outputAmount",
				"type": "uint256"
			}
		],
		"name": "ForceSwap",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
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
				"indexed": false,
				"internalType": "uint256",
				"name": "liquidity",
				"type": "uint256"
			}
		],
		"name": "Mint",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "quoteReserveBefore",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "quoteReserveAfter",
				"type": "uint256"
			}
		],
		"name": "Rebase",
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
				"indexed": true,
				"internalType": "address",
				"name": "inputToken",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "outputToken",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "inputAmount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "outputAmount",
				"type": "uint256"
			}
		],
		"name": "Swap",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint112",
				"name": "reserveBase",
				"type": "uint112"
			},
			{
				"indexed": false,
				"internalType": "uint112",
				"name": "reserveQuote",
				"type": "uint112"
			}
		],
		"name": "Sync",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "MINIMUM_LIQUIDITY",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "pure",
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
				"name": "to",
				"type": "address"
			}
		],
		"name": "burn",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "liquidity",
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
		"inputs": [
			{
				"internalType": "address",
				"name": "inputToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "outputToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "inputAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "outputAmount",
				"type": "uint256"
			}
		],
		"name": "estimateSwap",
		"outputs": [
			{
				"internalType": "uint256[2]",
				"name": "amounts",
				"type": "uint256[2]"
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
			},
			{
				"internalType": "address",
				"name": "inputToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "outputToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "inputAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "outputAmount",
				"type": "uint256"
			}
		],
		"name": "forceSwap",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getReserves",
		"outputs": [
			{
				"internalType": "uint112",
				"name": "reserveBase",
				"type": "uint112"
			},
			{
				"internalType": "uint112",
				"name": "reserveQuote",
				"type": "uint112"
			},
			{
				"internalType": "uint32",
				"name": "blockTimestamp",
				"type": "uint32"
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
				"name": "margin_",
				"type": "address"
			}
		],
		"name": "initialize",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "lastPrice",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "margin",
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
				"name": "to",
				"type": "address"
			}
		],
		"name": "mint",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "baseAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "quoteAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "liquidity",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "price0CumulativeLast",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "price1CumulativeLast",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
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
		"inputs": [],
		"name": "rebase",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quoteReserveAfter",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "rebaseFree",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quoteReserveAfter",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_baseReserve",
				"type": "uint256"
			}
		],
		"name": "setBaseReserve",
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
			},
			{
				"internalType": "address",
				"name": "inputToken",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "outputToken",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "inputAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "outputAmount",
				"type": "uint256"
			}
		],
		"name": "swap",
		"outputs": [
			{
				"internalType": "uint256[2]",
				"name": "amounts",
				"type": "uint256[2]"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""
}

CONFIG_INFO = {
    "CONTRACT_ADDRESS": "0xD661056569866dA894E4c2c9d5B3752C64552e7e",
    "CONTRACT_ABI":"""[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "oldOracle",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOracle",
				"type": "address"
			}
		],
		"name": "PriceOracleChanged",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "oldGap",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "newGap",
				"type": "uint256"
			}
		],
		"name": "RebasePriceGapChanged",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "router",
				"type": "address"
			}
		],
		"name": "RouterRegistered",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "router",
				"type": "address"
			}
		],
		"name": "RouterUnregistered",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "oldBeta",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "beta",
				"type": "uint256"
			}
		],
		"name": "SetBeta",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "oldFeeParameter",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "feeParameter",
				"type": "uint256"
			}
		],
		"name": "SetFeeParameter",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "oldInitMarginRatio",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "initMarginRatio",
				"type": "uint256"
			}
		],
		"name": "SetInitMarginRatio",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "oldLiquidateFeeRatio",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "liquidateFeeRatio",
				"type": "uint256"
			}
		],
		"name": "SetLiquidateFeeRatio",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "oldLiquidateThreshold",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "liquidateThreshold",
				"type": "uint256"
			}
		],
		"name": "SetLiquidateThreshold",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "oldMaxCPFBoost",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "maxCPFBoost",
				"type": "uint256"
			}
		],
		"name": "SetMaxCPFBoost",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "oldTradingSlippage",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "newTradingSlippage",
				"type": "uint256"
			}
		],
		"name": "TradingSlippageChanged",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "beta",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "feeParameter",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "initMarginRatio",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "liquidateFeeRatio",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "liquidateThreshold",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "maxCPFBoost",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "priceOracle",
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
		"name": "rebasePriceGap",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
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
				"name": "router",
				"type": "address"
			}
		],
		"name": "registerRouter",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "routerMap",
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
				"internalType": "uint8",
				"name": "newBeta",
				"type": "uint8"
			}
		],
		"name": "setBeta",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "newFeeParameter",
				"type": "uint256"
			}
		],
		"name": "setFeeParameter",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "marginRatio",
				"type": "uint256"
			}
		],
		"name": "setInitMarginRatio",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "feeRatio",
				"type": "uint256"
			}
		],
		"name": "setLiquidateFeeRatio",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "threshold",
				"type": "uint256"
			}
		],
		"name": "setLiquidateThreshold",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "newMaxCPFBoost",
				"type": "uint256"
			}
		],
		"name": "setMaxCPFBoost",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOracle",
				"type": "address"
			}
		],
		"name": "setPriceOracle",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "newGap",
				"type": "uint256"
			}
		],
		"name": "setRebasePriceGap",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "newTradingSlippage",
				"type": "uint256"
			}
		],
		"name": "setTradingSlippage",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "tradingSlippage",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
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
				"name": "router",
				"type": "address"
			}
		],
		"name": "unregisterRouter",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""
}