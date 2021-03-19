+++
type = "question"
title = "Is there a &#x27;post-capture&#x27; filter?"
description = '''Hi If my understanding is correct, capture filters are designed to discard packets before any processing takes place. Is there a way to discard packets after decryption? That is to allow Wireshark to decrypt using the information provided and then discard the unwanted packets so that they don&#x27;t take...'''
date = "2015-08-12T08:35:00Z"
lastmod = "2015-08-12T09:01:00Z"
weight = 45006
keywords = [ "filter" ]
aliases = [ "/questions/45006" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a 'post-capture' filter?](/questions/45006/is-there-a-post-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45006-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>If my understanding is correct, capture filters are designed to discard packets before any processing takes place. Is there a way to discard packets after decryption? That is to allow Wireshark to decrypt using the information provided and then discard the unwanted packets so that they don't take up memory. If not the GUI, could tshark handle it something similar?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/3c16c3b7b9d89a5736de02187a6253d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mun&#39;s gravatar image" /><p>mun<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mun has no accepted answers">0%</span></p></div></div><div id="comments-container-45006" class="comments-container"></div><div id="comment-tools-45006" class="comment-tools"></div><div class="clear"></div><div id="comment-45006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45009"></span>

<div id="answer-container-45009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45009-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is called the Read Filter. Open up the Open Capture File dialog and notice the filter at the southwest side of the dialog. It's a display filter format entry field which is used to filter packets when being loaded. The same can be achieved using -R on the command line for both Wireshark or Tshark.</p><p>(Note: you'll have to save the capture file first, then read it again, but this is as closed as it gets AFAIK).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Aug '15, 09:03</p></div></div><div id="comments-container-45009" class="comments-container"><span id="45010"></span><div id="comment-45010" class="comment"><div id="post-45010-score" class="comment-score"></div><div class="comment-text"><p>I see what you mean. But I was hoping for a 'post-capture' filter to be applied during capturing so that packets are discarded after processing during capturing. Is there something similar?</p></div><div id="comment-45010-info" class="comment-info"><span class="comment-age">(12 Aug '15, 09:05)</span> mun</div></div></div><div id="comment-tools-45009" class="comment-tools"></div><div class="clear"></div><div id="comment-45009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

