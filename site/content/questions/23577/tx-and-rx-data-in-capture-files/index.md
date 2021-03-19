+++
type = "question"
title = "Tx and Rx data in capture files"
description = '''Simple capture files in tutes etc contain frames both to and from multiple systems. How is that possible, given that a network card being used by Wireshark can only capture from the Rx pair of a cable?'''
date = "2013-08-06T03:18:00Z"
lastmod = "2013-08-06T05:34:00Z"
weight = 23577
keywords = [ "capture" ]
aliases = [ "/questions/23577" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tx and Rx data in capture files](/questions/23577/tx-and-rx-data-in-capture-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23577-score" class="post-score" title="current number of votes">0</div><span id="post-23577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Simple capture files in tutes etc contain frames both to and from multiple systems. How is that possible, given that a network card being used by Wireshark can only capture from the Rx pair of a cable?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '13, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/f53fafa68a3705ccbd7e31cb1a5a494b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RLH&#39;s gravatar image" /><p><span>RLH</span><br />
<span class="score" title="8 reputation points">8</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RLH has no accepted answers">0%</span></p></div></div><div id="comments-container-23577" class="comments-container"></div><div id="comment-tools-23577" class="comment-tools"></div><div class="clear"></div><div id="comment-23577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23579"></span>

<div id="answer-container-23579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23579-score" class="post-score" title="current number of votes">2</div><span id="post-23579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Receiving data doesn't mean that it is only unidirectional when it comes to the layers above the physical medium.</p><p>Usually, captures are done on SPAN ports or TAPs, which means that communication of other systems is channeled into the downstream towards the Wireshark PC (or any capture device). In that downstream you'll have packets that go back and forth between Ethernet/IP/... pairs of these systems. It's sort of what happens when someone at the post office takes a look at an envelope to see where to direct it to: the guy inspecting the address information isn't the receiver or sender, but still has the letter in it's hand. In Wiresharks case it is receiving copies of frames/packets and stores/analyzes them. It doesn't mean it needs to be the sender or receiver.</p><p>Also, if you capture with Wireshark on a local PC you'll get both directions, because it listens in on RX and TX.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '13, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-23579" class="comments-container"><span id="23583"></span><div id="comment-23583" class="comment"><div id="post-23583-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. I have more questions: 1. &gt;Usually, captures are done on SPAN ports or TAPs I'll have to read up on these.</p><ol><li><blockquote><p>communication of other systems is channeled into the downstream towards... Is this implying the presence of an (active) device that is listening to both the Rx and Tx pairs of a link between two system, and combining both of those streams into a single stream that is then received and captured by the Wireshark system?</p></blockquote></li><li><blockquote><p>if you capture with Wireshark on a local PC ... because it listens in on RX and TX</p></blockquote></li></ol><p>Does this mean that what is presented in the capture file as a transmission from the local PC is actually <strong>what it is expected will have been transmitted</strong> i.e. captured from buffers just before being passed to the lowest hardware component? Being picky, I know, but I'm trying to understand the nitty-gritty of capture.</p><p>Or do I still not understand...</p></div><div id="comment-23583-info" class="comment-info"><span class="comment-age">(06 Aug '13, 04:43)</span> <span class="comment-user userinfo">RLH</span></div></div><span id="23586"></span><div id="comment-23586" class="comment"><div id="post-23586-score" class="comment-score"></div><div class="comment-text"><ol><li><p>yes. A SPAN port aggregates RX/TX of the communication towards one TX output port that Wireshark listens on (as RX device). TAPs can do that same ("Link Aggregation TAP") or provide both directions on two separate TX outputs, which of course requires Wireshark to listen on <strong>two</strong> RX NICs at the same time.</p></li><li><p>yes, what Wireshark picks up is what is supposed to be sent. It may in fact be modified in the actual NIC before it is sent, which explains why you'll often see CRC errors and oversized/undersized frames when doing a capture like this - because the final frame construction is done on the NIC <strong>after</strong> Wireshark already captured the incomplete frame on it's way to the NIC.</p></li></ol><p>By the way, I can recommend this WIKI page: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div id="comment-23586-info" class="comment-info"><span class="comment-age">(06 Aug '13, 05:07)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="23587"></span><div id="comment-23587" class="comment"><div id="post-23587-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much Jasper. Now I have a starting place...</p></div><div id="comment-23587-info" class="comment-info"><span class="comment-age">(06 Aug '13, 05:20)</span> <span class="comment-user userinfo">RLH</span></div></div></div><div id="comment-tools-23579" class="comment-tools"></div><div class="clear"></div><div id="comment-23579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23581"></span>

<div id="answer-container-23581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23581-score" class="post-score" title="current number of votes">1</div><span id="post-23581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capture could have been made at the server so it would see client request from multiple machines and the server responses, or could have been made via a mirror port on a switch, or on multiple network interfaces, or (rarely these days) on a hub where all traffic is available on all ports.</p><p>The capture could also be synthesised by concatenating multiple captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '13, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23581" class="comments-container"><span id="23584"></span><div id="comment-23584" class="comment"><div id="post-23584-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb. "a mirror port on a switch". More reading for me; I (vaguely) thought that a mirror port was just a duplication of the original port... I don't quite get the significance...</p><p>"or on multiple network interfaces". Is the data from multiple interfaces captured into individual files? Do they have the same time-zero reference time? Can they be (or are they automatically) merged into a single file?</p><p>Thanks.</p></div><div id="comment-23584-info" class="comment-info"><span class="comment-age">(06 Aug '13, 04:57)</span> <span class="comment-user userinfo">RLH</span></div></div><span id="23588"></span><div id="comment-23588" class="comment"><div id="post-23588-score" class="comment-score"></div><div class="comment-text"><p>A mirror port is another name for a SPAN port as mentioned in the answer from <span>@Jasper</span>. Most switches that offer mirroring or spanning permit multiple switch ports to be mirrored or spanned.</p><p>Recent versions of Wireshark can capture on multiple interfaces at the same time into a single capture file. Unfortunately the timestamps of packets depend on the actual capturing mechanism in use and I believe this may vary for different NIC's and drivers and of course OS's.</p></div><div id="comment-23588-info" class="comment-info"><span class="comment-age">(06 Aug '13, 05:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23581" class="comment-tools"></div><div class="clear"></div><div id="comment-23581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

