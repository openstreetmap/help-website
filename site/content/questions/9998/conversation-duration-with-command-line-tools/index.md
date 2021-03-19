+++
type = "question"
title = "conversation duration with command line tools"
description = '''I need the values Rel Start and duration that is displayed in Wireshark conversation list window. However tshark does not provide these columns. So how can i get this information from the command line or is there any way to forward this output info into a text file from the command line.  Thanks'''
date = "2012-04-06T13:39:00Z"
lastmod = "2013-03-06T18:46:00Z"
weight = 9998
keywords = [ "conversationlist" ]
aliases = [ "/questions/9998" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [conversation duration with command line tools](/questions/9998/conversation-duration-with-command-line-tools)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9998-score" class="post-score" title="current number of votes">1</div><span id="post-9998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need the values Rel Start and duration that is displayed in Wireshark conversation list window. However tshark does not provide these columns. So how can i get this information from the command line or is there any way to forward this output info into a text file from the command line.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversationlist" rel="tag" title="see questions tagged &#39;conversationlist&#39;">conversationlist</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '12, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/4afe1e975d821217b82b70f5c796a8d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="esmayildirim&#39;s gravatar image" /><p><span>esmayildirim</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="esmayildirim has no accepted answers">0%</span></p></div></div><div id="comments-container-9998" class="comments-container"></div><div id="comment-tools-9998" class="comment-tools"></div><div class="clear"></div><div id="comment-9998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10094"></span>

<div id="answer-container-10094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10094-score" class="post-score" title="current number of votes">3</div><span id="post-10094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've added the required info to tshark in r42037. Either build your own from svn, or pick up one of the nightly builds with a later rev.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '12, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10094" class="comments-container"><span id="19255"></span><div id="comment-19255" class="comment"><div id="post-19255-score" class="comment-score"></div><div class="comment-text"><p>It's now provided in additional columns in various tables you can get with the <code>-z conv,</code> option</p></div><div id="comment-19255-info" class="comment-info"><span class="comment-age">(06 Mar '13, 18:46)</span> <span class="comment-user userinfo">rakslice</span></div></div></div><div id="comment-tools-10094" class="comment-tools"></div><div class="clear"></div><div id="comment-10094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

