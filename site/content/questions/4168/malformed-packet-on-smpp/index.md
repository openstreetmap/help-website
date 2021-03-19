+++
type = "question"
title = "Malformed Packet on SMPP"
description = '''I captured a packet using the command tethereal -i bond0 -R &quot;smpp&quot; -w /tmp/file. When I viewed the file its shows Malformed Packet on submit_sm. Why is that so?'''
date = "2011-05-20T17:06:00Z"
lastmod = "2011-05-20T23:17:00Z"
weight = 4168
keywords = [ "smpp", "tethereal", "malformed", "packet" ]
aliases = [ "/questions/4168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed Packet on SMPP](/questions/4168/malformed-packet-on-smpp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured a packet using the command tethereal -i bond0 -R "smpp" -w /tmp/file. When I viewed the file its shows Malformed Packet on submit_sm. Why is that so?</p></div><div id="question-tags" class="tags-container tags">smpp tethereal malformed packet</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '11, 17:06</strong></p><img src="https://secure.gravatar.com/avatar/83fa98a6fbfb2cd57a544a818b38f327?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="themask&#39;s gravatar image" /><p>themask<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="themask has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 May '11, 07:07</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4168" class="comments-container"></div><div id="comment-tools-4168" class="comment-tools"></div><div class="clear"></div><div id="comment-4168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4169"></span>

<div id="answer-container-4169" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4169-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although it's not 100% certain without looking at the actual trace, one possible explanation might be:</p><p>A smpp protocol PDU can be split across multiple tcp segments (and therefor frames). When you use a (display) filter like smpp, tshark will only show the frame in which the reassembly completed (in which the last segment of the PDU was found). So only that frame is saved in the capture file. When you reopen the capture file, the first fragment(s) of the smpp PDU are not found and you end up with a broken PDU, hence the "Malformed Packet"</p><p>(BTW 'tethereal' is realy old (at least 5 years), you might want to <a href="http://www.wireshark.org/download.html">upgrade to the latest wireshark/tshark version</a>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '11, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4169" class="comments-container"></div><div id="comment-tools-4169" class="comment-tools"></div><div class="clear"></div><div id="comment-4169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

