+++
type = "question"
title = "Nº windows event"
description = '''¿what is the windows event when run wireshark?'''
date = "2014-06-05T02:22:00Z"
lastmod = "2014-06-05T13:41:00Z"
weight = 33425
keywords = [ "pregunda" ]
aliases = [ "/questions/33425" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nº windows event](/questions/33425/no-windows-event)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33425-score" class="post-score" title="current number of votes">0</div><span id="post-33425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>¿what is the windows event when run wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pregunda" rel="tag" title="see questions tagged &#39;pregunda&#39;">pregunda</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '14, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/bad5368b645850344600d4ca775a0946?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="agonsed&#39;s gravatar image" /><p><span>agonsed</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="agonsed has no accepted answers">0%</span></p></div></div><div id="comments-container-33425" class="comments-container"><span id="33429"></span><div id="comment-33429" class="comment"><div id="post-33429-score" class="comment-score"></div><div class="comment-text"><p>Your question doesn't make much sense to me, can you try to describe your issue another way?</p></div><div id="comment-33429-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:36)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="33430"></span><div id="comment-33430" class="comment"><div id="post-33430-score" class="comment-score"></div><div class="comment-text"><p>I guess he wants to know what event ID shows up in the windows event log when Wireshark is run. Probably to be able to detect if anyone is using Wireshark unauthorized.</p></div><div id="comment-33430-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:38)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-33425" class="comment-tools"></div><div class="clear"></div><div id="comment-33425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33473"></span>

<div id="answer-container-33473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33473-score" class="post-score" title="current number of votes">0</div><span id="post-33473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no special windows event for Wireshark, but if you enable Security Audit Logging on Windows, it will log every process start with the event ID 4688. The log entry contains the process name, user, etc.</p><blockquote><p><a href="http://technet.microsoft.com/en-us/library/dd941613%28v=ws.10%29.aspx">http://technet.microsoft.com/en-us/library/dd941613%28v=ws.10%29.aspx</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33473" class="comments-container"></div><div id="comment-tools-33473" class="comment-tools"></div><div class="clear"></div><div id="comment-33473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

