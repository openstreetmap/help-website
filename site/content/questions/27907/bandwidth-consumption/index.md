+++
type = "question"
title = "bandwidth consumption"
description = '''I got some data from wireshark for the conversation between the client (B) and the server (A) and I am trying to do some analysis as far as the bandwidth consumption is concerned. The WAN link on the client side is a T1 and the link on the server side is 3MB. I have Wireshark captured on both ends. ...'''
date = "2013-12-07T20:38:00Z"
lastmod = "2013-12-08T00:48:00Z"
weight = 27907
keywords = [ "conversation", "bandwidth", "bps" ]
aliases = [ "/questions/27907" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [bandwidth consumption](/questions/27907/bandwidth-consumption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27907-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I got some data from wireshark for the conversation between the client (B) and the server (A) and I am trying to do some analysis as far as the bandwidth consumption is concerned.</p><p>The WAN link on the client side is a T1 and the link on the server side is 3MB. I have Wireshark captured on both ends.</p><p>Here it goes... This is the data from the statistic-&gt;conversation in Wireshark on the server side (3MB link). I got the A-&gt;B as 200,000 bps (0.19073 Mbps) and B-&gt;A as 50,000bps.</p><p>Questions: - Is it valid to say that the traffic from A-&gt;B (outbound of the gateway) takes ~7% (which is (0.19073/3)*100) of the 3MB? - Is it valid to say that the traffic from B-&gt;A (inbound of the gateway) takes 1.7% of the 3MB?</p></div><div id="question-tags" class="tags-container tags">conversation bandwidth bps</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '13, 20:38</strong></p><img src="https://secure.gravatar.com/avatar/4bf9a4681570406f873b404a912f2a7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="character9&#39;s gravatar image" /><p>character9<br />
<span class="score" title="16 reputation points">16</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="character9 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '13, 00:48</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-27907" class="comments-container"></div><div id="comment-tools-27907" class="comment-tools"></div><div class="clear"></div><div id="comment-27907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27912"></span>

<div id="answer-container-27912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27912-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it valid to say that the traffic from A-&gt;B (<strong>outbound</strong> of the gateway) takes ~7% of the 3MBbit/s?</p></blockquote><p>Yes, it 'takes' (actually it uses) 7% of the line, but only if the line offers 3 Mbit/s <strong>outbound</strong> bandwidth.</p><blockquote><ul><li>Is it valid to say that the traffic from B-&gt;A (<strong>inbound</strong> of the gateway) takes 1.7% of the 3MB?</li></ul></blockquote><p>Yes, it 'takes' (actually it uses) 1.7% of the line, but only if the line offers 3 Mbit/s <strong>inbound</strong> bandwidth.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '13, 00:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '13, 02:11</p></div></div><div id="comments-container-27912" class="comments-container"></div><div id="comment-tools-27912" class="comment-tools"></div><div class="clear"></div><div id="comment-27912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

