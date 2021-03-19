+++
type = "question"
title = "SIP tracing for connected Gigaset unit."
description = '''Siemens support have asked me to do a Wireshark trace of SIP traffic to/from a Gigaset unit connected to my Thompson Router. I have a windows PC also connected to the same router but, as all the SIP UDP traffic is routed to the GIGASET box, I cannot see how to set up the wireshark trace they are ask...'''
date = "2011-07-05T02:51:00Z"
lastmod = "2011-07-05T10:57:00Z"
weight = 4902
keywords = [ "sip" ]
aliases = [ "/questions/4902" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SIP tracing for connected Gigaset unit.](/questions/4902/sip-tracing-for-connected-gigaset-unit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4902-score" class="post-score" title="current number of votes">0</div><span id="post-4902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Siemens support have asked me to do a Wireshark trace of SIP traffic to/from a Gigaset unit connected to my Thompson Router. I have a windows PC also connected to the same router but, as all the SIP UDP traffic is routed to the GIGASET box, I cannot see how to set up the wireshark trace they are asking for (the PC running Wireshark will, I imagine, not see any of the traffic).</p><p>Am I mistaken or are they asking for the impossible.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '11, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/22958daf7551a9442531d290036bb577?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ColinAllinson&#39;s gravatar image" /><p><span>ColinAllinson</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ColinAllinson has no accepted answers">0%</span></p></div></div><div id="comments-container-4902" class="comments-container"></div><div id="comment-tools-4902" class="comment-tools"></div><div class="clear"></div><div id="comment-4902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4906"></span>

<div id="answer-container-4906" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4906-score" class="post-score" title="current number of votes">1</div><span id="post-4906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ColinAllinson has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not completely impossible but probably a little bit too much to ask if you're not familiar with capturing network packets. You'd need to either put in a hub or a switch with SPAN port feature to be able to monitor the communication between your SIP phone and your router. Or maybe your router has a packet dump feature that can be used to capture the phone line. Still, if you've never done anything like this it is a bit strange that they expect you to be able to figure this one out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '11, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4906" class="comments-container"><span id="4910"></span><div id="comment-4910" class="comment"><div id="post-4910-score" class="comment-score"></div><div class="comment-text"><p>Thank you for you help. You are right, although I am fairly technically literate, my area of expertise is somewhat different to this and this does seem beyond me. I have replied back to Siemens Gigaset support saying that either I have misunderstood what they were asking for or I am not able to perform this task.</p></div><div id="comment-4910-info" class="comment-info"><span class="comment-age">(05 Jul '11, 10:57)</span> <span class="comment-user userinfo">ColinAllinson</span></div></div></div><div id="comment-tools-4906" class="comment-tools"></div><div class="clear"></div><div id="comment-4906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

