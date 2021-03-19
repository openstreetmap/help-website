+++
type = "question"
title = "Bluetooth HSP with Ubertooth"
description = '''https://wiki.wireshark.org/Bluetooth As per the above link, it sounds like Wireshark can decode all HSP Packets (Rfcomm + SCO/eSCO) when used with Ubertooth One. Can I analyze all BT HSP Packets (Rfcomm + SCO/eSCO) communication between my Smart Phone and COTS Headset using Ubertooth One + Wireshark...'''
date = "2016-04-16T18:17:00Z"
lastmod = "2016-09-06T06:25:00Z"
weight = 51718
keywords = [ "4079" ]
aliases = [ "/questions/51718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bluetooth HSP with Ubertooth](/questions/51718/bluetooth-hsp-with-ubertooth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51718-score" class="post-score" title="current number of votes">0</div><span id="post-51718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="https://wiki.wireshark.org/Bluetooth">https://wiki.wireshark.org/Bluetooth</a></p><p>As per the above link, it sounds like Wireshark can decode all HSP Packets (Rfcomm + SCO/eSCO) when used with Ubertooth One. Can I analyze all BT HSP Packets (Rfcomm + SCO/eSCO) communication between my Smart Phone and COTS Headset using Ubertooth One + Wireshark? If so, could you please explain how?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-4079" rel="tag" title="see questions tagged &#39;4079&#39;">4079</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '16, 18:17</strong></p><img src="https://secure.gravatar.com/avatar/c4479ebb083d41b116749f65faf3250e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manoj%20Prasad&#39;s gravatar image" /><p><span>Manoj Prasad</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manoj Prasad has no accepted answers">0%</span></p></div></div><div id="comments-container-51718" class="comments-container"></div><div id="comment-tools-51718" class="comment-tools"></div><div class="clear"></div><div id="comment-51718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55349"></span>

<div id="answer-container-55349" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55349-score" class="post-score" title="current number of votes">0</div><span id="post-55349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, You probably need to know how to capture Bluetooth traffic by Ubertooth. Unfortunately I never be able to capture Bluetooth traffic by Ubertooth (expect Low Energy), so please ask Ubertooth team: <a href="https://github.com/greatscottgadgets/ubertooth/wiki/Getting-Help">https://github.com/greatscottgadgets/ubertooth/wiki/Getting-Help</a></p><p>Then if you back with logs then Wireshark should show you everything you want, however decoding SCO may be not perfect (most implementations do not allow to capture e/SCO). HSP (RFCOMM) is fully supported, if you do not see it try to use "Decode as" for L2CAP to RFCOMM then RFCOMM to HSP.</p><p>But please remember that Ubertooth does not support EDR, so if your device use it, you cannot capture HSP at all. Most devices use EDR...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '16, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p><span>Michał Łabędzki</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-55349" class="comments-container"></div><div id="comment-tools-55349" class="comment-tools"></div><div class="clear"></div><div id="comment-55349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

