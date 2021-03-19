+++
type = "question"
title = "How to display some UDP missing packets?"
description = '''Hello, I want to watch some packets of an unknown protocol which relies on UDP, but Wireshark doesn&#x27;t display these packets. Why does Wireshark do this? What can I do? I can&#x27;t believe I must write a dissector to display it. Wireshark should at least display the payload under UDP protocol.'''
date = "2013-06-03T09:08:00Z"
lastmod = "2013-06-03T09:55:00Z"
weight = 21715
keywords = [ "udp", "packets", "missing" ]
aliases = [ "/questions/21715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to display some UDP missing packets?](/questions/21715/how-to-display-some-udp-missing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I want to watch some packets of an unknown protocol which relies on UDP, but Wireshark doesn't display these packets. Why does Wireshark do this? What can I do? I can't believe I must write a dissector to display it. Wireshark should at least display the payload under UDP protocol.</p></div><div id="question-tags" class="tags-container tags">udp packets missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '13, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/3df550c5714f32c97ddd89b8107adfb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anon321123&#39;s gravatar image" /><p>anon321123<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anon321123 has no accepted answers">0%</span></p></div></div><div id="comments-container-21715" class="comments-container"></div><div id="comment-tools-21715" class="comment-tools"></div><div class="clear"></div><div id="comment-21715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21717"></span>

<div id="answer-container-21717" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21717-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You do not need to write a dissector to display packets for an unknown protocol. It will just be displayed as UDP.</p><p>What is your capture setup? Are you capturing on the sending or receiving host? Are you capturing in the same network of the sending or receiving host? Are you capturing somewhere in the middle? Did you use port mirroring?</p><p>Have a look at <a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a> and <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '13, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21717" class="comments-container"></div><div id="comment-tools-21717" class="comment-tools"></div><div class="clear"></div><div id="comment-21717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

