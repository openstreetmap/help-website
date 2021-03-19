+++
type = "question"
title = "Why doesn&#x27;t Wireshark open on my Mac OS X machine?"
description = '''Hi, I&#x27;ve been running Wireshark for a while in this computer, but I reinstalled Mac OS X and Wireshark won&#x27;t open. I&#x27;ve deleted it and reinstalled it but the answer is the same; it just doesn&#x27;t open. How do I fix it?'''
date = "2012-04-25T15:17:00Z"
lastmod = "2012-05-02T13:14:00Z"
weight = 10447
keywords = [ "mac", "open", "problem" ]
aliases = [ "/questions/10447" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why doesn't Wireshark open on my Mac OS X machine?](/questions/10447/why-doesnt-wireshark-open-on-my-mac-os-x-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10447-score" class="post-score" title="current number of votes">0</div><span id="post-10447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've been running Wireshark for a while in this computer, but I reinstalled Mac OS X and Wireshark won't open. I've deleted it and reinstalled it but the answer is the same; it just doesn't open. How do I fix it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-open" rel="tag" title="see questions tagged &#39;open&#39;">open</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '12, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/d3c16dc4332fa8d79ddb434313874224?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoseMtz&#39;s gravatar image" /><p><span>JoseMtz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoseMtz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Sep '12, 08:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-10447" class="comments-container"><span id="10613"></span><div id="comment-10613" class="comment"><div id="post-10613-score" class="comment-score"></div><div class="comment-text"><p>Open up Console (in the Utilities folder under Applications) if you don't already have it open, and try launching Wireshark; then see what, if anything, gets logged to Console when that happens ("Console Messages" should work on Snow Leopard; I forget what the equivalent is in Lion or in older releases).</p><p>Then add the output to your question (use the "edit" option).</p></div><div id="comment-10613-info" class="comment-info"><span class="comment-age">(02 May '12, 13:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-10447" class="comment-tools"></div><div class="clear"></div><div id="comment-10447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10448"></span>

<div id="answer-container-10448" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10448-score" class="post-score" title="current number of votes">1</div><span id="post-10448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JoseMtz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you re-installed OS X, did you install X11? In at least some versions of OS X, X11 isn't in the default installation. (Check whether there's an "X11" app in <code>/Applications/Utilities</code>.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '12, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10448" class="comments-container"><span id="10604"></span><div id="comment-10604" class="comment"><div id="post-10604-score" class="comment-score"></div><div class="comment-text"><p>Yes, I thought that to... so I opened X11 and it is working just fine... I think it is something about the configurations of the airport... does anybody knows how to configurate it?</p></div><div id="comment-10604-info" class="comment-info"><span class="comment-age">(02 May '12, 08:22)</span> <span class="comment-user userinfo">JoseMtz</span></div></div></div><div id="comment-tools-10448" class="comment-tools"></div><div class="clear"></div><div id="comment-10448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

