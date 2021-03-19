+++
type = "question"
title = "Is there a fast way to change C array into PCAP ?"
description = '''Besides changing it to a hex dump and import, is there a faster way to convert C style array (exported from other PCAP) back to a PCAP file? static unsigned char pkt[56] = { 0x45, 0x00, 0x00, 0x38, 0x00, 0xf2, 0x20, 0x00, /* E..8.. . */ 0x40, 0x11, 0x14, 0x33, 0xc0, 0x00, 0x00, 0x02, /* @..3.... */ ...'''
date = "2015-01-16T12:10:00Z"
lastmod = "2015-01-16T14:05:00Z"
weight = 39221
keywords = [ "bytearray", "conversion", "pcap" ]
aliases = [ "/questions/39221" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a fast way to change C array into PCAP ?](/questions/39221/is-there-a-fast-way-to-change-c-array-into-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39221-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Besides changing it to a hex dump and import, is there a faster way to convert C style array (exported from other PCAP) back to a PCAP file?</p><pre><code>static unsigned char pkt[56] = {
0x45, 0x00, 0x00, 0x38, 0x00, 0xf2, 0x20, 0x00, /* E..8.. . */
0x40, 0x11, 0x14, 0x33, 0xc0, 0x00, 0x00, 0x02, /* @..3.... */
0x0a, 0x2a, 0x7b, 0x64, 0x7c, 0xab, 0x4e, 0xe5, /* .*{d|.N. */
0x00, 0x24, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* .$...... */
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* ........ */
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* ........ */
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00        /* ....... */ 
};</code></pre></div><div id="question-tags" class="tags-container tags">bytearray conversion pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '15, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/5bf84cea20bbef3b33f74637c8814804?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gallon&#39;s gravatar image" /><p>Gallon<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gallon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '15, 13:25</p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-39221" class="comments-container"></div><div id="comment-tools-39221" class="comment-tools"></div><div class="clear"></div><div id="comment-39221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39226"></span>

<div id="answer-container-39226" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39226-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you are handling raw IP packets. Here is an example using the pcap API. Refer to the respective manual pages and the <code>pcap(3pcap)</code> overview for an explanation of the functions. Further error handling and cleanup is left as an exercise to the reader.</p><pre><code>#include &lt;stdio.h&gt;
#include &lt;pcap/pcap.h&gt;

static u_char ip_pkt[] = {
    0x45, 0x00, 0x00, 0x38, 0x00, 0xf2, 0x20, 0x00, /* E..8.. . */
    0x40, 0x11, 0x14, 0x33, 0xc0, 0x00, 0x00, 0x02, /* @..3.... */
    0x0a, 0x2a, 0x7b, 0x64, 0x7c, 0xab, 0x4e, 0xe5, /* .*{d|.N. */
    0x00, 0x24, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* .$...... */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* ........ */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, /* ........ */
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00        /* ....... */ 
};
static size_t ip_pkt_len = sizeof(ip_pkt)/sizeof(*ip_pkt);

int main(void)
{
    pcap_t *pcap;
    /* open pcap context for Raw IP (DLT_RAW), see
     * http://www.tcpdump.org/linktypes.html */
#define DLT_RAW 12
    pcap = pcap_open_dead(DLT_RAW, 65565);

    pcap_dumper_t *d;
    /* open output file (stdout) */
    d = pcap_dump_fopen(pcap, stdout);
    if (d == NULL) {
        pcap_perror(pcap, &quot;pcap_dump_fopen&quot;);
        return 1;
    }

    /* prepare for writing */
    struct pcap_pkthdr hdr;
    hdr.ts.tv_sec = 0;  /* sec */
    hdr.ts.tv_usec = 0; /* ms */
    hdr.caplen = hdr.len = ip_pkt_len;
    /* write single IP packet */
    pcap_dump((u_char *)d, &amp;hdr, ip_pkt);

    /* finish up */
    pcap_dump_close(d);
    return 0;
}</code></pre><p>An alternative (easier) way is to use the Scapy (in Python) to craft a capture file. Example with the data provided in the comments:</p><pre><code>#!/usr/bin/env python2
# Import dependencies
from scapy.all import Dot11, wrpcap

# raw 802.11 contents
hex = &#39;C0 00 3A 01 00 11 22 33 44 55 FF FF FF FF FF FF 00 11 22 33 44 55 20 EF 06 00 00 00 00 00&#39;

# Initialize a 802.11 structure from raw bytes
packet = Dot11(bytearray.fromhex())

# Optional: use Scapy for data interpretation
print(p.summary())
print(p.show())

# Write the contents to file
wrpcap(&#39;your.pcap&#39;, pkt)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '15, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Feb '15, 15:23</p></div></div><div id="comments-container-39226" class="comments-container"><span id="39227"></span><div id="comment-39227" class="comment"><div id="post-39227-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot! will try that. yes it is RAW IP packet.</p></div><div id="comment-39227-info" class="comment-info"><span class="comment-age">(16 Jan '15, 14:32)</span> Gallon</div></div><span id="39229"></span><div id="comment-39229" class="comment"><div id="post-39229-score" class="comment-score"></div><div class="comment-text"><p>There shouldn't be a need to do <code>#define DLT_RAW 12</code>; <code>pcap_open_dead()</code> takes the platform's value for <code>DLT_RAW</code> as an argument, and including <code>&lt;pcap.h&gt;</code> should cause that to be defined.</p><p>Also, older versions of libpcap generally had just <code>&lt;pcap.h&gt;</code>, so, for maximum portability, the program should include <code>&lt;pcap.h&gt;</code> rather than <code>&lt;pcap/pcap.h&gt;</code>.</p></div><div id="comment-39229-info" class="comment-info"><span class="comment-age">(16 Jan '15, 19:18)</span> Guy Harris ♦♦</div></div><span id="39878"></span><div id="comment-39878" class="comment"><div id="post-39878-score" class="comment-score"></div><div class="comment-text"><p>in visual studio I was using this code. I was getting an error of unresolved symbols at pacp_dump_fopen</p></div><div id="comment-39878-info" class="comment-info"><span class="comment-age">(15 Feb '15, 21:09)</span> sathish308</div></div><span id="39882"></span><div id="comment-39882" class="comment"><div id="post-39882-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I was getting an error of unresolved symbols at pacp_dump_fopen</p></blockquote><p>(Presumably that's a typo for "pcap_dump_fopen()")</p><p>You have to link with libpcap (on UN*X) or WinPcap (on WIndows).</p></div><div id="comment-39882-info" class="comment-info"><span class="comment-age">(16 Feb '15, 01:05)</span> Guy Harris ♦♦</div></div><span id="40059"></span><div id="comment-40059" class="comment"><div id="post-40059-score" class="comment-score"></div><div class="comment-text"><p>it was working if I use pcap_dump_open().</p><p>here we are using Raw packet data. if I want to dump 802.11 packets such as data, management,control packets, what should I do?.</p><p>I mean if I want to save a packet of hexa values like this--&gt;C0 00 3A 01 00 11 22 33 44 55 FF FF FF FF FF FF 00 11 22 33 44 55 20 EF 06 00 00 00 00 00</p></div><div id="comment-40059-info" class="comment-info"><span class="comment-age">(24 Feb '15, 21:40)</span> sathish308</div></div><span id="40075"></span><div id="comment-40075" class="comment not_top_scorer"><div id="post-40075-score" class="comment-score"></div><div class="comment-text"><p>@sathish308 you need to use the <code>DLT_IEEE802_11</code> link layer type, see <a href="http://www.tcpdump.org/linktypes.html.">http://www.tcpdump.org/linktypes.html.</a> Alternatively, you can use Python and the Scapy library (see edit).</p></div><div id="comment-40075-info" class="comment-info"><span class="comment-age">(25 Feb '15, 15:25)</span> Lekensteyn</div></div></div><div id="comment-tools-39226" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-39226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

