+++
type = "question"
title = "Wireshark unable to display captured trace file in correct format"
description = '''When my notebook PC is plugged into the office LAN network, running Wireshark can correctly display the trace file (such as those provided for Wireshark training purpose)showing protocol fields such as TCP. DNS, HTTP, etc. However, when I use the same notebook PC at home under the wireless LAN envir...'''
date = "2010-10-12T20:50:00Z"
lastmod = "2010-10-20T03:52:00Z"
weight = 493
keywords = [ "file", "display", "trace" ]
aliases = [ "/questions/493" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark unable to display captured trace file in correct format](/questions/493/wireshark-unable-to-display-captured-trace-file-in-correct-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-493-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When my notebook PC is plugged into the office LAN network, running Wireshark can correctly display the trace file (such as those provided for Wireshark training purpose)showing protocol fields such as TCP. DNS, HTTP, etc. However, when I use the same notebook PC at home under the wireless LAN environment, Wireshark cannot display the same trace file as I have done in office. In other words, protocol fields such as TCP, HTTP cannot be displayed.</p><p>I suspect this has something to do with the environment in which Wireshark is run. But I have no solution to this problem. What I want is simply to be able to read the trace file regardless of whichever network my notebook PC is connected to: wireless or wired.</p><p>I am stuck with this problem for months. Please help if there is a way.</p><p>Regards, HL</p><pre><code>enter code here</code></pre></div><div id="question-tags" class="tags-container tags">file display trace</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '10, 20:50</strong></p><img src="https://secure.gravatar.com/avatar/fedd8b3414b0a514f1e92b3005640c65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="korhl&#39;s gravatar image" /><p>korhl<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="korhl has no accepted answers">0%</span></p></div></div><div id="comments-container-493" class="comments-container"><span id="535"></span><div id="comment-535" class="comment"><div id="post-535-score" class="comment-score"></div><div class="comment-text"><p>Can you provide a screenshot via picasa or flickr?</p></div><div id="comment-535-info" class="comment-info"><span class="comment-age">(19 Oct '10, 07:46)</span> GeonJay</div></div></div><div id="comment-tools-493" class="comment-tools"></div><div class="clear"></div><div id="comment-493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="494"></span>

<div id="answer-container-494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-494-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you set up the decryption keys (assuming you use encryption on your home WLAN). Select View &gt; Wireless Toolbar. On the right you will see where you can add decryption keys.</p><p>If you are capturing the traffic on the wired network and seeing the TCP, DNS, HTTP protocol information, but capturing at home on your Wireless LAN environment, most likely you need to add those decryption keys so Wireshark can decrypt and show you the traffic.</p><p>See wiki.wireshark.org/CaptureSetup/WLAN for more information on capturing in a WLAN environment.</p><p>Hope that helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '10, 21:17</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-494" class="comments-container"></div><div id="comment-tools-494" class="comment-tools"></div><div class="clear"></div><div id="comment-494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="499"></span>

<div id="answer-container-499" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-499-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, I am using encryption for my wireless access at home (the 10-digit pass-code which was entered into my wireless router). However I am not capturing any traffic for viewing at home or at the office. The trace files that I am referring to are the files used for the Wireshark Lab practice such as the trace files used by Kurose book. I can display the trace file properly at the office but not at home, using the same notebook PC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '10, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/fedd8b3414b0a514f1e92b3005640c65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="korhl&#39;s gravatar image" /><p>korhl<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="korhl has no accepted answers">0%</span></p></div></div><div id="comments-container-499" class="comments-container"></div><div id="comment-tools-499" class="comment-tools"></div><div class="clear"></div><div id="comment-499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="554"></span>

<div id="answer-container-554" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-554-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A day or two I have posted the message, I finally managed to solve the problem through further exploration. In fact I wanted to share this piece of good news with all concerned but was delayed due to busy work schedule until I saw your message through my email notification today. What I did not say in my previous message in explaining the environment when such problem occurred was that I was using different user accounts to login to my notebook between office and home. The reason to this was that the office account has mapped up many network shared folders that are not needed at home. So I used another user account at home that practically has no mapped drives and this would make the power-up sequence to respond faster. When I looked into the respective users' folders, I realised Wireshark has created startup files (under &lt;user id=""&gt;Application DataWireshark folder)which would customise the way each user uses Wireshark. Somehow this file with the name "disable_protos" was found in the startup folder of my home user account but not office account and it, being a text file, consists of a line that reads as "ip". According to Wireshark manual, this means it will not interpret all packets from IP and above. So TCP, HTTP, DNS will not be interpreted. I deleted this diabled_protos file and the problem is immediately solved. Now I can display packets from HTTP, DNS TCP, etc from the trace files. I am happy to announce that this case is closed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '10, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/fedd8b3414b0a514f1e92b3005640c65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="korhl&#39;s gravatar image" /><p>korhl<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="korhl has no accepted answers">0%</span></p></div></div><div id="comments-container-554" class="comments-container"></div><div id="comment-tools-554" class="comment-tools"></div><div class="clear"></div><div id="comment-554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

