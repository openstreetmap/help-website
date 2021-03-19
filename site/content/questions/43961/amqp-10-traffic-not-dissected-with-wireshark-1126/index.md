+++
type = "question"
title = "AMQP 1.0 traffic not dissected with Wireshark 1.12.6"
description = '''Hi,  I have installed Wireshark v1.12.6.0 to inspect AMQP 1.0 network traffic. But the protocol column in Wireshark only contains &quot;TCP&quot; instead of &quot;AMQP&quot; for the inspected traffic. I expected that AMQP message packets would have been recognized automatically? If I right click on a selected row I can...'''
date = "2015-07-08T06:16:00Z"
lastmod = "2015-07-19T11:30:00Z"
weight = 43961
keywords = [ "amqp" ]
aliases = [ "/questions/43961" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [AMQP 1.0 traffic not dissected with Wireshark 1.12.6](/questions/43961/amqp-10-traffic-not-dissected-with-wireshark-1126)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43961-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have installed Wireshark v1.12.6.0 to inspect AMQP 1.0 network traffic. But the protocol column in Wireshark only contains "TCP" instead of "AMQP" for the inspected traffic. I expected that AMQP message packets would have been recognized automatically? If I right click on a selected row I can do "Decode as..." --&gt; AMQP but I don't see any decoding happen.</p><p>Is the AMQP 1.O dissector contained in Wireshark v1.12.6.0?</p><p>If yes, what do I have to do to decode the AMQP network traffic to get the payload of the messages (TCP segment data) in a human readable format (XML)?</p><p>If not what do I have to do to make the dissector running in Wireshark.</p><p>Regards, Erik</p></div><div id="question-tags" class="tags-container tags">amqp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '15, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/312b50adaffa2cdc7fbbbfc5a3364b0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ErikAs&#39;s gravatar image" /><p>ErikAs<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ErikAs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 08 Jul '15, 07:02</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43961" class="comments-container"></div><div id="comment-tools-43961" class="comment-tools"></div><div class="clear"></div><div id="comment-43961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44295"></span>

<div id="answer-container-44295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44295-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is the AMQP 1.O dissector contained in Wireshark v1.12.6.0?</p></blockquote><p>I think so (at least source code for the version contains the patches from <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9612">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9612</a>).</p><p>Is the AMQP 1.0 traffic sent via TCP port 5672? If not, right-click to some frame with TCP data (PSH bit enabled), select "Decode as", in Transport tab chose AMQP in right pane and click to OK (this will decode just the TCP flow of the selected frame but I think you get the point).</p><p>If AMQP 1.0 traffic is sent via port 5672, then either Wireshark cant decode a bit of conversation or the traffic is malformed (i.e. tcpdump -s &lt;very_small_value&gt; used). Would it be possible to share the tcpdump to provide more accurate answer? Anyway once Wireshark attempts to decode some frame as some protocol (here AMQP) and fails, it provides error/warning expert info (coloured bullet in left down corner of the application window) - that could be also valuable to check.</p><p>Yet another option is your AMQP traffic is sent over SSL (here usually on port 5671) i.e. encrypted. Then there is no way to decode it in Wireshark (or I am not aware of such a method).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '15, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/c8e23332a9122d57cb009c334a1b1b8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pavel%20Moravec&#39;s gravatar image" /><p>Pavel Moravec<br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pavel Moravec has no accepted answers">0%</span></p></div></div><div id="comments-container-44295" class="comments-container"><span id="45263"></span><div id="comment-45263" class="comment"><div id="post-45263-score" class="comment-score"></div><div class="comment-text"><p>Hi Pavel,</p><p>thanks for the answer.</p><p>Yes the AMQP traffic is not sent over port 5672 and sent over a SSL encrypted connection. So there is now chance to dissect the AMQP traffic in this case?</p><p>I thougt about letting Wireshark decode the SSL encrypted packets (like described here: <a href="http://packetpushers.net/using-wireshark-to-decode-ssltls-packets)">http://packetpushers.net/using-wireshark-to-decode-ssltls-packets)</a> first and then using the AMPQ dissector to dissect the decrypted data. But this does not seem to work either.</p><p>Regards, Erik</p></div><div id="comment-45263-info" class="comment-info"><span class="comment-age">(20 Aug '15, 02:28)</span> ErikAs</div></div><span id="45265"></span><div id="comment-45265" class="comment"><div id="post-45265-score" class="comment-score"></div><div class="comment-text"><p>You'll need the SSL master key, which isn't easy to come by, that's the point of SSL after all. Is your AMQP traffic from Azure?</p></div><div id="comment-45265-info" class="comment-info"><span class="comment-age">(20 Aug '15, 03:59)</span> grahamb ♦</div></div></div><div id="comment-tools-44295" class="comment-tools"></div><div class="clear"></div><div id="comment-44295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

