+++
type = "question"
title = "error updating record: invalid key format"
description = '''I&#x27;m trying to decrypt IEEE 802.11 wireless traffic and am using a NetGear router set to &quot;WPA-PSK [TKIP]&quot; with SSID: rasa and Pass:rasadesign. I&#x27;m using Wireshark 1.8.1 (with X11) for Mac and I&#x27;ve tried to enter the string created by Wireshark&#x27;s PSK generator: 1e3d2784c2693c013d5e20f58371b5b25b92ae00...'''
date = "2012-08-16T10:29:00Z"
lastmod = "2012-08-29T09:22:00Z"
weight = 13688
keywords = [ "wpa-psk", "format", "key", "invalid", "error" ]
aliases = [ "/questions/13688" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error updating record: invalid key format](/questions/13688/error-updating-record-invalid-key-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13688-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt IEEE 802.11 wireless traffic and am using a NetGear router set to "WPA-PSK [TKIP]" with SSID: rasa and Pass:rasadesign. I'm using Wireshark 1.8.1 (with X11) for Mac and I've tried to enter the string created by Wireshark's PSK generator: 1e3d2784c2693c013d5e20f58371b5b25b92ae00389eaf7c525427dd28b2c3ef but all I get is an error: "error updating record: invalid key format"</p><p>I've also tried wpa-pwd with the format "rasa:rasadesign" and "rasadesign:rasa" with the same effect.</p><p>I've checked everything I could find on the net about this error, but can't find this problem anywhere. What am I doing wrong? Thanks.</p></div><div id="question-tags" class="tags-container tags">wpa-psk format key invalid error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '12, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/adafdfc93927685f5928d0ee7cbf658b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tabula_rasa&#39;s gravatar image" /><p>tabula_rasa<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tabula_rasa has no accepted answers">0%</span></p></div></div><div id="comments-container-13688" class="comments-container"></div><div id="comment-tools-13688" class="comment-tools"></div><div class="clear"></div><div id="comment-13688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13958"></span>

<div id="answer-container-13958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13958-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As far as wpa-psk is concerned, there was a bug. I checked in a fix in <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=44694">r44694</a>, which will be scheduled to be backported to the 1.8 branch. For now, if you are running Windows, you can test with any <a href="http://www.wireshark.org/download/automated/">automated build</a> version 44694 or later. If the installer isn't there yet, wait a while until the <a href="http://buildbot.wireshark.org/trunk/waterfall">buildbots</a> have finished creating them.</p><p>I don't know what the problem is with wpa-pwd.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '12, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-13958" class="comments-container"></div><div id="comment-tools-13958" class="comment-tools"></div><div class="clear"></div><div id="comment-13958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

