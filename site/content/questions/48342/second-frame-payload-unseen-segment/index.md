+++
type = "question"
title = "Second frame payload unseen segment"
description = '''Hi  I am trying to get my server to send multiple TCP frames. the problem I am having is that the second frame (second half of the payload) is an unseen segment and never makes it to the client.  I have been trying to find the problem but I cant seem to resolve the issue.  I am new to using WS, so i...'''
date = "2015-12-07T21:27:00Z"
lastmod = "2015-12-09T01:13:00Z"
weight = 48342
keywords = [ "second", "segment", "frame", "unseen", "payload" ]
aliases = [ "/questions/48342" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Second frame payload unseen segment](/questions/48342/second-frame-payload-unseen-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48342-score" class="post-score" title="current number of votes">0</div><span id="post-48342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am trying to get my server to send multiple TCP frames. the problem I am having is that the second frame (second half of the payload) is an unseen segment and never makes it to the client. I have been trying to find the problem but I cant seem to resolve the issue.<br />
</p><p>I am new to using WS, so if you need more data let me know what you need. Thanks</p><p>Here is my WS captured info</p><p><img src="https://osqa-ask.wireshark.org/upfiles/WS1_uZXQWds.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-second" rel="tag" title="see questions tagged &#39;second&#39;">second</span> <span class="post-tag tag-link-segment" rel="tag" title="see questions tagged &#39;segment&#39;">segment</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-unseen" rel="tag" title="see questions tagged &#39;unseen&#39;">unseen</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '15, 21:27</strong></p><img src="https://secure.gravatar.com/avatar/300fc75c80fb5c852c1a1a092b110467?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cruzxia&#39;s gravatar image" /><p><span>cruzxia</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cruzxia has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-48342" class="comments-container"><span id="48354"></span><div id="comment-48354" class="comment"><div id="post-48354-score" class="comment-score"></div><div class="comment-text"><p>You mentioned that "the second frame (second half of the payload) is an unseen segment and never makes it to the client."</p><p>How do you know this? Are you capturing packets on the server or as near to the server as possible? This will determine if the server is sending the missing segment.</p><p>Also, screen captures are hard to read. If you can, it is best to upload your capture to Google Drive or cloudshark so others can review. Others in the forum can then look at the complete capture.</p><p>From what I can interpret from the screen captures, it appears the client is resetting the TCP connection after missing a segment. If that is the case, then we must determine where the packet is dropped or if the server even sends it.</p></div><div id="comment-48354-info" class="comment-info"><span class="comment-age">(08 Dec '15, 08:58)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-48342" class="comment-tools"></div><div class="clear"></div><div id="comment-48342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48373"></span>

<div id="answer-container-48373" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48373-score" class="post-score" title="current number of votes">0</div><span id="post-48373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the reply</p><p>I found the problem, the Ack in the second packet was increased by 1 so it wouldn't accept the data.</p><p>The strange thing is that it now works correctly and the server reports the correct value, but WireShark reports the Ack as 1 less than the value. The value is 405, it wasn't working when it was 406, I subtracted 1 and now WS shows as 404 and it works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '15, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/300fc75c80fb5c852c1a1a092b110467?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cruzxia&#39;s gravatar image" /><p><span>cruzxia</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cruzxia has no accepted answers">0%</span></p></div></div><div id="comments-container-48373" class="comments-container"></div><div id="comment-tools-48373" class="comment-tools"></div><div class="clear"></div><div id="comment-48373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

