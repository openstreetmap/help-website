+++
type = "question"
title = "Diameter credit control application sessions without termination"
description = '''Hi all, Could someone suggest a way to display or filter diameter session ID&#x27;s that have an initial request (CCR-I) but did not get a termination request (CCR-T)? I think this would be a two step process but just trying to find a way to do it with an expression rather than going session by session. ...'''
date = "2016-09-06T08:32:00Z"
lastmod = "2016-09-06T08:50:00Z"
weight = 55355
keywords = [ "diameter" ]
aliases = [ "/questions/55355" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter credit control application sessions without termination](/questions/55355/diameter-credit-control-application-sessions-without-termination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55355-score" class="post-score" title="current number of votes">0</div><span id="post-55355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Could someone suggest a way to display or filter diameter session ID's that have an initial request (CCR-I) but did not get a termination request (CCR-T)?</p><p>I think this would be a two step process but just trying to find a way to do it with an expression rather than going session by session.</p><p>Thanks a lot!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '16, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/a21450eb99e4a2e030ea4cbd77925799?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kanutomay&#39;s gravatar image" /><p><span>kanutomay</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kanutomay has no accepted answers">0%</span></p></div></div><div id="comments-container-55355" class="comments-container"></div><div id="comment-tools-55355" class="comment-tools"></div><div class="clear"></div><div id="comment-55355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55356"></span>

<div id="answer-container-55356" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55356-score" class="post-score" title="current number of votes">1</div><span id="post-55356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Consider using <a href="https://wiki.wireshark.org/Mate">MATE</a>. It allows to add metafields to packets' dissection trees based on custom-defined relationships between packets. So in your case, MATE would provide a meta-field (like <code>mate.ccr-session.terminated</code>), indicating whether the CCR-T has been captured for a given session ID, to all packets sharing that session ID. This would allow you to display-filter all CCR-I for which no matching CCR-T is present in the capture, using an expression like <code>diameter.CC-Request-Type == 1 and !mate.ccr-session.terminated</code>.</p><p>As you've anticipated, it actually is a two step process, but the first step is done by Wireshark as part of packet dissection so you can just use the result.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '16, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Sep '16, 10:49</strong> </span></p></div></div><div id="comments-container-55356" class="comments-container"></div><div id="comment-tools-55356" class="comment-tools"></div><div class="clear"></div><div id="comment-55356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

