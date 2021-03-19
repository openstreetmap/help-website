+++
type = "question"
title = "Why there are Retransmissions?"
description = '''Hi. I have some issues with https traffic. When I try to open this kind of pages, they are turned very slow. I captured some traffic whit wireshark, however I can´t see where the problem is. Into Wireshark I identified a lot of packet as retransmissions. I had done a lot of actions: • All the switch...'''
date = "2015-09-02T07:56:00Z"
lastmod = "2015-09-03T12:39:00Z"
weight = 45598
keywords = [ "retransmissions" ]
aliases = [ "/questions/45598" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why there are Retransmissions?](/questions/45598/why-there-are-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45598-score" class="post-score" title="current number of votes">0</div><span id="post-45598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I have some issues with https traffic. When I try to open this kind of pages, they are turned very slow. I captured some traffic whit wireshark, however I can´t see where the problem is. Into Wireshark I identified a lot of packet as retransmissions. I had done a lot of actions: • All the switch ports, router ports, AP ports I had revised. They haven’t errors, collisions or crc. • In the network there is many VLANs, this problem affected the more saturated vlan. • I have two router and they work in HSRP. I disabled the HSRP. • I revised the logs in all the devices but any message is about this problem.</p><p>Could anyone help me? How can I attach a wireshark file?</p><p>Regards</p><p>These two link correspond to the wireshark files.</p><p><a href="https://www.dropbox.com/s/c98hy9d2dbie5xb/Captura23%202sep15%20BBVA.pcapng?dl=0">https://www.dropbox.com/s/c98hy9d2dbie5xb/Captura23%202sep15%20BBVA.pcapng?dl=0</a> <a href="https://www.dropbox.com/s/sesfcbxsrcc5vfl/Captura24%202sep15%20BBVA.pcapng?dl=0">https://www.dropbox.com/s/sesfcbxsrcc5vfl/Captura24%202sep15%20BBVA.pcapng?dl=0</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '15, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/aa384875011b83b642a74df88a4e82ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorgeC&#39;s gravatar image" /><p><span>JorgeC</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorgeC has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Sep '15, 13:11</strong> </span></p></div></div><div id="comments-container-45598" class="comments-container"><span id="45601"></span><div id="comment-45601" class="comment"><div id="post-45601-score" class="comment-score"></div><div class="comment-text"><p>You can share a capture in a publicly accessible spot, e.g. CloudShark, Google Drive, Dropbox.</p></div><div id="comment-45601-info" class="comment-info"><span class="comment-age">(02 Sep '15, 09:44)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="45605"></span><div id="comment-45605" class="comment"><div id="post-45605-score" class="comment-score"></div><div class="comment-text"><p>First of all you should try:</p><pre><code> editcap -d INFILE OUTFILE</code></pre><p>This eleminates the duplicates in the tracefiles, because every packet has been captured twice.</p></div><div id="comment-45605-info" class="comment-info"><span class="comment-age">(02 Sep '15, 14:49)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-45598" class="comment-tools"></div><div class="clear"></div><div id="comment-45598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45606"></span>

<div id="answer-container-45606" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45606-score" class="post-score" title="current number of votes">0</div><span id="post-45606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So after cleaning the files we can see a packet loss rate higher then 4% in the tracefile. The MSS of the System 10.10.10.108 is really small with 696 Bytes. is it really needed? And we see a gap of 10 seconds between DUP ACK and Retransmission.(See Frame #1996 in Captura24...)</p><p>Where the packet loss occur... The easiest way is to follow the packets with your caprturepoint. And see where the packet loss occurs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '15, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-45606" class="comments-container"><span id="45623"></span><div id="comment-45623" class="comment"><div id="post-45623-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p><p>I will work into your recommends.</p><p>Best Regards.</p></div><div id="comment-45623-info" class="comment-info"><span class="comment-age">(03 Sep '15, 12:39)</span> <span class="comment-user userinfo">JorgeC</span></div></div></div><div id="comment-tools-45606" class="comment-tools"></div><div class="clear"></div><div id="comment-45606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

