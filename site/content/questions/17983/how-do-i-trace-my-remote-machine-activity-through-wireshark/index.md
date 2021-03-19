+++
type = "question"
title = "how do i trace my remote machine Activity through wireshark"
description = '''how do i trace my remote machine Activity through wireshark...?'''
date = "2013-01-27T05:14:00Z"
lastmod = "2013-01-27T11:20:00Z"
weight = 17983
keywords = [ "remote-monitoring" ]
aliases = [ "/questions/17983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how do i trace my remote machine Activity through wireshark](/questions/17983/how-do-i-trace-my-remote-machine-activity-through-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17983-score" class="post-score" title="current number of votes">0</div><span id="post-17983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how do i trace my remote machine Activity through wireshark...?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote-monitoring" rel="tag" title="see questions tagged &#39;remote-monitoring&#39;">remote-monitoring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '13, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/9c542ef867fb68a2cf3a5725ad24d3e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaushal&#39;s gravatar image" /><p><span>kaushal</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaushal has no accepted answers">0%</span></p></div></div><div id="comments-container-17983" class="comments-container"></div><div id="comment-tools-17983" class="comment-tools"></div><div class="clear"></div><div id="comment-17983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17988"></span>

<div id="answer-container-17988" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17988-score" class="post-score" title="current number of votes">0</div><span id="post-17988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, you need to capture the packets the remote machine sends and receives. Maybe this URL can help with the basic setup to do that:</p><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>If all else fails you could install Wireshark on the remote machine, but that is always a "last resort" action since it will not always give correct results. Maybe you could also use rpcapd, which is part of WinPCAP (if your remote machine is a Windows box), but while allowing convenient remote captures there are some drawbacks and additional Wireshark configuration work to be done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '13, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17988" class="comments-container"></div><div id="comment-tools-17988" class="comment-tools"></div><div class="clear"></div><div id="comment-17988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

