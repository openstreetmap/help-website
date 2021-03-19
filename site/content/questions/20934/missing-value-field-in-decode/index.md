+++
type = "question"
title = "missing value: field in decode"
description = '''I&#x27;m running multiple versions of Wireshark and noticed that the &quot;Value:&quot; field typically located under the &quot;Length:&quot; field for DHCP decodes is missing on Version 1.8.6 for Windows. Is there any way to turn this field back on?'''
date = "2013-05-03T10:19:00Z"
lastmod = "2013-05-03T11:32:00Z"
weight = 20934
keywords = [ "dhcp", "value" ]
aliases = [ "/questions/20934" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [missing value: field in decode](/questions/20934/missing-value-field-in-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20934-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running multiple versions of Wireshark and noticed that the "Value:" field typically located under the "Length:" field for DHCP decodes is missing on Version 1.8.6 for Windows. Is there any way to turn this field back on?</p></div><div id="question-tags" class="tags-container tags">dhcp value</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '13, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/f567aef30a04c1e711b858335c726821?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="onebithead&#39;s gravatar image" /><p>onebithead<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="onebithead has no accepted answers">0%</span></p></div></div><div id="comments-container-20934" class="comments-container"></div><div id="comment-tools-20934" class="comment-tools"></div><div class="clear"></div><div id="comment-20934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20938"></span>

<div id="answer-container-20938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20938-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Value item is now a hidden tree item and thus you cannot see it.</p><p>Please start Wireshark with the following option to make those hidden items visible.</p><blockquote><p><code>wireshark -o protocols.display_hidden_proto_items:TRUE -nr dhcp.pcap</code><br />
</p></blockquote><p>Alternatively you can set that option in the GUI:</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Protocols -&gt; Display hidden protocol items</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '13, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '13, 11:38</p></div></div><div id="comments-container-20938" class="comments-container"></div><div id="comment-tools-20938" class="comment-tools"></div><div class="clear"></div><div id="comment-20938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

