+++
type = "question"
title = "Triggers for wireshark"
description = '''How to have triggers for wireshark... i.e. i would like wireshark to capture the packets after a particular packet type Ex: custom.type = = 10 then show all the packets from the point you get that type to be 10'''
date = "2011-09-27T03:12:00Z"
lastmod = "2011-09-27T23:48:00Z"
weight = 6585
keywords = [ "trigger" ]
aliases = [ "/questions/6585" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Triggers for wireshark](/questions/6585/triggers-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6585-score" class="post-score" title="current number of votes">0</div><span id="post-6585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to have triggers for wireshark... i.e. i would like wireshark to capture the packets after a particular packet type</p><p>Ex: custom.type = = 10 then show all the packets from the point you get that type to be 10</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-trigger" rel="tag" title="see questions tagged &#39;trigger&#39;">trigger</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '11, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p><span>flashkicker</span><br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6585" class="comments-container"><span id="6586"></span><div id="comment-6586" class="comment"><div id="post-6586-score" class="comment-score"></div><div class="comment-text"><p>Using filter we can show all the packets with the same type but the thing is i would like to have the wireshark display all the packets of any type until the trigger action occurs</p></div><div id="comment-6586-info" class="comment-info"><span class="comment-age">(27 Sep '11, 03:13)</span> <span class="comment-user userinfo">flashkicker</span></div></div></div><div id="comment-tools-6585" class="comment-tools"></div><div class="clear"></div><div id="comment-6585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6589"></span>

<div id="answer-container-6589" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6589-score" class="post-score" title="current number of votes">1</div><span id="post-6589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flashkicker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As of now, this functionality does not yet exist; however, there is an open bug report for it, namely <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3967">bug 3967</a>, and it's also mentioned on the <a href="http://wiki.wireshark.org/WishList">wishlist</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '11, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6589" class="comments-container"><span id="6606"></span><div id="comment-6606" class="comment"><div id="post-6606-score" class="comment-score"></div><div class="comment-text"><p>Thank you .....</p></div><div id="comment-6606-info" class="comment-info"><span class="comment-age">(27 Sep '11, 23:48)</span> <span class="comment-user userinfo">flashkicker</span></div></div></div><div id="comment-tools-6589" class="comment-tools"></div><div class="clear"></div><div id="comment-6589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

