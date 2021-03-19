+++
type = "question"
title = "Dissector only processes first packet"
description = '''I&#x27;m writing my first dissector based on the example in the Developers Guide and README.developer. I register my dissector for a certain port using dissector_add_uint(&quot;udp.port&quot;, FOO_PORT, handle); I notice that it only gets applied to the first packet that matches the port and I can&#x27;t apply it to ot...'''
date = "2012-11-02T08:00:00Z"
lastmod = "2012-11-02T15:13:00Z"
weight = 15503
keywords = [ "debug", "development", "dissector", "wireshark" ]
aliases = [ "/questions/15503" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector only processes first packet](/questions/15503/dissector-only-processes-first-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15503-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing my first dissector based on the example in the Developers Guide and README.developer.</p><p>I register my dissector for a certain port using</p><p>dissector_add_uint("udp.port", FOO_PORT, handle);</p><p>I notice that it only gets applied to the first packet that matches the port and I can't apply it to other packets, not even using "Decode As".</p><p>How can I figure out what the problem might be ?</p><p>--- Update ---</p><p>I noticed my first packet is marked as "malformed" by the sub-dissector I'm calling. When run on other packets it works. How can I make my dissector ignore such errors so it will be applied to the following packets ? Is there some error flag I need to clear ?</p></div><div id="question-tags" class="tags-container tags">debug development dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '12, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/afe39c5876518d84943dbc30652e38d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jan&#39;s gravatar image" /><p>Jan<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Nov '12, 09:12</p></div></div><div id="comments-container-15503" class="comments-container"></div><div id="comment-tools-15503" class="comment-tools"></div><div class="clear"></div><div id="comment-15503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15517"></span>

<div id="answer-container-15517" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15517-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As per <a href="http://www.wireshark.org/lists/wireshark-dev/201211/msg00011.html">your mailing list message</a>, other packets in the capture are setting up an RTP session and Wireshark thinks your packets belong to that discussion. Future discussion will be on the wireshark-dev mailing list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '12, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15517" class="comments-container"></div><div id="comment-tools-15517" class="comment-tools"></div><div class="clear"></div><div id="comment-15517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

