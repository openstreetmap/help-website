+++
type = "question"
title = "SMTP Info Displaying | | | | | |"
description = '''I have trace that is displaying something that I have never seen before in Wireshark. The traffic is all SMTP but the reassembled packets that include multiple previous frames show up in the Wireshark info as: S: | | | | | | | | | | | Has anyone ever seen this before?'''
date = "2013-10-24T09:01:00Z"
lastmod = "2013-10-24T14:30:00Z"
weight = 26367
keywords = [ "smtp", "display" ]
aliases = [ "/questions/26367" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SMTP Info Displaying | | | | | |](/questions/26367/smtp-info-displaying)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26367-score" class="post-score" title="current number of votes">0</div><span id="post-26367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have trace that is displaying something that I have never seen before in Wireshark. The traffic is all SMTP but the reassembled packets that include multiple previous frames show up in the Wireshark info as:</p><p>S: | | | | | | | | | | |</p><p>Has anyone ever seen this before?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '13, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/eb83eed38341ba8be5695cc3a93c76d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jackster&#39;s gravatar image" /><p><span>jackster</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jackster has no accepted answers">0%</span></p></div></div><div id="comments-container-26367" class="comments-container"></div><div id="comment-tools-26367" class="comment-tools"></div><div class="clear"></div><div id="comment-26367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26375"></span>

<div id="answer-container-26375" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26375-score" class="post-score" title="current number of votes">0</div><span id="post-26375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's emtpy lines (newline) sent by the server. Every <code>|</code> marks a new line. Right-click on any of the SMTP frames and choose <code>Follow TCP Stream</code> and you'll see it.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '13, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Oct '13, 06:38</strong> </span></p></div></div><div id="comments-container-26375" class="comments-container"></div><div id="comment-tools-26375" class="comment-tools"></div><div class="clear"></div><div id="comment-26375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

