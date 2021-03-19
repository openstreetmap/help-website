+++
type = "question"
title = "Malformed NTLM packet"
description = '''Hey all! I&#x27;m receiving a Malformed Packet (Exception Occurred) error while trying to do an NTLMSSP AUTH over SMB2 using Wireshark 2.0.1 (see capture below). I do not receive the malformed packet error on Wireshark 1.12.1 despite the data being identical. In either case, however, I receive an NT STAT...'''
date = "2016-02-02T11:12:00Z"
lastmod = "2016-02-02T11:12:00Z"
weight = 49734
keywords = [ "ntlm", "malformed" ]
aliases = [ "/questions/49734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed NTLM packet](/questions/49734/malformed-ntlm-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey all!</p><p>I'm receiving a Malformed Packet (Exception Occurred) error while trying to do an NTLMSSP AUTH over SMB2 using Wireshark 2.0.1 (see capture below).</p><p>I do not receive the malformed packet error on Wireshark 1.12.1 despite the data being identical. In either case, however, I receive an NT STATUS INVALID PARAMETER from the server I'm trying to authenticate anonymously with, and I think that sorting out the Wireshark issue will help me diagnose and fix that problem!</p><p>Here's the capture with the malformed error (packet 4) on Wireshark 2.0.1: <a href="https://www.cloudshark.org/captures/aa9cb95e985a">https://www.cloudshark.org/captures/aa9cb95e985a</a></p><p>And here is the same capture on Wireshark 1.12.1. This shows the correct structure for the packet (number 4) (though it is still rejected by the server): <a href="https://www.cloudshark.org/captures/7aa8a2eea803">https://www.cloudshark.org/captures/7aa8a2eea803</a></p><p>I'd really appreciate any help!</p></div><div id="question-tags" class="tags-container tags">ntlm malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '16, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/00c8cb3a82c24ca6badf9474be3e63c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthewbird&#39;s gravatar image" /><p>matthewbird<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthewbird has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Feb '16, 11:16</p></div></div><div id="comments-container-49734" class="comments-container"></div><div id="comment-tools-49734" class="comment-tools"></div><div class="clear"></div><div id="comment-49734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

