+++
type = "question"
title = "What OSI layer protocols are examined, layer 4, 3 and 2 or all three?"
description = '''I&#x27;m a newbie to wireshark, being a networking student at a nearby technical college. What protocols are examined in layers 4 to 2?'''
date = "2014-02-20T08:17:00Z"
lastmod = "2014-02-20T08:25:00Z"
weight = 30045
keywords = [ "protocols" ]
aliases = [ "/questions/30045" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What OSI layer protocols are examined, layer 4, 3 and 2 or all three?](/questions/30045/what-osi-layer-protocols-are-examined-layer-4-3-and-2-or-all-three)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30045-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a newbie to wireshark, being a networking student at a nearby technical college. What protocols are examined in layers 4 to 2?</p></div><div id="question-tags" class="tags-container tags">protocols</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '14, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/e6be32fed9ea5812e14d1ecc2b745aaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BreakingBad&#39;s gravatar image" /><p>BreakingBad<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BreakingBad has no accepted answers">0%</span></p></div></div><div id="comments-container-30045" class="comments-container"></div><div id="comment-tools-30045" class="comment-tools"></div><div class="clear"></div><div id="comment-30045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30046"></span>

<div id="answer-container-30046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30046-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to work a bit on your Google Fu. A quick search found lots of hits comparing tcpip and OSI, e.g. <a href="http://electronicdesign.com/what-s-difference-between/what-s-difference-between-osi-seven-layer-network-model-and-tcpip">http://electronicdesign.com/what-s-difference-between/what-s-difference-between-osi-seven-layer-network-model-and-tcpip</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '14, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30046" class="comments-container"><span id="30048"></span><div id="comment-30048" class="comment"><div id="post-30048-score" class="comment-score"></div><div class="comment-text"><p>What I meant to say is: does wireshark look at all protocols, from layers 2-4?</p></div><div id="comment-30048-info" class="comment-info"><span class="comment-age">(20 Feb '14, 10:05)</span> BreakingBad</div></div><span id="30052"></span><div id="comment-30052" class="comment"><div id="post-30052-score" class="comment-score"></div><div class="comment-text"><p>Wireshark will, if a protocol dissector is available for the protocol, examine and dissect every protocol in every captured packet.</p><p>If there isn't a dissector available, then Wireshark will display the data at that level as "Data" and no further dissection of that data will be done.</p><p>So yes, Wireshark will show data over the OSI stack from layers 2-7 for all data link types that Wireshark understands.</p></div><div id="comment-30052-info" class="comment-info"><span class="comment-age">(20 Feb '14, 12:40)</span> grahamb ♦</div></div></div><div id="comment-tools-30046" class="comment-tools"></div><div class="clear"></div><div id="comment-30046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

