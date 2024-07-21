from Parser import parse_throughput_samples

throughput_sample1 = """
{
	"start":	{
		"connected":	[{
				"socket":	5,
				"local_host":	"10.18.5.195",
				"local_port":	34976,
				"remote_host":	"10.30.0.1",
				"remote_port":	5201
			}],
		"version":	"iperf 3.16",
		"system_info":	"Linux instance-0 6.5.0-1024-azure #25~22.04.1-Ubuntu SMP Mon Jun 17 18:38:57 UTC 2024 x86_64",
		"timestamp":	{
			"time":	"Sun, 21 Jul 2024 13:30:52 GMT",
			"timesecs":	1721568652
		},
		"connecting_to":	{
			"host":	"10.30.0.1",
			"port":	5201
		},
		"cookie":	"amyhzi4wokkmf5mm4axi7267uztshn327viv",
		"target_bitrate":	0,
		"fq_rate":	0,
		"sock_bufsize":	0,
		"sndbuf_actual":	212992,
		"rcvbuf_actual":	212992,
		"test_start":	{
			"protocol":	"UDP",
			"num_streams":	1,
			"blksize":	1398,
			"omit":	0,
			"duration":	20,
			"bytes":	0,
			"blocks":	0,
			"reverse":	0,
			"tos":	0,
			"target_bitrate":	0,
			"bidir":	0,
			"fqrate":	0
		}
	},
	"intervals":	[{
			"streams":	[{
					"socket":	5,
					"start":	0,
					"end":	1.000888,
					"seconds":	1.0008879899978638,
					"bytes":	206857866,
					"bits_per_second":	1653394730.0172241,
					"packets":	147968,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	0,
				"end":	1.000888,
				"seconds":	1.0008879899978638,
				"bytes":	206857866,
				"bits_per_second":	1653394730.0172241,
				"packets":	147968,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	1.000888,
					"end":	2.000903,
					"seconds":	1.0000150203704834,
					"bytes":	205294902,
					"bits_per_second":	1642334547.5266385,
					"packets":	146849,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	1.000888,
				"end":	2.000903,
				"seconds":	1.0000150203704834,
				"bytes":	205294902,
				"bits_per_second":	1642334547.5266385,
				"packets":	146849,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	2.000903,
					"end":	3.000896,
					"seconds":	0.99999302625656128,
					"bytes":	197350068,
					"bits_per_second":	1578811554.2267172,
					"packets":	141166,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	2.000903,
				"end":	3.000896,
				"seconds":	0.99999302625656128,
				"bytes":	197350068,
				"bits_per_second":	1578811554.2267172,
				"packets":	141166,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	3.000896,
					"end":	4.00094,
					"seconds":	1.0000439882278442,
					"bytes":	209444166,
					"bits_per_second":	1675479626.620436,
					"packets":	149817,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	3.000896,
				"end":	4.00094,
				"seconds":	1.0000439882278442,
				"bytes":	209444166,
				"bits_per_second":	1675479626.620436,
				"packets":	149817,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	4.00094,
					"end":	5.000895,
					"seconds":	0.99995499849319458,
					"bytes":	209926476,
					"bits_per_second":	1679487387.4630966,
					"packets":	150162,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	4.00094,
				"end":	5.000895,
				"seconds":	0.99995499849319458,
				"bytes":	209926476,
				"bits_per_second":	1679487387.4630966,
				"packets":	150162,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	5.000895,
					"end":	6.000901,
					"seconds":	1.0000059604644775,
					"bytes":	209722368,
					"bits_per_second":	1677768943.7178094,
					"packets":	150016,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	5.000895,
				"end":	6.000901,
				"seconds":	1.0000059604644775,
				"bytes":	209722368,
				"bits_per_second":	1677768943.7178094,
				"packets":	150016,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	6.000901,
					"end":	7.00106,
					"seconds":	1.0001590251922607,
					"bytes":	210111012,
					"bits_per_second":	1680620834.9486048,
					"packets":	150294,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	6.000901,
				"end":	7.00106,
				"seconds":	1.0001590251922607,
				"bytes":	210111012,
				"bits_per_second":	1680620834.9486048,
				"packets":	150294,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	7.00106,
					"end":	8.002562,
					"seconds":	1.00150203704834,
					"bytes":	194117892,
					"bits_per_second":	1550614056.2398512,
					"packets":	138854,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	7.00106,
				"end":	8.002562,
				"seconds":	1.00150203704834,
				"bytes":	194117892,
				"bits_per_second":	1550614056.2398512,
				"packets":	138854,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	8.002562,
					"end":	9.000903,
					"seconds":	0.99834102392196655,
					"bytes":	201117678,
					"bits_per_second":	1611615054.82295,
					"packets":	143861,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	8.002562,
				"end":	9.000903,
				"seconds":	0.99834102392196655,
				"bytes":	201117678,
				"bits_per_second":	1611615054.82295,
				"packets":	143861,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	9.000903,
					"end":	10.001061,
					"seconds":	1.0001579523086548,
					"bytes":	210967986,
					"bits_per_second":	1687477347.05723,
					"packets":	150908,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	9.000903,
				"end":	10.001061,
				"seconds":	1.0001579523086548,
				"bytes":	210967986,
				"bits_per_second":	1687477347.05723,
				"packets":	150908,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	10.001061,
					"end":	11.000892,
					"seconds":	0.99983102083206177,
					"bytes":	203271996,
					"bits_per_second":	1626450804.3036036,
					"packets":	145403,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	10.001061,
				"end":	11.000892,
				"seconds":	0.99983102083206177,
				"bytes":	203271996,
				"bits_per_second":	1626450804.3036036,
				"packets":	145403,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	11.000892,
					"end":	12.000888,
					"seconds":	0.9999960064888,
					"bytes":	212180052,
					"bits_per_second":	1697447194.7743835,
					"packets":	151774,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	11.000892,
				"end":	12.000888,
				"seconds":	0.9999960064888,
				"bytes":	212180052,
				"bits_per_second":	1697447194.7743835,
				"packets":	151774,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	12.000888,
					"end":	13.001252,
					"seconds":	1.0003639459609985,
					"bytes":	209929272,
					"bits_per_second":	1678823175.0861967,
					"packets":	150164,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	12.000888,
				"end":	13.001252,
				"seconds":	1.0003639459609985,
				"bytes":	209929272,
				"bits_per_second":	1678823175.0861967,
				"packets":	150164,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	13.001252,
					"end":	14.000905,
					"seconds":	0.99965298175811768,
					"bytes":	211246188,
					"bits_per_second":	1690556157.8256919,
					"packets":	151107,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	13.001252,
				"end":	14.000905,
				"seconds":	0.99965298175811768,
				"bytes":	211246188,
				"bits_per_second":	1690556157.8256919,
				"packets":	151107,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	14.000905,
					"end":	15.000898,
					"seconds":	0.99999302625656128,
					"bytes":	213150264,
					"bits_per_second":	1705214003.72497,
					"packets":	152468,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	14.000905,
				"end":	15.000898,
				"seconds":	0.99999302625656128,
				"bytes":	213150264,
				"bits_per_second":	1705214003.72497,
				"packets":	152468,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	15.000898,
					"end":	16.0009,
					"seconds":	1.0000020265579224,
					"bytes":	209409216,
					"bits_per_second":	1675270332.9676347,
					"packets":	149792,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	15.000898,
				"end":	16.0009,
				"seconds":	1.0000020265579224,
				"bytes":	209409216,
				"bits_per_second":	1675270332.9676347,
				"packets":	149792,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	16.0009,
					"end":	17.000044,
					"seconds":	0.99914401769638062,
					"bytes":	210018744,
					"bits_per_second":	1681589362.7364571,
					"packets":	150228,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	16.0009,
				"end":	17.000044,
				"seconds":	0.99914401769638062,
				"bytes":	210018744,
				"bits_per_second":	1681589362.7364571,
				"packets":	150228,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	17.000044,
					"end":	18.002956,
					"seconds":	1.0029120445251465,
					"bytes":	216889914,
					"bits_per_second":	1730081238.4016538,
					"packets":	155145,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	17.000044,
				"end":	18.002956,
				"seconds":	1.0029120445251465,
				"bytes":	216889914,
				"bits_per_second":	1730081238.4016538,
				"packets":	155145,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	18.002956,
					"end":	19.000892,
					"seconds":	0.99793601036071777,
					"bytes":	213770976,
					"bits_per_second":	1713704877.1111448,
					"packets":	152912,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	18.002956,
				"end":	19.000892,
				"seconds":	0.99793601036071777,
				"bytes":	213770976,
				"bits_per_second":	1713704877.1111448,
				"packets":	152912,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	19.000892,
					"end":	20.001315,
					"seconds":	1.0004229545593262,
					"bytes":	213994656,
					"bits_per_second":	1711233474.0001,
					"packets":	153072,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	19.000892,
				"end":	20.001315,
				"seconds":	1.0004229545593262,
				"bytes":	213994656,
				"bits_per_second":	1711233474.0001,
				"packets":	153072,
				"omitted":	false,
				"sender":	true
			}
		}],
	"end":	{
		"streams":	[{
				"udp":	{
					"socket":	5,
					"start":	0,
					"end":	20.001315,
					"seconds":	20.001315,
					"bytes":	4168780080,
					"bits_per_second":	1667402400.2921805,
					"jitter_ms":	0.05129019881009296,
					"lost_packets":	2744190,
					"packets":	2981960,
					"lost_percent":	92.0263853304538,
					"out_of_order":	0,
					"sender":	true
				}
			}],
		"sum":	{
			"start":	0,
			"end":	20.20963,
			"seconds":	20.20963,
			"bytes":	4168780080,
			"bits_per_second":	1667402400.2921805,
			"jitter_ms":	0.05129019881009296,
			"lost_packets":	2744190,
			"packets":	2981960,
			"lost_percent":	92.0263853304538,
			"sender":	true
		},
		"sum_sent":	{
			"start":	0,
			"end":	20.001315,
			"seconds":	20.001315,
			"bytes":	4168780080,
			"bits_per_second":	1667402400.2921805,
			"jitter_ms":	0,
			"lost_packets":	0,
			"packets":	2981960,
			"lost_percent":	0,
			"sender":	true
		},
		"sum_received":	{
			"start":	0,
			"end":	20.20963,
			"seconds":	20.20963,
			"bytes":	332398266,
			"bits_per_second":	131580149.06754848,
			"jitter_ms":	0.05129019881009296,
			"lost_packets":	2744190,
			"packets":	2981957,
			"lost_percent":	92.0263853304538,
			"sender":	false
		},
		"cpu_utilization_percent":	{
			"host_total":	97.526399221082556,
			"host_user":	8.70828475139437,
			"host_system":	88.818104471261449,
			"remote_total":	27.664934557012661,
			"remote_user":	4.7594931372395726,
			"remote_system":	22.90544636790381
		}
	}
}
"""

