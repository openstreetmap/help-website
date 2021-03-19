+++
type = "question"
title = "Wireshark not interpreting some SSL traffic"
description = '''Hi guys, I am using the v2.0.5 however for some SSL traffic, it does not interpret the &quot;Server Hello&quot; packet correctly. For example in a working one I see more &quot;Handshake Protocol&quot; fields such as &quot;Certificate&quot;, &quot;Server Key Exchange&quot;... etc however the non-working one only shows the &quot;Server Hello&quot; fi...'''
date = "2016-08-24T13:18:00Z"
lastmod = "2016-08-25T21:49:00Z"
weight = 55098
keywords = [ "ssl" ]
aliases = [ "/questions/55098" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not interpreting some SSL traffic](/questions/55098/wireshark-not-interpreting-some-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55098-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I am using the v2.0.5 however for some SSL traffic, it does not interpret the "Server Hello" packet correctly. For example in a working one I see more "Handshake Protocol" fields such as "Certificate", "Server Key Exchange"... etc however the non-working one only shows the "Server Hello" field. Please find my screenshots at this link</p><p><a href="https://www.dropbox.com/s/xn45gij35qfaf9v/Untitled.png?dl=0">https://www.dropbox.com/s/xn45gij35qfaf9v/Untitled.png?dl=0</a></p><p>Thanks! Difan</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '16, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/08a7db94810c538eed59c44ad2601ae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="difan&#39;s gravatar image" /><p>difan<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="difan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '16, 13:19</p></div></div><div id="comments-container-55098" class="comments-container"><span id="55108"></span><div id="comment-55108" class="comment"><div id="post-55108-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-55108-info" class="comment-info"><span class="comment-age">(25 Aug '16, 02:20)</span> Jaap ♦</div></div><span id="55116"></span><div id="comment-55116" class="comment"><div id="post-55116-score" class="comment-score"></div><div class="comment-text"><p>absolutely. <a href="https://www.dropbox.com/s/y3f451iajma2z6v/analytics.pcap?dl=0">https://www.dropbox.com/s/y3f451iajma2z6v/analytics.pcap?dl=0</a></p><p>Thanks!</p></div><div id="comment-55116-info" class="comment-info"><span class="comment-age">(25 Aug '16, 08:13)</span> difan</div></div></div><div id="comment-tools-55098" class="comment-tools"></div><div class="clear"></div><div id="comment-55098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55121"></span>

<div id="answer-container-55121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55121-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your trace did not contain full packets therefore wireshark cannot dissect the TLS protocol.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_248.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '16, 21:49</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-55121" class="comments-container"></div><div id="comment-tools-55121" class="comment-tools"></div><div class="clear"></div><div id="comment-55121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

