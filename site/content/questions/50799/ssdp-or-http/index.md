+++
type = "question"
title = "SSDP or HTTP ??"
description = '''Hello guys. As you know, SSDP uses HTTP NOTIFY in discovery and advertisement requests. now my question is; Can these requests be categorized as HTTP traffic??Why?? TNX.'''
date = "2016-03-10T08:01:00Z"
lastmod = "2016-03-13T09:26:00Z"
weight = 50799
keywords = [ "ssdp", "http" ]
aliases = [ "/questions/50799" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSDP or HTTP ??](/questions/50799/ssdp-or-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50799-score" class="post-score" title="current number of votes">0</div><span id="post-50799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys.</p><p>As you know, SSDP uses HTTP NOTIFY in discovery and advertisement <strong>requests</strong>.</p><p>now my question is;</p><p>Can these <strong>requests</strong> be categorized as HTTP traffic??Why??</p><p>TNX.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssdp" rel="tag" title="see questions tagged &#39;ssdp&#39;">ssdp</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '16, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/8752544ec453a6d8e08fdde4d465eca7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MehranBazgir&#39;s gravatar image" /><p><span>MehranBazgir</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MehranBazgir has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Mar '16, 08:03</strong> </span></p></div></div><div id="comments-container-50799" class="comments-container"><span id="50852"></span><div id="comment-50852" class="comment"><div id="post-50852-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid you'll have to reword your question. Are you asking <strong>why</strong> the protocol name shown in the packet list is SSDP (and maybe how to change it to HTTP), or are you asking <strong>how</strong> does Wireshark know (i.e. what criteria it uses to determine) that it should dissect these packets as HTTP ones?</p></div><div id="comment-50852-info" class="comment-info"><span class="comment-age">(13 Mar '16, 01:49)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50864"></span><div id="comment-50864" class="comment"><div id="post-50864-score" class="comment-score"></div><div class="comment-text"><p>Hello.</p><p>You said my question in better words. In fact my question is;</p><p>how does Wireshark know (i.e. what criteria it uses to determine) that it should dissect these packets as SSDP ones??</p><p>Is it possible that another standard packet capture software detects these traffic as HTTP??</p><p>TNX.</p></div><div id="comment-50864-info" class="comment-info"><span class="comment-age">(13 Mar '16, 08:56)</span> <span class="comment-user userinfo">MehranBazgir</span></div></div></div><div id="comment-tools-50799" class="comment-tools"></div><div class="clear"></div><div id="comment-50799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50865"></span>

<div id="answer-container-50865" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50865-score" class="post-score" title="current number of votes">1</div><span id="post-50865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MehranBazgir has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is in fact a two-step procedure.</p><ul><li><p>as you can see if you right-click on an SSDP packet in packet list and choose <code>Decode as...</code> in Wireshark 2.0.x, the criterion to choose the HTTP dissector is "UDP port 1900".</p></li><li><p>based on the HTTP payload contents, the HTTP dissector itself finds out that this particular packet is an SSDP one and marks it as such in the packet list pane. But here you have to look into the HTTP dissector code to find the exact criteria used.</p></li></ul><blockquote><p>Is it possible that another standard packet capture software detects these traffic as HTTP??</p></blockquote><p>This detection is normally a matter of packet <em>analysis</em> part of any software. If you are looking for a <em>capture filter</em> limiting the capture to these packets, the right one in tcpdump notation (also used by the Wireshark suite) would be <code>udp and port 1900</code>. To reduce the amount of captured data, you might want to extend it with <code>and host 239.0.0.0/8</code>, i.e. to further limit the capture to the private IPv4 multicast range. The code performing further analysis would then have to find out by contents whether packets matching this condition can actually be dissected as HTTP/SSDP ones. Note that in the tcpdump capture filter syntax, the well-known services have got textual aliases for port numbers, so <code>tcp and port http</code> is actually equal to <code>tcp and port 80</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '16, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50865" class="comments-container"></div><div id="comment-tools-50865" class="comment-tools"></div><div class="clear"></div><div id="comment-50865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

