+++
type = "question"
title = "Time Display format bug"
description = '''I am using wireshark 1.8.3 (windows 7 64 bit).  In View menu, Use &quot;time display format&quot; &quot;seconds since previous displayed packet&quot; Choose a packet, right click and select &quot;set time reference&quot; Approve the checkbox &quot;Switch to the appropriate Time Display Format?&quot; Choose a packet, right click and select...'''
date = "2015-03-19T06:23:00Z"
lastmod = "2015-03-19T23:37:00Z"
weight = 40684
keywords = [ "timedisplayformat" ]
aliases = [ "/questions/40684" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Time Display format bug](/questions/40684/time-display-format-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40684-score" class="post-score" title="current number of votes">0</div><span id="post-40684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark 1.8.3 (windows 7 64 bit).</p><ol><li>In View menu, Use "time display format" "seconds since previous displayed packet"</li><li>Choose a packet, right click and select "set time reference"</li><li>Approve the checkbox "Switch to the appropriate Time Display Format?"</li><li>Choose a packet, right click and select "set time reference"</li><li>In View menu, The "time display format" remains "seconds since previous displayed packet", but the actual display format is time since first packet. The only way to change back - select another display format and than again "seconds since previous displayed packet".</li></ol><p>Thanks, Elkana B</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timedisplayformat" rel="tag" title="see questions tagged &#39;timedisplayformat&#39;">timedisplayformat</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '15, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/2d3db1d74832604414387026e5bc3c8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lkanab&#39;s gravatar image" /><p><span>lkanab</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lkanab has no accepted answers">0%</span></p></div></div><div id="comments-container-40684" class="comments-container"><span id="40686"></span><div id="comment-40686" class="comment"><div id="post-40686-score" class="comment-score"></div><div class="comment-text"><p>Any particular reason working with this outdated Wireshark version? Version 1.12 is the current release branch, while 1.10 is the 'old stable' one. Yours is even older.</p></div><div id="comment-40686-info" class="comment-info"><span class="comment-age">(19 Mar '15, 06:38)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="40690"></span><div id="comment-40690" class="comment"><div id="post-40690-score" class="comment-score"></div><div class="comment-text"><p>The OP should be on a more recent version, but this behavior is still present in 1.10.13 and 1.12.4.</p></div><div id="comment-40690-info" class="comment-info"><span class="comment-age">(19 Mar '15, 10:42)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-40684" class="comment-tools"></div><div class="clear"></div><div id="comment-40684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40710"></span>

<div id="answer-container-40710" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40710-score" class="post-score" title="current number of votes">0</div><span id="post-40710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The fourth word in the subject line of this question, as originally posted, indicates where this should be posted. :-)</p><p>I.e., if you know it's a bug, file it on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> so that it can be properly tracked as a bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '15, 23:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40710" class="comments-container"></div><div id="comment-tools-40710" class="comment-tools"></div><div class="clear"></div><div id="comment-40710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

