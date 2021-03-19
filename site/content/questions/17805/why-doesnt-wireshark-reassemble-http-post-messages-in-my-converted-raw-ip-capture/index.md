+++
type = "question"
title = "Why doesn&#x27;t Wireshark reassemble HTTP POST messages in my converted raw IP capture"
description = '''Hi guys! I&#x27;m stuck with a problem with Wireshark. Background: I got a file filled with Raw Ip Packets captured by a third party device.  In order to make it readable by Wireshark i wrote a little C program converting the raw ip format into a wireshark readable one. It worked well for 99% of the case...'''
date = "2013-01-21T07:08:00Z"
lastmod = "2013-01-21T07:08:00Z"
weight = 17805
keywords = [ "reassembly", "http", "tcp", "raw" ]
aliases = [ "/questions/17805" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why doesn't Wireshark reassemble HTTP POST messages in my converted raw IP capture](/questions/17805/why-doesnt-wireshark-reassemble-http-post-messages-in-my-converted-raw-ip-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17805-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys!</p><p>I'm stuck with a problem with Wireshark.</p><p>Background: I got a file filled with Raw Ip Packets captured by a third party device. In order to make it readable by Wireshark i wrote a little C program converting the raw ip format into a wireshark readable one. It worked well for 99% of the cases. FYI this is the code:</p><pre><code>#include &lt; stdio.h &gt;
#include &lt; stdlib.h &gt;

typedef struct pcap_hdr_s {
        uint32_t magic_number;   /* magic number */
        uint16_t version_major;  /* major version number */
        uint16_t version_minor;  /* minor version number */
        int32_t  thiszone;       /* GMT to local correction */
        uint32_t sigfigs;        /* accuracy of timestamps */
        uint32_t snaplen;        /* max length of captured packets, in octets */
        uint32_t network;        /* data link type */
} pcap_hdr_t;

typedef struct pcaprec_hdr_s {
        uint32_t ts_sec;         /* timestamp seconds */
        uint32_t ts_usec;        /* timestamp microseconds */
        uint32_t incl_len;       /* number of octets of packet saved in file */
        uint32_t orig_len;       /* actual length of packet */
} pcaprec_hdr_t;

int main(int argc, char *argv[])
{

    unsigned char ipbuf[65537];
    uint32_t length;
    char minibuf[8];
    uint32_t longvar;
    uint32_t shortvar;
    char outfile[8192];

    pcap_hdr_t hdr;
    pcaprec_hdr_t pkt;

    if (argc &lt; 2)
    {
        printf(&quot;Usage: a.out [rawip filename]\n&quot;);
        exit(1);
    }

    sprintf(outfile, &quot;%s.pcap&quot;, argv[1]);

    FILE *fp = fopen(argv[1], &quot;r&quot;);
    FILE *ofp = fopen(outfile, &quot;w+&quot;);

    /**** DUMP HEADER ****/
    hdr.magic_number = 0xa1b2c3d4;
    hdr.version_major = 2;
    hdr.version_minor = 4;
    hdr.thiszone = 0;
    hdr.sigfigs = 0;
    hdr.snaplen = 65535;
    hdr.network = 228; // means raw ip4

    fwrite(&amp;hdr, 1, sizeof(pcap_hdr_t), ofp);

    while ((fread(ipbuf, 1, 4, fp) &gt; 0) &amp;&amp; (!(feof(fp))))
    {
        length = (uint32_t) (ipbuf[2] * 256 + ipbuf[3]);

        if (fread(&amp;ipbuf[4], 1, length - 4, fp) &lt; 1)
            break;

        // build and dump packet header
        pkt.ts_sec = 0;
        pkt.ts_usec++;
        pkt.incl_len = (uint32_t) length;
        pkt.orig_len = (uint32_t) length;

        fwrite(&amp;pkt, 1, sizeof(pcaprec_hdr_t), ofp);

        // finally, dump data
        fwrite(ipbuf, 1, length, ofp);
    }

    fclose(fp);
    fclose(ofp);

    exit(0);
}</code></pre><p>My problem is that lately, i've obtained a pcap file that partically can't rebuild part of the TCP stream. The latter contains HTTP packets, POST as request and 200 OK as response.</p><p>The POST part is not reassembled but the 200 OK is.</p><p>"Follow TCP stream" command seems like fully rebuild the stream. That's weird.</p><p>How can I get any information about the errors during the TCP reassembly? Is it possible that is my conversion program the culprit?</p><p>Thank you in advance</p><p><strong>UPDATE</strong></p><p>I came up that the problem is about the order the packets are written into the ipraw file. Infact it DOESN'T MATCH with the order the packets are captured from the device.</p><p>Despite the wrong order, if I select "Follow TCP stream" the correct conversation is rebuilt (so, i can tell wireshark CAN rebuild the TCP flow correctly), but into the main wireshark window, it can't recognize it contains an HTTP (MMS) stream and i can't filter it.</p><p>I wrote a little program that manually switch the out-of-order packets and wireshark recognize 100% the HTTP stream.</p><p>There's a way to tell wireshark to try to always follow the TCP streams and ignore the order of the packet written to pcap file?</p></div><div id="question-tags" class="tags-container tags">reassembly http tcp raw</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '13, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/949b4496263a3a86ef9cab80641ff270?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davide%20Berra&#39;s gravatar image" /><p>Davide Berra<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davide Berra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jun '13, 01:51</p></div></div><div id="comments-container-17805" class="comments-container"><span id="17806"></span><div id="comment-17806" class="comment"><div id="post-17806-score" class="comment-score"></div><div class="comment-text"><p>It might help if you post the resulting pcap file somewhere, e.g. <a href="http://cloudshark.org/">Cloudshark</a> and add a link back to it here by editing your question. Only post the capture if the contents can be made public.</p></div><div id="comment-17806-info" class="comment-info"><span class="comment-age">(21 Jan '13, 07:26)</span> grahamb ♦</div></div><span id="17809"></span><div id="comment-17809" class="comment"><div id="post-17809-score" class="comment-score"></div><div class="comment-text"><p>Unfortunally it contains reserved data but i can make print screen with the sensible data obfuscated if you guide me on what you want to see.</p></div><div id="comment-17809-info" class="comment-info"><span class="comment-age">(21 Jan '13, 07:46)</span> Davide Berra</div></div><span id="17810"></span><div id="comment-17810" class="comment"><div id="post-17810-score" class="comment-score"></div><div class="comment-text"><p>Debugging stuff via print screen output isn't usually very efficient, and more so for reassembly as you need to see all the preceding packets. You can try to add screenshots to see if someone can help.</p></div><div id="comment-17810-info" class="comment-info"><span class="comment-age">(21 Jan '13, 08:15)</span> grahamb ♦</div></div><span id="17811"></span><div id="comment-17811" class="comment"><div id="post-17811-score" class="comment-score"></div><div class="comment-text"><p>Just a question... the timestamp i arbitrarily set to every packet i dump, can lead to error during the TCP reassembly? Or wireshark uses just TCP sequences to rebuild the stream?</p></div><div id="comment-17811-info" class="comment-info"><span class="comment-age">(21 Jan '13, 08:19)</span> Davide Berra</div></div><span id="17813"></span><div id="comment-17813" class="comment"><div id="post-17813-score" class="comment-score"></div><div class="comment-text"><p>The HTTP dissector uses a TCP reassembly function by continuously asking for more data from the stream until it gets all that's required, I don't think timestamp is relevant here.</p><p>Can you confirm you have enabled reassembly for all the parts in the http protocol preferences?</p></div><div id="comment-17813-info" class="comment-info"><span class="comment-age">(21 Jan '13, 08:51)</span> grahamb ♦</div></div><span id="17814"></span><div id="comment-17814" class="comment not_top_scorer"><div id="post-17814-score" class="comment-score"></div><div class="comment-text"><p>I forgot to mention that is HTTP POST of an MMS message. Could it act different compared to HTTP dissector? Anyway, i confirm that i have enabled reassembly for all the parts.</p></div><div id="comment-17814-info" class="comment-info"><span class="comment-age">(21 Jan '13, 08:57)</span> Davide Berra</div></div><span id="17816"></span><div id="comment-17816" class="comment not_top_scorer"><div id="post-17816-score" class="comment-score"></div><div class="comment-text"><p>The HTTP dissector reassembles the content of the post, de-chunks and decompresses it as required, then hands the data off to sub-dissectors if one can be found to handle the specific data type.</p></div><div id="comment-17816-info" class="comment-info"><span class="comment-age">(21 Jan '13, 09:08)</span> grahamb ♦</div></div></div><div id="comment-tools-17805" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-17805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

