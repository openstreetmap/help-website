+++
type = "question"
title = "Wireshark 1.4.6 crashes when saving"
description = '''I&#x27;m using version 1.4.6 running on a windows XP machine with all the latest updates. I&#x27;m running a capture on a spanned network port. I&#x27;ve left the capture running for 4 hours and it saves ok (File&amp;gt;save as) But when I come to do a longer test it crashes, this has been the case for a 72 hour captu...'''
date = "2011-06-13T02:01:00Z"
lastmod = "2011-06-13T12:10:00Z"
weight = 4535
keywords = [ "windows", "crash" ]
aliases = [ "/questions/4535" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.4.6 crashes when saving](/questions/4535/wireshark-146-crashes-when-saving)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4535-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using version 1.4.6 running on a windows XP machine with all the latest updates.</p><p>I'm running a capture on a spanned network port. I've left the capture running for 4 hours and it saves ok (File&gt;save as)</p><p>But when I come to do a longer test it crashes, this has been the case for a 72 hour capture and a 24 hour capture.</p><p>Should this be possible? This has happened on two different machines, both have 100GB+ drives in them so there should be plenty of storage.</p></div><div id="question-tags" class="tags-container tags">windows crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '11, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/8e78a2a53dc91a566216390caf232185?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scate&#39;s gravatar image" /><p>scate<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scate has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 14 Jun '11, 19:02</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4535" class="comments-container"><span id="4602"></span><div id="comment-4602" class="comment"><div id="post-4602-score" class="comment-score"></div><div class="comment-text"><p>Is that "crashes when doing File -&gt; Save As" or "crashes while it's running the capture before I get a chance to save the file with File -&gt; Save As"? If it's the latter, then it could just be running out of memory, as indicated in the answers. If it's the former, that might be another problem, but we'd need more details about the crash to know what it is.</p></div><div id="comment-4602-info" class="comment-info"><span class="comment-age">(16 Jun '11, 11:53)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-4535" class="comment-tools"></div><div class="clear"></div><div id="comment-4535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4536"></span>

<div id="answer-container-4536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4536-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The answer is: Use <a href="http://packetlife.net/blog/2011/mar/9/long-term-traffic-capture-wireshark/">dumpcap</a> for long running captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '11, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4536" class="comments-container"></div><div id="comment-tools-4536" class="comment-tools"></div><div class="clear"></div><div id="comment-4536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4542"></span>

<div id="answer-container-4542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4542-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The reason your Wireshark is crashing for long-running captures is likely because it's running out of memory (<a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">known issue</a>). One of the workarounds is to use dumpcap as Jaap suggests.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '11, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jun '11, 12:13</p></div></div><div id="comments-container-4542" class="comments-container"></div><div id="comment-tools-4542" class="comment-tools"></div><div class="clear"></div><div id="comment-4542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

