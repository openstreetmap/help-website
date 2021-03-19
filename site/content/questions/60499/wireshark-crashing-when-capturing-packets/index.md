+++
type = "question"
title = "wireshark crashing when capturing packets"
description = '''Hi I&#x27;ve posted this question earlier but it never has shown up. Apologies if there&#x27;s multiples. I was trying to understand how a particular internet speed test works so I captured all packets while running testmy.net with a manual download size of 12 MByte and then a manual UL size of 1 MByte. Then ...'''
date = "2017-03-31T14:17:00Z"
lastmod = "2017-04-01T04:15:00Z"
weight = 60499
keywords = [ "speedtest", "unresponsive" ]
aliases = [ "/questions/60499" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark crashing when capturing packets](/questions/60499/wireshark-crashing-when-capturing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60499-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I've posted this question earlier but it never has shown up. Apologies if there's multiples.</p><p>I was trying to understand how a particular internet speed test works so I captured all packets while running testmy.net with a manual download size of 12 MByte and then a manual UL size of 1 MByte. Then each time I try to stop the packet capture, after a few mins, wireshark goes unresponsive and I end up having to kill it with the Task Manager. This is on a laptop running Win 7. This procedure worked fine when I captured packets during dslreports.com and fast.com, but each time I try testmy.net, it hangs.</p><p>I am not using a VPN and am doing a wired ethernet test.</p><p>Any idea what I might be doing wrong? I am running ver 2.2.5.</p><p>thank you, 'mark</p></div><div id="question-tags" class="tags-container tags">speedtest unresponsive</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '17, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/62ae163c40f3b555b98762a3d73d235c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mahlenius&#39;s gravatar image" /><p>mahlenius<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mahlenius has no accepted answers">0%</span></p></div></div><div id="comments-container-60499" class="comments-container"></div><div id="comment-tools-60499" class="comment-tools"></div><div class="clear"></div><div id="comment-60499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60503"></span>

<div id="answer-container-60503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60503-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like Wireshark is having trouble with the packets that are captured; sometimes it's the sheer amount, but it could also be something else.</p><p>As a better solution I recommend capturing with dumpcap on the command line directly, which removes a lot of overhead. See this blog post for how to use dumpcap:</p><p><a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '17, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60503" class="comments-container"><span id="60571"></span><div id="comment-60571" class="comment"><div id="post-60571-score" class="comment-score">1</div><div class="comment-text"><p>I have to agree here. I learned it the hard way a couple times.</p><p>I always use Wireshark when I have something very specific to search / capture takes less than a minute to complete.</p><p>For everything else, I use dumpcap.</p><p>Don't be affraid to capture everything with no filters (unless you have limited space on hard drive) and if your capture file is too large, use editcap to split it. Both are very easy to use.</p></div><div id="comment-60571-info" class="comment-info"><span class="comment-age">(04 Apr '17, 12:15)</span> jerioux</div></div></div><div id="comment-tools-60503" class="comment-tools"></div><div class="clear"></div><div id="comment-60503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

