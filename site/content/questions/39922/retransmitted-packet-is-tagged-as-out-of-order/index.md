+++
type = "question"
title = "Retransmitted packet is tagged as &quot;Out of Order&quot;?"
description = '''Hi Below is the screenshot taken during debug of some throughput issue. I see wireshark flagging a &quot;802.11 retransmission packet&quot; (please see the highlighted packet) as &quot;TCP Out of order packet&quot;.  Third column &quot;Sequence number&quot; is 802.11 sequence number. Fifth column is TCP Seq No.  Let me elaborate...'''
date = "2015-02-18T02:35:00Z"
lastmod = "2015-03-01T07:13:00Z"
weight = 39922
keywords = [ "of", "out-of-order", "out" ]
aliases = [ "/questions/39922" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Retransmitted packet is tagged as "Out of Order"?](/questions/39922/retransmitted-packet-is-tagged-as-out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Below is the screenshot taken during debug of some throughput issue. I see wireshark flagging a "802.11 retransmission packet" (please see the highlighted packet) as "TCP Out of order packet".</p><p>Third column "Sequence number" is 802.11 sequence number. Fifth column is TCP Seq No.</p><p>Let me elaborate situation: This capture is taken on wireless channel. Due to some problem the peer didn't ACK (WLAN) the TCP SYN packet. SO he has retried the same packet (with out any modifications to TCP contents). But wireshark shows that packet as Out of Order . Shouldn't it be showing TCP re-transmission instead of Out of order?</p><p>If you want to look into capture, I can upload as well.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcp-2.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">of out-of-order out</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '15, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/5c59321a66976ba615e1a50b46a4d209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramprasad&#39;s gravatar image" /><p>Ramprasad<br />
<span class="score" title="20 reputation points">20</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramprasad has no accepted answers">0%</span></p></img></div></div><div id="comments-container-39922" class="comments-container"><span id="39955"></span><div id="comment-39955" class="comment"><div id="post-39955-score" class="comment-score"></div><div class="comment-text"><p>Can someone help to clarify my question?</p></div><div id="comment-39955-info" class="comment-info"><span class="comment-age">(19 Feb '15, 09:24)</span> Ramprasad</div></div><span id="40002"></span><div id="comment-40002" class="comment"><div id="post-40002-score" class="comment-score"></div><div class="comment-text"><p>Hard to answer your question with a screenshot alone. Upload the trace to <a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a></p></div><div id="comment-40002-info" class="comment-info"><span class="comment-age">(21 Feb '15, 02:48)</span> mrEEde</div></div><span id="40006"></span><div id="comment-40006" class="comment"><div id="post-40006-score" class="comment-score"></div><div class="comment-text"><p>As the file size is large, I've trimmed the capture &amp; uploaded with packets starting from SYN to next ~90 more packets. Please find the capture uploaded @ https://www.cloudshark.org/captures/e30a9f842f03</p></div><div id="comment-40006-info" class="comment-info"><span class="comment-age">(21 Feb '15, 09:00)</span> Ramprasad</div></div></div><div id="comment-tools-39922" class="comment-tools"></div><div class="clear"></div><div id="comment-39922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40029"></span>

<div id="answer-container-40029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40029-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the code (packet-tcp.c), it's because the duplicate frames came in too fast. delta(t) &lt; ooo_thres (3ms) - see code below.</p><p>So, to answer you question: Wireshark shows it as out-of-order because that's the way it is currently implemented, looking at a delta to determine if it's a retransmission or out-of-order.</p><p>Maybe a user-configurable parameter would be a good idea, to improve retransmission detection on very fast networks (&gt;= 10 Gbit/s).</p><p>See also my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/27662/how-to-understand-out-of-order-tcp-segments">https://ask.wireshark.org/questions/27662/how-to-understand-out-of-order-tcp-segments</a></p></blockquote><p><strong>Code:</strong></p><pre><code>         / If the segment came relatively close since the segment with the highest
           * seen sequence number and it doesn&#39;t look like a retransmission
           * then it is an OUT-OF-ORDER segment.
           /
          t=(pinfo-&gt;fd-&gt;abs_ts.secs-tcpd-&gt;fwd-&gt;nextseqtime.secs)*1000000000;
          t=t+(pinfo-&gt;fd-&gt;abs_ts.nsecs)-tcpd-&gt;fwd-&gt;nextseqtime.nsecs;
HERE ===&gt; if( t &lt; ooo_thres 

          &amp;&amp; tcpd-&gt;fwd-&gt;nextseq != seq + seglen ) {
            if(!tcpd-&gt;ta) {
                tcp_analyze_get_acked_struct(pinfo-&gt;fd-&gt;num, seq, ack, TRUE, tcpd);
            }
HERE ===&gt;   tcpd-&gt;ta-&gt;flags|=TCP_A_OUT_OF_ORDER;
            goto finished_checking_retransmission_type;
        }</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '15, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-40029" class="comments-container"><span id="40165"></span><div id="comment-40165" class="comment"><div id="post-40165-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for the answer. but I still have some further confusion...</p><p>I understand, as the gap is less than 3ms you don't want to flag it as re-transmission, but is there a specific reason to mark this as out-of-order?</p><p>I was understanding, a packet can be flagged as out-of-order only if the packet with higher sequence number is there before the lower sequence number, probably due to different round trips if assymmetric routing is present? Isn't it? Then how can packets with same sequence numbers can be flagged as Out-of-order?</p></div><div id="comment-40165-info" class="comment-info"><span class="comment-age">(01 Mar '15, 05:25)</span> Ramprasad</div></div><span id="40186"></span><div id="comment-40186" class="comment"><div id="post-40186-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Then how can packets with same sequence numbers can be flagged as Out-of-order?</p></blockquote><p>because that's the way the Wireshark code currently works.</p><p>If the design is perfect or not is a totally different question, and yes you are right, flagging a repeated SYN as "out-of-order" does not sound like that should be the final solution ;-))</p><p>Please file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p></div><div id="comment-40186-info" class="comment-info"><span class="comment-age">(02 Mar '15, 09:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-40029" class="comment-tools"></div><div class="clear"></div><div id="comment-40029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40166"></span>

