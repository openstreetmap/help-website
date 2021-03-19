+++
type = "question"
title = "[Malformed Packet: CAMEL]"
description = '''Hi, Wireshark latest tool showing error as &quot;Malformed Packet: CAMEL&quot;, actually filled generic filled in the CONNECT message. Note : One more issue is also facing, the above message sent to the network but network sent Reject status with &quot;MisTypedArgument&quot;, If you have any idea please share. The appl...'''
date = "2016-12-16T02:36:00Z"
lastmod = "2016-12-16T22:26:00Z"
weight = 58160
keywords = [ "ss7", "inap", "camel" ]
aliases = [ "/questions/58160" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [\[Malformed Packet: CAMEL\]](/questions/58160/malformed-packet-camel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58160-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Wireshark latest tool showing error as "Malformed Packet: CAMEL", actually filled generic filled in the CONNECT message.</p><p>Note : One more issue is also facing, the above message sent to the network but network sent Reject status with "MisTypedArgument", If you have any idea please share. The application is for modifying the CLI.</p><p>Can you check what is the issue ?, I have downloaded latest version but that version also didn't helped to decode the values properly.</p><p>Thanks, Hanosh Varghese</p></div><div id="question-tags" class="tags-container tags">ss7 inap camel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '16, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/947b7a306a061178060e0e2a11b93d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hanosh&#39;s gravatar image" /><p>Hanosh<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hanosh has no accepted answers">0%</span></p></div></div><div id="comments-container-58160" class="comments-container"><span id="58162"></span><div id="comment-58162" class="comment"><div id="post-58162-score" class="comment-score"></div><div class="comment-text"><p>Without the capture it's very difficult for anyone else to understand your issue from a textual description.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc.?</p></div><div id="comment-58162-info" class="comment-info"><span class="comment-age">(16 Dec '16, 03:19)</span> grahamb ♦</div></div><span id="58164"></span><div id="comment-58164" class="comment"><div id="post-58164-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for the quick reply ..</p><p>Here is the cloud shark link..</p><p><a href="https://www.cloudshark.org/captures/51d0007e87ed?filter=camel">https://www.cloudshark.org/captures/51d0007e87ed?filter=camel</a></p></div><div id="comment-58164-info" class="comment-info"><span class="comment-age">(16 Dec '16, 03:49)</span> Hanosh</div></div></div><div id="comment-tools-58160" class="comment-tools"></div><div class="clear"></div><div id="comment-58160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58178"></span>

<div id="answer-container-58178" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58178-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is kind of far from a "wireshark question" but the SCP's Generic Number argument is formatted incorrectly. It should follow the format of ITU Q.1902.3 figure 66, but instead it just includes the first field of the argument and ends abruptly. If you look at it in raw hex, no number digits are being passed, nor any other fields, after the number qualifier indicator.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '16, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-58178" class="comments-container"><span id="58198"></span><div id="comment-58198" class="comment"><div id="post-58198-score" class="comment-score"></div><div class="comment-text"><p>I.e., both Wireshark and the machine to which the message was sent agree - the packet is <em>not</em> formatted correctly. Wireshark reported a "Malformed packet", and the machine to which the message was sent replied with a Reject status.</p></div><div id="comment-58198-info" class="comment-info"><span class="comment-age">(17 Dec '16, 13:55)</span> Guy Harris ♦♦</div></div><span id="58219"></span><div id="comment-58219" class="comment"><div id="post-58219-score" class="comment-score"></div><div class="comment-text"><p>Thanks for ITU-T document reference, it was the error due to invalid digits packing.</p><p>Thanks, Hanosh Varghese</p></div><div id="comment-58219-info" class="comment-info"><span class="comment-age">(18 Dec '16, 23:28)</span> Hanosh</div></div><span id="58227"></span><div id="comment-58227" class="comment"><div id="post-58227-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-58227-info" class="comment-info"><span class="comment-age">(19 Dec '16, 07:46)</span> Jaap ♦</div></div></div><div id="comment-tools-58178" class="comment-tools"></div><div class="clear"></div><div id="comment-58178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

