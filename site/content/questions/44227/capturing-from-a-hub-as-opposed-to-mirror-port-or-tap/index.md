+++
type = "question"
title = "Capturing from a Hub as opposed to Mirror Port or TAP"
description = '''Hi, I was checking some capturing methods while I wait for a TAP purchase to go through: I noticed that when I mirror a port there is a LOT of slow down in the delivery of the packets to me. The client has long since finished his session and the mirror is still delivering packets from it. Okay, swit...'''
date = "2015-07-16T23:56:00Z"
lastmod = "2015-07-17T01:44:00Z"
weight = 44227
keywords = [ "capture", "packetdelay", "hub" ]
aliases = [ "/questions/44227" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing from a Hub as opposed to Mirror Port or TAP](/questions/44227/capturing-from-a-hub-as-opposed-to-mirror-port-or-tap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44227-score" class="post-score" title="current number of votes">0</div><span id="post-44227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I was checking some capturing methods while I wait for a TAP purchase to go through: I noticed that when I mirror a port there is a LOT of slow down in the delivery of the packets to me. The client has long since finished his session and the mirror is still delivering packets from it. Okay, switch may be busy, lets try a hub.</p><p>Delay is now gone, everything looks good: Except that the packets are coming in in bursts. Every 15-16ms a large chunk of data arrives all with the same Timestamp, down to microseconds, which obviously makes reading the trace later somewhat interesting with out of order and retransmissions all occurring at the same time. I do not know 100% what is an issue and what is not.</p><p>Is this usual behaviour or is my hub ever so slightly mad? Am I just going to have to wait for my dedicated TAP to be really be sure?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packetdelay" rel="tag" title="see questions tagged &#39;packetdelay&#39;">packetdelay</span> <span class="post-tag tag-link-hub" rel="tag" title="see questions tagged &#39;hub&#39;">hub</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '15, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-44227" class="comments-container"></div><div id="comment-tools-44227" class="comment-tools"></div><div class="clear"></div><div id="comment-44227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44229"></span>

<div id="answer-container-44229" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44229-score" class="post-score" title="current number of votes">0</div><span id="post-44229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DarrenWright has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like both SPAN and hub are doing things in a strange way, so yes, go for a TAP to see what really happens.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44229" class="comments-container"><span id="44230"></span><div id="comment-44230" class="comment"><div id="post-44230-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, yeah. I managed to finally get a sign off on the ProfiShark 1G. Now I just need to wait some time..</p></div><div id="comment-44230-info" class="comment-info"><span class="comment-age">(17 Jul '15, 01:44)</span> <span class="comment-user userinfo">DarrenWright</span></div></div></div><div id="comment-tools-44229" class="comment-tools"></div><div class="clear"></div><div id="comment-44229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

