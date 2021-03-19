+++
type = "question"
title = "How to troubleshoot wireshark when it doesn&#x27;t want to capture?"
description = '''I&#x27;m trying to capture RTP traffic from one of my IP phones. When I run wireshark on the server connected to a span port I can easily see the RTP traffic. Unfortunately when I use capture filter like this: host 192.168.9.4 where the given IP is the address of my IP phone it doesn&#x27;t display RTP traffi...'''
date = "2012-03-07T00:15:00Z"
lastmod = "2012-03-07T02:55:00Z"
weight = 9415
keywords = [ "windows2k8", "winpcap" ]
aliases = [ "/questions/9415" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to troubleshoot wireshark when it doesn't want to capture?](/questions/9415/how-to-troubleshoot-wireshark-when-it-doesnt-want-to-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9415-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture RTP traffic from one of my IP phones. When I run wireshark on the server connected to a span port I can easily see the RTP traffic. Unfortunately when I use capture filter like this:</p><p>host 192.168.9.4</p><p>where the given IP is the address of my IP phone it doesn't display RTP traffic at all (just some ARP traffic). Actually when I use any capture filter at all (even just "udp") it cuts almost all traffic.</p><p>I know wireshark itself is ok because when I connect my laptop with the same version of wireshark to the same span port - it works just fine.</p><p>Is possible that there's some other driver on the server that is conflicting with the pcap driver installed with wireshark?</p></div><div id="question-tags" class="tags-container tags">windows2k8 winpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '12, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/956e86eaba16bec45796ea3f9e9fb87c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kyrisu&#39;s gravatar image" /><p>kyrisu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kyrisu has no accepted answers">0%</span></p></div></div><div id="comments-container-9415" class="comments-container"></div><div id="comment-tools-9415" class="comment-tools"></div><div class="clear"></div><div id="comment-9415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9416"></span>

<div id="answer-container-9416" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9416-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Most likely, your server does <strong>not</strong> strip the vlan tags from the frames (while your laptop does). This means you need to change the capture filter to:</p><pre><code>vlan and host 192.168.9.4</code></pre><p>to capture all traffic to and from host 192.168.9.4.</p><p>You can check whether there are vlan tags in your packets by capturing without a filter and then look at the ethernet details is there is a vlan tag present.</p><p>See also: <a href="http://wiki.wireshark.org/CaptureSetup/VLAN#Capture_filters">http://wiki.wireshark.org/CaptureSetup/VLAN#Capture_filters</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '12, 02:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9416" class="comments-container"><span id="9417"></span><div id="comment-9417" class="comment"><div id="post-9417-score" class="comment-score"></div><div class="comment-text"><p>Thank you that was exactly the issue :) Is there a way to force winpcap to catch vlan traffic by default? I'm using an app that has hardcoded capture filter.</p></div><div id="comment-9417-info" class="comment-info"><span class="comment-age">(07 Mar '12, 03:23)</span> kyrisu</div></div><span id="9418"></span><div id="comment-9418" class="comment"><div id="post-9418-score" class="comment-score"></div><div class="comment-text"><p>If the application uses a hardcoded capture filter, then you will have to make sure that WinPcap does not see vlag tags. You might be able to configure your NIC driver to strip them (which most NIC drivers do by default). This can be doen either in the normal settings or the registry. Have a look at the other information on the above-mentioned wiki-page and/or contact your NIC vendor :-)</p></div><div id="comment-9418-info" class="comment-info"><span class="comment-age">(07 Mar '12, 03:33)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-9416" class="comment-tools"></div><div class="clear"></div><div id="comment-9416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

