+++
type = "question"
title = "wireshark without interfaces | no npcap or winpcap"
description = '''Hi i use wireshark to review PCAP files and do not need to actually capture packets. I cannot get winpcap to run (win10 + endpoint encryption) and I cannot incstall npcap in my environment. how can i run wireshark and have it skip &quot;loading module preferences&quot;? my current install just hangs and preve...'''
date = "2017-10-12T05:11:00Z"
lastmod = "2017-10-12T05:11:00Z"
weight = 63841
keywords = [ "read", "filesonly", "npcap" ]
aliases = [ "/questions/63841" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark without interfaces | no npcap or winpcap](/questions/63841/wireshark-without-interfaces-no-npcap-or-winpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63841-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i use wireshark to review PCAP files and do not need to actually capture packets. I cannot get winpcap to run (win10 + endpoint encryption) and I cannot incstall npcap in my environment. how can i run wireshark and have it skip "loading module preferences"? my current install just hangs and prevents me from looking at pcap files</p></div><div id="question-tags" class="tags-container tags">read filesonly npcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '17, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/be14ffbff7b4c7fbfdb6589cbc72f2f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SharkWhatWhat&#39;s gravatar image" /><p>SharkWhatWhat<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SharkWhatWhat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Oct '17, 09:14</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-63841" class="comments-container"><span id="63845"></span><div id="comment-63845" class="comment"><div id="post-63845-score" class="comment-score"></div><div class="comment-text"><p>That sounds strange. Is WinPcap installed or not? If no packet capturing library is installed, Wireshark should start in the "file only" mode as you expect. Installed USBPcap and unfavourable circumstances can break this rule, but in such case Wireshark normally freezes at other stage than "loading module preferences".</p></div><div id="comment-63845-info" class="comment-info"><span class="comment-age">(12 Oct '17, 07:08)</span> sindy</div></div><span id="63869"></span><div id="comment-63869" class="comment"><div id="post-63869-score" class="comment-score"></div><div class="comment-text"><p>Thanks! Winpcap is currently installed. but WS hangs on "loading module preferences" other forum answers lead to the protection software being used on my PC. I'd like to know if i can start WS and have it ignore winpcap so i can view a file i have locally.</p></div><div id="comment-63869-info" class="comment-info"><span class="comment-age">(13 Oct '17, 10:54)</span> SharkWhatWhat</div></div><span id="63892"></span><div id="comment-63892" class="comment"><div id="post-63892-score" class="comment-score"></div><div class="comment-text"><p>Try to uninstall WinPcap. As you cannot use it anyway, uninstalling it should make sure whether Wireshark doesn't freeze waiting for a response from WinPcap which never comes. I don't know any softer way of making Wireshark "ignore WinPcap".</p></div><div id="comment-63892-info" class="comment-info"><span class="comment-age">(14 Oct '17, 02:13)</span> sindy</div></div></div><div id="comment-tools-63841" class="comment-tools"></div><div class="clear"></div><div id="comment-63841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

