+++
type = "question"
title = "Use TShark to write Protocol like the column in Wireshark"
description = '''Hi. I need to process pcap files and extract data into csv files, including the protocol name. If I do this via Wireshark, the Protocol column is exactly what I need. However, it&#x27;s very inconvenient to manually open files and export them. I&#x27;ve tried using TShark and it&#x27;s great, but the closest thing...'''
date = "2013-07-31T09:51:00Z"
lastmod = "2014-06-19T16:58:00Z"
weight = 23482
keywords = [ "pcap", "protocol", "tshark", "wireshark" ]
aliases = [ "/questions/23482" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Use TShark to write Protocol like the column in Wireshark](/questions/23482/use-tshark-to-write-protocol-like-the-column-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23482-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I need to process pcap files and extract data into csv files, including the protocol name. If I do this via Wireshark, the Protocol column is exactly what I need. However, it's very inconvenient to manually open files and export them. I've tried using TShark and it's great, but the closest thing I've found to the Protoocl is frame.protocols. I don't mind the extra data, but in several files I've tried to open this does not display the needed information. Sometimes I get eth:ip:tcp:data while Wireshark's protocol column will display the protocol name accurately.</p><p>Anything I'm missing?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">pcap protocol tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '13, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/eb19c4016864033ca12788883d2c251e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vadgros&#39;s gravatar image" /><p>vadgros<br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vadgros has no accepted answers">0%</span></p></div></div><div id="comments-container-23482" class="comments-container"></div><div id="comment-tools-23482" class="comment-tools"></div><div class="clear"></div><div id="comment-23482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23485"></span>

<div id="answer-container-23485" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23485-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use <code>-e col.Protocol</code>. The col prefix is short for column, then the column name with the same case as is shown in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '13, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23485" class="comments-container"><span id="23486"></span><div id="comment-23486" class="comment"><div id="post-23486-score" class="comment-score"></div><div class="comment-text"><p>Great. Thanks a lot.</p></div><div id="comment-23486-info" class="comment-info"><span class="comment-age">(31 Jul '13, 10:22)</span> vadgros</div></div></div><div id="comment-tools-23485" class="comment-tools"></div><div class="clear"></div><div id="comment-23485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33970"></span>

<div id="answer-container-33970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33970-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As of the 1.11.x and 1.12 versions of tshark, the field names are "_ws.col.Protocol" and "_ws.col.Info", instead of "col.Protocol" and "col.Info".</p><p>Example:</p><p><code>tshark -T fields -e _ws.col.Protocol -e _ws.col.Info</code></p><p>Source: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10201">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10201</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '14, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/028a4be69999143f43a3ed2e97f42159?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CraigGarrett&#39;s gravatar image" /><p>CraigGarrett<br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CraigGarrett has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '14, 10:21</p></div></div><div id="comments-container-33970" class="comments-container"></div><div id="comment-tools-33970" class="comment-tools"></div><div class="clear"></div><div id="comment-33970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

