+++
type = "question"
title = "how to find previous frame in dissector"
description = '''I&#x27;m extending the radiotap dissector to calculate the inter frame space since the previous frame, so I need to reference the previous frame in the dissector. What is the correct way to do this? I&#x27;m currently using a global reference to cfile, and call to frame_data_sequence_find, but this global ref...'''
date = "2012-11-21T15:01:00Z"
lastmod = "2012-11-22T18:43:00Z"
weight = 16183
keywords = [ "cfile", "search", "dissector" ]
aliases = [ "/questions/16183" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to find previous frame in dissector](/questions/16183/how-to-find-previous-frame-in-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16183-score" class="post-score" title="current number of votes">0</div><span id="post-16183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm extending the radiotap dissector to calculate the inter frame space since the previous frame, so I need to reference the previous frame in the dissector. What is the correct way to do this? I'm currently using a global reference to cfile, and call to frame_data_sequence_find, but this global reference is a problem at link time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cfile" rel="tag" title="see questions tagged &#39;cfile&#39;">cfile</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '12, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/56993b38fa37140b783e7913ec139f45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="protocolmagic&#39;s gravatar image" /><p><span>protocolmagic</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="protocolmagic has no accepted answers">0%</span></p></div></div><div id="comments-container-16183" class="comments-container"></div><div id="comment-tools-16183" class="comment-tools"></div><div class="clear"></div><div id="comment-16183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16215"></span>

<div id="answer-container-16215" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16215-score" class="post-score" title="current number of votes">0</div><span id="post-16215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should probably set up a conversation saving information in the conversation data use that data in the next frame to do the calculation save the result in per packet data, store the new base in conersation data etc. Guarding it with pinfo-&gt;visited to only do the calculation on the first pass and use the per packet data when displaying the result.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-16215" class="comments-container"><span id="16219"></span><div id="comment-16219" class="comment"><div id="post-16219-score" class="comment-score"></div><div class="comment-text"><p>Correct. Wireshark isn't set up to have dissectors look at any frame other than the current frame; the correct way to process information in earlier frames is to save it in a data structure for future reference.</p></div><div id="comment-16219-info" class="comment-info"><span class="comment-age">(22 Nov '12, 10:11)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-16215" class="comment-tools"></div><div class="clear"></div><div id="comment-16215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16228"></span>

<div id="answer-container-16228" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16228-score" class="post-score" title="current number of votes">0</div><span id="post-16228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think I found the correct way to do this. Before wireshark makes an initial pass through all the frames in a capture it calls your dissector's 'init' routine, if you register one. Here you can reset your state, and maintain it. Next when the dissect routine is called if the fd-&gt;flags-&gt;visited is not set then the frame is the next one to be dissected. If the visited flag is set this may be a random access and sould be ignored. So I create a static 'last frame' variable, reset it in 'init', update it every time the dissector is called with a unvisited frame. Next i add local frame data to the unvisited frame, and put what i need in there (reference to previous frame).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 18:43</strong></p><img src="https://secure.gravatar.com/avatar/56993b38fa37140b783e7913ec139f45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="protocolmagic&#39;s gravatar image" /><p><span>protocolmagic</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="protocolmagic has no accepted answers">0%</span></p></div></div><div id="comments-container-16228" class="comments-container"></div><div id="comment-tools-16228" class="comment-tools"></div><div class="clear"></div><div id="comment-16228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

