+++
type = "question"
title = "PS2  NAS SMB Packet Capturing issue"
description = '''I would like to know why I only see ARP packets and not the SMB ones I want to debug ( http://psx-scene.com/forums/f150/how-make-packet-capture-wireshark-debugging-132438/ )... Any input ideas a d extra information would be welcome!'''
date = "2015-05-22T04:28:00Z"
lastmod = "2015-05-24T08:17:00Z"
weight = 42612
keywords = [ "ps2", "opl", "arp", "smb", "nas" ]
aliases = [ "/questions/42612" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PS2 NAS SMB Packet Capturing issue](/questions/42612/ps2-nas-smb-packet-capturing-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42612-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know why I only see ARP packets and not the SMB ones I want to debug ( <a href="http://psx-scene.com/forums/f150/how-make-packet-capture-wireshark-debugging-132438/">http://psx-scene.com/forums/f150/how-make-packet-capture-wireshark-debugging-132438/</a> )... Any input ideas a d extra information would be welcome!</p></div><div id="question-tags" class="tags-container tags">ps2 opl arp smb nas</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '15, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/9dac56422d5eb1150ac3d82af08ea2ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doctorxyz&#39;s gravatar image" /><p>doctorxyz<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doctorxyz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 May '15, 09:22</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-42612" class="comments-container"></div><div id="comment-tools-42612" class="comment-tools"></div><div class="clear"></div><div id="comment-42612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42639"></span>

<div id="answer-container-42639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42639-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you running Wireshark on the actual SMB server, and is the SMB service actually working? When you can only see ARP packets, I'm thinking it might be that you can only see <em>broadcast</em> packets, suggesting that you aren't doing the packet capture on the system in-line with the non-broadcast packets (the SMB traffic, for example).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '15, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-42639" class="comments-container"><span id="42662"></span><div id="comment-42662" class="comment"><div id="post-42662-score" class="comment-score"></div><div class="comment-text"><p>SMB service was actually working. I ran Wireshark from a PC connected wirelessly to router - only PS2 SCPH-70012 and Addonics NAS2U device were connected by CAT5 ETH cables.</p></div><div id="comment-42662-info" class="comment-info"><span class="comment-age">(26 May '15, 06:23)</span> doctorxyz</div></div><span id="42667"></span><div id="comment-42667" class="comment"><div id="post-42667-score" class="comment-score"></div><div class="comment-text"><p>With the capture setup you have described, you can only capture the broadcast packets (ARP) of this connection. The SMB Traffic is unicast traffic, which you can´t see on your actual capture position.</p><p>For further information about the right capture setup I recommend yiu the following link:</p><p><a href="https://wiki.wireshark.org/CaptureSetup">https://wiki.wireshark.org/CaptureSetup</a></p></div><div id="comment-42667-info" class="comment-info"><span class="comment-age">(26 May '15, 11:41)</span> Christian_R</div></div></div><div id="comment-tools-42639" class="comment-tools"></div><div class="clear"></div><div id="comment-42639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

