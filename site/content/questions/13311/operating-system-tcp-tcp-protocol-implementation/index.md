+++
type = "question"
title = "Operating System TCP &amp; TCP protocol implementation"
description = '''Hi All, I have implemented TCP protocol (RFC 793). For testing it I am using Windows Sockets. From my TCP I am sending SYN packet(Connect). I can capture the syn packet in wireshark.. It seems that the server written using Win Socket does not receives any message. Does anyone knows why this is happe...'''
date = "2012-08-02T03:34:00Z"
lastmod = "2012-08-02T06:26:00Z"
weight = 13311
keywords = [ "implementation", "and", "protocol", "windows", "tcp" ]
aliases = [ "/questions/13311" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Operating System TCP & TCP protocol implementation](/questions/13311/operating-system-tcp-tcp-protocol-implementation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13311-score" class="post-score" title="current number of votes">0</div><span id="post-13311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have implemented TCP protocol (RFC 793). For testing it I am using Windows Sockets. From my TCP I am sending SYN packet(Connect). I can capture the syn packet in wireshark.. It seems that the server written using Win Socket does not receives any message. Does anyone knows why this is happening??</p><p>Wireshark displays checksum error. Even i could not fix this checksum error also.</p><p>Thanks in advance for any help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-implementation" rel="tag" title="see questions tagged &#39;implementation&#39;">implementation</span> <span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '12, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/f80796612a9bd2e5c17778ae0a41d8ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prithvi&#39;s gravatar image" /><p><span>prithvi</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prithvi has no accepted answers">0%</span></p></div></div><div id="comments-container-13311" class="comments-container"></div><div id="comment-tools-13311" class="comment-tools"></div><div class="clear"></div><div id="comment-13311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13314"></span>

<div id="answer-container-13314" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13314-score" class="post-score" title="current number of votes">0</div><span id="post-13314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I can capture the syn packet in wireshark.. It seems that the server written using Win Socket does not receives any message.</p></blockquote><p>If the SYN packet is sent to the right IP address (I assume everything is O.K. with the SYN packet), and your server does not "see/process" it, these are possible reasons:</p><ul><li>a firewall on the server (windows firewall) or a network firewall between client and server blocks the SYN packet</li><li>there is a bug in your server implementation (check with netstat -na if the port, your server is using, is in LISTEN state)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '12, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13314" class="comments-container"></div><div id="comment-tools-13314" class="comment-tools"></div><div class="clear"></div><div id="comment-13314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

