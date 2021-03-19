+++
type = "question"
title = "ASCII dump Custom Column"
description = '''I am trying to set up a column to display an ASCII dump. The &#x27;Packet Bytes&#x27; pane shows this information, but I cannot find a way to create a custom column to display the same information. When I use the data.data filter, the hex dump is displayed. When I use the data.text filter, a strange string is...'''
date = "2015-04-20T08:31:00Z"
lastmod = "2015-04-20T08:31:00Z"
weight = 41601
keywords = [ "column", "data.text", "ascii", "data.data" ]
aliases = [ "/questions/41601" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ASCII dump Custom Column](/questions/41601/ascii-dump-custom-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41601-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to set up a column to display an ASCII dump. The 'Packet Bytes' pane shows this information, but I cannot find a way to create a custom column to display the same information. When I use the data.data filter, the hex dump is displayed. When I use the data.text filter, a strange string is displayed instead of the ASCII dump that I was expecting. For example, I have a payload (encapsulated in a TCP frame):</p><p>3c0b64c8ff4cd802026d67fa3e</p><p>I can display this hex dump in a custom column using a data.data filter, but when I use data.text, this is displayed:</p><p>&lt;\vd\357\277\275\357\277\275L\357\277\275\002\002mg\357\277\275&gt;</p><p>When I use data.text, I would like this to be displayed (this is displayed in the Packet Bytes pane):</p><p>&lt;.d..L...mg.&gt;</p><p>I don't know where Wireshark is coming up with the information that is displayed using the data.text filter. Is there any way to display this hex payload as ASCII?</p><p>I am running Wireshark 1.12.4 on Windows 7.</p></div><div id="question-tags" class="tags-container tags">column data.text ascii data.data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '15, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/6acf3c1293dde7d08c204b9265e46764?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J_Turner&#39;s gravatar image" /><p>J_Turner<br />
<span class="score" title="71 reputation points">71</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J_Turner has no accepted answers">0%</span></p></div></div><div id="comments-container-41601" class="comments-container"></div><div id="comment-tools-41601" class="comment-tools"></div><div class="clear"></div><div id="comment-41601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

