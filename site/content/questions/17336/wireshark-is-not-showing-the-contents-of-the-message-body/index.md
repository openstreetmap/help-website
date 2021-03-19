+++
type = "question"
title = "wireshark is not showing the contents of the message body"
description = '''can any please tell me are there any setting preferences to change how message body content is shown??'''
date = "2012-12-31T03:22:00Z"
lastmod = "2012-12-31T04:34:00Z"
weight = 17336
keywords = [ "body", "message" ]
aliases = [ "/questions/17336" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark is not showing the contents of the message body](/questions/17336/wireshark-is-not-showing-the-contents-of-the-message-body)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17336-score" class="post-score" title="current number of votes">0</div><span id="post-17336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can any please tell me are there any setting preferences to change how message body content is shown?<img src="https://osqa-ask.wireshark.org/upfiles/wireshark_3.png" alt="alt text" />?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-body" rel="tag" title="see questions tagged &#39;body&#39;">body</span> <span class="post-tag tag-link-message" rel="tag" title="see questions tagged &#39;message&#39;">message</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '12, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/063d3a8f56059f88844e33145cc53ba5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gantashalavenki&#39;s gravatar image" /><p><span>gantashalavenki</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gantashalavenki has no accepted answers">0%</span></p></img></div></div><div id="comments-container-17336" class="comments-container"></div><div id="comment-tools-17336" class="comment-tools"></div><div class="clear"></div><div id="comment-17336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17337"></span>

<div id="answer-container-17337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17337-score" class="post-score" title="current number of votes">0</div><span id="post-17337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please enable the following setting to see 'raw text' in SIP messages.</p><blockquote><p><code>Edit -&gt; Preferences -&gt; SIP -&gt; Display raw text for SIP Messages</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '12, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-17337" class="comments-container"><span id="17338"></span><div id="comment-17338" class="comment"><div id="post-17338-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response.....i already tried that,its showing one more section with heading SIP as RAW text. no change in message body content</p></div><div id="comment-17338-info" class="comment-info"><span class="comment-age">(31 Dec '12, 03:53)</span> <span class="comment-user userinfo">gantashalavenki</span></div></div><span id="17340"></span><div id="comment-17340" class="comment"><div id="post-17340-score" class="comment-score"></div><div class="comment-text"><p>can you upload just that single packet as a <strong>pcap file</strong> somewhere (your web server, one click hoster, google docs, <a href="http://cloudshark.org">cloudshark.org</a>)?</p><blockquote><p><code>CTRL-M (mark the packet) then :: File -&gt; Export Specified Packtes -&gt; Marked packets</code></p></blockquote></div><div id="comment-17340-info" class="comment-info"><span class="comment-age">(31 Dec '12, 04:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17337" class="comment-tools"></div><div class="clear"></div><div id="comment-17337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17339"></span>

<div id="answer-container-17339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17339-score" class="post-score" title="current number of votes">0</div><span id="post-17339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you show us the Content-Type header we could tell you what non-text/plain MIME type is being used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '12, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-17339" class="comments-container"></div><div id="comment-tools-17339" class="comment-tools"></div><div class="clear"></div><div id="comment-17339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

