+++
type = "question"
title = "Filtering Initial Capture File"
description = '''Hi, I&#x27;m wanting to filter the initial capture file using the following expression &quot;(expert.message contains &quot;GET /Pages/Home.aspx&quot;) &amp;amp;&amp;amp; (ip.dst == x.x.x.x)&quot;. Unfortunately when I come to setup the capture file and apply the filter it won&#x27;t accept the expression. It would be much appreicated i...'''
date = "2012-07-30T11:04:00Z"
lastmod = "2012-07-30T13:02:00Z"
weight = 13121
keywords = [ "capture-filter" ]
aliases = [ "/questions/13121" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering Initial Capture File](/questions/13121/filtering-initial-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13121-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm wanting to filter the initial capture file using the following expression "(expert.message contains "GET /Pages/<a href="http://Home.aspx">Home.aspx</a>") &amp;&amp; (ip.dst == x.x.x.x)". Unfortunately when I come to setup the capture file and apply the filter it won't accept the expression.</p><p>It would be much appreicated if you could point me in the right direction.</p><p>Thanks!!</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '12, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/bd7046c4497013821ad749013d2e9e34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Testsubjec&#39;s gravatar image" /><p>Testsubjec<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Testsubjec has no accepted answers">0%</span></p></div></div><div id="comments-container-13121" class="comments-container"><span id="13125"></span><div id="comment-13125" class="comment"><div id="post-13125-score" class="comment-score"></div><div class="comment-text"><p>sounds like a version problem. It works with Wireshark 1.8.1.</p></div><div id="comment-13125-info" class="comment-info"><span class="comment-age">(30 Jul '12, 12:27)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13121" class="comment-tools"></div><div class="clear"></div><div id="comment-13121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13126"></span>

<div id="answer-container-13126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13126-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Besides that your filter works with Wireshark 1.8.1, I suggest to use the following display filter, which should work with pretty much every Wireshark version (at least with the last few releases).</p><blockquote><p><code>ip.dst == 1.2.3.4 and http.request.method == "GET" and http.request.uri contains "/Pages/Home.aspx"</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '12, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13126" class="comments-container"></div><div id="comment-tools-13126" class="comment-tools"></div><div class="clear"></div><div id="comment-13126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13128"></span>

<div id="answer-container-13128" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13128-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your expression worked fine for me in Wireshark 1.6.9 (substituting a real address in place of "x.x.x.x" of course). Are you trying to apply a capture filter or a display filter? Your expression is a display filter. It will not work as a capture filter; display filters and capture filters use different syntax.</p><p>There is no capture filter equivalent to "expert.message contains". You will have to capture the data first, and then apply that as a display filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '12, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-13128" class="comments-container"></div><div id="comment-tools-13128" class="comment-tools"></div><div class="clear"></div><div id="comment-13128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

