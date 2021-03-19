+++
type = "question"
title = "Wireshark question"
description = '''Hi, I am a beginner learning to use Wireshark to detect network vulnerabilities. Once I capture a packet, can anybody tell me one way I can detect unusual traffic in the captured data? Thanks, James'''
date = "2014-03-27T12:50:00Z"
lastmod = "2014-03-27T13:22:00Z"
weight = 31235
keywords = [ "network", "wireshark" ]
aliases = [ "/questions/31235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark question](/questions/31235/wireshark-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am a beginner learning to use Wireshark to detect network vulnerabilities. Once I capture a packet, can anybody tell me one way I can detect unusual traffic in the captured data?</p><p>Thanks, James</p></div><div id="question-tags" class="tags-container tags">network wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '14, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/4ca7fd3a03d4e23794f6dbd416047569?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koel26&#39;s gravatar image" /><p>koel26<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koel26 has no accepted answers">0%</span></p></div></div><div id="comments-container-31235" class="comments-container"></div><div id="comment-tools-31235" class="comment-tools"></div><div class="clear"></div><div id="comment-31235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31237"></span>

<div id="answer-container-31237" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31237-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>can anybody tell me one way I can detect <strong>unusual traffic</strong> in the captured data?</p></blockquote><p>well, <strong>unusual</strong> means different things in different networks. If you only have Windows hosts on your network, SSH (Secure Shell traffic) or X11 could be 'unusual'. If you have only Linux, Unix or *BSD systems on your network, <strong>Netbios</strong> could be 'unusual'.</p><p>As you see, it depends on the definition of 'unusual' and the environment you are looking at.</p><p>To answer your question: You will be able to detect <strong>unusual</strong> traffic in networks, if you have a <strong>lot of experience</strong> with networking in general and typical networking protocols. With that kind of knowledge you will <strong>sometimes</strong> spot things in a capture file that shouldn't be there. Unfortunately, there is no 'simple' method or best practice what to look for.</p><p>So, here is how you will get that experience:</p><ul><li>read</li><li>practice</li><li>read</li><li>practice</li><li>read</li><li>practice</li><li>etc</li></ul><p>To be honest: I would not use Wireshark to detect 'network vulnerabilities' (can you please define what that means for you). There are better tools for that, like IPS/IDS, anomaly detection tools, etc. Just google/bing those terms and you should find some information.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Mar '14, 14:40</p></div></div><div id="comments-container-31237" class="comments-container"></div><div id="comment-tools-31237" class="comment-tools"></div><div class="clear"></div><div id="comment-31237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

