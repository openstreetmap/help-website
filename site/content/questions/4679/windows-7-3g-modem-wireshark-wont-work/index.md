+++
type = "question"
title = "Windows 7, 3g modem. Wireshark wont work"
description = '''Hi. I installed wireshark on windows 7, the latest winpcap but i cannot capture anything. I think the problem is that i cannot select the correct interface. It shows only one interface in the drop down menu and it&#x27;s a wrong one. I&#x27;m using a ZTE 3G modem. Any help would be appriciated. Thank you in a...'''
date = "2011-06-22T14:03:00Z"
lastmod = "2011-06-23T10:15:00Z"
weight = 4679
keywords = [ "interface", "zte", "modem", "3g" ]
aliases = [ "/questions/4679" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Windows 7, 3g modem. Wireshark wont work](/questions/4679/windows-7-3g-modem-wireshark-wont-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4679-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I installed wireshark on windows 7, the latest winpcap but i cannot capture anything. I think the problem is that i cannot select the correct interface. It shows only one interface in the drop down menu and it's a wrong one. I'm using a ZTE 3G modem. Any help would be appriciated. Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">interface zte modem 3g</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '11, 14:03</strong></p><img src="https://secure.gravatar.com/avatar/59ff00ac1f07888c3f4942002cc969c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Syokk&#39;s gravatar image" /><p>Syokk<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Syokk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '11, 22:22</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-4679" class="comments-container"></div><div id="comment-tools-4679" class="comment-tools"></div><div class="clear"></div><div id="comment-4679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4697"></span>

<div id="answer-container-4697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4697-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://www.winpcap.org/misc/faq.htm#Q-5">question 5 in the WinPcap FAQ</a>, which says</p><blockquote><p>Windows Vista and more recent. It's not possible to capture on PPP/VPN connections on these operating systems.</p></blockquote><p>Mobile-phone modems show up like other modems - the protocol run over the session is PPP, so they're PPP connections, and, as such, aren't supported by applications using WinPcap, such as WinDump and Wireshark, on Windows Vista or Windows 7 (or the corresponding versions of Windows Server).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '11, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4697" class="comments-container"><span id="4729"></span><div id="comment-4729" class="comment"><div id="post-4729-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. And is there a way to fix that?</p></div><div id="comment-4729-info" class="comment-info"><span class="comment-age">(24 Jun '11, 07:10)</span> Syokk</div></div></div><div id="comment-tools-4697" class="comment-tools"></div><div class="clear"></div><div id="comment-4697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

