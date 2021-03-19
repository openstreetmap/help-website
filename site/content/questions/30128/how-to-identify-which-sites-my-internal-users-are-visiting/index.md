+++
type = "question"
title = "How to identify which sites my internal users are visiting"
description = '''I want to look through websites and when I find something they shouldn&#x27;t be looking at I want to find what IP address they are so I can tell them to get off the website. Please help'''
date = "2014-02-24T06:39:00Z"
lastmod = "2014-02-25T03:58:00Z"
weight = 30128
keywords = [ "http", "ipv4", "wireshark" ]
aliases = [ "/questions/30128" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to identify which sites my internal users are visiting](/questions/30128/how-to-identify-which-sites-my-internal-users-are-visiting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30128-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to look through websites and when I find something they shouldn't be looking at I want to find what IP address they are so I can tell them to get off the website. Please help</p></div><div id="question-tags" class="tags-container tags">http ipv4 wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '14, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/27470515a91f812c1290b68b48b4361f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbohling&#39;s gravatar image" /><p>jbohling<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbohling has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Feb '14, 12:18</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-30128" class="comments-container"><span id="30130"></span><div id="comment-30130" class="comment"><div id="post-30130-score" class="comment-score"></div><div class="comment-text"><p>I have absolutely no clue what you are trying to ask in this thread. You want to find out the IP Address of a certain website??</p></div><div id="comment-30130-info" class="comment-info"><span class="comment-age">(24 Feb '14, 07:27)</span> CipherSpec</div></div><span id="30145"></span><div id="comment-30145" class="comment"><div id="post-30145-score" class="comment-score"></div><div class="comment-text"><p>I want to find what websites are being viewed on my network and then be able to see who was visiting those websites.</p></div><div id="comment-30145-info" class="comment-info"><span class="comment-age">(24 Feb '14, 11:32)</span> jbohling</div></div><span id="30147"></span><div id="comment-30147" class="comment"><div id="post-30147-score" class="comment-score"></div><div class="comment-text"><p>so, you want to know which sites <strong>your internal users</strong> are visiting?</p></div><div id="comment-30147-info" class="comment-info"><span class="comment-age">(24 Feb '14, 11:38)</span> Kurt Knochner ♦</div></div><span id="30150"></span><div id="comment-30150" class="comment"><div id="post-30150-score" class="comment-score"></div><div class="comment-text"><p>yes, exactly. I know how to see what websites are being visited but I don't know how to see which user is visiting them or what IP address they are.</p></div><div id="comment-30150-info" class="comment-info"><span class="comment-age">(24 Feb '14, 12:04)</span> jbohling</div></div></div><div id="comment-tools-30128" class="comment-tools"></div><div class="clear"></div><div id="comment-30128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30175"></span>

<div id="answer-container-30175" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30175-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>make note of the client's IP addresses and filter wireshark for http and https traffic</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '14, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/270068c5096560aa74a319961e02594f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flicker&#39;s gravatar image" /><p>flicker<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flicker has no accepted answers">0%</span></p></div></div><div id="comments-container-30175" class="comments-container"></div><div id="comment-tools-30175" class="comment-tools"></div><div class="clear"></div><div id="comment-30175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

