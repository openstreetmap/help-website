+++
type = "question"
title = "How many TCP warnings should there be on a cross-datacenter connection"
description = '''I&#x27;m trying to diagnose some issues between an Azure VM and a Google Compute Engine VM. Every now and then, the Azure server reports it cannot connect over HTTP to the GCE machine. There&#x27;s no errors logged on the GCE machine. I ran a PCAP for a while, and if I filter with _ws.expert.severity &amp;gt;= no...'''
date = "2015-02-11T16:52:00Z"
lastmod = "2015-02-12T06:15:00Z"
weight = 39823
keywords = [ "azure", "kvm", "google", "vm", "tcp" ]
aliases = [ "/questions/39823" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How many TCP warnings should there be on a cross-datacenter connection](/questions/39823/how-many-tcp-warnings-should-there-be-on-a-cross-datacenter-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39823-score" class="post-score" title="current number of votes">0</div><span id="post-39823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to diagnose some issues between an Azure VM and a Google Compute Engine VM. Every now and then, the Azure server reports it cannot connect over HTTP to the GCE machine. There's no errors logged on the GCE machine.</p><p>I ran a PCAP for a while, and if I filter with _ws.expert.severity &gt;= note, over 2% of all packets are flagged. 0.1% of all TCP packets are flagged as a retransmission. Apart from that, it seems that there's a repeating pattern of "TCP Previous segment not captured, TCP Dup ACK, then TCP Out-Of-Order". I see those groups of 3 packets repeated all over, with apparently no real effects, like increased http.time.</p><p>Does this sound typical? Could the fact that it's a VM under KVM on GCE be causing some confusion here?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-azure" rel="tag" title="see questions tagged &#39;azure&#39;">azure</span> <span class="post-tag tag-link-kvm" rel="tag" title="see questions tagged &#39;kvm&#39;">kvm</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span> <span class="post-tag tag-link-vm" rel="tag" title="see questions tagged &#39;vm&#39;">vm</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '15, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/ee274e0f76943bacbc5168ad7845284e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MichaelGG&#39;s gravatar image" /><p><span>MichaelGG</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MichaelGG has no accepted answers">0%</span></p></div></div><div id="comments-container-39823" class="comments-container"></div><div id="comment-tools-39823" class="comment-tools"></div><div class="clear"></div><div id="comment-39823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39833"></span>

<div id="answer-container-39833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39833-score" class="post-score" title="current number of votes">1</div><span id="post-39833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How many TCP warnings should there be on a cross-datacenter connection</p></blockquote><p>in an <strong>ideal world</strong> there <strong>should</strong> be zero, but in the real world there are always errors, no matter what type of connection it is (btw. you did not mention that). Without knowing the link type, I'd say 0.1% retransmissions are more than O.K.</p><p>Regarding the rest of your reported problems:</p><ul><li>not every problem the wireshark expert marks as &gt;= "note" is a real problem. You have to look at the problems yourself to classify them.</li><li>please take into consideration that errors in Wireshark are not always real errors on the link. If you try to capture on a heavily loaded link your capturing system might drop packets (NIC, OS, etc.) or is unable to write all frames to disk at the required speed (disk speed slower than network speed). Those missing frames are only missing in the capture file and thus will create false positives while you are analyzing the capture file! So, it's always good practice to check of there were drops during the capture process (dumpcap will show it at the end).</li></ul><p>To troubleshoot your problem, I suggest to run dumpcap with ring buffer files (see man page of dumpcap) and with a capture filter for the destination IP address and port 80. Then monitor the error logs of the Azure server (with a script) and as soon as you see the error messages stop dumpcap. Then take a look at the last capture file and try to find failed TCP connections (RESET, etc.) and/or HTTP error messages.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '15, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39833" class="comments-container"></div><div id="comment-tools-39833" class="comment-tools"></div><div class="clear"></div><div id="comment-39833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

