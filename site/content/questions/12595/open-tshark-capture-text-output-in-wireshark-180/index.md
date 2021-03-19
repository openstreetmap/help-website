+++
type = "question"
title = "Open tshark capture text output in Wireshark 1.8.0"
description = '''I have a tshark capture file capture using the following command: tshark -i bond0 -t ad &amp;gt; cap.txt  How to open the cap.txt in Wireshark 1.8.0 ?'''
date = "2012-07-11T02:19:00Z"
lastmod = "2012-07-11T02:43:00Z"
weight = 12595
keywords = [ "tshark" ]
aliases = [ "/questions/12595" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Open tshark capture text output in Wireshark 1.8.0](/questions/12595/open-tshark-capture-text-output-in-wireshark-180)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12595-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a tshark capture file capture using the following command:</p><pre><code>tshark -i bond0 -t ad &gt; cap.txt</code></pre><p>How to open the <a href="http://cap.txt">cap.txt</a> in Wireshark 1.8.0 ?</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '12, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/8d3a904912a5e61e0aba98998a31f715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raptor&#39;s gravatar image" /><p>Raptor<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raptor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jul '12, 02:44</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-12595" class="comments-container"></div><div id="comment-tools-12595" class="comment-tools"></div><div class="clear"></div><div id="comment-12595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12597"></span>

<div id="answer-container-12597" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12597-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's just text output. You cannot read that with Wireshark. Please use this command instead:</p><blockquote><p><code>tshark -ni bond0 -t ad -w /var/tmp/output.cap</code></p></blockquote><p>Then open /var/tmp/output.cap in Wireshark OR capture directly with Wireshark (Capture -&gt; Interfaces).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '12, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12597" class="comments-container"></div><div id="comment-tools-12597" class="comment-tools"></div><div class="clear"></div><div id="comment-12597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

