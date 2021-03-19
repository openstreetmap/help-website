+++
type = "question"
title = "Multiple ip in single live capture"
description = '''Hi There, I would like to capture &quot;multiple host&quot; tcp trace in wireshark. An Example, I am getting a request from ip host &quot;a.b.c.d&quot; on port 15900 (of my server). processing this request and forward request to host &quot;w.x.y.z&quot; and listing reply on port 15122 (of my server). Processing response from hos...'''
date = "2013-11-20T21:54:00Z"
lastmod = "2013-11-21T02:44:00Z"
weight = 27193
keywords = [ "multiple-ip-capture" ]
aliases = [ "/questions/27193" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple ip in single live capture](/questions/27193/multiple-ip-in-single-live-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27193-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There,</p><p>I would like to capture "multiple host" tcp trace in wireshark. An Example, I am getting a request from ip host "a.b.c.d" on port 15900 (of my server). processing this request and forward request to host "w.x.y.z" and listing reply on port 15122 (of my server). Processing response from host "w.x.y.z" and reply back to host "a.b.c.d".</p><p>My question is, how to capture these tcp trace in single live capture. I tried combination of or &amp; and but no result. However when i run 2 live capture, one for host "a.b.c.d" and another for "w.x.y.z" its working well.</p><p>please suggest.</p><p>Thanks Vikash Kumar</p></div><div id="question-tags" class="tags-container tags">multiple-ip-capture</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/816610377460c87c2c21722bc29cd35e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VikashKumar&#39;s gravatar image" /><p>VikashKumar<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VikashKumar has no accepted answers">0%</span></p></div></div><div id="comments-container-27193" class="comments-container"></div><div id="comment-tools-27193" class="comment-tools"></div><div class="clear"></div><div id="comment-27193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27204"></span>

<div id="answer-container-27204" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27204-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try the following <strong>capture filter</strong></p><blockquote><p>(host a.b.c.d and port 15900) or (host w.x.y.z and port 15122)</p></blockquote><p>If that does not work, because the ports are changing, try the following</p><blockquote><p>host a.b.c.d or host w.x.y.z</p></blockquote><p>and then use a <strong>display filter</strong> to find whatever you are interested in.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '13, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27204" class="comments-container"></div><div id="comment-tools-27204" class="comment-tools"></div><div class="clear"></div><div id="comment-27204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

