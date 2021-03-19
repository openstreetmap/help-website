+++
type = "question"
title = "Sniffer port down while Wireshark shows packets receive"
description = '''Currently we are involved in Nice VoIP Infrastructure. We had a case where sniffer port was unable to receive data but wireshark shows packets receive. Is it a current status of sniffer port? Is it that wireshark is only capturing what switch port is throwing not what sniffer captures? Your quick re...'''
date = "2012-06-16T04:09:00Z"
lastmod = "2012-06-16T04:43:00Z"
weight = 11988
keywords = [ "switch", "sniffer", "systems", "nice" ]
aliases = [ "/questions/11988" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Sniffer port down while Wireshark shows packets receive](/questions/11988/sniffer-port-down-while-wireshark-shows-packets-receive)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11988-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Currently we are involved in Nice VoIP Infrastructure. We had a case where sniffer port was unable to receive data but wireshark shows packets receive.</p><p>Is it a current status of sniffer port?</p><p>Is it that wireshark is only capturing what switch port is throwing not what sniffer captures?</p><p>Your quick response will be highly appreciated.</p><p>Thanks.</p><p>Umar.</p></div><div id="question-tags" class="tags-container tags">switch sniffer systems nice</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '12, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/4b26647155fcbdfcaf66cbb00b6890d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umarfawad&#39;s gravatar image" /><p>umarfawad<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umarfawad has no accepted answers">0%</span></p></div></div><div id="comments-container-11988" class="comments-container"></div><div id="comment-tools-11988" class="comment-tools"></div><div class="clear"></div><div id="comment-11988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11990"></span>

<div id="answer-container-11990" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11990-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not really sure what you are asking, but here is my guess, based on the information you provided:</p><blockquote><p>We had a case where sniffer port was unable to receive data but wireshark shows packets receive.</p></blockquote><p>Maybe you did not connect wireshark to the monitor/mirror/span/sniffer port on the switch and you saw broadcast traffic in wireshark, as you do on any regular access port of a switch. Maybe it was traffic to/from your sniffer PC. To verify that, please tell us more about your sniffer (switch) setup and tell us what you saw in wireshark.</p><blockquote><p>Is it that wireshark is only capturing what switch port is throwing not what sniffer captures?</p></blockquote><p>what do you mean by "what sniffer captures"? Wireshark IS the sniffer. Maybe you can tell us a bit more about your setup.</p><p>Did you check this: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '12, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jun '12, 04:46</p></div></div><div id="comments-container-11990" class="comments-container"></div><div id="comment-tools-11990" class="comment-tools"></div><div class="clear"></div><div id="comment-11990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

