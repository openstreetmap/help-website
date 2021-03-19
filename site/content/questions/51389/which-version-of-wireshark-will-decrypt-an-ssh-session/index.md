+++
type = "question"
title = "which version of Wireshark will decrypt an ssh session?"
description = '''which version of the Wireshark will decrypt an ssh session '''
date = "2016-04-03T19:56:00Z"
lastmod = "2016-04-04T12:39:00Z"
weight = 51389
keywords = [ "ssh" ]
aliases = [ "/questions/51389" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [which version of Wireshark will decrypt an ssh session?](/questions/51389/which-version-of-wireshark-will-decrypt-an-ssh-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>which version of the Wireshark will decrypt an ssh session</p></div><div id="question-tags" class="tags-container tags">ssh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '16, 19:56</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p>srinu_bel<br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Apr '16, 02:39</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-51389" class="comments-container"></div><div id="comment-tools-51389" class="comment-tools"></div><div class="clear"></div><div id="comment-51389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51390"></span>

<div id="answer-container-51390" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51390-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No version of Wireshark will do that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '16, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-51390" class="comments-container"><span id="51404"></span><div id="comment-51404" class="comment"><div id="post-51404-score" class="comment-score"></div><div class="comment-text"><p>Both server and client hosts are with me &amp; required key files are also available... Even then, can't we decrypt the section by importing key info to wireshark?</p><p>If your reply is no, why it is like so??? what is the challenge after having keys also with us?</p><p>If we want to trouble shoot the performance of the TCP link on SSH, How we can do it, As port numbers / window size info in encrypted format???</p></div><div id="comment-51404-info" class="comment-info"><span class="comment-age">(04 Apr '16, 19:42)</span> srinu_bel</div></div></div><div id="comment-tools-51390" class="comment-tools"></div><div class="clear"></div><div id="comment-51390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51399"></span>

<div id="answer-container-51399" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51399-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If "decoding SSH section" means "decrypting SSH", that is not possible at the moment. See the <a href="https://wiki.wireshark.org/SSH">SSH - Wireshark Wiki</a> page.</p><p>For decryption of SSH traffic to be possible, the key material must first be extracted from a SSH client or server. The private keyfiles are insufficient, the actual symmetric encryption keys are <a href="https://tools.ietf.org/html/rfc4253#section-7.2">derived from a shared secret</a> based on the DH key exchange. Note that unlike SSL, SSH does not define a RSA key exchange method, so in the case of SSH the RSA private key file will never be useful for traffic decryption. The private key file is used only for authentication purposes, not encryption.</p><p>Note that only the SSH payload (commands, passwords, file transfers, ...) are encrypted. Upper layers (TCP, IP, Ethernet, ...) are not suddenly encrypted so you can still analyze TCP port numbers, sequence numbers, etc. Besides that you also have timing and size information which (for example) can be used to guess when a large file transfer has started.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '16, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Apr '16, 01:38</p></div></div><div id="comments-container-51399" class="comments-container"><span id="51403"></span><div id="comment-51403" class="comment"><div id="post-51403-score" class="comment-score"></div><div class="comment-text"><p>Both server and client hosts are with me &amp; required key files are also available... Even then can't we decrypt the section by importing key info to wireshark?</p><p>If your reply is know why it is like so??? what is the challenge after having keys also with us?</p><p>If we want to trouble shoot the performance of the TCP link on SSH, How we can do it, As port numbers / window size info in encrypted format???</p></div><div id="comment-51403-info" class="comment-info"><span class="comment-age">(04 Apr '16, 19:41)</span> srinu_bel</div></div><span id="51405"></span><div id="comment-51405" class="comment"><div id="post-51405-score" class="comment-score"></div><div class="comment-text"><p>Pl. read above line " If your reply is know why it is like so???" As ... If your reply is no why it is like so???</p><p>Sorry i am not good at English...</p></div><div id="comment-51405-info" class="comment-info"><span class="comment-age">(04 Apr '16, 19:44)</span> srinu_bel</div></div><span id="51408"></span><div id="comment-51408" class="comment"><div id="post-51408-score" class="comment-score"></div><div class="comment-text"><p>The key file is only used for authentication, not encryption. See the updated answer.</p></div><div id="comment-51408-info" class="comment-info"><span class="comment-age">(05 Apr '16, 01:38)</span> Lekensteyn</div></div><span id="51411"></span><div id="comment-51411" class="comment"><div id="post-51411-score" class="comment-score"></div><div class="comment-text"><p>@srinu_bel, if I understand your problem properly, you actually need to analyse a tcp session <strong>tunnelled through</strong> ssh, because the tcp headers (port numbers, window size etc.) of the tcp session carrying the ssh session itself are <strong>not</strong> encrypted.</p><p>If I am mistaken and you only cannot see "TCP" and its summary information in the "Info" column in packet list, simply disable SSH dissection (<code>Analyze -&gt; Enabled Protocols</code>, write "ssh" into the search field at the bottom left of the window which pops up, untick the checkbox next to <code>SSH</code> in the pane above, and click <code>OK</code>) and all your SSH packets will be shown as plain TCP ones.</p><p>If my guess is correct, you'll have to capture on the loopback interface. ssh allows you to make a local port N represent a remote socket X:Y, you then tell your application to connect to localhost:N instead of X:Y (which is inaccessible directly), and you have to capture at the loopback interface to analyze the tcp session using the tunnel. If your client application runs on Windows, you'll have to use npcap instead of WinPcap to be able to capture at loopback interface, because the loopback normally does not exist as an interface in Windows; npcap creates it for you.</p></div><div id="comment-51411-info" class="comment-info"><span class="comment-age">(05 Apr '16, 02:08)</span> sindy</div></div></div><div id="comment-tools-51399" class="comment-tools"></div><div class="clear"></div><div id="comment-51399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

