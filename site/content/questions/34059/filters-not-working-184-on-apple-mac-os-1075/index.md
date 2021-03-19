+++
type = "question"
title = "Filters not working 1.8.4 on Apple Mac OS 10.7.5"
description = '''Hi Community, I captured via a VMWare command the traffic from and to a virtual machine into a pcap file[#1]. Now I opened the pcap file in wireshark and tried to filter out the traffic belonging to the local network but no known filter works. I tried the filter expression listed on wireshark wiki b...'''
date = "2014-06-23T02:55:00Z"
lastmod = "2014-06-23T03:02:00Z"
weight = 34059
keywords = [ "capture-filter", "display-filter" ]
aliases = [ "/questions/34059" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filters not working 1.8.4 on Apple Mac OS 10.7.5](/questions/34059/filters-not-working-184-on-apple-mac-os-1075)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34059-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Community, I captured via a VMWare command the traffic from and to a virtual machine into a pcap file[#1]. Now I opened the pcap file in wireshark and tried to filter out the traffic belonging to the local network but no known filter works. I tried the filter expression listed on wireshark <a href="http://wiki.wireshark.org/CaptureFilters">wiki</a> but they failed with the error message for example: <a href="http://media.prontosystems.org/v/bk/wserror.png.html">&lt;"net 192.168.110.0/24" isn't a valid display filter: "192.168.1110.0./24" was unexpected in this context&gt;</a>. Anyone out there with a clue what's wrong with this expression?</p><p>Thx &amp; Bye Tom</p><p><a href="http://">1</a>: vmnet-sniffer -e -w vmnet8.pcap vmnet8</p></div><div id="question-tags" class="tags-container tags">capture-filter display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '14, 02:55</strong></p><img src="https://secure.gravatar.com/avatar/00115bfb6054a7a889424ba9486fd451?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20Wildgruber&#39;s gravatar image" /><p>Thomas Wildg...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas Wildgruber has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '14, 03:52</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-34059" class="comments-container"></div><div id="comment-tools-34059" class="comment-tools"></div><div class="clear"></div><div id="comment-34059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34060"></span>

<div id="answer-container-34060" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34060-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As per the filter page you referenced, that syntax is for capture filters. As you already have a capture you need a <a href="http://wiki.wireshark.org/DisplayFilters">display filter</a>.</p><p>In your particular case the display filter would be <code>ip.src==192.168.110.0/24 and ip.dst==192.168.110.0/24</code>.</p><p>You might also note that Wireshark 1.8.4 is quite old, 1.10.8 is the current stable release with 1.12 coming real soon now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '14, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '14, 03:03</p></div></div><div id="comments-container-34060" class="comments-container"><span id="34062"></span><div id="comment-34062" class="comment"><div id="post-34062-score" class="comment-score"></div><div class="comment-text"><p>Life could be so easy if you look into the right manual, thanks a lot. Because the version I thought that I installed Wireshark for a couple of month ago but you are right, there is a version 1.10 available. I will update Wireshark after this job, also thanks for that.</p><p>Bye Thomas</p></div><div id="comment-34062-info" class="comment-info"><span class="comment-age">(23 Jun '14, 03:22)</span> Thomas Wildg...</div></div><span id="34063"></span><div id="comment-34063" class="comment"><div id="post-34063-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-34063-info" class="comment-info"><span class="comment-age">(23 Jun '14, 03:53)</span> grahamb ♦</div></div></div><div id="comment-tools-34060" class="comment-tools"></div><div class="clear"></div><div id="comment-34060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

