+++
type = "question"
title = "Anlyzing SMB write issue"
description = '''Hello, I have a situation with station that have video feed that writing the video directly into Netapp storage as follows. The client that write the feed write it in dv25 format (approx. 4MB/s) the issue is that every few min 2~3 we have error in write application took more than 400~800ms to write ...'''
date = "2012-02-15T02:23:00Z"
lastmod = "2012-02-15T03:01:00Z"
weight = 9011
keywords = [ "smb" ]
aliases = [ "/questions/9011" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Anlyzing SMB write issue](/questions/9011/anlyzing-smb-write-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9011-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a situation with station that have video feed that writing the video directly into Netapp storage as follows.</p><p>The client that write the feed write it in dv25 format (approx. 4MB/s) the issue is that every few min 2~3 we have error in write application took more than 400~800ms to write the frame causing frame lost , i have done a trace from station feed and started to analyze it i can see that <code>SMB Service response time Write andX MAX</code> have 826ms which correspond to issue we have but looking on <code>TCP [TCP segment of a reassembled PDU]</code> related i can see many notification during pdu transmit <code>[TCP Window Full] [TCP segment of a reassembled PDU]</code> My question would be ,can that be the reason for the high <code>Write andX MAX response</code> meaning pure storage system latency or the fact that client writing have no buffer multiplier causing the delay for late response.</p><p>Please advice Thanks <img src="https://public.sn2.livefilestore.com/y1pZpLfRByJmZvGmVT5Q6-n62s13Mh2i2tFI-ury8qHugFugXd_Q8hn8eiyp0aYI_IVMYWJ6PD6tySSmDF-ibS56w/storage_dv25.png?psid=1" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '12, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p>tbaror<br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></img></div></div><div id="comments-container-9011" class="comments-container"></div><div id="comment-tools-9011" class="comment-tools"></div><div class="clear"></div><div id="comment-9011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9012"></span>

<div id="answer-container-9012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9012-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, deactivate the TCP protocol setting "Allow subdisectors to reassemble TCP streams" to avoid confusion when looking at time deltas. If you need to analyze time issues you should always disable it to see exactly what happened. Go to Edit -&gt; Preferences -&gt; Protocols -&gt; TCP and remove the check mark. As soon as you've done that you'll see that the SMB commands will be at a different (now correct) position in the packet list info column, and you'll not have the "reassembled PDU" messages anymore.</p><p>Second, I suspect that your problem may be caused by the receiver not processing data fast enough, or not offering a receive window big enough. The "Window Full" messages are a big indicator that there may be trouble with too much data streaming towards the target system, so take a look at the TCP window size values as well as the "Bytes in Flight". Either the storage system has trouble writing the incoming data to disk (which your storage admin should be able to see in the device statistics), or you have a high latency connection where the available bandwidth can't be fully exploited.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9012" class="comments-container"><span id="9016"></span><div id="comment-9016" class="comment"><div id="post-9016-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper for the answer ,</p><p>But i need to understand the process to be clear , since i am not so familiar how the write mechanism works.</p><p>The Client that write announce "Window Full" message since its detects the receive buffer on the storage is about to run-out of it , right?. Next the late "Write AndX Response" related to the fact the "PDU train" had some delay due to the fact of receive run out of buffer or purely system storage behave to confirm write on storage side?</p><p>Thanks</p><p>[converted to a comment]</p></div><div id="comment-9016-info" class="comment-info"><span class="comment-age">(15 Feb '12, 04:02)</span> tbaror</div></div><span id="9017"></span><div id="comment-9017" class="comment"><div id="post-9017-score" class="comment-score">1</div><div class="comment-text"><p>The client doesn't announce "Window Full", it is a diagnostic message created by Wireshark. You can tell from the square brackets; everything enclosed in those is additional information coming from Wireshark when analyzing frames.</p><p>And the receive buffer we're talking about is the TCP receive buffer, it doesn't have anything to do with buffers the filer application uses. It basically tells the sender how much data may be sent before he has to stop and wait for an acknowledge packet. If you see "Window Full" that limit was reached, slowing down the Sender (though not always critically).</p></div><div id="comment-9017-info" class="comment-info"><span class="comment-age">(15 Feb '12, 04:06)</span> Jasper ♦♦</div></div></div><div id="comment-tools-9012" class="comment-tools"></div><div class="clear"></div><div id="comment-9012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

