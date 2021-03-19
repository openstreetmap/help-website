+++
type = "question"
title = "TCP StreamGraph Throughput"
description = '''If I run a TCP throughput graph I see that there are plots placed at around 450,000,000 bytes. However if I add up the bytes from the total bytes column from the statistics of the same capture via tshark I get a total of 163,672,972 bytes.  The Tshark command is :   &quot;C:&#92;Program Files&#92;Wireshark&#92;tshar...'''
date = "2013-12-14T13:13:00Z"
lastmod = "2013-12-15T14:20:00Z"
weight = 28110
keywords = [ "tcp" ]
aliases = [ "/questions/28110" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP StreamGraph Throughput](/questions/28110/tcp-streamgraph-throughput)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28110-score" class="post-score" title="current number of votes">0</div><span id="post-28110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I run a TCP throughput graph I see that there are plots placed at around 450,000,000 bytes. However if I add up the bytes from the total bytes column from the statistics of the same capture via tshark I get a total of 163,672,972 bytes.</p><p>The Tshark command is : "C:\Program Files\Wireshark\tshark.exe" -q -z conv,ip -r C:\capture.pcap</p><p>Can anyone explain how the TCP throughput graph is calculated , and why this difference is occuring... ?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '13, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p><span>bart80</span><br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div></div><div id="comments-container-28110" class="comments-container"></div><div id="comment-tools-28110" class="comment-tools"></div><div class="clear"></div><div id="comment-28110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28122"></span>

<div id="answer-container-28122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28122-score" class="post-score" title="current number of votes">0</div><span id="post-28122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Which version of Wireshark are you using? For 1.10 and below the graph shows 21 (yes, 21) segment simple moving average. If the timestamps on a 21-segment span of packets are close together or far apart it will skew the graph high or low, respectively. The packet timestamps Wireshark sees may or may not accurately reflect what happened on the wire depending on <a href="http://www.winpcap.org/pipermail/winpcap-users/2007-December/002206.html">a number of factors</a>.</p><p>For 1.11.x the Gtk+ interface uses a 20 segment SMA (i.e. I fixed the off-by-one error). The <a href="https://blog.wireshark.org/2013/10/switching-to-qt/">Qt interface</a> uses a 1 second SMA.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '13, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-28122" class="comments-container"><span id="28126"></span><div id="comment-28126" class="comment"><div id="post-28126-score" class="comment-score"></div><div class="comment-text"><p>Ok thanks, im running 1.11.x. could you poss explain how the 20 segment SMA works ?</p></div><div id="comment-28126-info" class="comment-info"><span class="comment-age">(15 Dec '13, 11:43)</span> <span class="comment-user userinfo">bart80</span></div></div><span id="28131"></span><div id="comment-28131" class="comment"><div id="post-28131-score" class="comment-score"></div><div class="comment-text"><p>If I recall the code correctly it keeps a 20 segment long sliding window of the start time, end time, start byte count, and end byte count. The point plotted is the delta bytes over delta time. The function in question is tput_make_elmtlist(), currently at line 4092 of <a href="http://anonsvn.wireshark.org/viewvc/trunk/ui/gtk/tcp_graph.c?view=markup">tcp_graph.c</a>.</p></div><div id="comment-28131-info" class="comment-info"><span class="comment-age">(15 Dec '13, 13:07)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div><span id="28135"></span><div id="comment-28135" class="comment"><div id="post-28135-score" class="comment-score"></div><div class="comment-text"><p>Ok thanks, the main point Im trying to find is when dealing with microbursts to see the true amount of traffic that was sent/received during the peak (i.e burst) . Ive played around with the IO graphs but they never showed me the totals that I would of expected (prob duing to averaging and the ticks etc)</p></div><div id="comment-28135-info" class="comment-info"><span class="comment-age">(15 Dec '13, 14:20)</span> <span class="comment-user userinfo">bart80</span></div></div></div><div id="comment-tools-28122" class="comment-tools"></div><div class="clear"></div><div id="comment-28122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

