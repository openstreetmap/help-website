+++
type = "question"
title = "can wireshark pick up data from a mobile"
description = '''hi can wireshark sniff the data directly from a mobile phone or does does the phone have to go through my router for it to pick up the packets?? many thanks'''
date = "2014-01-07T07:55:00Z"
lastmod = "2014-01-07T19:22:00Z"
weight = 28634
keywords = [ "mobile" ]
aliases = [ "/questions/28634" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [can wireshark pick up data from a mobile](/questions/28634/can-wireshark-pick-up-data-from-a-mobile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28634-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi</p><p>can wireshark sniff the data directly from a mobile phone or does does the phone have to go through my router for it to pick up the packets??</p><p>many thanks</p></div><div id="question-tags" class="tags-container tags">mobile</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '14, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/2f71902b61e9ff0244b76254eadfd590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobsta&#39;s gravatar image" /><p>bobsta<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobsta has no accepted answers">0%</span></p></div></div><div id="comments-container-28634" class="comments-container"></div><div id="comment-tools-28634" class="comment-tools"></div><div class="clear"></div><div id="comment-28634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28657"></span>

<div id="answer-container-28657" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28657-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What kind of traffic are you trying to catch? if its 802.11 (wirless) - you can use this guide <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WLAN</a></p><p>If you are talking about 3G - I never able to capture 3G traffic with wireless (even with 3G modem - as it seem to have some kind of issue with Winpcap) - maybe one of the experts can assist here...-</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '14, 19:04</strong></p><img src="https://secure.gravatar.com/avatar/94630d1ea1108afeafb344e884044d15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boaz%20Galil&#39;s gravatar image" /><p>Boaz Galil<br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boaz Galil has no accepted answers">0%</span></p></div></div><div id="comments-container-28657" class="comments-container"></div><div id="comment-tools-28657" class="comment-tools"></div><div class="clear"></div><div id="comment-28657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28658"></span>

<div id="answer-container-28658" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28658-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>For 802.11, see Boaz Galil's answer.</p><p>For mobile phone networks (2G, 3G, etc.):</p><ul><li><p>If you're trying to run Wireshark on some machine <em>other</em> than your mobile phone, capturing traffic to and from your mobile phone isn't possible without specialized hardware and software.</p></li><li><p>If you're trying to capture with software running <em>on</em> the phone (or on a machine with a mobile phone network modem), IP traffic will probably appear as PPP traffic, so <a href="http://wiki.wireshark.org/CaptureSetup/PPP">the Wireshark Wiki CaptureSetup/PPP</a> page applies. ("WinPcap" implies "Windows", and that page says "doesn't work on modern versions of Windows".)</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '14, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-28658" class="comments-container"></div><div id="comment-tools-28658" class="comment-tools"></div><div class="clear"></div><div id="comment-28658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