throughput_sample2 = """
{
	"start":	{
		"connected":	[{
				"socket":	5,
				"local_host":	"10.18.5.195",
				"local_port":	34976,
				"remote_host":	"10.30.0.1",
				"remote_port":	5201
			}],
		"version":	"iperf 3.16",
		"system_info":	"Linux instance-0 6.5.0-1024-azure #25~22.04.1-Ubuntu SMP Mon Jun 17 18:38:57 UTC 2024 x86_64",
		"timestamp":	{
			"time":	"Sun, 21 Jul 2024 13:30:52 GMT",
			"timesecs":	1721568652
		},
		"connecting_to":	{
			"host":	"10.30.0.1",
			"port":	5201
		},
		"cookie":	"amyhzi4wokkmf5mm4axi7267uztshn327viv",
		"target_bitrate":	0,
		"fq_rate":	0,
		"sock_bufsize":	0,
		"sndbuf_actual":	212992,
		"rcvbuf_actual":	212992,
		"test_start":	{
			"protocol":	"UDP",
			"num_streams":	1,
			"blksize":	1398,
			"omit":	0,
			"duration":	20,
			"bytes":	0,
			"blocks":	0,
			"reverse":	0,
			"tos":	0,
			"target_bitrate":	0,
			"bidir":	0,
			"fqrate":	0
		}
	},
	"intervals":	[{
			"streams":	[{
					"socket":	5,
					"start":	0,
					"end":	1.000888,
					"seconds":	1.0008879899978638,
					"bytes":	206857866,
					"bits_per_second":	1653394730.0172241,
					"packets":	147968,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	0,
				"end":	1.000888,
				"seconds":	1.0008879899978638,
				"bytes":	206857866,
				"bits_per_second":	1653394730.0172241,
				"packets":	147968,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	1.000888,
					"end":	2.000903,
					"seconds":	1.0000150203704834,
					"bytes":	205294902,
					"bits_per_second":	1642334547.5266385,
					"packets":	146849,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	1.000888,
				"end":	2.000903,
				"seconds":	1.0000150203704834,
				"bytes":	205294902,
				"bits_per_second":	1642334547.5266385,
				"packets":	146849,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	2.000903,
					"end":	3.000896,
					"seconds":	0.99999302625656128,
					"bytes":	197350068,
					"bits_per_second":	1578811554.2267172,
					"packets":	141166,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	2.000903,
				"end":	3.000896,
				"seconds":	0.99999302625656128,
				"bytes":	197350068,
				"bits_per_second":	1578811554.2267172,
				"packets":	141166,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	3.000896,
					"end":	4.00094,
					"seconds":	1.0000439882278442,
					"bytes":	209444166,
					"bits_per_second":	1675479626.620436,
					"packets":	149817,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	3.000896,
				"end":	4.00094,
				"seconds":	1.0000439882278442,
				"bytes":	209444166,
				"bits_per_second":	1675479626.620436,
				"packets":	149817,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	4.00094,
					"end":	5.000895,
					"seconds":	0.99995499849319458,
					"bytes":	209926476,
					"bits_per_second":	1679487387.4630966,
					"packets":	150162,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	4.00094,
				"end":	5.000895,
				"seconds":	0.99995499849319458,
				"bytes":	209926476,
				"bits_per_second":	1679487387.4630966,
				"packets":	150162,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	5.000895,
					"end":	6.000901,
					"seconds":	1.0000059604644775,
					"bytes":	209722368,
					"bits_per_second":	1677768943.7178094,
					"packets":	150016,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	5.000895,
				"end":	6.000901,
				"seconds":	1.0000059604644775,
				"bytes":	209722368,
				"bits_per_second":	1677768943.7178094,
				"packets":	150016,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	6.000901,
					"end":	7.00106,
					"seconds":	1.0001590251922607,
					"bytes":	210111012,
					"bits_per_second":	1680620834.9486048,
					"packets":	150294,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	6.000901,
				"end":	7.00106,
				"seconds":	1.0001590251922607,
				"bytes":	210111012,
				"bits_per_second":	1680620834.9486048,
				"packets":	150294,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	7.00106,
					"end":	8.002562,
					"seconds":	1.00150203704834,
					"bytes":	194117892,
					"bits_per_second":	1550614056.2398512,
					"packets":	138854,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	7.00106,
				"end":	8.002562,
				"seconds":	1.00150203704834,
				"bytes":	194117892,
				"bits_per_second":	1550614056.2398512,
				"packets":	138854,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	8.002562,
					"end":	9.000903,
					"seconds":	0.99834102392196655,
					"bytes":	201117678,
					"bits_per_second":	1611615054.82295,
					"packets":	143861,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	8.002562,
				"end":	9.000903,
				"seconds":	0.99834102392196655,
				"bytes":	201117678,
				"bits_per_second":	1611615054.82295,
				"packets":	143861,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	9.000903,
					"end":	10.001061,
					"seconds":	1.0001579523086548,
					"bytes":	210967986,
					"bits_per_second":	1687477347.05723,
					"packets":	150908,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	9.000903,
				"end":	10.001061,
				"seconds":	1.0001579523086548,
				"bytes":	210967986,
				"bits_per_second":	1687477347.05723,
				"packets":	150908,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	10.001061,
					"end":	11.000892,
					"seconds":	0.99983102083206177,
					"bytes":	203271996,
					"bits_per_second":	1626450804.3036036,
					"packets":	145403,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	10.001061,
				"end":	11.000892,
				"seconds":	0.99983102083206177,
				"bytes":	203271996,
				"bits_per_second":	1626450804.3036036,
				"packets":	145403,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	11.000892,
					"end":	12.000888,
					"seconds":	0.9999960064888,
					"bytes":	212180052,
					"bits_per_second":	1697447194.7743835,
					"packets":	151774,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	11.000892,
				"end":	12.000888,
				"seconds":	0.9999960064888,
				"bytes":	212180052,
				"bits_per_second":	1697447194.7743835,
				"packets":	151774,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	12.000888,
					"end":	13.001252,
					"seconds":	1.0003639459609985,
					"bytes":	209929272,
					"bits_per_second":	1678823175.0861967,
					"packets":	150164,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	12.000888,
				"end":	13.001252,
				"seconds":	1.0003639459609985,
				"bytes":	209929272,
				"bits_per_second":	1678823175.0861967,
				"packets":	150164,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	13.001252,
					"end":	14.000905,
					"seconds":	0.99965298175811768,
					"bytes":	211246188,
					"bits_per_second":	1690556157.8256919,
					"packets":	151107,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	13.001252,
				"end":	14.000905,
				"seconds":	0.99965298175811768,
				"bytes":	211246188,
				"bits_per_second":	1690556157.8256919,
				"packets":	151107,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	14.000905,
					"end":	15.000898,
					"seconds":	0.99999302625656128,
					"bytes":	213150264,
					"bits_per_second":	1705214003.72497,
					"packets":	152468,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	14.000905,
				"end":	15.000898,
				"seconds":	0.99999302625656128,
				"bytes":	213150264,
				"bits_per_second":	1705214003.72497,
				"packets":	152468,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	15.000898,
					"end":	16.0009,
					"seconds":	1.0000020265579224,
					"bytes":	209409216,
					"bits_per_second":	1675270332.9676347,
					"packets":	149792,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	15.000898,
				"end":	16.0009,
				"seconds":	1.0000020265579224,
				"bytes":	209409216,
				"bits_per_second":	1675270332.9676347,
				"packets":	149792,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	16.0009,
					"end":	17.000044,
					"seconds":	0.99914401769638062,
					"bytes":	210018744,
					"bits_per_second":	1681589362.7364571,
					"packets":	150228,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	16.0009,
				"end":	17.000044,
				"seconds":	0.99914401769638062,
				"bytes":	210018744,
				"bits_per_second":	1681589362.7364571,
				"packets":	150228,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	17.000044,
					"end":	18.002956,
					"seconds":	1.0029120445251465,
					"bytes":	216889914,
					"bits_per_second":	1730081238.4016538,
					"packets":	155145,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	17.000044,
				"end":	18.002956,
				"seconds":	1.0029120445251465,
				"bytes":	216889914,
				"bits_per_second":	1730081238.4016538,
				"packets":	155145,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	18.002956,
					"end":	19.000892,
					"seconds":	0.99793601036071777,
					"bytes":	213770976,
					"bits_per_second":	1713704877.1111448,
					"packets":	152912,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	18.002956,
				"end":	19.000892,
				"seconds":	0.99793601036071777,
				"bytes":	213770976,
				"bits_per_second":	1713704877.1111448,
				"packets":	152912,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	19.000892,
					"end":	20.001315,
					"seconds":	1.0004229545593262,
					"bytes":	213994656,
					"bits_per_second":	1711233474.0001,
					"packets":	153072,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	19.000892,
				"end":	20.001315,
				"seconds":	1.0004229545593262,
				"bytes":	213994656,
				"bits_per_second":	1711233474.0001,
				"packets":	153072,
				"omitted":	false,
				"sender":	true
			}
		}],
	"end":	{
		"streams":	[{
				"udp":	{
					"socket":	5,
					"start":	0,
					"end":	20.001315,
					"seconds":	20.001315,
					"bytes":	4168780080,
					"bits_per_second":	1667402400.2921805,
					"jitter_ms":	0.05129019881009296,
					"lost_packets":	2744190,
					"packets":	2981960,
					"lost_percent":	92.0263853304538,
					"out_of_order":	0,
					"sender":	true
				}
			}],
		"sum":	{
			"start":	0,
			"end":	20.20963,
			"seconds":	20.20963,
			"bytes":	4168780080,
			"bits_per_second":	1667402400.2921805,
			"jitter_ms":	0.05129019881009296,
			"lost_packets":	2744190,
			"packets":	2981960,
			"lost_percent":	92.0263853304538,
			"sender":	true
		},
		"sum_sent":	{
			"start":	0,
			"end":	20.001315,
			"seconds":	20.001315,
			"bytes":	4168780080,
			"bits_per_second":	1667402400.2921805,
			"jitter_ms":	0,
			"lost_packets":	0,
			"packets":	2981960,
			"lost_percent":	0,
			"sender":	true
		},
		"sum_received":	{
			"start":	0,
			"end":	20.20963,
			"seconds":	20.20963,
			"bytes":	332398266,
			"bits_per_second":	131580149.06754848,
			"jitter_ms":	0.05129019881009296,
			"lost_packets":	2744190,
			"packets":	2981957,
			"lost_percent":	92.0263853304538,
			"sender":	false
		},
		"cpu_utilization_percent":	{
			"host_total":	97.526399221082556,
			"host_user":	8.70828475139437,
			"host_system":	88.818104471261449,
			"remote_total":	27.664934557012661,
			"remote_user":	4.7594931372395726,
			"remote_system":	22.90544636790381
		}
	}
}
"""

