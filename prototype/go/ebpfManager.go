package main

import (
	"ebpfManager/ebpf/firewall"
	"github.com/cilium/ebpf/rlimit"
	"github.com/gin-gonic/gin"
	"log"
	"net"
	"net/http"
)

//go:generate ./generate_ebpf.sh

type FirewallRequest struct {
	Proto   string `json:"proto"`
	SrcIp   string `json:"srcIp"`
	DstIp   string `json:"dstIp"`
	SrcPort uint16 `json:"scrPort"`
	DstPort uint16 `json:"dstPort"`
}

var fw = firewall.New()

func attachFirewall() {
	// Remove resource limits for kernels <5.11.
	if err := rlimit.RemoveMemlock(); err != nil {
		log.Fatal("Removing memlock:", err)
	}
	fw.Load()
	fw.AttachTC("veth-ns2")
}

func getFirewall(c *gin.Context) {
	c.JSON(http.StatusOK, "This return a JSON object representing the current firewall settings and status")
}

func postRule(c *gin.Context) {
	var request FirewallRequest
	if err := c.BindJSON(&request); err != nil {
		return
	}

	src := net.ParseIP(request.SrcIp).To4()
	dst := net.ParseIP(request.DstIp).To4()

	// TODO ben default is always TCP. Does that make sense? + can I add this parsing step to JSON serialiser?
	proto := firewall.TCP
	if request.Proto == "UDP" {
		proto = firewall.UDP
	} else if request.Proto == "ICMP" {
		proto = firewall.ICMP
	}

	err := fw.AddRule(src, dst, proto, request.SrcPort, request.DstPort)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "An error occurred."})
		return
	}

	c.Status(http.StatusOK)
}

func deleteRule(c *gin.Context) {
	var request FirewallRequest
	if err := c.BindJSON(&request); err != nil {
		return
	}
	src := net.ParseIP(request.SrcIp).To4()
	dst := net.ParseIP(request.DstIp).To4()

	// TODO ben default is always TCP. Does that make sense? + can I add this parsing step to JSON serialiser?
	proto := firewall.TCP
	if request.Proto == "UDP" {
		proto = firewall.UDP
	} else if request.Proto == "ICMP" {
		proto = firewall.ICMP
	}

	err := fw.DeleteRule(src, dst, proto, request.SrcPort, request.DstPort)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "An error occurred."})
		return
	}

	c.Status(http.StatusOK)
}

func main() {
	attachFirewall()
	defer fw.Close()

	router := gin.Default()

	router.POST("/firewall", postRule)

	// delete (and detach) firewall
	router.DELETE("/firewall/:id", deleteRule)

	// return all info about firewall
	router.GET("/firewall", getFirewall)

	err := router.Run("0.0.0.0:8081")

	if err != nil {
		return
	}
}

// TODO ben store for later
//func attachFirewall(c *gin.Context) {
//	var request FirewallRequest
//	if err := c.BindJSON(&request); err != nil {
//		return
//	}
//
//	networkNamespace := "ns1"
//	ifaceName := "veth-ns1-peer"
//	if request.Service == 2 {
//		networkNamespace = "ns2"
//		ifaceName = "veth-ns2-peer"
//	}
//	println(ifaceName)        // TODO ben remove
//	println(networkNamespace) // TODO ben remove

//originalNS, err := netns.Get()
//if err != nil {
//	log.Fatalf("failed to get current namespace: %v", err)
//}
//defer originalNS.Close()
//
//nsHandle, err := netns.GetFromName(networkNamespace)
//if err != nil {
//	log.Fatalf("failed to get network namespace handle: %v", err)
//}
//defer nsHandle.Close()
//
//err = netns.Set(nsHandle)
//if err != nil {
//	log.Fatalf("failed to set network namespace: %v", err)
//}
//defer netns.Set(originalNS) // Revert to the original namespace before exit.
//
//	fw := firewall.New()
//	fw.LoadAndAttach("br0")
//}
