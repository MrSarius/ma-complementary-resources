from Parser import parse_throughput_samples, parse_jitter_samples, parse_latency_samples

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
				"local_host":	"10.0.0.6",
				"local_port":	36770,
				"remote_host":	"45.147.210.189",
				"remote_port":	5201
			}],
		"version":	"iperf 3.9",
		"system_info":	"Linux main2 6.5.0-1024-azure #25~22.04.1-Ubuntu SMP Mon Jun 17 18:38:57 UTC 2024 x86_64",
		"timestamp":	{
			"time":	"Mon, 22 Jul 2024 03:23:00 GMT",
			"timesecs":	1721618580
		},
		"connecting_to":	{
			"host":	"iperf3.moji.fr",
			"port":	5201
		},
		"cookie":	"r6mtrbq7mjelcy2iu2lsp5gcs6qodzijfx7m",
		"sock_bufsize":	0,
		"sndbuf_actual":	212992,
		"rcvbuf_actual":	212992,
		"test_start":	{
			"protocol":	"UDP",
			"num_streams":	1,
			"blksize":	1448,
			"omit":	0,
			"duration":	10,
			"bytes":	0,
			"blocks":	0,
			"reverse":	0,
			"tos":	0
		}
	},
	"intervals":	[{
			"streams":	[{
					"socket":	5,
					"start":	0,
					"end":	1.000085,
					"seconds":	1.00008499622345,
					"bytes":	131768,
					"bits_per_second":	1054054.4093558942,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	0,
				"end":	1.000085,
				"seconds":	1.00008499622345,
				"bytes":	131768,
				"bits_per_second":	1054054.4093558942,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	1.000085,
					"end":	2.000083,
					"seconds":	0.99999797344207764,
					"bytes":	130320,
					"bits_per_second":	1042562.1128125093,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	1.000085,
				"end":	2.000083,
				"seconds":	0.99999797344207764,
				"bytes":	130320,
				"bits_per_second":	1042562.1128125093,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	2.000083,
					"end":	3.000085,
					"seconds":	1.0000020265579224,
					"bytes":	131768,
					"bits_per_second":	1054141.8637204547,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	2.000083,
				"end":	3.000085,
				"seconds":	1.0000020265579224,
				"bytes":	131768,
				"bits_per_second":	1054141.8637204547,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	3.000085,
					"end":	4.000102,
					"seconds":	1.0000170469284058,
					"bytes":	130320,
					"bits_per_second":	1042542.2278572817,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	3.000085,
				"end":	4.000102,
				"seconds":	1.0000170469284058,
				"bytes":	130320,
				"bits_per_second":	1042542.2278572817,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	4.000102,
					"end":	5.000087,
					"seconds":	0.9999849796295166,
					"bytes":	131768,
					"bits_per_second":	1054159.8338712535,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	4.000102,
				"end":	5.000087,
				"seconds":	0.9999849796295166,
				"bytes":	131768,
				"bits_per_second":	1054159.8338712535,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	5.000087,
					"end":	6.000074,
					"seconds":	0.999987006187439,
					"bytes":	131768,
					"bits_per_second":	1054157.6975275315,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	5.000087,
				"end":	6.000074,
				"seconds":	0.999987006187439,
				"bytes":	131768,
				"bits_per_second":	1054157.6975275315,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	6.000074,
					"end":	7.000614,
					"seconds":	1.000540018081665,
					"bytes":	130320,
					"bits_per_second":	1041997.3026155414,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	6.000074,
				"end":	7.000614,
				"seconds":	1.000540018081665,
				"bytes":	130320,
				"bits_per_second":	1041997.3026155414,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	7.000614,
					"end":	8.000076,
					"seconds":	0.99946200847625732,
					"bytes":	131768,
					"bits_per_second":	1054711.4258070788,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	7.000614,
				"end":	8.000076,
				"seconds":	0.99946200847625732,
				"bytes":	131768,
				"bits_per_second":	1054711.4258070788,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	8.000076,
					"end":	9.000074,
					"seconds":	0.99999797344207764,
					"bytes":	130320,
					"bits_per_second":	1042562.1128125093,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	8.000076,
				"end":	9.000074,
				"seconds":	0.99999797344207764,
				"bytes":	130320,
				"bits_per_second":	1042562.1128125093,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	9.000074,
					"end":	10.000084,
					"seconds":	1.0000100135803223,
					"bytes":	131768,
					"bits_per_second":	1054133.4443500845,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	9.000074,
				"end":	10.000084,
				"seconds":	1.0000100135803223,
				"bytes":	131768,
				"bits_per_second":	1054133.4443500845,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}],
	"end":	{
		"streams":	[{
				"udp":	{
					"socket":	5,
					"start":	0,
					"end":	10.000084,
					"seconds":	10.000084,
					"bytes":	1311888,
					"bits_per_second":	1049501.584186693,
					"jitter_ms":	0.033234065012906613,
					"lost_packets":	0,
					"packets":	906,
					"lost_percent":	0,
					"out_of_order":	0,
					"sender":	true
				}
			}],
		"sum":	{
			"start":	0,
			"end":	10.01306,
			"seconds":	10.01306,
			"bytes":	1311888,
			"bits_per_second":	1049501.584186693,
			"jitter_ms":	0.033234065012906613,
			"lost_packets":	0,
			"packets":	906,
			"lost_percent":	0,
			"sender":	true
		},
		"cpu_utilization_percent":	{
			"host_total":	1.784229068570869,
			"host_user":	1.784229068570869,
			"host_system":	0,
			"remote_total":	0.30558060614776489,
			"remote_user":	0.030639953580670065,
			"remote_system":	0.27494065256709482
		}
	}
}

"""

jitter_sample2 = """
{
	"start":	{
		"connected":	[{
				"socket":	5,
				"local_host":	"10.0.0.6",
				"local_port":	38005,
				"remote_host":	"45.147.210.189",
				"remote_port":	5201
			}],
		"version":	"iperf 3.9",
		"system_info":	"Linux main2 6.5.0-1024-azure #25~22.04.1-Ubuntu SMP Mon Jun 17 18:38:57 UTC 2024 x86_64",
		"timestamp":	{
			"time":	"Mon, 22 Jul 2024 03:21:57 GMT",
			"timesecs":	1721618517
		},
		"connecting_to":	{
			"host":	"iperf3.moji.fr",
			"port":	5201
		},
		"cookie":	"cnc6thrvnuhxrjm7n4t7piz5lvtfq5ch6sum",
		"sock_bufsize":	0,
		"sndbuf_actual":	212992,
		"rcvbuf_actual":	212992,
		"test_start":	{
			"protocol":	"UDP",
			"num_streams":	1,
			"blksize":	1448,
			"omit":	0,
			"duration":	10,
			"bytes":	0,
			"blocks":	0,
			"reverse":	0,
			"tos":	0
		}
	},
	"intervals":	[{
			"streams":	[{
					"socket":	5,
					"start":	0,
					"end":	1.000079,
					"seconds":	1.0000790357589722,
					"bytes":	131768,
					"bits_per_second":	1054060.6915132436,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	0,
				"end":	1.000079,
				"seconds":	1.0000790357589722,
				"bytes":	131768,
				"bits_per_second":	1054060.6915132436,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	1.000079,
					"end":	2.000071,
					"seconds":	0.9999920129776,
					"bytes":	130320,
					"bits_per_second":	1042568.3270165813,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	1.000079,
				"end":	2.000071,
				"seconds":	0.9999920129776,
				"bytes":	130320,
				"bits_per_second":	1042568.3270165813,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	2.000071,
					"end":	3.000065,
					"seconds":	0.99999397993087769,
					"bytes":	131768,
					"bits_per_second":	1054150.3460579487,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	2.000071,
				"end":	3.000065,
				"seconds":	0.99999397993087769,
				"bytes":	131768,
				"bits_per_second":	1054150.3460579487,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	3.000065,
					"end":	4.000078,
					"seconds":	1.000012993812561,
					"bytes":	130320,
					"bits_per_second":	1042546.453346799,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	3.000065,
				"end":	4.000078,
				"seconds":	1.000012993812561,
				"bytes":	130320,
				"bits_per_second":	1042546.453346799,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	4.000078,
					"end":	5.00007,
					"seconds":	0.9999920129776,
					"bytes":	131768,
					"bits_per_second":	1054152.4195389878,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	4.000078,
				"end":	5.00007,
				"seconds":	0.9999920129776,
				"bytes":	131768,
				"bits_per_second":	1054152.4195389878,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	5.00007,
					"end":	6.000067,
					"seconds":	0.99999701976776123,
					"bytes":	131768,
					"bits_per_second":	1054147.1416032959,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	5.00007,
				"end":	6.000067,
				"seconds":	0.99999701976776123,
				"bytes":	131768,
				"bits_per_second":	1054147.1416032959,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	6.000067,
					"end":	7.000076,
					"seconds":	1.0000089406967163,
					"bytes":	130320,
					"bits_per_second":	1042550.6788705689,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	6.000067,
				"end":	7.000076,
				"seconds":	1.0000089406967163,
				"bytes":	130320,
				"bits_per_second":	1042550.6788705689,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	7.000076,
					"end":	8.000082,
					"seconds":	1.0000059604644775,
					"bytes":	131768,
					"bits_per_second":	1054137.7168495844,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	7.000076,
				"end":	8.000082,
				"seconds":	1.0000059604644775,
				"bytes":	131768,
				"bits_per_second":	1054137.7168495844,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	8.000082,
					"end":	9.000074,
					"seconds":	0.9999920129776,
					"bytes":	130320,
					"bits_per_second":	1042568.3270165813,
					"packets":	90,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	8.000082,
				"end":	9.000074,
				"seconds":	0.9999920129776,
				"bytes":	130320,
				"bits_per_second":	1042568.3270165813,
				"packets":	90,
				"omitted":	false,
				"sender":	true
			}
		}, {
			"streams":	[{
					"socket":	5,
					"start":	9.000074,
					"end":	10.000096,
					"seconds":	1.0000220537185669,
					"bytes":	131768,
					"bits_per_second":	1054120.7527175841,
					"packets":	91,
					"omitted":	false,
					"sender":	true
				}],
			"sum":	{
				"start":	9.000074,
				"end":	10.000096,
				"seconds":	1.0000220537185669,
				"bytes":	131768,
				"bits_per_second":	1054120.7527175841,
				"packets":	91,
				"omitted":	false,
				"sender":	true
			}
		}],
	"end":	{
		"streams":	[{
				"udp":	{
					"socket":	5,
					"start":	0,
					"end":	10.000096,
					"seconds":	10.000096,
					"bytes":	1311888,
					"bits_per_second":	1049500.324796882,
					"jitter_ms":	0.0356716434871972,
					"lost_packets":	0,
					"packets":	906,
					"lost_percent":	0,
					"out_of_order":	0,
					"sender":	true
				}
			}],
		"sum":	{
			"start":	0,
			"end":	10.013031,
			"seconds":	10.013031,
			"bytes":	1311888,
			"bits_per_second":	1049500.324796882,
			"jitter_ms":	0.0356716434871972,
			"lost_packets":	0,
			"packets":	906,
			"lost_percent":	0,
			"sender":	true
		},
		"cpu_utilization_percent":	{
			"host_total":	1.8392408491101833,
			"host_user":	0.31105012399810539,
			"host_system":	1.5281907251120777,
			"remote_total":	0.28581718007031626,
			"remote_user":	0.02618584318614799,
			"remote_system":	0.25962134991117586
		}
	}
}

"""

latency_sample1 = """
HPING google.com (eth0 142.250.185.110): S set, 40 headers + 0 data bytes
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=0 win=65535 rtt=3.7 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=1 win=65535 rtt=7.6 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=2 win=65535 rtt=7.5 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=3 win=65535 rtt=7.4 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=4 win=65535 rtt=3.3 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=5 win=65535 rtt=3.1 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=6 win=65535 rtt=3.0 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=7 win=65535 rtt=6.9 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=8 win=65535 rtt=2.8 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=9 win=65535 rtt=2.5 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=10 win=65535 rtt=2.4 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=11 win=65535 rtt=2.0 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=12 win=65535 rtt=5.9 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=13 win=65535 rtt=1.8 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=14 win=65535 rtt=7.9 ms

"""

latency_sample2 = """
HPING google.com (eth0 142.250.185.110): S set, 40 headers + 0 data bytes
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=0 win=65535 rtt=3.8 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=1 win=65535 rtt=3.7 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=2 win=65535 rtt=3.6 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=3 win=65535 rtt=7.5 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=4 win=65535 rtt=3.3 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=5 win=65535 rtt=7.3 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=6 win=65535 rtt=3.1 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=7 win=65535 rtt=3.1 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=8 win=65535 rtt=6.9 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=9 win=65535 rtt=6.6 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=10 win=65535 rtt=6.5 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=11 win=65535 rtt=2.4 ms
len=46 ip=142.250.185.110 ttl=120 DF id=0 sport=80 flags=SA seq=12 win=65535 rtt=10.4 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=13 win=65535 rtt=2.1 ms
len=46 ip=142.250.185.110 ttl=119 DF id=0 sport=80 flags=SA seq=14 win=65535 rtt=4.0 ms

"""

parse_throughput_samples([throughput_sample1, throughput_sample2],"throughput")
parse_throughput_samples([throughput_sample1, throughput_sample2],"throughput_ebpf")

parse_jitter_samples([jitter_sample1, jitter_sample2], "jitter")
parse_jitter_samples([jitter_sample1, jitter_sample2], "jitter_ebpf")

parse_latency_samples([latency_sample1, latency_sample2], "latency")
parse_latency_samples([latency_sample1, latency_sample2], "latency_jitter")
