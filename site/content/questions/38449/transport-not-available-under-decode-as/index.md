+++
type = "question"
title = "&quot;Transport&quot; not available under &quot;Decode as&quot;"
description = '''I was trying to capture Netflow traffic from a device to my NMS server. I wanted to use the CFLOW decode as option under transport. I couldnt see transport window under decode as option. Is there a wayi Can enable this? All the protocols option is already checked. Regards, K.B.L'''
date = "2014-12-08T13:16:00Z"
lastmod = "2014-12-08T17:24:00Z"
weight = 38449
keywords = [ "cflow" ]
aliases = [ "/questions/38449" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Transport" not available under "Decode as"](/questions/38449/transport-not-available-under-decode-as)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38449-score" class="post-score" title="current number of votes">0</div><span id="post-38449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying to capture Netflow traffic from a device to my NMS server. I wanted to use the CFLOW decode as option under transport. I couldnt see transport window under decode as option. Is there a wayi Can enable this? All the protocols option is already checked.</p><p>Regards, K.B.L</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cflow" rel="tag" title="see questions tagged &#39;cflow&#39;">cflow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '14, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/25a53375c677a86f4b00d0bc44468c28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KBL&#39;s gravatar image" /><p><span>KBL</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KBL has no accepted answers">0%</span></p></div></div><div id="comments-container-38449" class="comments-container"></div><div id="comment-tools-38449" class="comment-tools"></div><div class="clear"></div><div id="comment-38449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38454"></span>

<div id="answer-container-38454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38454-score" class="post-score" title="current number of votes">0</div><span id="post-38454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like there is something wrong with the captured frames. Did you capture the <strong>whole frame</strong> or just the first few bytes (60 bytes, or so)?</p><p>Please check the size of the catured frame by looking at the Frame layer. Compare the values for "bytes on wire" and "bytes captured". If "bytes captured" is much lower than the value for "bytes on wire", then you might have missed the transport layer.</p><p>BTW: Can you please share a small sample capture file (pcap - single frame is enough)? Please upload the file to google drive, dropbox or cloudshark.org and post the link here.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '14, 17:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38454" class="comments-container"></div><div id="comment-tools-38454" class="comment-tools"></div><div class="clear"></div><div id="comment-38454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

