+++
type = "question"
title = "_ws.col.Protocol changes in wireshark 2.1.0?"
description = '''It looks like the _ws.col.Protocol has changed in wireshark/tshark 2.1.0 - IPv4 UDP traffic is reported as &quot;IPV4&quot; rather than &quot;UDP&quot; for example. Is there documentation available on what has changed? Is there a new translated protocol field name? Thanks..'''
date = "2015-10-19T13:16:00Z"
lastmod = "2015-10-20T01:14:00Z"
weight = 46711
keywords = [ "_ws.col.protocol", "2.1.0", "wireshark" ]
aliases = [ "/questions/46711" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\_ws.col.Protocol changes in wireshark 2.1.0?](/questions/46711/_wscolprotocol-changes-in-wireshark-210)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46711-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It looks like the _ws.col.Protocol has changed in wireshark/tshark 2.1.0 - IPv4 UDP traffic is reported as "IPV4" rather than "UDP" for example. Is there documentation available on what has changed? Is there a new translated protocol field name? Thanks..</p></div><div id="question-tags" class="tags-container tags">_ws.col.protocol 2.1.0 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/c789876c68e660af96be83475c0270dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Loki&#39;s gravatar image" /><p>Loki<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Loki has no accepted answers">0%</span></p></div></div><div id="comments-container-46711" class="comments-container"></div><div id="comment-tools-46711" class="comment-tools"></div><div class="clear"></div><div id="comment-46711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46748"></span>

<div id="answer-container-46748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46748-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Using v2.1.0rc0-168-ge8a3769, _ws.col.Protocol filter is working as usual: UDP packets display UDP in the column and not IPv4. Did you verify that you did not deactivate UDP dissector by error (in Analyze -&gt; Enabled Protocols)?</p><p>Edit: during a few commits, the code adding the UDP name to the Protocols column was removed by mistake. It is now back so upgrading your Wireshark copy to a newer version should fix the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '15, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Oct '15, 01:16</p></div></div><div id="comments-container-46748" class="comments-container"></div><div id="comment-tools-46748" class="comment-tools"></div><div class="clear"></div><div id="comment-46748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

