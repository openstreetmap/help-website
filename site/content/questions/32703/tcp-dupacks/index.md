+++
type = "question"
title = "TCP DupACKs"
description = '''hi there  i have a client keeps sending a lot of [FIN, ACK] after sending &#x27;&#x27;TCP DupACKs&#x27;&#x27; to the server. what could be the reason.'''
date = "2014-05-10T02:52:00Z"
lastmod = "2014-05-10T12:52:00Z"
weight = 32703
keywords = [ "tcpdupacks" ]
aliases = [ "/questions/32703" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP DupACKs](/questions/32703/tcp-dupacks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32703-score" class="post-score" title="current number of votes">0</div><span id="post-32703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi there</p><p>i have a client keeps sending a lot of [FIN, ACK] after sending ''TCP DupACKs'' to the server.</p><p>what could be the reason.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdupacks" rel="tag" title="see questions tagged &#39;tcpdupacks&#39;">tcpdupacks</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '14, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/66908e9fba5a8e0303a26830cf1c139a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Safwan%20Khairi%20Hallfawi&#39;s gravatar image" /><p><span>Safwan Khair...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Safwan Khairi Hallfawi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> wikified <strong>10 May '14, 02:53</strong> </span></p></div></div><div id="comments-container-32703" class="comments-container"></div><div id="comment-tools-32703" class="comment-tools"></div><div class="clear"></div><div id="comment-32703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32707"></span>

<div id="answer-container-32707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32707-score" class="post-score" title="current number of votes">0</div><span id="post-32707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is not unusual to see those in a packet capture: - sending DupACKs means the TCP stack has seen inbound packets arriving out of order - sending a FIN,ACK means the local socket application has issued a close() call, terminating the tcp connection in an orderly fashion</p><p>Both scenarios are very common and not necessarily indicative af a problem.</p><p>Could you share the capture at <a href="http://cloudshark.org"></a><a href="http://cloudshark.org">http://cloudshark.org</a> so we can give a more precise explanation</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '14, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-32707" class="comments-container"></div><div id="comment-tools-32707" class="comment-tools"></div><div class="clear"></div><div id="comment-32707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

