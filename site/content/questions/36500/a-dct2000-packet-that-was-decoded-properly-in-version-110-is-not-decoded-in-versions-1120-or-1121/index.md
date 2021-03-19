+++
type = "question"
title = "A DCT2000 packet that was decoded properly in version 1.10 is not decoded in versions 1.12.0 or 1.12.1"
description = '''Hello,  A DCT2000 protocol related packet namely LTE &quot;Schceduling Request&quot; which was decoded properly in version 1.10 is not decoded and shown as Malformed Packet in version 1.12.0/1. Please suggest a way in which the packet content can be seen in Packet Details section in newer version or if revert...'''
date = "2014-09-21T23:15:00Z"
lastmod = "2014-09-22T03:52:00Z"
weight = 36500
keywords = [ "dct2000", "lte" ]
aliases = [ "/questions/36500" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [A DCT2000 packet that was decoded properly in version 1.10 is not decoded in versions 1.12.0 or 1.12.1](/questions/36500/a-dct2000-packet-that-was-decoded-properly-in-version-110-is-not-decoded-in-versions-1120-or-1121)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36500-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, A DCT2000 protocol related packet namely LTE "Schceduling Request" which was decoded properly in version 1.10 is not decoded and shown as Malformed Packet in version 1.12.0/1. Please suggest a way in which the packet content can be seen in Packet Details section in newer version or if reverting to version 1.10 needs to be done.</p><p>Regards,</p><p>Pankaj.</p></div><div id="question-tags" class="tags-container tags">dct2000 lte</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '14, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/7709dc914eaed81742e7a0f2bb27716e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pankaj_ad&#39;s gravatar image" /><p>pankaj_ad<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pankaj_ad has no accepted answers">0%</span></p></div></div><div id="comments-container-36500" class="comments-container"></div><div id="comment-tools-36500" class="comment-tools"></div><div class="clear"></div><div id="comment-36500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36503"></span>

<div id="answer-container-36503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36503-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please open a <a href="https://bugs.wireshark.org">bug report</a> and attach the file so we can have a look at it and fix the potential bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '14, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '14, 07:40</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-36503" class="comments-container"><span id="36507"></span><div id="comment-36507" class="comment"><div id="post-36507-score" class="comment-score"></div><div class="comment-text"><p>I think I fixed this in July (<a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=7801a97fd86acdee8c4525be503720d791124f64)">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=7801a97fd86acdee8c4525be503720d791124f64)</a> but not backported to the 1.12 branch.</p></div><div id="comment-36507-info" class="comment-info"><span class="comment-age">(22 Sep '14, 09:14)</span> MartinM</div></div></div><div id="comment-tools-36503" class="comment-tools"></div><div class="clear"></div><div id="comment-36503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

