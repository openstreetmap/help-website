+++
type = "question"
title = "send packetdata from tshark to wireshark"
description = '''I want to run tshark on a Raspberry Pi after booting or for a defined period of time and save the captured packets into a file. This file should then be accessible from Wireshark on my Windows laptop. I want to do this because I want to capture packets for example when I am not at home and then can ...'''
date = "2016-02-09T07:58:00Z"
lastmod = "2016-02-15T15:24:00Z"
weight = 50018
keywords = [ "raspberry", "tshark", "wireshark" ]
aliases = [ "/questions/50018" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [send packetdata from tshark to wireshark](/questions/50018/send-packetdata-from-tshark-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50018-score" class="post-score" title="current number of votes">0</div><span id="post-50018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to run tshark on a Raspberry Pi after booting or for a defined period of time and save the captured packets into a file. This file should then be accessible from Wireshark on my Windows laptop. I want to do this because I want to capture packets for example when I am not at home and then can analyze the captured data when I am back home. Is that possible? How can I start capturing after booting or for a defined period of time into a file and then send it to Wireshark on my laptop?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-raspberry" rel="tag" title="see questions tagged &#39;raspberry&#39;">raspberry</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '16, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/9dadea16d29f84f50196e1ddbf17a80e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vin&#39;s gravatar image" /><p><span>Vin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vin has no accepted answers">0%</span></p></div></div><div id="comments-container-50018" class="comments-container"></div><div id="comment-tools-50018" class="comment-tools"></div><div class="clear"></div><div id="comment-50018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50019"></span>

<div id="answer-container-50019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50019-score" class="post-score" title="current number of votes">0</div><span id="post-50019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just copy the capture file in the same way you would transfer any other file from the Pi, e.g. scp, or samba.</p><p>Note that capturing for an extended period using tshark may either:</p><ol><li>Run out of memory</li><li>Run out of disk space.</li></ol><p>The former can be fixed by using dumpcap rather than tshark, the same files are produced, but dumpcap doesn't retain any state so doesn't have an ever increasing memory usage.</p><p>The latter can only be fixed by providing the Pi with more disk space, or capturing in a "ring" of files, but note that when the ring "wraps", the earliest files are lost. See the <code>-b</code> option to tshark\dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50019" class="comments-container"><span id="50023"></span><div id="comment-50023" class="comment"><div id="post-50023-score" class="comment-score"></div><div class="comment-text"><p>Similarly, tcpdump can be used to dump to a file; if run with the <code>-w</code> flag, it'll just write raw packet data to the file without interpreting it, and thus won't maintain any memory-eating state. If you have it, but not any of Wireshark's components, installed on the RPi, you won't need to install Wireshark just to get dumpcap.</p></div><div id="comment-50023-info" class="comment-info"><span class="comment-age">(09 Feb '16, 12:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-50019" class="comment-tools"></div><div class="clear"></div><div id="comment-50019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50024"></span>

<div id="answer-container-50024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50024-score" class="post-score" title="current number of votes">0</div><span id="post-50024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I start capturing after booting</p></blockquote><p>That would depend on the OS you're running on your RPi - and Linux isn't "the OS", a particular Linux <em>distribution</em> is "the OS", and the answer may differ between distributions. (System V init? systemd? etc.)</p><blockquote><p>or for a defined period of time into a file</p></blockquote><p>For dumpcap:</p><pre><code>dumpcap -a duration:{N} -w {filename}</code></pre><p>where {N} is the number of seconds for which you want it to capture (which can be a large number, so you can, for example, capture for an entire day with {N} = 86400) and {filename} is the name of the file to which to write. <code>-b</code>, as Graham noted, lets you have a ring of files, so that, if you have limited "disk" space, you can have a ring of files and save only the most recent packets if you don't have enough "disk" space for all the packets.</p><p>Tcpdump, unfortunately, doesn't have a "stop capturing after {N} seconds" option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50024" class="comments-container"><span id="50220"></span><div id="comment-50220" class="comment"><div id="post-50220-score" class="comment-score"></div><div class="comment-text"><p>I run Raspbian on my Raspberry Pi. How can I start capturing after booting there? I read that it can be done by adding a line in /etc/rc.local but I am not sure what to put there.</p></div><div id="comment-50220-info" class="comment-info"><span class="comment-age">(15 Feb '16, 15:24)</span> <span class="comment-user userinfo">Vin</span></div></div></div><div id="comment-tools-50024" class="comment-tools"></div><div class="clear"></div><div id="comment-50024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

