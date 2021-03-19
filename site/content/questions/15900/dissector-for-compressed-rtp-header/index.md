+++
type = "question"
title = "dissector for compressed RTP header"
description = '''Ok, Here is another question. A thousand points to whoever can help me.  Lets say my protocol consist of only one byte. This byte indicates if this is a compressed RTP header or Uncompressed RTP header following.  Now, if it is a uncompressed header, I want to apply the rtp dissector. (which I now k...'''
date = "2012-11-14T05:40:00Z"
lastmod = "2012-11-22T04:48:00Z"
weight = 15900
keywords = [ "dissector", "rtp" ]
aliases = [ "/questions/15900" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dissector for compressed RTP header](/questions/15900/dissector-for-compressed-rtp-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15900-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok, Here is another question. A thousand points to whoever can help me.</p><p>Lets say my protocol consist of only one byte. This byte indicates if this is a compressed RTP header or Uncompressed RTP header following.</p><p>Now, if it is a uncompressed header, I want to apply the rtp dissector. (which I now know, thank you Jaap)<br />
</p><p>However, if it is a compressed header, I want to add my own decoding (since there does not exist an dissector for rtp compressed)</p><p>How can I do this in the best manner? I am very grateful for the help !</p></div><div id="question-tags" class="tags-container tags">dissector rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '12, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/7709c0c87ed4ba426f119187d3f0c705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harkap&#39;s gravatar image" /><p>harkap<br />
<span class="score" title="5 reputation points">5</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harkap has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 21 Nov '12, 02:05</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-15900" class="comments-container"><span id="16190"></span><div id="comment-16190" class="comment"><div id="post-16190-score" class="comment-score"></div><div class="comment-text"><p>Does anyone know if this is possible to do?</p></div><div id="comment-16190-info" class="comment-info"><span class="comment-age">(21 Nov '12, 23:36)</span> harkap</div></div><span id="16191"></span><div id="comment-16191" class="comment"><div id="post-16191-score" class="comment-score"></div><div class="comment-text"><p>To clarify the question. I have an incoming packet [ IP, UDP, My protocol, RTP ]</p><p>My protocol consist of just one byte. The data is 1 if the RTP header is compressed. 0 if it is uncompressed.</p><p>I want to read my byte, and depending on it, decode the RTP.</p><p>Thank you!</p></div><div id="comment-16191-info" class="comment-info"><span class="comment-age">(21 Nov '12, 23:38)</span> harkap</div></div><span id="16193"></span><div id="comment-16193" class="comment"><div id="post-16193-score" class="comment-score"></div><div class="comment-text"><p>@harkap, I've converted your "answers" to comments as that's how this site works. Please read the FAQ for more info.</p><p>Be patient, when someone has knowledge of the problem and some spare time they'll post an answer that may help.</p></div><div id="comment-16193-info" class="comment-info"><span class="comment-age">(22 Nov '12, 00:40)</span> grahamb ♦</div></div></div><div id="comment-tools-15900" class="comment-tools"></div><div class="clear"></div><div id="comment-15900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16205"></span>

<div id="answer-container-16205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16205-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If there's a control protocol, like SDP or H.245, setting up conversations with RTP as dissector it might be tricky to get in between them. If not you can use registering for UDP, so 'Decode as' works, or any of the other ways RTP employs itself to register for traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16205" class="comments-container"></div><div id="comment-tools-16205" class="comment-tools"></div><div class="clear"></div><div id="comment-16205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

