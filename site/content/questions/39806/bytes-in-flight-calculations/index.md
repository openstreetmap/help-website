+++
type = "question"
title = "Bytes in Flight calculations"
description = '''How does Wireshark calculate Bytes in Flight (BIF)? Do the BIF also consider the SACK left-edge and right-edge values? I have an 19MB file that I would like to share, but do not see a way to attach the file to this post. Here is a general formula that I am using to determine BIF assuming with SACK: ...'''
date = "2015-02-11T13:15:00Z"
lastmod = "2017-03-02T23:59:00Z"
weight = 39806
keywords = [ "tcp", "tcp-bytes-in-flight" ]
aliases = [ "/questions/39806" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Bytes in Flight calculations](/questions/39806/bytes-in-flight-calculations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39806-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does Wireshark calculate Bytes in Flight (BIF)? Do the BIF also consider the SACK left-edge and right-edge values? I have an 19MB file that I would like to share, but do not see a way to attach the file to this post. Here is a general formula that I am using to determine BIF assuming with SACK:</p><ol><li>(Sequence # of sender) + (TCP Length of sender) - (SACK right edge of receiver) = Value #1</li><li>(SACK left edge of receiver) - (Last TCP ACK # from receiver) = Value #2</li></ol><p>BIF = (Value #1) + (Value #2)</p><p>Are the above equations correct? Please correct any of the above equations as needed.</p></div><div id="question-tags" class="tags-container tags">tcp tcp-bytes-in-flight</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '15, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-39806" class="comments-container"><span id="39807"></span><div id="comment-39807" class="comment"><div id="post-39807-score" class="comment-score"></div><div class="comment-text"><p>Put it on <a href="http://www.cloudshark.org">http://www.cloudshark.org</a>, and sanitize it with TraceWrangler first if necessary.</p></div><div id="comment-39807-info" class="comment-info"><span class="comment-age">(11 Feb '15, 13:16)</span> Jasper ♦♦</div></div></div><div id="comment-tools-39806" class="comment-tools"></div><div class="clear"></div><div id="comment-39806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59815"></span>

<div id="answer-container-59815" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59815-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>At the point you mention, there are 9 packets missing, forming a data gap between #264 and #270. It would appear that these really were missing from the flow, because SACKs #283-#293 report that missing data. #308-#316 are the TCP retransmissions that fill that gap.</p><p>According to the bug report, this is why Wireshark doesn't count them in the BIF calculation.</p><p>There are also 5 packets missing between #274 and #275. However, these are selectively acknowledged, very soon after, by those same SACKs mentioned above.</p><p>This capture is a treasure trove of interesting behaviour.</p><p>There are also many examples of:</p><ul><li><p>Packets retransmitted at the radio level, where we see the original in the trace (eg, #303 and #317 ; #352-#360 are repeats of #308-#316).</p></li><li><p>This happens for ACKs too (eg, #2225-#2233, then #2236-#2244).</p></li><li><p>Packets retransmitted at the radio level, where we DON'T see the original in the trace (eg, #332-#336).</p></li><li><p>Packets unnecessarily retransmitted at the TCP/IP level, where we see the original in the trace and they are ACKed. These also trigger Duplicate SACKs (eg, #352-#360 are retransmissions of #308-#316, #395 is a D-SACK for #360).</p></li><li><p>Packets seen in the trace but not seen at the TCP/IP level by the receiver (eg, #343 is selectively not-ACKed but the radio retransmission, #396, does get ACKed. Likewise for #346/#397 and #347/#398).</p></li><li><p>Transmit Window "inflation", where the sender outputs more "packets in flight" in response to many SACKs.</p></li></ul><p>I guess that your capturing WiFi device is closer to the access point than your real receiver (since we see packets that the receiver doesn't - at both the radio and TCP/IP level). Your capture device also drops some real packets that the receiver does see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '17, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p>Philst<br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Mar '17, 18:05</p></div></div><div id="comments-container-59815" class="comments-container"><span id="59875"></span><div id="comment-59875" class="comment"><div id="post-59875-score" class="comment-score"></div><div class="comment-text"><p>@Philst = thank you for the detailed analysis. By showing the flow analysis in NetData, it has become evident the complexity of the capture goes beyond a miscalculation in Bytes-in-Flight.</p></div><div id="comment-59875-info" class="comment-info"><span class="comment-age">(06 Mar '17, 19:05)</span> Amato_C</div></div></div><div id="comment-tools-59815" class="comment-tools"></div><div class="clear"></div><div id="comment-59815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39821"></span>

<div id="answer-container-39821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39821-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As I understand the code, Wireshark sums up the TCP length of all un<strong>ACK</strong>ed frames by walking throuh a list of those un<strong>ACK</strong>ed frames (ual).</p><p>File: packet-tcp.c</p><pre><code>    /* how many bytes of data are there in flight after this frame
     * was sent
     */
    ual=tcpd-&gt;fwd-&gt;segments;
    if (tcp_track_bytes_in_flight &amp;&amp; seglen!=0 &amp;&amp; ual &amp;&amp; tcpd-&gt;fwd-&gt;valid_bif) {
        guint32 first_seq, last_seq, in_flight;

        first_seq = ual-&gt;seq - tcpd-&gt;fwd-&gt;base_seq;
        last_seq = ual-&gt;nextseq - tcpd-&gt;fwd-&gt;base_seq;
        while (ual) {
            if ((ual-&gt;nextseq-tcpd-&gt;fwd-&gt;base_seq)&gt;last_seq) {
                last_seq = ual-&gt;nextseq-tcpd-&gt;fwd-&gt;base_seq;
            }
            if ((ual-&gt;seq-tcpd-&gt;fwd-&gt;base_seq)&lt;first_seq) {=&quot;&quot; first_seq=&quot;ual-&quot;&gt;seq-tcpd-&gt;fwd-&gt;base_seq;
            }
            ual = ual-&gt;next;
        }
        in_flight = last_seq-first_seq;

        if (in_flight&gt;0 &amp;&amp; in_flight&lt;2000000000) {
            if(!tcpd-&gt;ta) {
                tcp_analyze_get_acked_struct(pinfo-&gt;fd-&gt;num, seq, ack, TRUE, tcpd);
            }
            tcpd-&gt;ta-&gt;bytes_in_flight = in_flight;
        }
    }
</code></pre><p>SLE and SRE are not considered. You can see it pretty good in a SACK sample capture with packet loss.</p><blockquote><p><a href="http://packetlife.net/captures/TCP_SACK.cap">http://packetlife.net/captures/TCP_SACK.cap</a></p></blockquote><p>Add a column for bytes in flight to see it (Frames #30 - #39).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39821" class="comments-container"><span id="39834"></span><div id="comment-39834" class="comment"><div id="post-39834-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Thank you for the code and example. It is clear now that SACK is not used to determine the Bytes-in-Flight (BIF) calculation. However, I am still seeing a problem with the BIF calculation with my Wireshark trace.<br />
First, let's look at the capture file you provided: "TCP_SACK.cap". Looking at packets #36-#38, the BIF calculation is: (Sequence # of sender) + (TCP Length of sender) - (ACK of receiver) = 23169 + 1222 - 17377 = 7014 This is the exact number reported as BIF by Wireshark on packet #38.</p><p>Now I will perform the same analysis using the file at: <a href="https://drive.google.com/file/d/0B3IDBN3nIwLzeVViaXhUVkFjVGc/view?usp=sharing">https://drive.google.com/file/d/0B3IDBN3nIwLzeVViaXhUVkFjVGc/view?usp=sharing</a></p><p>Please download and view the file: "Stitcher-Only-TCP-Traffic-Stream3.pcap" Let's look at packets #293-#294: (Sequence # of sender) + (TCP Length of sender) - (ACK of receiver) = 211914 + 1448 - 174266 = 39096 However, packet #294 is reporting BIF = 26064 That is a difference of 39096 - 26064 = 13032 bytes or (13032/1448) = 9 packets</p><p>Why such the large discrepancy?</p></div><div id="comment-39834-info" class="comment-info"><span class="comment-age">(12 Feb '15, 08:06)</span> Amato_C</div></div><span id="39891"></span><div id="comment-39891" class="comment"><div id="post-39891-score" class="comment-score"></div><div class="comment-text"><p>Wireshark reporting incorrect bytes-in-flight values is a known issue. Please reference <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7703">Bug ID #7703</a>.</p></div><div id="comment-39891-info" class="comment-info"><span class="comment-age">(16 Feb '15, 07:08)</span> Amato_C</div></div><span id="39895"></span><div id="comment-39895" class="comment"><div id="post-39895-score" class="comment-score"></div><div class="comment-text"><p>yep, looks like there is 'room for improvement' ;-)</p></div><div id="comment-39895-info" class="comment-info"><span class="comment-age">(16 Feb '15, 12:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-39821" class="comment-tools"></div><div class="clear"></div><div id="comment-39821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

