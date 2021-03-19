+++
type = "question"
title = "Packets with &quot;Time Reference&quot; toggled displayed when &quot;rtp.marker==1&quot; display filter applied"
description = '''Very strange thing happening with Wireshark 1.10.7. If you toggle the time reference for any packet (doesn&#x27;t even have to be an RTP packet), and then apply the &quot;rtp.marker==1&quot; display filter, that packet will be displayed when it should not be. Can anyone else confirm this is happening? Is this a bu...'''
date = "2014-05-29T18:19:00Z"
lastmod = "2014-05-29T19:29:00Z"
weight = 33183
keywords = [ "time-reference", "rtp", "display-filter" ]
aliases = [ "/questions/33183" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Packets with "Time Reference" toggled displayed when "rtp.marker==1" display filter applied](/questions/33183/packets-with-time-reference-toggled-displayed-when-rtpmarker1-display-filter-applied)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33183-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Very strange thing happening with Wireshark 1.10.7. If you toggle the time reference for any packet (doesn't even have to be an RTP packet), and then apply the "rtp.marker==1" display filter, that packet will be displayed when it should not be.</p><p>Can anyone else confirm this is happening? Is this a bug or am I doing something wrong here?</p><p>Thanks.</p><p>Travis</p></div><div id="question-tags" class="tags-container tags">time-reference rtp display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '14, 18:19</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 May '14, 18:20</p></div></div><div id="comments-container-33183" class="comments-container"></div><div id="comment-tools-33183" class="comment-tools"></div><div class="clear"></div><div id="comment-33183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33184"></span>

<div id="answer-container-33184" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33184-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you're not doing anything wrong. Some testing shows that packets with a Time Reference set are <em>always</em> displayed, regardless of what display filter is applied, even when the display filter is</p><p>"!(frame.ref_time)"</p><p>which should explicitly exclude all packets that have a Time Reference set.</p><p>Update: I have reported this as a bug on the Wireshark Bugzilla. Bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10142">10142</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '14, 19:29</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 May '14, 21:52</p></div></div><div id="comments-container-33184" class="comments-container"><span id="33185"></span><div id="comment-33185" class="comment"><div id="post-33185-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jim. Would you mind posting the bug number? I would be interested in following it. Thanks again.</p><p>Travis</p></div><div id="comment-33185-info" class="comment-info"><span class="comment-age">(29 May '14, 21:06)</span> Rooster_50</div></div><span id="33189"></span><div id="comment-33189" class="comment"><div id="post-33189-score" class="comment-score"></div><div class="comment-text"><p>Not sure this is a bug at all - it is often quite useful to see time reference points even when the packet would have been normally hidden by a filter. So this may be intentional.</p></div><div id="comment-33189-info" class="comment-info"><span class="comment-age">(30 May '14, 01:45)</span> Jasper ♦♦</div></div></div><div id="comment-tools-33184" class="comment-tools"></div><div class="clear"></div><div id="comment-33184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

