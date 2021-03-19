+++
type = "question"
title = "Newbie question on finding out why application not connecting to server"
description = '''I have a project where we are trying to figure out why client/server traffic is not making it across some segments of a client network. The systems were working, but then &quot;something&quot; was changed on the network and now they cannot connect. We think it has to do with TTL, but need to tack it down. We ...'''
date = "2011-08-10T05:18:00Z"
lastmod = "2011-08-10T05:45:00Z"
weight = 5618
keywords = [ "compare" ]
aliases = [ "/questions/5618" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie question on finding out why application not connecting to server](/questions/5618/newbie-question-on-finding-out-why-application-not-connecting-to-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5618-score" class="post-score" title="current number of votes">0</div><span id="post-5618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a project where we are trying to figure out why client/server traffic is not making it across some segments of a client network. The systems were working, but then "something" was changed on the network and now they cannot connect. We think it has to do with TTL, but need to tack it down. We had a similar problem in the past and it was solved by a third party taking a wireshark trace from one location on the network where the client could connect to the server and then at a second location where the client could not connect and comparing them. I know how to do the two traces, but am not sure where to go in wireshark (or third party tools) to compare the traces to find what is missing. Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compare" rel="tag" title="see questions tagged &#39;compare&#39;">compare</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '11, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/086ce001bb9154e25a84cb2ea5c56510?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dclark&#39;s gravatar image" /><p><span>dclark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dclark has no accepted answers">0%</span></p></div></div><div id="comments-container-5618" class="comments-container"></div><div id="comment-tools-5618" class="comment-tools"></div><div class="clear"></div><div id="comment-5618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5619"></span>

<div id="answer-container-5619" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5619-score" class="post-score" title="current number of votes">0</div><span id="post-5619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark cuts your packets to bits and gives you back the bloody ends. You'll have to know the protocols used in order to make your analysis. Although Wireshark helps you with the individual traces, comparing them is another matter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '11, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5619" class="comments-container"></div><div id="comment-tools-5619" class="comment-tools"></div><div class="clear"></div><div id="comment-5619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

