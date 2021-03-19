+++
type = "question"
title = "How stop the dissection when tvb buffer ends  ?????"
description = '''I want to stop the dissection of the packet when tvb buffer ends. Is there any API for stop the dissection of that packet??????'''
date = "2012-11-01T22:49:00Z"
lastmod = "2012-11-05T00:48:00Z"
weight = 15483
keywords = [ "tvbuff_t" ]
aliases = [ "/questions/15483" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How stop the dissection when tvb buffer ends ?????](/questions/15483/how-stop-the-dissection-when-tvb-buffer-ends)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15483-score" class="post-score" title="current number of votes">0</div><span id="post-15483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to stop the dissection of the packet when tvb buffer ends.</p><p>Is there any API for stop the dissection of that packet??????</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tvbuff_t" rel="tag" title="see questions tagged &#39;tvbuff_t&#39;">tvbuff_t</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '12, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p><span>Akhil</span><br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div></div><div id="comments-container-15483" class="comments-container"><span id="15491"></span><div id="comment-15491" class="comment"><div id="post-15491-score" class="comment-score"></div><div class="comment-text"><p>What do you mean? The "normal" thing is that the dissector keeps track of how many bytes that should be dissected either from length information in the protocol or by checking the (reported) length of the tvb.</p></div><div id="comment-15491-info" class="comment-info"><span class="comment-age">(02 Nov '12, 04:19)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-15483" class="comment-tools"></div><div class="clear"></div><div id="comment-15483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15505"></span>

<div id="answer-container-15505" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15505-score" class="post-score" title="current number of votes">0</div><span id="post-15505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Akhil has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't want to keep track of when the buffer ends (which you can detect by looking at the TVB length(s) as Anders said), you can also just keep reading/dissecting: when you get past the end of the buffer your access with throw an exception and stop dissection for you (of course it will also report your packet as malformed or cut short during capture).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '12, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-15505" class="comments-container"><span id="15530"></span><div id="comment-15530" class="comment"><div id="post-15530-score" class="comment-score"></div><div class="comment-text"><p>I am checking the end of the buffer by if(tvb_length_remaining()&lt;=0). If the condition is true which api/function should i call to stop the dissection?????. If i call exit(1) then i guess whireshark will terminate....I want to stop the dissection of that particular packet.</p></div><div id="comment-15530-info" class="comment-info"><span class="comment-age">(04 Nov '12, 21:52)</span> <span class="comment-user userinfo">Akhil</span></div></div><span id="15533"></span><div id="comment-15533" class="comment"><div id="post-15533-score" class="comment-score"></div><div class="comment-text"><p>just 'return' from your dissector.</p></div><div id="comment-15533-info" class="comment-info"><span class="comment-age">(05 Nov '12, 00:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15534"></span><div id="comment-15534" class="comment"><div id="post-15534-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Kurt</p></div><div id="comment-15534-info" class="comment-info"><span class="comment-age">(05 Nov '12, 00:48)</span> <span class="comment-user userinfo">Akhil</span></div></div></div><div id="comment-tools-15505" class="comment-tools"></div><div class="clear"></div><div id="comment-15505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

