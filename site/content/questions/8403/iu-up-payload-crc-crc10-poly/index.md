+++
type = "question"
title = "Iu UP payload CRC - CRC10 poly"
description = '''Hi All, CRC-10 poly = G(D) = D^10+D^9+D^5+D^4+D^1+1 I thought it is simple CRC-10 implementation. But Wireshark does this in different way. Why it so? You can find the code here. Wireshark code is different. Due to this I am getting CRC error in Iu UP layer.  If the way I implement is wrong then ple...'''
date = "2012-01-16T03:36:00Z"
lastmod = "2012-01-16T15:17:00Z"
weight = 8403
keywords = [ "iuup" ]
aliases = [ "/questions/8403" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Iu UP payload CRC - CRC10 poly](/questions/8403/iu-up-payload-crc-crc10-poly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8403-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>CRC-10 poly = G(D) = D^10+D^9+D^5+D^4+D^1+1</p><p>I thought it is simple CRC-10 implementation. But Wireshark does this in different way. Why it so?</p><p>You can find the code <a href="http://www.packet.cc/files/CRC-10-code-ex.html">here</a>.</p><p>Wireshark code is different. Due to this I am getting CRC error in Iu UP layer.</p><p>If the way I implement is wrong then please explain how Wireshark is calculating CRC-10.</p></div><div id="question-tags" class="tags-container tags">iuup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '12, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/f80796612a9bd2e5c17778ae0a41d8ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prithvi&#39;s gravatar image" /><p>prithvi<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prithvi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '12, 15:04</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-8403" class="comments-container"></div><div id="comment-tools-8403" class="comment-tools"></div><div class="clear"></div><div id="comment-8403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8419"></span>

<div id="answer-container-8419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8419-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The referenced code is notoriously hard to read due to lack of proper indentation. From what I can make out there's little difference between this and the Wireshark code found <a href="http://anonsvn.wireshark.org/wireshark/trunk/wsutil/crc10.c">here</a>. You may want to look at the lookup table generation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '12, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8419" class="comments-container"><span id="8422"></span><div id="comment-8422" class="comment"><div id="post-8422-score" class="comment-score"></div><div class="comment-text"><p>If you have compared the Wireshark code &amp; the code in the referenced link then you would have found that first loop is same in both.</p><p>crc10_accum = ((crc10_accum &lt;&lt; 8) &amp; 0x3ff) ^ byte_crc10_table[( crc10_accum &gt;&gt; 2) &amp; 0xff] ^ (crc10&gt;&gt;2);</p><p>crc10_accum = ((crc10_accum &lt;&lt; 8) &amp; 0x3ff) ^ byte_crc10_table[( crc10_accum &gt;&gt; 2) &amp; 0xff] ^ ((crc10&lt;&lt;6) &amp; 0xFF);</p><p>These two lines are extra in wireshark code. Why these two lines of code is required.</p><p>I tried to backtrak the variable "crc10" &amp; lost in the middle. As it goes on points to different functions.</p></div><div id="comment-8422-info" class="comment-info"><span class="comment-age">(16 Jan '12, 21:37)</span> prithvi</div></div><span id="30199"></span><div id="comment-30199" class="comment"><div id="post-30199-score" class="comment-score"></div><div class="comment-text"><p>did you backtrack the wireshark expression to get the actual expression? Can you please share the expression</p></div><div id="comment-30199-info" class="comment-info"><span class="comment-age">(26 Feb '14, 01:41)</span> biswa00</div></div><span id="30201"></span><div id="comment-30201" class="comment"><div id="post-30201-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>I did not get the value of CRC10 variable in the expression</p></div><div id="comment-30201-info" class="comment-info"><span class="comment-age">(26 Feb '14, 01:54)</span> prithvi</div></div><span id="30202"></span><div id="comment-30202" class="comment"><div id="post-30202-score" class="comment-score"></div><div class="comment-text"><p>would you mind sharing the expression for crc10 checksum calculation. As iam facing similar issue where iam using the first loop and wireshark detects the checksum as incorrect.</p><p>thanks, biswa</p></div><div id="comment-30202-info" class="comment-info"><span class="comment-age">(26 Feb '14, 02:02)</span> biswa00</div></div><span id="30204"></span><div id="comment-30204" class="comment"><div id="post-30204-score" class="comment-score"></div><div class="comment-text"><p>@biswa00, @prithvi</p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-30204-info" class="comment-info"><span class="comment-age">(26 Feb '14, 02:12)</span> grahamb ♦</div></div><span id="30220"></span><div id="comment-30220" class="comment not_top_scorer"><div id="post-30220-score" class="comment-score"></div><div class="comment-text"><p>I've seen a lot of Iu user-plane without CRC errors... Are you talking IuPS or IuCS? Are you able to upload an example and link to it (<a href="http://cloudshark.org/">http://cloudshark.org/</a> )?</p></div><div id="comment-30220-info" class="comment-info"><span class="comment-age">(26 Feb '14, 18:03)</span> Quadratic</div></div></div><div id="comment-tools-8419" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-8419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

