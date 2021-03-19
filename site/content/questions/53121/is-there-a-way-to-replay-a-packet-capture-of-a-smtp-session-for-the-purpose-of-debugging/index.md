+++
type = "question"
title = "Is there a way to “replay” a packet capture of a smtp session for the purpose of debugging?"
description = '''I&#x27;m troubleshooting a smtp issue involving character-set encoding and it&#x27;s extremely difficult to involve the end user. I have a packet capture of an incoming smtp session that results in problematic behavior but if I try to copy/paste the mime source from wireshark, the issue doesn&#x27;t occur. I&#x27;m rea...'''
date = "2016-06-01T17:14:00Z"
lastmod = "2016-06-01T22:23:00Z"
weight = 53121
keywords = [ "characterset", "smtp", "encoding" ]
aliases = [ "/questions/53121" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to “replay” a packet capture of a smtp session for the purpose of debugging?](/questions/53121/is-there-a-way-to-replay-a-packet-capture-of-a-smtp-session-for-the-purpose-of-debugging)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53121-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm troubleshooting a smtp issue involving character-set encoding and it's extremely difficult to involve the end user. I have a packet capture of an incoming smtp session that results in problematic behavior but if I try to copy/paste the mime source from wireshark, the issue doesn't occur.</p><p>I'm reasonably certain that the difference in my testing is that I'm copying the strings in the packet capture from the Wireshark "follow tcp stream" output and that's not necessarily the bit-for-bit accurate copy of the data as it arrived on the wire.</p><p>So my question is this: how can I get an EXACT copy of the bit-for-bit SMTP data and send it again for reproduction purposes? Is there a way to "replay" a transmission?</p></div><div id="question-tags" class="tags-container tags">characterset smtp encoding</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '16, 17:14</strong></p><img src="https://secure.gravatar.com/avatar/b228c21359e1fc1d1ad0d7552fa1b7d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thecgmguy&#39;s gravatar image" /><p>thecgmguy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thecgmguy has no accepted answers">0%</span></p></div></div><div id="comments-container-53121" class="comments-container"></div><div id="comment-tools-53121" class="comment-tools"></div><div class="clear"></div><div id="comment-53121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53126"></span>

<div id="answer-container-53126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53126-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might find something in <a href="https://wiki.wireshark.org/Tools">the Wiki</a> that suits your needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53126" class="comments-container"></div><div id="comment-tools-53126" class="comment-tools"></div><div class="clear"></div><div id="comment-53126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53127"></span>

<div id="answer-container-53127" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53127-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, there is, look for "tcpreplay". Please note that it is important that you have captured the session establishment phase (SYN, SYN+ACK, ACK) - not for the tool to work but for your SNMP machine to accept the replayed packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 22:23</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53127" class="comments-container"></div><div id="comment-tools-53127" class="comment-tools"></div><div class="clear"></div><div id="comment-53127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

