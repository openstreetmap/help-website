+++
type = "question"
title = "Installing 64 bit on 2012 R2 VM -causes obsolete driver install??"
description = '''Hi New to Wireshark. I have installed the latest 64bit version on a Citrix 6.0 VM Xen running a fully patched Win 2012 R2 64 bit server with windows auto update. The host for the VM is suggesting this has caused/triggered installation of citrix 5.5 drivers and other obsolete stuff. This then cause t...'''
date = "2014-02-06T04:21:00Z"
lastmod = "2014-02-06T07:20:00Z"
weight = 29487
keywords = [ "drivers", "vm", "citrix" ]
aliases = [ "/questions/29487" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Installing 64 bit on 2012 R2 VM -causes obsolete driver install??](/questions/29487/installing-64-bit-on-2012-r2-vm-causes-obsolete-driver-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29487-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi New to Wireshark. I have installed the latest 64bit version on a Citrix 6.0 VM Xen running a fully patched Win 2012 R2 64 bit server with windows auto update. The host for the VM is suggesting this has caused/triggered installation of citrix 5.5 drivers and other obsolete stuff. This then cause the VM to stop talking to the world in a big way. I cant find (Google) any references to this sort of problem. Also There was previously a reasonable amount of memory free, then we got memory alarms. Anyone had any similar problems with an Wireshark install causing various old drivers to be installed also?</p><p>Anyone installed Wireshark 64 on a Citrix xen 6.0 and windows 2012 R2 without problems please?</p></div><div id="question-tags" class="tags-container tags">drivers vm citrix</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '14, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/1e85cb6152cb954d0d44a9b94ece55e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sad%20Developer&#39;s gravatar image" /><p>Sad Developer<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sad Developer has no accepted answers">0%</span></p></div></div><div id="comments-container-29487" class="comments-container"></div><div id="comment-tools-29487" class="comment-tools"></div><div class="clear"></div><div id="comment-29487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29490"></span>

<div id="answer-container-29490" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29490-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The only driver that's being installed by the Wireshark installer package is the WinPcap NDIS driver, as part of the WinPcap installation. Wireshark itself has no drivers. That NDIS driver could be considered 'old' on a Windows 2012 R2. However, that's something the WinPcap community needs to fix. Please file a bug report for WinPcap</p><blockquote><p><a href="http://www.winpcap.org/bugs.htm">http://www.winpcap.org/bugs.htm</a></p></blockquote><p>BTW: Can you please test if you get the same error message, when you install WinPcap only?</p><blockquote><p><a href="http://www.winpcap.org/install/default.htm">http://www.winpcap.org/install/default.htm</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '14, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29490" class="comments-container"></div><div id="comment-tools-29490" class="comment-tools"></div><div class="clear"></div><div id="comment-29490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

