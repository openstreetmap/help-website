+++
type = "question"
title = "How to count packets per second?"
description = '''Hello all, I have been using wireshark for while, but I am stuck in a question. I am using Windows cause I am doing that in the college. I am doing a VoIP call and capturing the traffic with wireshark, so I wanna know the number of RTP packets in on second. How I can do that besides counting them ba...'''
date = "2015-06-17T14:32:00Z"
lastmod = "2015-06-17T21:40:00Z"
weight = 43285
keywords = [ "voipcalls", "rtp", "voip", "wireshark" ]
aliases = [ "/questions/43285" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to count packets per second?](/questions/43285/how-to-count-packets-per-second)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43285-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all, I have been using wireshark for while, but I am stuck in a question. I am using Windows cause I am doing that in the college. I am doing a VoIP call and capturing the traffic with wireshark, so I wanna know the number of RTP packets in on second. How I can do that besides counting them based on the wireshark time.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">voipcalls rtp voip wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a5a800fe37aa77679c4d5b8aca375e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ethaless&#39;s gravatar image" /><p>ethaless<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ethaless has no accepted answers">0%</span></p></div></div><div id="comments-container-43285" class="comments-container"></div><div id="comment-tools-43285" class="comment-tools"></div><div class="clear"></div><div id="comment-43285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43299"></span>

<div id="answer-container-43299" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43299-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Statistics -&gt; Summary on your filtered packets should give you the average <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-247.png" alt="alt text" /><br />
Statistics -&gt; IO Graph allows you to draw a graph of packets/tick over the time. <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-248.png" alt="alt text" /></p><p>Did you try those and does it do want you want?<br />
Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 21:40</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-43299" class="comments-container"></div><div id="comment-tools-43299" class="comment-tools"></div><div class="clear"></div><div id="comment-43299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

