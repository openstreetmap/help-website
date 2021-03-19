+++
type = "question"
title = "Display entire streams containing packets matching a display filter"
description = '''I have a display filter that correctly identifies the packets I&#x27;m interested in. What I would really like, though, is to display the entire TCP stream containing each of the matching packets. Is that possible?'''
date = "2014-03-27T10:33:00Z"
lastmod = "2014-03-28T15:03:00Z"
weight = 31224
keywords = [ "display-filter" ]
aliases = [ "/questions/31224" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display entire streams containing packets matching a display filter](/questions/31224/display-entire-streams-containing-packets-matching-a-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31224-score" class="post-score" title="current number of votes">0</div><span id="post-31224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a display filter that correctly identifies the packets I'm interested in. What I would really like, though, is to display the entire TCP stream containing each of the matching packets. Is that possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '14, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/8dfdc3bde976b9b6482b47cb25fd158a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Insyte&#39;s gravatar image" /><p><span>Insyte</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Insyte has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Mar '14, 10:34</strong> </span></p></div></div><div id="comments-container-31224" class="comments-container"><span id="31238"></span><div id="comment-31238" class="comment"><div id="post-31238-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I <strong>have thousands to review</strong> and manually interrogating each of them would be prohibitive.</p></blockquote><p>thousands to review? manually?</p><p>Well, maybe there is a better way. Please add more details what you are trying to do.</p></div><div id="comment-31238-info" class="comment-info"><span class="comment-age">(27 Mar '14, 13:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31248"></span><div id="comment-31248" class="comment"><div id="post-31248-score" class="comment-score"></div><div class="comment-text"><p>I have packet dumps of tens of thousands HTTP API calls inbound to our network. I am interested in reviewing a subset of those calls that are only identifiable based on the content of the POST. I would like to load those into the conversations dialog so I can quickly identify the ones that are slow (sort on the duration column) and try to figure out <em>why</em> they're slow.</p></div><div id="comment-31248-info" class="comment-info"><span class="comment-age">(28 Mar '14, 11:51)</span> <span class="comment-user userinfo">Insyte</span></div></div></div><div id="comment-tools-31224" class="comment-tools"></div><div class="clear"></div><div id="comment-31224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31234"></span>

<div id="answer-container-31234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31234-score" class="post-score" title="current number of votes">0</div><span id="post-31234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Right click on any TCP packet in the stream and choose "Follow TCP stream" from the drop-down.<br />
</p><p>A new window will open showing the two sides of the conversation, or you can look at the original window which is now filtered to show only the stream that was selected.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p><span>griff</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span> </br></p></div></div><div id="comments-container-31234" class="comments-container"><span id="31236"></span><div id="comment-31236" class="comment"><div id="post-31236-score" class="comment-score"></div><div class="comment-text"><p>My apologies for not being more clear, but what I'm trying to accomplish is for the packet list to display the matching packets and all of the other packets in the stream. For all of the matching packets and streams at once. I have thousands to review and manually interrogating each of them would be prohibitive.</p></div><div id="comment-31236-info" class="comment-info"><span class="comment-age">(27 Mar '14, 12:55)</span> <span class="comment-user userinfo">Insyte</span></div></div></div><div id="comment-tools-31234" class="comment-tools"></div><div class="clear"></div><div id="comment-31234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31263"></span>

<div id="answer-container-31263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31263-score" class="post-score" title="current number of votes">0</div><span id="post-31263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>I would like to load those into the conversations dialog</strong> so I can quickly identify the ones that are slow (sort on the duration column) and try to figure out why they're slow.</p></blockquote><p>well, then do just that ;-))</p><ul><li>Set a display filter</li><li>Open the conversations</li><li>Enable the option <strong>'Limit to display filter'</strong> (at the bottom)</li></ul><p>Now, you will only see those conversations that the filtered frames are part of.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '14, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31263" class="comments-container"></div><div id="comment-tools-31263" class="comment-tools"></div><div class="clear"></div><div id="comment-31263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

