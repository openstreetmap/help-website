+++
type = "question"
title = "txpower dBm rate"
description = '''Hey I am interested in sniffing packets and monitoring their tx power dBm rate on linux. How do i do that? I tried many things: - I right click on the columns tool bar and click &quot;edit columns Details&quot; select &quot;ieee802.11 Tx rate&quot; - the column does not show me anything - no information. - I tried to f...'''
date = "2013-06-09T21:06:00Z"
lastmod = "2013-06-09T23:25:00Z"
weight = 21864
keywords = [ "monitor", "tx" ]
aliases = [ "/questions/21864" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [txpower dBm rate](/questions/21864/txpower-dbm-rate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21864-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey I am interested in sniffing packets and monitoring their tx power dBm rate on linux. How do i do that? I tried many things: - I right click on the columns tool bar and click "edit columns Details" select "ieee802.11 Tx rate" - the column does not show me anything - no information. - I tried to filter the packets by a certain tx power using radiotap.txpower &gt;/&lt; 0 etc and it shows me zero packets, as if none of them have a positive or negative tx power</p><p>Does anyone know what am i doing wrong?</p><p>Thanks Matt</p></div><div id="question-tags" class="tags-container tags">monitor tx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '13, 21:06</strong></p><img src="https://secure.gravatar.com/avatar/c13c2a43050315ac917822d92e1e4e64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattigot&#39;s gravatar image" /><p>mattigot<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattigot has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '13, 21:21</p></div></div><div id="comments-container-21864" class="comments-container"></div><div id="comment-tools-21864" class="comment-tools"></div><div class="clear"></div><div id="comment-21864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21867"></span>

<div id="answer-container-21867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21867-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Hey I am interested in sniffing packets and monitoring their tx power dBm rate on linux. How do i do that?</p></blockquote><p>You do it by capturing in monitor mode. If you're not capturing in monitor mode, the capture mechanism that libpcap, and thus Wireshark, uses will not supply radio information such as transmit power.</p><p>Some Linux drivers may not use radiotap, in which case <code>radiotap.txpower</code> won't work, but most modern drivers do (<em>if</em> you're capturing in monitor mode).</p><p>Note also that packets received by the host, rather than transmitted by the host, probably won't have transmit power, as the host won't be able to determine the power level at the <em>transmitting</em> antenna used when transmitting the packet, it'll only be able to determine the power at the <em>receiving</em> antenna when the packet was received.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '13, 23:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21867" class="comments-container"><span id="21868"></span><div id="comment-21868" class="comment"><div id="post-21868-score" class="comment-score"></div><div class="comment-text"><p>I am not able to set it to monitor mode. under capture options, monitor mode is greyd out. is there another way?</p></div><div id="comment-21868-info" class="comment-info"><span class="comment-age">(09 Jun '13, 23:58)</span> mattigot</div></div><span id="21869"></span><div id="comment-21869" class="comment"><div id="post-21869-score" class="comment-score"></div><div class="comment-text"><p>Try using the <a href="http://www.aircrack-ng.org/doku.php?id=airmon-ng">airmon-ng</a> script.</p></div><div id="comment-21869-info" class="comment-info"><span class="comment-age">(10 Jun '13, 01:47)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-21867" class="comment-tools"></div><div class="clear"></div><div id="comment-21867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

