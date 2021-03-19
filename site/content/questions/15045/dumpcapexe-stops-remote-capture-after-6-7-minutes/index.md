+++
type = "question"
title = "dumpcap.exe stops remote capture after 6-7 minutes"
description = '''Hi, I have problem with remote capturing. After 6-7 minutes from tshark remote start, pcap file stops growing. Nothing happens, no errors shows up. Dumpcap.exe is still running in Task Manager, and the lock to pcap file is still holding by dumpcap. I use command: C:&#92;Program Files (x86)&#92;Wireshark&#92;tsh...'''
date = "2012-10-17T01:23:00Z"
lastmod = "2012-10-17T05:12:00Z"
weight = 15045
keywords = [ "dumpcap", "hangs" ]
aliases = [ "/questions/15045" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dumpcap.exe stops remote capture after 6-7 minutes](/questions/15045/dumpcapexe-stops-remote-capture-after-6-7-minutes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15045-score" class="post-score" title="current number of votes">0</div><span id="post-15045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have problem with remote capturing. After 6-7 minutes from tshark remote start, pcap file stops growing. Nothing happens, no errors shows up. Dumpcap.exe is still running in Task Manager, and the lock to pcap file is still holding by dumpcap. I use command: C:\Program Files (x86)\Wireshark\tshark.exe -i rpcap://[10.154.5.33]:2002/\Device\NPF_{E5C7CD1D-35A9-4C3C-8E5F-C0BC37904D10} -w D:/tshark_dump.pcap</p><p>BR, Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-hangs" rel="tag" title="see questions tagged &#39;hangs&#39;">hangs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '12, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/a084efff9bbb656a084b107022d55386?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul_PL&#39;s gravatar image" /><p><span>Paul_PL</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul_PL has no accepted answers">0%</span></p></div></div><div id="comments-container-15045" class="comments-container"></div><div id="comment-tools-15045" class="comment-tools"></div><div class="clear"></div><div id="comment-15045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15056"></span>

<div id="answer-container-15056" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15056-score" class="post-score" title="current number of votes">1</div><span id="post-15056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably not a problem with the remote capture in itself, but with tshark crashing because it ran out of memory.</p><p>See <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '12, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15056" class="comments-container"></div><div id="comment-tools-15056" class="comment-tools"></div><div class="clear"></div><div id="comment-15056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

