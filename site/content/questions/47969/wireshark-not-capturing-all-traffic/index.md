+++
type = "question"
title = "Wireshark not capturing all traffic"
description = '''Hello, I am running wireshark 1.12.8 on Windows 7. I am begin the capture on my desired interface but I am not seeing traffic that I know for a fact should be detected. Any ideas? I set it up to capture in promiscuous mode on all interfaces. I was able to rule out the interface having issues, becaus...'''
date = "2015-11-25T06:45:00Z"
lastmod = "2015-11-25T07:02:00Z"
weight = 47969
keywords = [ "failure", "packet-capture" ]
aliases = [ "/questions/47969" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not capturing all traffic](/questions/47969/wireshark-not-capturing-all-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47969-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am running wireshark 1.12.8 on Windows 7. I am begin the capture on my desired interface but I am not seeing traffic that I know for a fact should be detected. Any ideas? I set it up to capture in promiscuous mode on all interfaces.</p><p>I was able to rule out the interface having issues, because I tried to capture the same traffic on another interface and the issue remains. I used a completely different computer to capture while connected to the same cable and I was able to capture fine. I also swapped out network cables, but I still have the same issue.</p><p>thanks in advanced!<br />
</p></div><div id="question-tags" class="tags-container tags">failure packet-capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/ca14147f42e6721ce2529b80d2ec5a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adrian549092&#39;s gravatar image" /><p>adrian549092<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adrian549092 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-47969" class="comments-container"></div><div id="comment-tools-47969" class="comment-tools"></div><div class="clear"></div><div id="comment-47969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47973"></span>

<div id="answer-container-47973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47973-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's probably a software on your PC that blocks the packets before they can reach Wireshark. Usual candidates are virus scanners, personal firewalls and host intrusion prevention applications. You should turn them off and try capturing again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-47973" class="comments-container"></div><div id="comment-tools-47973" class="comment-tools"></div><div class="clear"></div><div id="comment-47973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

