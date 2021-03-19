+++
type = "question"
title = "Easiest way to detect prohibited activity?"
description = '''I have mirrored the &quot;hot&quot; port on our switch and run that to a dedicated PC we used only to monitor network activity and I am able to monitor all traffic on our network this way, so when we have a network bottleneck I am able to fairly easily see what IP is using the bandwidth (I then use Angry IP S...'''
date = "2014-07-29T17:22:00Z"
lastmod = "2014-08-01T16:23:00Z"
weight = 34986
keywords = [ "url", "streaming", "facebook", "youtube" ]
aliases = [ "/questions/34986" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Easiest way to detect prohibited activity?](/questions/34986/easiest-way-to-detect-prohibited-activity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34986-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have mirrored the "hot" port on our switch and run that to a dedicated PC we used only to monitor network activity and I am able to monitor all traffic on our network this way, so when we have a network bottleneck I am able to fairly easily see what IP is using the bandwidth (I then use Angry IP Scanner to get the machine name and sometimes it also shows the name of the user logged in).</p><p>The issue is that I have a lot of difficulty seeing what they are doing. For example one user today I know was on Youtube (which is prohibited 99% of the time), and I filtered the capture using "http includes youtube" and it did show several packets to the IP address for that machine...but the boss wants to know what video he was watching so he can determine if it is work related, not work related but not inappropriate, or inappropriate. I expanded every field for every packet that turned up using the filter and I didn't see a URL or even the word Youtube for that matter.</p><p>In addition to doing this when issues occur, the boss wants me to spend an hour or two per week filtering through the traffic that week and notify him if people are on Youtube, Facebook, and really anything streaming that will use a lot of bandwidth (we are in a rural area and our whole facility only has 6Mbps down and about 4Mbps up).</p></div><div id="question-tags" class="tags-container tags">url streaming facebook youtube</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '14, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/2782c7972b618e5ba018a4fd41f733f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20M&#39;s gravatar image" /><p>Chris M<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris M has no accepted answers">0%</span></p></div></div><div id="comments-container-34986" class="comments-container"></div><div id="comment-tools-34986" class="comment-tools"></div><div class="clear"></div><div id="comment-34986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34999"></span>

<div id="answer-container-34999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34999-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your looking at Wireshark you're probably looking in the wrong place. This tool is poised to get to the details of every bit of every packet it sees. What you are looking for is traffic analysis. Then tools like etherape and ntopng come to mind. These are much better suited for these kinds of tasks.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '14, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-34999" class="comments-container"><span id="35002"></span><div id="comment-35002" class="comment"><div id="post-35002-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I was talking about using Wireshark. I just started a couple of months ago and they have just been doing what they could with Wireshark for the past several years. This is currently on XP machine in a 100% Windows environment (about 90% Windows 7 and the rest XP excluding servers most of which are on Server 2003).</p><p>Can anyone suggest a good free tool for this that works in a 100% Windows environment?</p></div><div id="comment-35002-info" class="comment-info"><span class="comment-age">(30 Jul '14, 06:56)</span> Chris M</div></div><span id="35003"></span><div id="comment-35003" class="comment"><div id="post-35003-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Can anyone suggest a good free tool for this that works in a 100% Windows environment?</p></blockquote><p>sure:</p><blockquote><p><a href="https://www.google.com/?q=windows%20network%20monitor%20freeware">https://www.google.com/?q=windows%20network%20monitor%20freeware</a></p></blockquote></div><div id="comment-35003-info" class="comment-info"><span class="comment-age">(30 Jul '14, 08:48)</span> Kurt Knochner ♦</div></div><span id="35009"></span><div id="comment-35009" class="comment"><div id="post-35009-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, that did not turn up anything particularly useful. 90% of what is there is either not free or won't work for monitoring more than 5 or 10 PCs. Network Miner seems to be the closest bet, allowing me to easily see who is on Youtube, Facebook, etc...I just still am unable to see what they were doing on the site.</p><p>Anyone have a favorite free software to monitor network traffic similar to my described needs?</p></div><div id="comment-35009-info" class="comment-info"><span class="comment-age">(30 Jul '14, 11:37)</span> Chris M</div></div></div><div id="comment-tools-34999" class="comment-tools"></div><div class="clear"></div><div id="comment-34999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35079"></span>

<div id="answer-container-35079" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35079-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I did a little testing just now on my own machine, and it looks like this just plain isn't possible to do. It looks like the initial connection of youtube is using HTTP, but once the connection is established it moves over to HTTPS/TLSv1. Try it yourself if you like. I'm using the lazy filter on a trace: frame contains "youtube"</p><p>Sorry, but you might be out of luck on this one...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '14, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/4a4df10c701372e5dbbb8015a1d6b67b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_harrold&#39;s gravatar image" /><p>patrick_harrold<br />
<span class="score" title="36 reputation points">36</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_harrold has no accepted answers">0%</span></p></div></div><div id="comments-container-35079" class="comments-container"></div><div id="comment-tools-35079" class="comment-tools"></div><div class="clear"></div><div id="comment-35079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

