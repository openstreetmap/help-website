+++
type = "question"
title = "IP checksum offload error"
description = '''I have RDP session setup between 2 clients but I am getting checksum error when they are doing TCP 3 way handshake at the time of ACK I see below error. Can someone please help me understand why I am getting that? Header checksum: 0x0000 [incorrect, should be 0xb46a (may be caused by &quot;IP checksum of...'''
date = "2013-02-28T22:58:00Z"
lastmod = "2013-08-17T16:55:00Z"
weight = 19013
keywords = [ "ip", "checksum", "offload", "error" ]
aliases = [ "/questions/19013" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [IP checksum offload error](/questions/19013/ip-checksum-offload-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have RDP session setup between 2 clients but I am getting checksum error when they are doing TCP 3 way handshake at the time of ACK I see below error.</p><p>Can someone please help me understand why I am getting that? Header checksum: 0x0000 [incorrect, should be 0xb46a (may be caused by "IP checksum offload"?)]</p><p>Thanks for help.</p></div><div id="question-tags" class="tags-container tags">ip checksum offload error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/6615a61d69b703d89076bb0f18342bbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m_1607&#39;s gravatar image" /><p>m_1607<br />
<span class="score" title="35 reputation points">35</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m_1607 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '13, 07:20</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-19013" class="comments-container"></div><div id="comment-tools-19013" class="comment-tools"></div><div class="clear"></div><div id="comment-19013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19020"></span>

<div id="answer-container-19020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19020-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's an artefact of the capture mechanism on your host. See the wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Offloading">Checksum Offloading</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19020" class="comments-container"><span id="19126"></span><div id="comment-19126" class="comment"><div id="post-19126-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the link, i am still unsure if I should disable Offloading. I guess its worth a try</p></div><div id="comment-19126-info" class="comment-info"><span class="comment-age">(04 Mar '13, 07:47)</span> drewdin</div></div><span id="19127"></span><div id="comment-19127" class="comment"><div id="post-19127-score" class="comment-score"></div><div class="comment-text"><p>Unless you have a buggy driver/NIC firmware that doesn't do the checksums correctly you're probably best to leave it on for performance reasons.</p><p>If the "errors" reported by Wireshark are bothering you, turn them off in the preferences for each protocol with the "Validate the xxx checksum if possible" setting.</p></div><div id="comment-19127-info" class="comment-info"><span class="comment-age">(04 Mar '13, 08:02)</span> grahamb ♦</div></div><span id="19132"></span><div id="comment-19132" class="comment"><div id="post-19132-score" class="comment-score"></div><div class="comment-text"><p>good idea, ill just turn them off in WS, thanks!</p></div><div id="comment-19132-info" class="comment-info"><span class="comment-age">(04 Mar '13, 10:32)</span> drewdin</div></div></div><div id="comment-tools-19020" class="comment-tools"></div><div class="clear"></div><div id="comment-19020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23838"></span>

<div id="answer-container-23838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23838-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Some drivers had the RX checksum offloading bug fixed. Bad cabling and programmatic-ally disabling and reenabling the card as well as getting new drivers addressed the issue. There's more in depth details and analysis available from sources here:</p><p><a href="http://microdevsys.com/wp/windows-linux-the-local-device-name-is-already-in-use-this-connection-has-not-been-restored-and-ip-checksum-offload/">Windows / Linux: The local device name is already in use. This connection has not been restored and IP checksum offload</a></p><p>Cheers, TK</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '13, 16:55</strong></p><img src="https://secure.gravatar.com/avatar/944d025df3447474e900159c65dea1da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomMDS&#39;s gravatar image" /><p>TomMDS<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomMDS has no accepted answers">0%</span></p></div></div><div id="comments-container-23838" class="comments-container"></div><div id="comment-tools-23838" class="comment-tools"></div><div class="clear"></div><div id="comment-23838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