jitter_sample1 = """
{
	"start":	{
		"connected":	[{
				"socket":	5,
				"local_host":	"10.18.2.195",
				"local_port":	53207,
				"remote_host":	"10.30.0.1",
				"remote_port":	5201
			}],
		"version":	"iperf 3.16",
		"system_info":	"Linux instance-0 6.5.0-1024-azure #25~22.04.1-Ubuntu SMP Mon Jun 17 18:38:57 UTC 2024 x86_64",
		"timestamp":	{
			"time":	"Thu, 18 Jul 2024 13:29:34 GMT",
			"timesecs":	1721309374
		},
		"connecting_to":	{
			"host":	"10.30.0.1",
			"port":	5201
		},
		"cookie":	"sox7x6agugsigbyhz4nrxd7ccnziaayr644m",
		"target_bitrate":	1000000,
		"fq_rate":	0,
		"sock_bufsize":	0,
		"sndbuf_actual":	212992,
		"rcvbuf_actual":	212992,
		"test_start":	{
			"protocol":	"UDP",
			"num_streams":	1,
			"blksize":	1398,
			"omit":	0,
			"duration":	20,
			"bytes":	0,
			"blocks":	0,
			"reverse":	0,
			"tos":	0,
			"target_bitrate":	1000000,
			"bidir":	0,
			"fqrate":	0
		}
	},
	"intervals":	[{
			"streams":	[{
					"socket":	5,
					"start":	0,
					"end":	1.000071,
					"seconds":	1.0000710487365723,
					"bytes":	125820,
					"bits_per_second":	1006488.4902643922,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	0,
				"end":	1.000071,
				"seconds":	1.0000710487365723,
				"bytes":	125820,
				"bits_per_second":	1006488.4902643922,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	1.000071,
					"end":	2.000066,
					"seconds":	0.999994993209839,
					"bytes":	124422,
					"bits_per_second":	995380.98366371554,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	1.000071,
				"end":	2.000066,
				"seconds":	0.999994993209839,
				"bytes":	124422,
				"bits_per_second":	995380.98366371554,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	2.000066,
					"end":	3.000045,
					"seconds":	0.999979019165039,
					"bytes":	125820,
					"bits_per_second":	1006581.1189123307,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	2.000066,
				"end":	3.000045,
				"seconds":	0.999979019165039,
				"bytes":	125820,
				"bits_per_second":	1006581.1189123307,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	3.000045,
					"end":	4.000067,
					"seconds":	1.0000220537185669,
					"bytes":	124422,
					"bits_per_second":	995354.04874193459,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	3.000045,
				"end":	4.000067,
				"seconds":	1.0000220537185669,
				"bytes":	124422,
				"bits_per_second":	995354.04874193459,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	4.000067,
					"end":	5.000074,
					"seconds":	1.0000070333480835,
					"bytes":	124422,
					"bits_per_second":	995368.999223357,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	4.000067,
				"end":	5.000074,
				"seconds":	1.0000070333480835,
				"bytes":	124422,
				"bits_per_second":	995368.999223357,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	5.000074,
					"end":	6.000071,
					"seconds":	0.99999701976776123,
					"bytes":	125820,
					"bits_per_second":	1006562.9997915024,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	5.000074,
				"end":	6.000071,
				"seconds":	0.99999701976776123,
				"bytes":	125820,
				"bits_per_second":	1006562.9997915024,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	6.000071,
					"end":	7.000071,
					"seconds":	1,
					"bytes":	124422,
					"bits_per_second":	995376,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	6.000071,
				"end":	7.000071,
				"seconds":	1,
				"bytes":	124422,
				"bits_per_second":	995376,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	7.000071,
					"end":	8.000065,
					"seconds":	0.99999397993087769,
					"bytes":	125820,
					"bits_per_second":	1006566.059597255,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	7.000071,
				"end":	8.000065,
				"seconds":	0.99999397993087769,
				"bytes":	125820,
				"bits_per_second":	1006566.059597255,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	8.000065,
					"end":	9.000065,
					"seconds":	1,
					"bytes":	124422,
					"bits_per_second":	995376,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	8.000065,
				"end":	9.000065,
				"seconds":	1,
				"bytes":	124422,
				"bits_per_second":	995376,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	9.000065,
					"end":	10.000046,
					"seconds":	0.99998098611831665,
					"bytes":	125820,
					"bits_per_second":	1006579.1389766535,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	9.000065,
				"end":	10.000046,
				"seconds":	0.99998098611831665,
				"bytes":	125820,
				"bits_per_second":	1006579.1389766535,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	10.000046,
					"end":	11.000063,
					"seconds":	1.0000170469284058,
					"bytes":	124422,
					"bits_per_second":	995359.0321858403,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	10.000046,
				"end":	11.000063,
				"seconds":	1.0000170469284058,
				"bytes":	124422,
				"bits_per_second":	995359.0321858403,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	11.000063,
					"end":	12.000071,
					"seconds":	1.0000079870224,
					"bytes":	124422,
					"bits_per_second":	995368.04997308867,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	11.000063,
				"end":	12.000071,
				"seconds":	1.0000079870224,
				"bytes":	124422,
				"bits_per_second":	995368.04997308867,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	12.000071,
					"end":	13.000073,
					"seconds":	1.0000020265579224,
					"bytes":	125820,
					"bits_per_second":	1006557.9601519916,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	12.000071,
				"end":	13.000073,
				"seconds":	1.0000020265579224,
				"bytes":	125820,
				"bits_per_second":	1006557.9601519916,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	13.000073,
					"end":	14.000069,
					"seconds":	0.9999960064888,
					"bytes":	124422,
					"bits_per_second":	995379.97506107856,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	13.000073,
				"end":	14.000069,
				"seconds":	0.9999960064888,
				"bytes":	124422,
				"bits_per_second":	995379.97506107856,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	14.000069,
					"end":	15.000065,
					"seconds":	0.9999960064888,
					"bytes":	125820,
					"bits_per_second":	1006564.0197246863,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	14.000069,
				"end":	15.000065,
				"seconds":	0.9999960064888,
				"bytes":	125820,
				"bits_per_second":	1006564.0197246863,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	15.000065,
					"end":	16.000066,
					"seconds":	1.0000009536743164,
					"bytes":	124422,
					"bits_per_second":	995375.050736379,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	15.000065,
				"end":	16.000066,
				"seconds":	1.0000009536743164,
				"bytes":	124422,
				"bits_per_second":	995375.050736379,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	16.000066,
					"end":	17.000065,
					"seconds":	0.99999898672103882,
					"bytes":	124422,
					"bits_per_second":	995377.00859458128,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	16.000066,
				"end":	17.000065,
				"seconds":	0.99999898672103882,
				"bytes":	124422,
				"bits_per_second":	995377.00859458128,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	17.000065,
					"end":	18.000066,
					"seconds":	1.0000009536743164,
					"bytes":	125820,
					"bits_per_second":	1006559.0400704956,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	17.000065,
				"end":	18.000066,
				"seconds":	1.0000009536743164,
				"bytes":	125820,
				"bits_per_second":	1006559.0400704956,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	18.000066,
					"end":	19.000066,
					"seconds":	1,
					"bytes":	124422,
					"bits_per_second":	995376,
					"packets":	89,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	18.000066,
				"end":	19.000066,
				"seconds":	1,
				"bytes":	124422,
				"bits_per_second":	995376,
				"packets":	89,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	19.000066,
					"end":	20.000319,
					"seconds":	1.0002529621124268,
					"bytes":	125820,
					"bits_per_second":	1006305.4428494303,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	19.000066,
				"end":	20.000319,
				"seconds":	1.0002529621124268,
				"bytes":	125820,
				"bits_per_second":	1006305.4428494303,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}],
	"end":	{
		"streams":	[{
				"udp":	{
					"socket":	5,
					"start":	0,
					"end":	20.000319,
					"seconds":	20.000319,
					"bytes":	2501022,
					"bits_per_second":	1000392.8437341424,
					"jitter_ms":	0.05150706013209632,
					"lost_packets":	0,
					"packets":	1789,
					"lost_percent":	0,
					"out_of_order":	0,
					"sender":	true
				}
			}],
		"sum":	{
			"start":	0,
			"end":	20.000809,
			"seconds":	20.000809,
			"bytes":	2501022,
			"bits_per_second":	1000392.8437341424,
			"jitter_ms":	0.05150706013209632,
			"lost_packets":	0,
			"packets":	1789,
			"lost_percent":	0,
			"sender":	true
		},
		"sum_sent":	{
			"start":	0,
			"end":	20.000319,
			"seconds":	20.000319,
			"bytes":	2501022,
			"bits_per_second":	1000392.8437341424,
			"jitter_ms":	0,
			"lost_packets":	0,
			"packets":	1789,
			"lost_percent":	0,
			"sender":	true
		},
		"sum_received":	{
			"start":	0,
			"end":	20.000809,
			"seconds":	20.000809,
			"bytes":	2501022,
			"bits_per_second":	1000368.3351008452,
			"jitter_ms":	0.05150706013209632,
			"lost_packets":	0,
			"packets":	1789,
			"lost_percent":	0,
			"sender":	false
		},
		"cpu_utilization_percent":	{
			"host_total":	100.84258832639009,
			"host_user":	100.80219772088796,
			"host_system":	0.040385606046062186,
			"remote_total":	0.359769871676896,
			"remote_user":	0.0967059335154957,
			"remote_system":	0.26305893837164146
		}
	}
}
"""

parse_throughput_samples([throughput_sample1, throughput_sample2],"test")
