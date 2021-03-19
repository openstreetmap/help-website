+++
type = "question"
title = "Need help in upgrading the code to analyze traffic"
description = '''Hello! Please help me deal with this problem. Need to analyze packets on a LAN in obtaining certain information to perform actions. Specifically, there is a computer network connected to it cisco ip phones and need to analyze packets SKINNY Protocol, which the phone communicates with the server. The...'''
date = "2011-01-08T10:28:00Z"
lastmod = "2011-01-08T13:24:00Z"
weight = 1684
keywords = [ "analyze", "pcap", "c++", "tcp" ]
aliases = [ "/questions/1684" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need help in upgrading the code to analyze traffic](/questions/1684/need-help-in-upgrading-the-code-to-analyze-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1684-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! Please help me deal with this problem. Need to analyze packets on a LAN in obtaining certain information to perform actions. Specifically, there is a computer network connected to it cisco ip phones and need to analyze packets SKINNY Protocol, which the phone communicates with the server. These packets arrive at port 2000 TCP protocol on the server. IP-address of the server such as 10.0.20.1, IP-address of the phone - 10.0.10.1, and the IP of the computer operator - 10.0.30.1. My program is on the operator's computer. The problem is that my program can see only those packets that come from the server to the operator and vice versa. Packets that the server sends the phone and back, for some reason I can not see. Simply put, I need to make the program contained on computer 1, saw the packets that come from the computer 2 to computer 3. All computers on the same network, but in different subnets. Here's the source code. #include "stdafx.h" #define HAVE_REMOTE #include "pcap.h" #include &lt;cstdlib&gt; #include &lt;iostream&gt; using namespace std;</p><pre><code>#pragma warning(push)
#pragma warning(disable:4035)
int Swap(int val)
{
    __asm mov eax,val;
    __asm bswap eax
}
#pragma warning(pop)

/* 4 bytes IP address */
typedef struct ip_address{
    u_char byte1;
    u_char byte2;
    u_char byte3;
    u_char byte4;
}ip_address;

/* IPv4 header */
typedef struct ip_header{
    u_char  ver_ihl;        // Version (4 bits) + Internet header length (4 bits)
    u_char  tos;            // Type of service 
    u_short tlen;           // Total length 
    u_short identification; // Identification
    u_short flags_fo;       // Flags (3 bits) + Fragment offset (13 bits)
    u_char  ttl;            // Time to live
    u_char  proto;          // Protocol
    u_short crc;            // Header checksum
    ip_address  saddr;      // Source address
    ip_address  daddr;      // Destination address
    u_int   op_pad;         // Option + Padding
}ip_header;

/* UDP header*/
typedef struct udp_header{
    u_short sport;          // Source port
    u_short dport;          // Destination port
    u_short len;            // Datagram length
    u_short crc;            // Checksum
}udp_header;

/* prototype of the packet handler */
void packet_handler(u_char *param, const struct pcap_pkthdr *header, const u_char *pkt_data);

int _tmain(int argc, _TCHAR* argv[])
{

pcap_if_t *alldevs;
pcap_if_t *d;
int inum;
int i=0;
pcap_t *adhandle;
char errbuf[PCAP_ERRBUF_SIZE];

    /* Retrieve the device list on the local machine */
    if (pcap_findalldevs_ex(PCAP_SRC_IF_STRING, NULL, &amp;alldevs, errbuf) == -1)
    {
        fprintf(stderr,&quot;Error in pcap_findalldevs: %s\n&quot;, errbuf);
        exit(1);
    }

    /* Print the list */
    for(d=alldevs; d; d=d-&gt;next)
    {
        printf(&quot;%d. %s&quot;, ++i, d-&gt;name);
        if (d-&gt;description)
            printf(&quot; (%s)\n&quot;, d-&gt;description);
        else
            printf(&quot; (No description available)\n&quot;);
    }

    if(i==0)
    {
        printf(&quot;\nNo interfaces found! Make sure WinPcap is installed.\n&quot;);
        return -1;
    }

    printf(&quot;Enter the interface number (1-%d):&quot;,i);
    scanf_s(&quot;%d&quot;, &amp;inum);

    if(inum &lt; 1 || inum &gt; i)
    {
        printf(&quot;\nInterface number out of range.\n&quot;);
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

    /* Jump to the selected adapter */
    for(d=alldevs, i=0; i&lt; inum-1 ;d=d-&gt;next, i++);

    /* Open the device */
    if ( (adhandle= pcap_open(d-&gt;name,          // name of the device
                              65536,            // portion of the packet to capture
                                                // 65536 guarantees that the whole packet will be captured on all the link layers
                              PCAP_OPENFLAG_PROMISCUOUS,    // promiscuous mode
                              1000,             // read timeout
                              NULL,             // authentication on the remote machine
                              errbuf            // error buffer
                              ) ) == NULL)
    {
        fprintf(stderr,&quot;\nUnable to open the adapter. %s is not supported by WinPcap\n&quot;, d-&gt;name);
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

    printf(&quot;\nlistening on %s...\n&quot;, d-&gt;description);

    long netmask;
    bpf_program fcode;

    //Filter packets
    if (d-&gt;addresses != NULL)
        /* Retrieve the mask of the first address of the interface */
        netmask=((struct sockaddr_in *)(d-&gt;addresses-&gt;netmask))-&gt;sin_addr.S_un.S_addr;
    else
        /* If the interface is without an address we suppose to be in a C class network */
        netmask=0xffffff;

    if (pcap_compile(adhandle, &amp;fcode, &quot;tcp port 2000&quot;, 1, netmask) &lt; 0)
    {
        fprintf(stderr,&quot;\nUnable to compile the packet filter. Check the syntax.\n&quot;);
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

    if (pcap_setfilter(adhandle, &amp;fcode) &lt; 0)
    {
        fprintf(stderr,&quot;\nError setting the filter.\n&quot;);
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

     /* At this point, we don&#39;t need any more the device list. Free it */
    pcap_freealldevs(alldevs);

    /* start the capture */
    pcap_loop(adhandle, 0, packet_handler, NULL);
    return 0;

}

/* Callback function invoked by libpcap for every incoming packet */
void packet_handler(u_char *param, const struct pcap_pkthdr *header, const u_char *pkt_data)
{
    struct tm ltime;
    char timestr[16];
    ip_header *ih;
    udp_header *uh;
    u_int ip_len;
    u_short sport,dport;
    time_t local_tv_sec;

    /*
     * Unused variable
     */
    (VOID)(param);

    /* convert the timestamp to readable format */
    local_tv_sec = header-&gt;ts.tv_sec;
    localtime_s(&amp;ltime, &amp;local_tv_sec);
    strftime( timestr, sizeof timestr, &quot;%H:%M:%S&quot;, &amp;ltime);

    printf(&quot;%s,%.6d len:%d\n&quot;, timestr, header-&gt;ts.tv_usec, header-&gt;len);

    /* retireve the position of the ip header */
    ih = (ip_header *) (pkt_data +
        14); //length of ethernet header

    /* retireve the position of the udp header */
    ip_len = (ih-&gt;ver_ihl &amp; 0xf) * 4;
    uh = (udp_header *) ((u_char*)ih + ip_len);

    /* convert from network byte order to host byte order */
    sport = Swap( uh-&gt;sport );
    dport = Swap( uh-&gt;dport );

    /* print ip addresses and udp ports */
    printf(&quot;%d.%d.%d.%d.%d -&gt; %d.%d.%d.%d.%d\n&quot;,
        ih-&gt;saddr.byte1,
        ih-&gt;saddr.byte2,
        ih-&gt;saddr.byte3,
        ih-&gt;saddr.byte4,
        sport,
        ih-&gt;daddr.byte1,
        ih-&gt;daddr.byte2,
        ih-&gt;daddr.byte3,
        ih-&gt;daddr.byte4,
        dport);

}</code></pre><p>Thanks for the help</p></div><div id="question-tags" class="tags-container tags">analyze pcap c++ tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '11, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/dd20d3abb5d78de1f6ac206f33946fc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="masterbloger&#39;s gravatar image" /><p>masterbloger<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="masterbloger has no accepted answers">0%</span></p></div></div><div id="comments-container-1684" class="comments-container"></div><div id="comment-tools-1684" class="comment-tools"></div><div class="clear"></div><div id="comment-1684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1685"></span>

<div id="answer-container-1685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1685-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This source code is irrelevant, you should read up on <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">network capture setup</a> and <a href="http://www.cacetech.com/SHARKFEST.08/D01_Blok_Advanced%20Scripting,%20Command%20Line%20Usage%20with%20tshark.ppt">using tshark</a> for your analysis.</p><p>If you insist writing your own code you should address the <a href="https://www.wireshark.org/mailman/listinfo/wireshark-dev">Wireshark developer mailing list</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '11, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1685" class="comments-container"></div><div id="comment-tools-1685" class="comment-tools"></div><div class="clear"></div><div id="comment-1685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

