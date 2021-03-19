+++
type = "question"
title = "TCP ZeroWindow Probe."
description = '''After doing a capture from the source to the destination address. I keep seeing an TCP {Ack} being sent and an a{PSH}, but no {ACK}. After a minute or so I get the {TCP ZEROWINDOW PROBE}, which is causing the backup server to hang since theres no data actually being sent correctly. Not sure what wou...'''
date = "2012-04-30T12:00:00Z"
lastmod = "2012-04-30T13:20:00Z"
weight = 10531
keywords = [ "window", "zero", "tcp" ]
aliases = [ "/questions/10531" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ZeroWindow Probe.](/questions/10531/tcp-zerowindow-probe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10531-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>After doing a capture from the source to the destination address. I keep seeing an TCP {Ack} being sent and an a{PSH}, but no {ACK}. After a minute or so I get the {TCP ZEROWINDOW PROBE}, which is causing the backup server to hang since theres no data actually being sent correctly. Not sure what would cause the {TCP ZEROWINDOW PROBE}. I have read up on it and I believe it has something to do with the destination IP Address Buffer being filled up to quickly.</p></div><div id="question-tags" class="tags-container tags">window zero tcp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '12, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/91b1e4909e1b0cc85ec4eb36baaafc77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pshaw085&#39;s gravatar image" /><p>pshaw085<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pshaw085 has no accepted answers">0%</span></p></div></div><div id="comments-container-10531" class="comments-container"></div><div id="comment-tools-10531" class="comment-tools"></div><div class="clear"></div><div id="comment-10531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10534"></span>

<div id="answer-container-10534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10534-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>Correct. TCP window probe means that the receiver has reduced his receive buffer (a.k.a. window) to zero, basically telling the sender to stop sending - usually for performance reasons. If the receiver does not recover and send an so called "Window Update" with a buffer size greater than zero (meaning, the sender is allowed to continue) the sender will become "impatient" at some point and "check" if the receiver is able to receive more data. That "check" is the Zero Window Probe you observed.</p><p>If you run into packets diagnosed as Zero Window Probe you can tell that your receiving node is not able to process incoming data fast enough. That is the typical performance problem that everybody blames the network for, while it is in fact a software/hardware problem on the receiving node.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10534" class="comments-container"><span id="14966"></span><div id="comment-14966" class="comment"><div id="post-14966-score" class="comment-score"></div><div class="comment-text"><p>what would cause it to happen on multiple printers (different brands) on the same network?</p></div><div id="comment-14966-info" class="comment-info"><span class="comment-age">(12 Oct '12, 11:42)</span> aPauling</div></div><span id="14970"></span><div id="comment-14970" class="comment"><div id="post-14970-score" class="comment-score"></div><div class="comment-text"><p>I have seen printers use zero window signaling to slow down/stop transmission from print servers/workstations while they're busy waking up and spinning up their internal mechanical parts. When ready, the zero window is pulled up to signal that the sender may continue. It's like a "wait a second, need to get running first... okay, send".</p></div><div id="comment-14970-info" class="comment-info"><span class="comment-age">(12 Oct '12, 14:07)</span> Jasper ♦♦</div></div><span id="25928"></span><div id="comment-25928" class="comment"><div id="post-25928-score" class="comment-score"></div><div class="comment-text"><p>Our HP printers use zero window signaling during the "ink drying" phase when we use double-sided printing. It's weird since they have plenty of RAM, but they don't want to buffer the jobs. They'd rather tell our hosts to stop sending while those little squirrels inside the printer blow on the paper to dry the ink... &lt;grin&gt;</p></div><div id="comment-25928-info" class="comment-info"><span class="comment-age">(11 Oct '13, 20:30)</span> lchappell ♦</div></div><span id="25932"></span><div id="comment-25932" class="comment"><div id="post-25932-score" class="comment-score"></div><div class="comment-text"><p>Could you please post a sample capture of such a session? That would be a good sample for an excercise ;-)</p></div><div id="comment-25932-info" class="comment-info"><span class="comment-age">(12 Oct '13, 02:17)</span> Kurt Knochner ♦</div></div><span id="27739"></span><div id="comment-27739" class="comment"><div id="post-27739-score" class="comment-score"></div><div class="comment-text"><p>I am having the same problem, I am having some zebra printers that I am not sure if it can handle the volume we are sending to them. I keep seeing the tcp-zerowindow-probe message.</p><p>This is at packet 39343, 39359, 39383, 39411 Any idea as to what is causing this?</p><p>The packet capture can be found here: <a href="http://sdrv.ms/188QS3m">packet capture download</a></p></div><div id="comment-27739-info" class="comment-info"><span class="comment-age">(03 Dec '13, 19:11)</span> indy_dude</div></div><span id="27748"></span><div id="comment-27748" class="comment not_top_scorer"><div id="post-27748-score" class="comment-score"></div><div class="comment-text"><p>Yes. Your printer seems to be overwhelmed with incoming packets, which means it is too slow to process (print) them right on time to continue without a pause. Also see my answer in your own question.</p></div><div id="comment-27748-info" class="comment-info"><span class="comment-age">(04 Dec '13, 02:05)</span> Jasper ♦♦</div></div><span id="27752"></span><div id="comment-27752" class="comment not_top_scorer"><div id="post-27752-score" class="comment-score"></div><div class="comment-text"><p>Is there a chance that this could be causing the shutdown of the web server on the printer also? When we do a port scan on the printer and the web interface times out?</p></div><div id="comment-27752-info" class="comment-info"><span class="comment-age">(04 Dec '13, 02:41)</span> indy_dude</div></div></div><div id="comment-tools-10534" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-10534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

