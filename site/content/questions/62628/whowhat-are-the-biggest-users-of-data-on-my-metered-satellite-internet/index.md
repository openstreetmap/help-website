+++
type = "question"
title = "Who/what are the biggest users of data on my metered satellite internet?"
description = '''I live in a rural area and can only get satellite based internet. I have a monthly data limit of 10GB. For the past several months, I have come close to hitting that limit but I&#x27;m not sure why. Is there a way to use wireshark to see what IP addresses are using the most external data? Local data is n...'''
date = "2017-07-09T19:43:00Z"
lastmod = "2017-07-09T23:06:00Z"
weight = 62628
keywords = [ "usage" ]
aliases = [ "/questions/62628" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Who/what are the biggest users of data on my metered satellite internet?](/questions/62628/whowhat-are-the-biggest-users-of-data-on-my-metered-satellite-internet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62628-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I live in a rural area and can only get satellite based internet. I have a monthly data limit of 10GB. For the past several months, I have come close to hitting that limit but I'm not sure why. Is there a way to use wireshark to see what IP addresses are using the most external data? Local data is not of concern.</p></div><div id="question-tags" class="tags-container tags">usage</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '17, 19:43</strong></p><img src="https://secure.gravatar.com/avatar/8673095cdd9d04fab476195c6258e026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="logbuilder&#39;s gravatar image" /><p>logbuilder<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="logbuilder has no accepted answers">0%</span></p></div></div><div id="comments-container-62628" class="comments-container"></div><div id="comment-tools-62628" class="comment-tools"></div><div class="clear"></div><div id="comment-62628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62630"></span>

<div id="answer-container-62630" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62630-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is intended to look at network traffic in as much details as possible, up to the individual bits. What you are looking for is a statistical analysis of a month worth of traffic. As you may notice this are opposite ends of the scale. If you look at tools like <a href="http://www.ntop.org/products/traffic-analysis/ntop/">ntopng</a> these are more tailored to your needs. So, in theory Wireshark can show the network statistics, but it would be much more cumbersome than tools like mentioned.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '17, 23:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62630" class="comments-container"><span id="62631"></span><div id="comment-62631" class="comment"><div id="post-62631-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much for that answer. I had not used wireshark but it was something I knew was good for looking at network traffic. I just downloaded ntop and it looks like it has what I am interested in.</p><p>Thanks again. You saved me lots of time.</p></div><div id="comment-62631-info" class="comment-info"><span class="comment-age">(10 Jul '17, 00:55)</span> logbuilder</div></div><span id="62632"></span><div id="comment-62632" class="comment"><div id="post-62632-score" class="comment-score"></div><div class="comment-text"><p>If an Answer was useful, mark it as such by clicking the checkmark icon next to it, to help others find usefully answered questions. See site FAQ for details.</p></div><div id="comment-62632-info" class="comment-info"><span class="comment-age">(10 Jul '17, 01:18)</span> sindy</div></div></div><div id="comment-tools-62630" class="comment-tools"></div><div class="clear"></div><div id="comment-62630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

