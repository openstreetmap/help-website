+++
type = "question"
title = "How can get netflow information when pcap file is too big for wireshark to open"
description = '''I usually obtain flow information by opening statistics features in the wireshark. However, this way is blocked when the pcap file is too big to open(it will cause RAM overload when loading big pcap file into wireshark). I wonder if I could get flow statistical feature via command line, like tshark,...'''
date = "2016-06-15T01:04:00Z"
lastmod = "2016-06-15T05:05:00Z"
weight = 53456
keywords = [ "netflow", "statistics", "editcap", "tshark" ]
aliases = [ "/questions/53456" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can get netflow information when pcap file is too big for wireshark to open](/questions/53456/how-can-get-netflow-information-when-pcap-file-is-too-big-for-wireshark-to-open)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53456-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I usually obtain flow information by opening statistics features in the wireshark. However, this way is blocked when the pcap file is too big to open(it will cause RAM overload when loading big pcap file into wireshark). I wonder if I could get flow statistical feature via command line, like tshark, editcap or something else. I really appreciate if some experts help me out. Best regards</p></div><div id="question-tags" class="tags-container tags">netflow statistics editcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '16, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/e5680786b535deed45d34baaa37e45a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rui&#39;s gravatar image" /><p>Rui<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rui has no accepted answers">0%</span></p></div></div><div id="comments-container-53456" class="comments-container"></div><div id="comment-tools-53456" class="comment-tools"></div><div class="clear"></div><div id="comment-53456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53459"></span>

<div id="answer-container-53459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53459-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can cut the capture files in half if that helps. Have a look at the command line tools capinfos and editcap.</p><p>Tshark has some interesting statistics options as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '16, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53459" class="comments-container"><span id="53465"></span><div id="comment-53465" class="comment"><div id="post-53465-score" class="comment-score"></div><div class="comment-text"><p>I wanna get netflow information like flow duration, flow start time, flow transmission rate on both ends. The pcap file is merged from 180 small pcap files and ends up about 83GB. I conduct that for the reason that some single flow perhaps divide into multi flow if don't merge all the files. I dont wanna miss any details on the flow information. Could you help me out?</p></div><div id="comment-53465-info" class="comment-info"><span class="comment-age">(15 Jun '16, 06:56)</span> Rui</div></div><span id="53466"></span><div id="comment-53466" class="comment"><div id="post-53466-score" class="comment-score">1</div><div class="comment-text"><p>netflow, that's not an available output of Wireshark related tools. These are tools primarily aimed at getting at the every individual bit of a packet and show its meaning. Netflow is aggregating as much as possible, an analysis function which Wireshark has some of, but not its strong suit.</p><p>Maybe riverbed has something on offer for you, click on their logo on the right.</p></div><div id="comment-53466-info" class="comment-info"><span class="comment-age">(15 Jun '16, 08:34)</span> Jaap ♦</div></div><span id="53481"></span><div id="comment-53481" class="comment"><div id="post-53481-score" class="comment-score">1</div><div class="comment-text"><p>As suggested by Jaap, look at Riverbed's SteelCentral Packet Analyzer, there's a 30 day free trial.</p></div><div id="comment-53481-info" class="comment-info"><span class="comment-age">(15 Jun '16, 14:10)</span> grahamb ♦</div></div><span id="53484"></span><div id="comment-53484" class="comment"><div id="post-53484-score" class="comment-score"></div><div class="comment-text"><p>@Jaap @grahamb Thank you for your commitment, I really appreciate your valuable advice for me. I will have a trail on the software you recommended</p></div><div id="comment-53484-info" class="comment-info"><span class="comment-age">(15 Jun '16, 18:20)</span> Rui</div></div></div><div id="comment-tools-53459" class="comment-tools"></div><div class="clear"></div><div id="comment-53459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

