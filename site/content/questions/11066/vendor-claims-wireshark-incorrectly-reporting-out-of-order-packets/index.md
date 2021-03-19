+++
type = "question"
title = "Vendor claims Wireshark incorrectly reporting Out of Order Packets"
description = '''I am getting traces from TCP Dump from interface of EMC NAS device sending from one network over MPLS WAN to another NAS device. TCP Dump taken from both sending and receiving end. Since we saw out of order reported in trace file of sending device, we assumed it was happening at device. However, the...'''
date = "2012-05-16T14:37:00Z"
lastmod = "2012-05-17T00:35:00Z"
weight = 11066
keywords = [ "out-of-order", "out" ]
aliases = [ "/questions/11066" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Vendor claims Wireshark incorrectly reporting Out of Order Packets](/questions/11066/vendor-claims-wireshark-incorrectly-reporting-out-of-order-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11066-score" class="post-score" title="current number of votes">0</div><span id="post-11066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting traces from TCP Dump from interface of EMC NAS device sending from one network over MPLS WAN to another NAS device. TCP Dump taken from both sending and receiving end. Since we saw out of order reported in trace file of sending device, we assumed it was happening at device. However, the vendor (EMC) says that this is a known problem with the Wireshark dissector. That they have written their own to solve the problem. That they are actually retransmissions and not out of order. We can see that the SEQ's are not coming out in order (not just relying on expert message).</p><p>They said the way to know is to look at the IP ID. If you look at the packets that the sender is sending, the IP ID's are sequential. However, the "next SEQ" that is expected is not in the right order so Wirehshark is saying out of order.</p><p>Is it true that if IP ID's are sequential, they are not out of order? They are arriving out of order on the remote side after traversing MPLS network which is not a big surprise but in order to prove it's happening while on the WAN, we have to figure out if Wireshark is incorrect in saying they are out of order when taken from the source host. Has anyone heard of this? EMC is calling it "False Positives". The good news is we actually have a vendor who uses Wireshark! Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span> <span class="post-tag tag-link-out" rel="tag" title="see questions tagged &#39;out&#39;">out</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '12, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/a1feffebe8015bb53af00f9d97157cda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Janis%20Bishop&#39;s gravatar image" /><p><span>Janis Bishop</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Janis Bishop has no accepted answers">0%</span></p></div></div><div id="comments-container-11066" class="comments-container"></div><div id="comment-tools-11066" class="comment-tools"></div><div class="clear"></div><div id="comment-11066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11068"></span>

<div id="answer-container-11068" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11068-score" class="post-score" title="current number of votes">0</div><span id="post-11068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If Wireshark reports "Out-of-order" packets at the TCP layer, it means that packets are seen which are not yet expected in respect to the sequence numbers of the packets. This does not say anything about whether the packets were re-ordered on the way. They could very well be sent out-of-order to begin with. Maybe this is what EMC means by "looking at the IP-id". Usually traffic between two hosts uses IP-id's that are increasing by 1 for each new IP datagram.</p><p>Without a trace file it is very hard to tell what's going on. Can you upload a small example file to <a href="http://www.cloudshark.org"></a><a href="http://www.cloudshark.org">www.cloudshark.org</a> and post the link here?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11068" class="comments-container"><span id="11070"></span><div id="comment-11070" class="comment"><div id="post-11070-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I am allowed to do that, so will check.</p></div><div id="comment-11070-info" class="comment-info"><span class="comment-age">(16 May '12, 15:14)</span> <span class="comment-user userinfo">Janis Bishop</span></div></div><span id="11071"></span><div id="comment-11071" class="comment"><div id="post-11071-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", as that's the way this site works best, please see the FAQ)</p><p>Yes, please DO check whether (a part of) the file can be posted. If not, you can also post the output of the command:</p><pre><code>tshark -r &lt;file&gt; -T fields -e tcp.srcport -e tcp.dstport -e ip.id -e tcp.seq -e tcp.len -e tcp.ack -e tcp.analysis.out_of_order</code></pre><p>this will not disclose any sensitive information and will give us an idea on what is going on.</p></div><div id="comment-11071-info" class="comment-info"><span class="comment-age">(16 May '12, 15:33)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="11074"></span><div id="comment-11074" class="comment"><div id="post-11074-score" class="comment-score"></div><div class="comment-text"><p>Could you please add the timestamp, as the "out of order" detection (also) relies on a time delta (see packet-tcp.c).</p><blockquote><pre><code>  /* If the segment came &lt;3ms since the segment with the highest
    * seen sequence number and it doesn&#39;t look like a retransmission
    * then it is an OUT-OF-ORDER segment.
    *   (3ms is an arbitrary number)
    */</code></pre></blockquote><p>tshark -r &lt;file&gt; -T fields <strong>-e frame.time_epoch</strong> -e tcp.srcport -e tcp.dstport -e <a href="http://ip.id">ip.id</a> -e tcp.seq -e tcp.len -e tcp.ack -e tcp.analysis.out_of_order</p></div><div id="comment-11074-info" class="comment-info"><span class="comment-age">(16 May '12, 16:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11084"></span><div id="comment-11084" class="comment"><div id="post-11084-score" class="comment-score"></div><div class="comment-text"><p>better use the filter <strong>frame.time_relative</strong></p></div><div id="comment-11084-info" class="comment-info"><span class="comment-age">(17 May '12, 00:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11068" class="comment-tools"></div><div class="clear"></div><div id="comment-11068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

