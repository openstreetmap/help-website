+++
type = "question"
title = "capture filter does not capture when active"
description = '''tried multiple wireshark versions. read Help files, wiki and forums but no one seems to have my issue. Now using wireshark 1.10, I can capture packets using my laptop gig port. I can filter SIP traffic and notice it&amp;lt;s using port 5060, and IP phones are using IP addresses in the 10.x.x.x range. Bu...'''
date = "2013-07-23T08:17:00Z"
lastmod = "2013-07-23T14:36:00Z"
weight = 23289
keywords = [ "filter", "capture", "not", "working", "issues" ]
aliases = [ "/questions/23289" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter does not capture when active](/questions/23289/capture-filter-does-not-capture-when-active)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23289-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>tried multiple wireshark versions. read Help files, wiki and forums but no one seems to have my issue. Now using wireshark 1.10, I can capture packets using my laptop gig port. I can filter SIP traffic and notice it&lt;s using port 5060, and IP phones are using IP addresses in the 10.x.x.x range.</p><p>But if i select that same network card, attempt to add a packet filter (ex: net 10.x.x.x/24, or port 5060, host 10.x.x.x.) no packets are captured. The only filter that actually work is "ip"</p><p>what am I doing wrong?</p><p>One thing I should mention is that the sip session is mirrored to my ip address, not a mirrored port.</p></div><div id="question-tags" class="tags-container tags">filter capture not working issues</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '13, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/7a7be9ea65ee7adca653afc2b64e7037?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simseb451&#39;s gravatar image" /><p>simseb451<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simseb451 has no accepted answers">0%</span></p></div></div><div id="comments-container-23289" class="comments-container"><span id="23299"></span><div id="comment-23299" class="comment"><div id="post-23299-score" class="comment-score"></div><div class="comment-text"><blockquote><p>One thing I should mention is that the sip session is mirrored to my ip address, not a mirrored port.</p></blockquote><p>How did you do that?</p><blockquote><p>But if i select that same network card, attempt to add a packet filter (ex: net 10.x.x.x/24, or port 5060, host 10.x.x.x.) no packets are captured.</p></blockquote><p>What was the capture filter you used?</p></div><div id="comment-23299-info" class="comment-info"><span class="comment-age">(23 Jul '13, 10:09)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-23289" class="comment-tools"></div><div class="clear"></div><div id="comment-23289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23295"></span>

<div id="answer-container-23295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23295-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are there 802.1q vlan tags in the packets? If so, you will need to use the <code>vlan</code> keyword in your capture filter, e.g.:</p><pre><code>vlan and host 10.x.x.x</code></pre><p>See also:</p><ul><li><a href="http://wiki.wireshark.org/CaptureSetup/VLAN#Capture_filters">http://wiki.wireshark.org/CaptureSetup/VLAN#Capture_filters</a></li><li><a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a></li><li><a href="https://www.wireshark.org/docs/man-pages/pcap-filter.html">https://www.wireshark.org/docs/man-pages/pcap-filter.html</a></li></ul><p>If that's not the answer, then maybe you could post a small capture file to <a href="http://cloudshark.org/">cloudshark</a> and share the link to it here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-23295" class="comments-container"></div><div id="comment-tools-23295" class="comment-tools"></div><div class="clear"></div><div id="comment-23295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23304"></span>

<div id="answer-container-23304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23304-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since the filter <code>ip</code> works, it is not vlan or pppoe encapsulation that interferes with your filter. But since you say <code>One thing I should mention is that the sip session is mirrored to my ip address, not a mirrored port.</code>, I suspect the protocol hierarchy in your packets must be something like:</p><pre><code>ethernet
IP
TCP or UDP
IP
UDP
SIP</code></pre><p>All the capture filters you mentioned will filter only on the first IP headers, while you want to filter on the second IP headers or udp port. You will need to build a filter that dynamically skips the first IP/TCP layers. But that filter will depend on the actual layers that are in your trace.</p><p>Could you share a couple of packets on www.cloudshark.org and paste the link here? Beware to not upload any sensitive data. That way we can help you build a filter...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23304" class="comments-container"></div><div id="comment-tools-23304" class="comment-tools"></div><div class="clear"></div><div id="comment-23304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

