+++
type = "question"
title = "How to decode the UDP to RTP in command line?"
description = '''Hi all,  Under the Wireshark GUI, I am able to decode the UDP to RTP by using the   &quot;Analyze &amp;gt; decode as...&quot;  .  However, for the command line, I am not able to do it tshark -r c:&#92;input.cap -d udp.port==20390,rtp -w c:&#92;output.cap  it runs without error but after I open the output.cap in Wireshark...'''
date = "2012-04-25T08:33:00Z"
lastmod = "2012-04-26T07:08:00Z"
weight = 10440
keywords = [ "decode", "udp", "rtp" ]
aliases = [ "/questions/10440" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode the UDP to RTP in command line?](/questions/10440/how-to-decode-the-udp-to-rtp-in-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10440-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Under the Wireshark GUI, I am able to decode the UDP to RTP by using the</p><blockquote><p>"Analyze &gt; decode as..."</p></blockquote><p>. However, for the command line, I am not able to do it</p><pre><code>tshark -r c:\input.cap -d udp.port==20390,rtp -w c:\output.cap</code></pre><p>it runs without error but after I open the output.cap in Wireshark GUI, the problem is <strong>all the frames are still UDP</strong>. Seems the file not change?? Anybody could help?</p><p>Thanks Sam</p></div><div id="question-tags" class="tags-container tags">decode udp rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '12, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/37b682ab09006e00bd4f53d761690338?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manfree&#39;s gravatar image" /><p>manfree<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manfree has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '12, 08:36</p></div></div><div id="comments-container-10440" class="comments-container"></div><div id="comment-tools-10440" class="comment-tools"></div><div class="clear"></div><div id="comment-10440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10458"></span>

<div id="answer-container-10458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10458-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the Wireshark GUI set the RTP dissector preference: Try to decode RTP outside of conversations.</p><p>or</p><p>Add <code>-o rtp.heuristic_rtp:TRUE</code> to your command line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '12, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-10458" class="comments-container"></div><div id="comment-tools-10458" class="comment-tools"></div><div class="clear"></div><div id="comment-10458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

