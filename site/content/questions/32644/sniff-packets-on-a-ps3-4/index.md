+++
type = "question"
title = "Sniff packets on a PS3 &amp; 4"
description = '''Hi All I am currently running Version 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10) I get a sudden random drop out on my network and there are no trails left on the logs of the cisco switches. I have had Cisco Tac have a look at this issue. Cant find anything. I have a 600mb pipe on the network. I on...'''
date = "2014-05-08T07:23:00Z"
lastmod = "2014-05-08T07:45:00Z"
weight = 32644
keywords = [ "console", "game", "span", "dropped", "packet" ]
aliases = [ "/questions/32644" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Sniff packets on a PS3 & 4](/questions/32644/sniff-packets-on-a-ps3-4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32644-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All I am currently running Version 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10)</p><p>I get a sudden random drop out on my network and there are no trails left on the logs of the cisco switches. I have had Cisco Tac have a look at this issue. Cant find anything. I have a 600mb pipe on the network.</p><p>I only seem to have these issues with games console that run a bespoke app.</p><p>I want to test this by have a dumb switch plugged in to the network port with a laptop running wire shark plugged in to it and a PlayStation plugged in to it too.</p><p>I want to know how I can sniff the port of the PS3 without having to configure span port on the switch</p><p>Many thanks</p></div><div id="question-tags" class="tags-container tags">console game span dropped packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '14, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/2030ebdfaafb9807075af345b41eb7c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamessimo1980&#39;s gravatar image" /><p>jamessimo1980<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamessimo1980 has no accepted answers">0%</span></p></div></div><div id="comments-container-32644" class="comments-container"></div><div id="comment-tools-32644" class="comment-tools"></div><div class="clear"></div><div id="comment-32644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32645"></span>

<div id="answer-container-32645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32645-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><em>I want to know how I can sniff the port of the PS3 without having to configure span port on the switch</em></p></blockquote><p>You can't (easily). The whole reason for a switch is to segregate traffic to the ports appropriate for the traffic, so the traffic between the PS3 and the unnamed external entity will only appear on the switch ports those two items are connected to. See the wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a> for more info on how you can make the capture you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '14, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '14, 07:48</p></div></div><div id="comments-container-32645" class="comments-container"><span id="32646"></span><div id="comment-32646" class="comment"><div id="post-32646-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Thanks for the response. The link gives great examples, but is not really geared around to helping me with my issue.</p><p>So is it fair to say that there is no actual way with this method</p><p>Thanks</p></div><div id="comment-32646-info" class="comment-info"><span class="comment-age">(08 May '14, 08:00)</span> jamessimo1980</div></div><span id="32647"></span><div id="comment-32647" class="comment"><div id="post-32647-score" class="comment-score"></div><div class="comment-text"><p>Only by messing with ARP tables, but that introduces a whole lot of other issues.</p><p>Why can't you use a cheap switch that does spanning?</p></div><div id="comment-32647-info" class="comment-info"><span class="comment-age">(08 May '14, 09:50)</span> grahamb ♦</div></div><span id="32656"></span><div id="comment-32656" class="comment"><div id="post-32656-score" class="comment-score"></div><div class="comment-text"><p>You could run it through a bridged dual-nic PC. Or like @grahamb said, get a fairly inexpensive port spanning/port mirroring switch.</p></div><div id="comment-32656-info" class="comment-info"><span class="comment-age">(08 May '14, 22:10)</span> Rooster_50</div></div></div><div id="comment-tools-32645" class="comment-tools"></div><div class="clear"></div><div id="comment-32645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

