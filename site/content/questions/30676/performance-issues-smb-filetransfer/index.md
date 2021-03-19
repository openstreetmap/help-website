+++
type = "question"
title = "Performance issues SMB filetransfer"
description = '''I have read and heard of some similar cases but are unable to pinpoint the problem using wireshark. When we upload files to our servers (behind a firewall) file transfer seems to be capped to 5MB/s. As soon as I download a file from one of our servers the speed starts at 5MB/s and then jumps up to (...'''
date = "2014-03-11T00:08:00Z"
lastmod = "2014-03-12T13:57:00Z"
weight = 30676
keywords = [ "slow", "smb" ]
aliases = [ "/questions/30676" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Performance issues SMB filetransfer](/questions/30676/performance-issues-smb-filetransfer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30676-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have read and heard of some similar cases but are unable to pinpoint the problem using wireshark.</p><p>When we upload files to our servers (behind a firewall) file transfer seems to be capped to 5MB/s. As soon as I download a file from one of our servers the speed starts at 5MB/s and then jumps up to (the maximum of our clients, in this case) 11MB/s. When I start a new upload to the server (after the actions described above) it starts and stays at 11MB/s.</p><p>It is not just one server, it concerns all servers behind our firewall, we even tested the above by moving two servers in front of the firewall and the issue automatically resolves. It also immediately returns when we place the servers behind the firewall again.</p><p>We are currently working on replacing this firewall, but since my interest in wireshark ... I should be able to confirm this entire issue with a few good captures right? What am I looking for, throughput, TCP windows sizes? All the other key points are good (like round trip time, no extremely delayed packets, no replacements of sequence numbers, this I all checked).</p></div><div id="question-tags" class="tags-container tags">slow smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '14, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/25daf811ebe1190b06093b3676a2533f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoepMeloen86&#39;s gravatar image" /><p>JoepMeloen86<br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoepMeloen86 has one accepted answer">50%</span></p></div></div><div id="comments-container-30676" class="comments-container"><span id="30712"></span><div id="comment-30712" class="comment"><div id="post-30712-score" class="comment-score"></div><div class="comment-text"><p>&lt;bump&gt;</p><p>Tried to create some throughput graphs, and came up with the following:</p><p><a href="http://imageshack.com/a/img34/2668/wvcr.png">http://imageshack.com/a/img34/2668/wvcr.png</a></p><p>To be honest, this doesn't make much sense. Can anyone explain to me why this graph shows both high and low throughput at the same time?</p></div><div id="comment-30712-info" class="comment-info"><span class="comment-age">(12 Mar '14, 02:40)</span> JoepMeloen86</div></div><span id="30732"></span><div id="comment-30732" class="comment"><div id="post-30732-score" class="comment-score"></div><div class="comment-text"><p>Really, nobody?</p><p>I zoomed in on the above graph and viewed a couple of packets that were extremely close together (hence the impression that the throughput is high and low at the same time) but could not find a difference.</p><p>How does Wireshark determine a high or low throughput? Windowsize and payload are exactly the same with each packets I compare... ?</p><p>In other terms, how does Wireshark calculate a 5MB/s throughput (for example) from a single packet?</p></div><div id="comment-30732-info" class="comment-info"><span class="comment-age">(12 Mar '14, 08:19)</span> JoepMeloen86</div></div></div><div id="comment-tools-30676" class="comment-tools"></div><div class="clear"></div><div id="comment-30676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30743"></span>

<div id="answer-container-30743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30743-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not calculate throughput from a single packet; it uses a 21-segment moving average. See <a href="http://ask.wireshark.org/questions/28110/tcp-streamgraph-throughput">this question</a> for an explanation by Gerald Combs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-30743" class="comments-container"><span id="30793"></span><div id="comment-30793" class="comment"><div id="post-30793-score" class="comment-score"></div><div class="comment-text"><p>Ok, sounds like that's the thing I'm looking for. However, I can't seem to verify this.</p><p>Most packets in these 40 segments have a payload of 1514 bytes, and there a no large delays (as far as I can see) between the first 20 segments and the next.</p><p>However the throughput graph is very clear that every other 20 segments is slow, fast, slow, fast, creating this weird graph.</p></div><div id="comment-30793-info" class="comment-info"><span class="comment-age">(14 Mar '14, 01:32)</span> JoepMeloen86</div></div></div><div id="comment-tools-30743" class="comment-tools"></div><div class="clear"></div><div id="comment-30743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

