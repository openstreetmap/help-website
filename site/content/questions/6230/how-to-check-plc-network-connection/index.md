+++
type = "question"
title = "How to check plc network connection"
description = '''Hi, I am new to Wireshark and not a network specialist, but I have a special question, and maybe Wireshark can help me with it. I have already read the documentation (partly), but I could not find an answer. So before spending hours I would like to ask a specialist. Maybe he or she knows right away....'''
date = "2011-09-09T03:31:00Z"
lastmod = "2011-09-19T06:47:00Z"
weight = 6230
keywords = [ "windows", "capture", "analysis" ]
aliases = [ "/questions/6230" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to check plc network connection](/questions/6230/how-to-check-plc-network-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6230-score" class="post-score" title="current number of votes">0</div><span id="post-6230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am new to Wireshark and not a network specialist, but I have a special question, and maybe Wireshark can help me with it. I have already read the documentation (partly), but I could not find an answer. So before spending hours I would like to ask a specialist. Maybe he or she knows right away. Here it is:</p><p>I built up a direct communication between two PCs (Win 7) using power line adaptors. Now it will surely happen that the power line is loaded with noisy currents, and I want to find out how this influences communication quality. I thought about just displaying corrupted packets. Best would be an online display (graph, meter, or simply percentage number updated every n sec).</p><p>Is that possible with Wireshark? If yes, please give me a short hint how to start.</p><p>Thanks a lot,</p><p>Martin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '11, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/3a8ca29741032bd7a1c89a6204788138?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mr_M_from_R&#39;s gravatar image" /><p><span>Mr_M_from_R</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mr_M_from_R has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Sep '11, 13:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6230" class="comments-container"></div><div id="comment-tools-6230" class="comment-tools"></div><div class="clear"></div><div id="comment-6230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6256"></span>

<div id="answer-container-6256" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6256-score" class="post-score" title="current number of votes">1</div><span id="post-6256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to use the I/O Graph from the statistics menu for this. You can enter a filter like "tcp.analysis.lost_segment" in the filter line of Graph2, and enable it by clicking it's button. I usually use the style type "FBar" for those things, to show them as little blocks, and - if necessary - set the Y-Axxis to logarithmic.</p><p>Keep in mind that you won't see corrupted packets because your network card will drop it before Wireshark even sees it. You'll only see lost packets because of it, and the according retransmissions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '11, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6256" class="comments-container"><span id="6446"></span><div id="comment-6446" class="comment"><div id="post-6446-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>thank you for your answer and please excuse my late reaction to it. I have installed wire shark and made some tests with it, also what you suggested. Til now there are only very few lost segments but the hard conditions are not yet tested. I would like to ask one more thing for my understanding:</p><p>As much as I read a packet is said to be lost if there is no acknowledge packet returned to the sender before the corresponding RTT timer runs out. Now my question is, how it can be detected that a segment is lost and then retansmitted when being on the receiver side. I also found a filter tcp.analysis.retransmission. Would this lead to the same results as tcp.analysis.lost_segment ??</p><p>Thank you for any help</p><p>Martin</p></div><div id="comment-6446-info" class="comment-info"><span class="comment-age">(19 Sep '11, 06:47)</span> <span class="comment-user userinfo">Mr_M_from_R</span></div></div></div><div id="comment-tools-6256" class="comment-tools"></div><div class="clear"></div><div id="comment-6256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

