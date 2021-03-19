+++
type = "question"
title = "TCP ACKed Unseen segment issue"
description = '''Seeing an issues where a remote host seems to be sending an ACK for a packet it never received. What is really strange is that the ACK# it sends is extremly high and way out of line with normal sequence#/ACK flow. This happens repeatedly on this one host. 2015-09-17 09:21:21 |TCP: 55206→51583 [PSH, ...'''
date = "2015-09-17T10:02:00Z"
lastmod = "2015-09-20T13:11:00Z"
weight = 45925
keywords = [ "tcp" ]
aliases = [ "/questions/45925" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ACKed Unseen segment issue](/questions/45925/tcp-acked-unseen-segment-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45925-score" class="post-score" title="current number of votes">0</div><span id="post-45925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Seeing an issues where a remote host seems to be sending an ACK for a packet it never received. What is really strange is that the ACK# it sends is extremly high and way out of line with normal sequence#/ACK flow. This happens repeatedly on this one host.</p><pre><code>2015-09-17 09:21:21 |TCP: 55206→51583 [PSH, ACK] Seq=10689 Ack=797 Win=7936 Len=8 TSval=3510183220 TSecr=64598928 **(Source server sends and an 8 byte packet of data) (Sequence# 10689 + 8 bytes = Ack# 10697 seen in the next packet)**

2015-09-17 09:21:21 |TCP: 51583→55206 [ACK] Seq=797 Ack=10697 Win=39680 Len=0 **(Destination Server ACKs the packet)**

2015-09-17 09:21:24 |TCP: [TCP ACKed unseen segment] 51583→55206 [PSH, ACK] Seq=797 Ack=1073751598 Win=34048 Len=62 **(Approx 3 seconds later Destination server sends an ACK for a packet it never received. Notice the extremely high Ack#)**

2015-09-17 09:21:24|TCP: 55206→51583 [RST] Seq=1073751598 Win=0 Len=0 **(Source server resets the connection. I assume it is because of the previous packet)**</code></pre><p>Just wondering if anyone has seen this type of behavior before?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '15, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/e6abd976f19bc307429bdbda801136d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Racer5&#39;s gravatar image" /><p><span>Racer5</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Racer5 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '15, 12:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-45925" class="comments-container"><span id="45937"></span><div id="comment-45937" class="comment"><div id="post-45937-score" class="comment-score"></div><div class="comment-text"><p>Interestingly enough, 1073751598 is 0x4000262e. and 0x262e is 9774</p><p>I don't know what's going on, but maybe the fact that Wireshark normally shows relative sequence numbers (i.e., offset from the actual sequence number seen in the first captured packet for the TCP connection) is causing some confusion.</p><p>So: the first thing I would do is to go to the Wireshark TCP protocol preferences and disable relative sequence numbers and then look again at the capture.</p></div><div id="comment-45937-info" class="comment-info"><span class="comment-age">(17 Sep '15, 17:02)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="45939"></span><div id="comment-45939" class="comment"><div id="post-45939-score" class="comment-score"></div><div class="comment-text"><p>Yes I would turn off the relative sequence numbers, too. Are there any Loadbalancers or Firewalls between the server and the client?</p></div><div id="comment-45939-info" class="comment-info"><span class="comment-age">(17 Sep '15, 17:30)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="45976"></span><div id="comment-45976" class="comment"><div id="post-45976-score" class="comment-score"></div><div class="comment-text"><p>would it be possible to post a sample capture file somewhere?</p><p>BTW: What is your Wireshark version?</p></div><div id="comment-45976-info" class="comment-info"><span class="comment-age">(20 Sep '15, 13:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-45925" class="comment-tools"></div><div class="clear"></div><div id="comment-45925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

