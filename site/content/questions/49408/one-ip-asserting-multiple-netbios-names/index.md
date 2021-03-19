+++
type = "question"
title = "One IP asserting multiple NetBIOS names"
description = '''In a recent capture, I noticed that all NetBIOS machines on the network behaved as expected with NBNS registration broadcast packets in an environment without a WINS server (i.e. they all periodically asserted their name and workgroup). The process was identical except for one IP which frequently se...'''
date = "2016-01-20T10:05:00Z"
lastmod = "2016-01-20T10:05:00Z"
weight = 49408
keywords = [ "spoof", "nbns" ]
aliases = [ "/questions/49408" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [One IP asserting multiple NetBIOS names](/questions/49408/one-ip-asserting-multiple-netbios-names)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49408-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a recent capture, I noticed that all NetBIOS machines on the network behaved as expected with NBNS registration broadcast packets in an environment without a WINS server (i.e. they all periodically asserted their name and workgroup). The process was identical except for one IP which frequently sent a NBNS registration with a name and workgroup that mimicked one of the other machines on the network, cycling through all of the other machine names in an irregular fashion. So is this machine a NetBIOSoTCPIP attack vector, or am I just making things up?</p></div><div id="question-tags" class="tags-container tags">spoof nbns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '16, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/40031c9a6c6054daf72f59db2a3a958b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msumbufu&#39;s gravatar image" /><p>msumbufu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msumbufu has no accepted answers">0%</span></p></div></div><div id="comments-container-49408" class="comments-container"><span id="49433"></span><div id="comment-49433" class="comment"><div id="post-49433-score" class="comment-score"></div><div class="comment-text"><p>To me it sounds like an infected machine, yes, at least if the capture confirms that these packets systematically come from the same IP and MAC address.</p><p>Another explanation could be some weird routing loop involving a NAT, causing the original packets from their legal sources to be forwarded back to the same LAN from which they came with NATed source IP.</p><p>So what is the intended role of the machine behaving this way? Is it meant to be an ordinary workstation or it should do something more sophisticated intentionally?</p></div><div id="comment-49433-info" class="comment-info"><span class="comment-age">(21 Jan '16, 05:04)</span> sindy</div></div></div><div id="comment-tools-49408" class="comment-tools"></div><div class="clear"></div><div id="comment-49408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

