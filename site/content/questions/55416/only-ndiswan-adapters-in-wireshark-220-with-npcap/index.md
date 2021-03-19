+++
type = "question"
title = "Only NdisWan adapters in Wireshark 2.2.0 with Npcap"
description = '''Hi all, After uprgading Wireshark to 2.2.0 I see only 3 &quot;NdisWan Adapters&quot; in list: screenshot Dumpcap gives me the same list (screenshot2): screenshot After reverting to 2.0.5 all interfaces came back again. Rebooting, restarting NPF didn&#x27;t help. OS - Windows 7x64. Tried on another PC with the same...'''
date = "2016-09-09T00:19:00Z"
lastmod = "2016-09-09T02:30:00Z"
weight = 55416
keywords = [ "capture", "npcap", "adapters", "2.2.0", "wireshark" ]
aliases = [ "/questions/55416" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Only NdisWan adapters in Wireshark 2.2.0 with Npcap](/questions/55416/only-ndiswan-adapters-in-wireshark-220-with-npcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55416-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, After uprgading Wireshark to 2.2.0 I see only 3 "NdisWan Adapters" in list: <a href="https://www.dropbox.com/s/93w4h9bdt44qcf1/screen1.JPG?dl=0">screenshot</a></p><p>Dumpcap gives me the same list (screenshot2): <a href="https://www.dropbox.com/s/2ijyrkhvq3am7e7/screen2.JPG?dl=0">screenshot</a></p><p>After reverting to 2.0.5 all interfaces came back again. Rebooting, restarting NPF didn't help. OS - Windows 7x64. Tried on another PC with the same OS - found no such problem.</p><p>Point me please what to look at.</p></div><div id="question-tags" class="tags-container tags">capture npcap adapters 2.2.0 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '16, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p>Packet_vlad<br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Sep '16, 13:15</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-55416" class="comments-container"></div><div id="comment-tools-55416" class="comment-tools"></div><div class="clear"></div><div id="comment-55416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55420"></span>

<div id="answer-container-55420" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55420-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using Npcap? If yes, did you try upgrading it?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '16, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-55420" class="comments-container"><span id="55426"></span><div id="comment-55426" class="comment"><div id="post-55426-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, Yes, you're exactly right - upgrading Npcap to 0.09-r5 solved the problem. Thanks!</p></div><div id="comment-55426-info" class="comment-info"><span class="comment-age">(09 Sep '16, 03:33)</span> Packet_vlad</div></div><span id="55435"></span><div id="comment-55435" class="comment"><div id="post-55435-score" class="comment-score"></div><div class="comment-text"><p>If my suggestion solved your issue, please consider accepting it by clicking on the check mark next to the answer</p></div><div id="comment-55435-info" class="comment-info"><span class="comment-age">(09 Sep '16, 08:17)</span> Pascal Quantin</div></div></div><div id="comment-tools-55420" class="comment-tools"></div><div class="clear"></div><div id="comment-55420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

