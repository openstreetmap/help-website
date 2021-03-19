+++
type = "question"
title = "TCP connection caught in retransmission"
description = '''Hello I&#x27;m working on a project where we have an embedded unit using Lwip 1.2. It&#x27;s old, but it has been working ok for us for quite a while. However, recently we have run into a problem with lost connections. From the log, it seems that we start to get retransmissions on TCP. Those retransmissions h...'''
date = "2016-04-01T07:02:00Z"
lastmod = "2016-04-04T12:09:00Z"
weight = 51348
keywords = [ "retransmissions", "tcp" ]
aliases = [ "/questions/51348" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP connection caught in retransmission](/questions/51348/tcp-connection-caught-in-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51348-score" class="post-score" title="current number of votes">0</div><span id="post-51348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I'm working on a project where we have an embedded unit using Lwip 1.2. It's old, but it has been working ok for us for quite a while. However, recently we have run into a problem with lost connections. From the log, it seems that we start to get retransmissions on TCP. Those retransmissions happen again and agin without being resolved and we eventually get a problem with buffer allocation on the embedded unit which then hangs the entire stack on the unit.</p><p>I'm no TCP expert but looking at the first few lines in the log file found <a href="https://www.dropbox.com/s/9wyjo774rc15hq4/problem.pcapng?dl=0">Here</a> is seems that LWIP in the embedded (192.168.0.100) never gets over a lost sequence number (1876719045). From my understanding, the PC (192.168.0.1) resends that sequence number which turns out to be a pure ack, but LWIP won't let that go and keeps insisting on getting an ack for 1876719045.</p><p>Can someone please confirm my analysis, or correct me if I'm wrong. Does 192.168.0.1 do something wrong which I don't realize. Or do the retransmissions later on stem from something else?</p><p>Thanks a million :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '16, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/57fc0fe989e5038cad99dac0dcd794c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikT&#39;s gravatar image" /><p><span>FredrikT</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikT has no accepted answers">0%</span></p></div></div><div id="comments-container-51348" class="comments-container"><span id="51361"></span><div id="comment-51361" class="comment"><div id="post-51361-score" class="comment-score"></div><div class="comment-text"><p>You should take a trace as close as possible near the device 192.168.0.1. Well out of a quick look I would say sommething goes wrong with the devive 192.168.0.1 maybe the app or the OS...???? Buffer shortage is a possible cause, too. If I were you I would investigate that device.</p><p>At the end it seems not to answer the ARP Request, which would say something goes wrong with this device or we just didn´t capture them.</p></div><div id="comment-51361-info" class="comment-info"><span class="comment-age">(01 Apr '16, 13:17)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-51348" class="comment-tools"></div><div class="clear"></div><div id="comment-51348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51398"></span>

<div id="answer-container-51398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51398-score" class="post-score" title="current number of votes">0</div><span id="post-51398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like your capture was taken somewhere between the embedded unit and the PC. Based on your capture, I see issues on both sides, but more on the embedded unit. Early on, the PC is not responding to simple SYN requests. But later in the capture, the embedded unit is not responding to simple ACKs.</p><p>Is there any non-switch device between the two machines?</p><p>Based on IP, they seem to be on the same local network. However, if that's the case, the response times should be fairly quick. There should not be multi-second response times from the embedded unit if it is local to the PC.</p><p>I think the buffer error and the hanging of the unit is evident at the end of the capture, when the PC is sending ARP requests and not getting any replies. I think that by that time, the embedded unit is completely hosed and cannot respond. I also think that this is due to the fact that it's embedded, and does not have the appropriate level of buffer storage to process all those retransmissions.</p><p>So I would do a couple things to troubleshoot this further:</p><ol><li>Capture data on or as close to both the embedded unit and the PC. This way, you will be able to verify whether those high response times from the unit are not because of the connectivity between the two, but instead are from the unit itself. And if that's the case, it likely is some OS or application-related issue on the unit.</li><li>Take a look at the performance of any network devices between the PC and embedded unit. You want to verify that no such device is causing a degradation in the performance.</li><li>Verify that there were no recent changes to the embedded unit.</li></ol><p>Let us know what you find.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '16, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/0eafb94fc68881ab754f30924ce504ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeantunis&#39;s gravatar image" /><p><span>jeantunis</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeantunis has no accepted answers">0%</span></p></div></div><div id="comments-container-51398" class="comments-container"></div><div id="comment-tools-51398" class="comment-tools"></div><div class="clear"></div><div id="comment-51398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

