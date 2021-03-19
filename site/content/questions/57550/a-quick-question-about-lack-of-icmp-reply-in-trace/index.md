+++
type = "question"
title = "A quick question about lack of ICMP reply in trace"
description = '''Hello can someone please help me with the following question :) We have a Windows Server and a NetApp Cluster-Mode iSCSI attached storage (NAS) on the same vLAN Basically, for want of a better description, one of the interface on the NetApp (one of the LIFs) is not responding (let&#x27;s just say it&#x27;s hu...'''
date = "2016-11-22T06:57:00Z"
lastmod = "2016-11-22T07:01:00Z"
weight = 57550
keywords = [ "icmp" ]
aliases = [ "/questions/57550" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [A quick question about lack of ICMP reply in trace](/questions/57550/a-quick-question-about-lack-of-icmp-reply-in-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57550-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>can someone please help me with the following question :)</p><p>We have a Windows Server and a NetApp Cluster-Mode iSCSI attached storage (NAS) on the same vLAN</p><p>Basically, for want of a better description, one of the interface on the NetApp (one of the LIFs) is not responding (let's just say it's hung).</p><p>Therefore when you do a ping (from a Windows command prompt) to the NetApp interface in question (again both on the same subnet) I receive the following</p><p>Reply from 172.20.11.249: TTL expired in transit</p><p>However, in the Wireshark capture (and I have check I am capturing on the correct interface) there is nothing displayed for ICMP (not a single ICMP packet)</p><p>Could it be I am not seeing an ICMP as I am not crossing a router and the interface is just not responding at all and therefore unable to build and ICMP packet of its own to send back?</p><p>Any advice most welcome</p><p>Thanks Ernie</p></div><div id="question-tags" class="tags-container tags">icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '16, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/ff39c11ae2cb05528da757366e76d84b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EBrant&#39;s gravatar image" /><p>EBrant<br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EBrant has no accepted answers">0%</span></p></div></div><div id="comments-container-57550" class="comments-container"></div><div id="comment-tools-57550" class="comment-tools"></div><div class="clear"></div><div id="comment-57550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57551"></span>

<div id="answer-container-57551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57551-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If modern versions of Windows cannot find a device on a given interface, it may send the request to the default GW. Is the ping client multihomed? If so, sniff on that interface. You may see ICMP echoes on that interface or ARPs, depending if you are local or not.</p><p>So, capture on all interfaces and see what shows.</p><p>Finally found a reference to this -</p><p><a href="https://blogs.technet.microsoft.com/networking/2009/04/24/source-ip-address-selection-on-a-multi-homed-windows-computer/">https://blogs.technet.microsoft.com/networking/2009/04/24/source-ip-address-selection-on-a-multi-homed-windows-computer/</a></p><p>Check the section on <strong>What about Neighbor Unreachability?</strong> and see if it applies to you in this case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '16, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '16, 02:40</p></div></div><div id="comments-container-57551" class="comments-container"></div><div id="comment-tools-57551" class="comment-tools"></div><div class="clear"></div><div id="comment-57551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