<div id="answer-container-40166" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40166-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Flagging repeated SYN packets as out-of-order doesn't make sense, so I'd say this is not correctly diagnosed. You might want to open a bug report for this at the <a href="https://bugs.wireshark.org">bug tracker</a>. Other than that - since version 1.12, Wireshark considers the initial round trip time (iRTT) to determine if a packet is a retransmission or an out-of-order. So the 3ms boundary is only used when iRTT is unknown. See <a href="https://blog.packet-foo.com/2014/08/tcp-expert-updates-in-wireshark-1-12/">https://blog.packet-foo.com/2014/08/tcp-expert-updates-in-wireshark-1-12/</a></p><p>It is possible that the new iRTT based determination of retransmissions needs some fine tuning in some special cases where iRTT is very small or slightly missed by the retransmission. I have that one on my todo list and will probably bother the core devs at <a href="http://sharkfest.wireshark.org/">Sharkfest 2015</a> with some ideas on how to improve the TCP expert :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '15, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40166" class="comments-container"><span id="40254"></span><div id="comment-40254" class="comment"><div id="post-40254-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt &amp; Jasper. But....</p><p>""Flagging repeated SYN packets as out-of-order doesn't make sense ""</p><p>But my concern is mainly for TCP data packets, not just for SYN packets. I feel in no-circumstance a packet with same serial number can be flagged as out of order. Am I failing to understand something?</p><p>If my assumption is correct, I'll log bug @ provided URLs.</p></div><div id="comment-40254-info" class="comment-info"><span class="comment-age">(04 Mar '15, 04:40)</span> Ramprasad</div></div></div><div id="comment-tools-40166" class="comment-tools"></div><div class="clear"></div><div id="comment-40166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

