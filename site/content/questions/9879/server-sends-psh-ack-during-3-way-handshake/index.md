+++
type = "question"
title = "Server sends PSH, ACK during 3-way handshake"
description = '''This is the sequence: Client sends SYN – sequence number 0 Server returns PSH, ACK – Sequence number 1, Acknowledgement number 31267 I was expecting SYN, ACK from the server. What is going on here? So, client sends RST and connection never gets established.  Normally everything works fine but once i...'''
date = "2012-03-31T16:29:00Z"
lastmod = "2012-04-16T03:24:00Z"
weight = 9879
keywords = [ "tcp" ]
aliases = [ "/questions/9879" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Server sends PSH, ACK during 3-way handshake](/questions/9879/server-sends-psh-ack-during-3-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9879-score" class="post-score" title="current number of votes">0</div><span id="post-9879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>This is the sequence:</p><p>Client sends SYN – sequence number 0</p><p>Server returns PSH, ACK – Sequence number 1, Acknowledgement number 31267</p><p>I was expecting SYN, ACK from the server. What is going on here?</p><p>So, client sends RST and connection never gets established.</p><p>Normally everything works fine but once in a while this issue occurs</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '12, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/dd9a4e68d01344be582fb9fcbb94d775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fox2&#39;s gravatar image" /><p><span>Fox2</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fox2 has no accepted answers">0%</span></p></div></div><div id="comments-container-9879" class="comments-container"></div><div id="comment-tools-9879" class="comment-tools"></div><div class="clear"></div><div id="comment-9879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9880"></span>

<div id="answer-container-9880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9880-score" class="post-score" title="current number of votes">2</div><span id="post-9880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I recently saw this at a customer and was able to narrow the problem down to a Cisco ASA running an ancient version of firmware (7.0.4). They are planning an upgrade. Is there a Cisco ASA involved in the communication between your client and server too?</p><p>In my case, I could see the SYN enter the FW on the outside, but it was never forwarded on the inside. Instead a PSH/ACK with "random" ACK number was returned to the client.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '12, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9880" class="comments-container"><span id="10183"></span><div id="comment-10183" class="comment"><div id="post-10183-score" class="comment-score"></div><div class="comment-text"><p>I just received word from my customer that the upgrade of the Cisco ASA FW from version 7.0.4 to 7.2 did indeed solve the issue they were having.</p><p>Hope this helps. If you are not running a Cisco ASA, are you able to get a trace of both the client side and the server side? If so, can you post them to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and paste the URL's to the captures here?</p></div><div id="comment-10183-info" class="comment-info"><span class="comment-age">(16 Apr '12, 03:24)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-9880" class="comment-tools"></div><div class="clear"></div><div id="comment-9880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

