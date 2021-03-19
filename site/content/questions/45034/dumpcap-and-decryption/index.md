+++
type = "question"
title = "Dumpcap and decryption"
description = '''Does anyone know how to setup dumpcap to decrypt packets in monitor mode? Or, should it be used with the -I option, save the captured packets and decrypt them in Wireshark GUI? WS can be quite memory intensive though, so it might not like the large packet file. Thanks'''
date = "2015-08-12T22:29:00Z"
lastmod = "2015-08-13T00:36:00Z"
weight = 45034
keywords = [ "dumpcap" ]
aliases = [ "/questions/45034" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap and decryption](/questions/45034/dumpcap-and-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45034-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know how to setup dumpcap to decrypt packets in monitor mode? Or, should it be used with the -I option, save the captured packets and decrypt them in Wireshark GUI? WS can be quite memory intensive though, so it might not like the large packet file.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 22:29</strong></p><img src="https://secure.gravatar.com/avatar/3c16c3b7b9d89a5736de02187a6253d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mun&#39;s gravatar image" /><p>mun<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mun has no accepted answers">0%</span></p></div></div><div id="comments-container-45034" class="comments-container"></div><div id="comment-tools-45034" class="comment-tools"></div><div class="clear"></div><div id="comment-45034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45038"></span>

<div id="answer-container-45038" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45038-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>dumpcap is just a tool to record packets from a network card (or other communication port) to disk. It has no additional processing logic, so no, you cannot decrypt packets with dumpcap. Decrypting needs to be performed by Wireshark.</p><p>If your files are too large you might want to split them in smaller files, either during capture (multi file capture) or using editcap with the "-c" parameter later. There may be problems with decrypting packets though if the session setup is in a different file than the rest of the conversation, so reconstructing those may require merging them first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '15, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45038" class="comments-container"></div><div id="comment-tools-45038" class="comment-tools"></div><div class="clear"></div><div id="comment-45038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45039"></span>

<div id="answer-container-45039" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45039-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See this question: <a href="https://ask.wireshark.org/questions/24249/decrypt-wpa-with-tshark">https://ask.wireshark.org/questions/24249/decrypt-wpa-with-tshark</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '15, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45039" class="comments-container"><span id="45052"></span><div id="comment-45052" class="comment"><div id="post-45052-score" class="comment-score"></div><div class="comment-text"><p>Gah, didn't read question properly about using dumpcap. As @Jasper says, need to use Wireshark or tshark is as per my link.</p></div><div id="comment-45052-info" class="comment-info"><span class="comment-age">(13 Aug '15, 03:46)</span> grahamb ♦</div></div></div><div id="comment-tools-45039" class="comment-tools"></div><div class="clear"></div><div id="comment-45039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

