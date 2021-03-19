+++
type = "question"
title = "Why wireshark cannot display TLS/SSL"
description = '''Hi, everyone: Today I have written a simple JAVA program to test communication between SSL client and server. I run my client and server, and try to use Wireshark to capture the packets. But I could only see &quot;TCP&quot; instead of TLS/SSL in &quot;protocol&quot;:  And I just send a string (10 bytes) from client to ...'''
date = "2014-06-23T06:31:00Z"
lastmod = "2014-06-23T07:12:00Z"
weight = 34075
keywords = [ "tls", "ssl" ]
aliases = [ "/questions/34075" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why wireshark cannot display TLS/SSL](/questions/34075/why-wireshark-cannot-display-tlsssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34075-score" class="post-score" title="current number of votes">0</div><span id="post-34075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, everyone:</p><p>Today I have written a simple JAVA program to test communication between SSL client and server.</p><p>I run my client and server, and try to use Wireshark to capture the packets. But I could only see "TCP" instead of TLS/SSL in "protocol": <img src="https://osqa-ask.wireshark.org/upfiles/n.png" alt="alt text" /></p><p>And I just send a string (10 bytes) from client to server. I think the first packets are handshake packets. But why it doesn't show as "TLS/SSL"?</p><p>Any one could help me?</p><p>Thank you very much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '14, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/44959625f5849a8c85cdf05ca9802478?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lzq8272587&#39;s gravatar image" /><p><span>lzq8272587</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lzq8272587 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jun '14, 06:32</strong> </span></p></div></div><div id="comments-container-34075" class="comments-container"></div><div id="comment-tools-34075" class="comment-tools"></div><div class="clear"></div><div id="comment-34075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34078"></span>

<div id="answer-container-34078" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34078-score" class="post-score" title="current number of votes">2</div><span id="post-34078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lzq8272587 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But why it doesn't show as "TLS/SSL"?</p></blockquote><p>Because it's not on the standard port for SSL/TLS. You can add your port (12120):</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; SSL/TLS Ports</p></blockquote><p>Change it to: 443,12120</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '14, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34078" class="comments-container"><span id="34079"></span><div id="comment-34079" class="comment"><div id="post-34079-score" class="comment-score"></div><div class="comment-text"><p>wow, now I could see TLSv1 in the "protocol".</p><p>Thank you very much!</p></div><div id="comment-34079-info" class="comment-info"><span class="comment-age">(23 Jun '14, 07:12)</span> <span class="comment-user userinfo">lzq8272587</span></div></div></div><div id="comment-tools-34078" class="comment-tools"></div><div class="clear"></div><div id="comment-34078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

