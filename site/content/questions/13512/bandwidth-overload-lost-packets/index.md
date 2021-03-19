+++
type = "question"
title = "bandwidth overload - lost packets"
description = '''Hello, Recently we had problem with one of our branch office - due to bandwidth overload we had 35% of lost packets to that site. We contacted our ISP and they told us that on our 2mbit leased line we were using 2.7 mbit of bandwidth. This only happens at 3pm when most of application contact it&#x27;s se...'''
date = "2012-08-09T04:59:00Z"
lastmod = "2012-08-09T06:21:00Z"
weight = 13512
keywords = [ "wan", "bandwidth" ]
aliases = [ "/questions/13512" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [bandwidth overload - lost packets](/questions/13512/bandwidth-overload-lost-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13512-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Recently we had problem with one of our branch office - due to bandwidth overload we had 35% of lost packets to that site. We contacted our ISP and they told us that on our 2mbit leased line we were using 2.7 mbit of bandwidth. This only happens at 3pm when most of application contact it's servers over WAN.</p><p>I have used wireshark at exact time of WAN bandwidth overload and have captured a lot of packets.. But how can I figure our which service is doing the overload of bandwidth? As I have heard most applications are optimized to test how much bandwidth there is for use and to use it so that no overload happens..</p><p>Have you ever experienced this kind of WAN behavior?</p></div><div id="question-tags" class="tags-container tags">wan bandwidth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '12, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/051d87188981a4a8e8aec629d47db51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsladojevic&#39;s gravatar image" /><p>dsladojevic<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsladojevic has no accepted answers">0%</span></p></div></div><div id="comments-container-13512" class="comments-container"><span id="13513"></span><div id="comment-13513" class="comment"><div id="post-13513-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have used wireshark at exact time of WAN bandwidth overload and have captured a lot of packets.</p></blockquote><p>Where did you capture? At your client or in front of the WAN router?</p></div><div id="comment-13513-info" class="comment-info"><span class="comment-age">(09 Aug '12, 06:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13512" class="comment-tools"></div><div class="clear"></div><div id="comment-13512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13514"></span>

<div id="answer-container-13514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13514-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But how can I figure our which service is doing the overload of bandwidth?</p></blockquote><p>Take a look at the Protocol Statistics and at the Conversations</p><blockquote><p><code>Statistics -&gt; Protocol Hierarchy</code><br />
</p></blockquote><p>Look at the percentage of the various protocols.</p><blockquote><p><code>Statistics -&gt; Conversations -&gt; Tab: IPv4</code><br />
</p></blockquote><p>Sort the output for Bytes. Take a closer look at those conversations with the most data. Do the same for the Tab "TCP" in that GUI.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '12, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13514" class="comments-container"><span id="13532"></span><div id="comment-13532" class="comment"><div id="post-13532-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt! You have really helped me find the issue!</p></div><div id="comment-13532-info" class="comment-info"><span class="comment-age">(10 Aug '12, 03:40)</span> dsladojevic</div></div><span id="13534"></span><div id="comment-13534" class="comment"><div id="post-13534-score" class="comment-score"></div><div class="comment-text"><p>@dsladojevic I've converted your "answer" to a comment as that's how this site works, see the FAQ for more info.</p><p>If the answer does in fact answer your question, please accept it by clicking on the checkmark icon at the left hand side of the answer. This lets other folks know the correct answer(s) to your question.</p></div><div id="comment-13534-info" class="comment-info"><span class="comment-age">(10 Aug '12, 03:50)</span> grahamb ♦</div></div></div><div id="comment-tools-13514" class="comment-tools"></div><div class="clear"></div><div id="comment-13514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

