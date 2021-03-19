+++
type = "question"
title = "Wireshark and 2008 R2 server reliability issues"
description = '''I&#x27;ve been having reliability issues with multiple Wireshark versions on 2008 server. Initially the GUI would crash mid-capture. So I then started to use tshark, but this suffered the following issue: When capturing to file the packet counter displayed within cmd prompt would freeze. Pressing any key...'''
date = "2013-09-04T01:10:00Z"
lastmod = "2013-09-04T01:40:00Z"
weight = 24335
keywords = [ "server2008", "tshark", "dumpcap" ]
aliases = [ "/questions/24335" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark and 2008 R2 server reliability issues](/questions/24335/wireshark-and-2008-r2-server-reliability-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24335-score" class="post-score" title="current number of votes">0</div><span id="post-24335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been having reliability issues with multiple Wireshark versions on 2008 server. Initially the GUI would crash mid-capture. So I then started to use tshark, but this suffered the following issue:</p><p>When capturing to file the packet counter displayed within cmd prompt would freeze. Pressing any key on the keyboard (i.e. STDIN) would get the counter incrementing again. I assumed it was just the counter freezing, however looking at the capture file there's a complete gap in capture whilst the screen is frozen.</p><p>Note: The same issue occurs with dumpcap.</p><p>Any help massively appreciated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-server2008" rel="tag" title="see questions tagged &#39;server2008&#39;">server2008</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '13, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/31534d84848dcc810494dce199a020f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timchampion&#39;s gravatar image" /><p><span>Timchampion</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timchampion has no accepted answers">0%</span></p></div></div><div id="comments-container-24335" class="comments-container"></div><div id="comment-tools-24335" class="comment-tools"></div><div class="clear"></div><div id="comment-24335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24336"></span>

<div id="answer-container-24336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24336-score" class="post-score" title="current number of votes">0</div><span id="post-24336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark and tshark crashes are inevitable when doing captures that run for a long time or just capture a lot of packets. Both keep information about TCP connections in memory (mostly for reassembly), which will lead to a crash sooner or later, even when storing packets into multiple files.</p><p>Dumpcap should work, because it just writes packets to disk, without any overhead. Are you sure that dumpcap has the exact same issue as tshark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '13, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24336" class="comments-container"></div><div id="comment-tools-24336" class="comment-tools"></div><div class="clear"></div><div id="comment-24336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

