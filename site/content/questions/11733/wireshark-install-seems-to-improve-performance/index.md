+++
type = "question"
title = "Wireshark install seems to improve performance"
description = '''We have a web based system (HTTP) which seems to be having performance issues. In our UAT environment performance is fine, in production, there is a significant reduction. These are typically request / response type messages for data lookups (i.e. search a data cache for filtered data). UAT and Prod...'''
date = "2012-06-07T02:03:00Z"
lastmod = "2012-06-08T01:46:00Z"
weight = 11733
keywords = [ "performance" ]
aliases = [ "/questions/11733" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark install seems to improve performance](/questions/11733/wireshark-install-seems-to-improve-performance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11733-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a web based system (HTTP) which seems to be having performance issues. In our UAT environment performance is fine, in production, there is a significant reduction. These are typically request / response type messages for data lookups (i.e. search a data cache for filtered data).</p><p>UAT and Prod reside on the exactly the same infrastructure, only differecne is the hardware. I installed wireshark to moinitor network traffic and performance.</p><p>I know it sounds wierd but since I have installed wireshark, the web based applications performance has significaly improved. We have a few users, some with and some without wireshark. All those with wireshark dont seem to have the same slow performance. I know that wirehsark is simply a monitoring tool, but is there nothing that occurs that will change network parameter in some way?</p></div><div id="question-tags" class="tags-container tags">performance</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '12, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/64815e84ffd38ca630ed7be8639f7249?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jarrow&#39;s gravatar image" /><p>jarrow<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jarrow has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jun '12, 02:05</p></div></div><div id="comments-container-11733" class="comments-container"></div><div id="comment-tools-11733" class="comment-tools"></div><div class="clear"></div><div id="comment-11733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11749"></span>

<div id="answer-container-11749" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11749-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>I KNOW it sounds weird</strong>, but I have seen similar effects. As soon as the interface of a machine runs in promiscuous mode (sniffing), some applications behave differently. I cannot recall the details, but I have seen this several times. I don't have any explanation as I never tried to track it down. That is one reason why you should not sniff ON the target system you are trying to analyze.</p><p>To verify if your observation is not just a psychological effect (seeing what you believe), I suggest to do this:</p><ol><li>Find a computer with the symptoms of slow performance</li><li>Capture the slow traffic <strong>in front of that computer</strong>: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></li><li>Install wireshark on that computer and repeat step 2.</li><li>Compare the two capture files</li></ol><p>After step 4. you will see, if there is a measurable effect, or if it's just some sort of <strong>network</strong> (wind) <strong>chill factor</strong> ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '12, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '12, 05:19</p></div></div><div id="comments-container-11749" class="comments-container"><span id="11758"></span><div id="comment-11758" class="comment"><div id="post-11758-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt</p><p>Fantastic thanks, great plan. I will give it a go.</p></div><div id="comment-11758-info" class="comment-info"><span class="comment-age">(08 Jun '12, 04:11)</span> jarrow</div></div><span id="11761"></span><div id="comment-11761" class="comment"><div id="post-11761-score" class="comment-score"></div><div class="comment-text"><p>good luck!</p></div><div id="comment-11761-info" class="comment-info"><span class="comment-age">(08 Jun '12, 04:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11749" class="comment-tools"></div><div class="clear"></div><div id="comment-11749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

