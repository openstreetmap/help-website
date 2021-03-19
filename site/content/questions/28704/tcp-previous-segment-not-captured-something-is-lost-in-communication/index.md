+++
type = "question"
title = "[TCP Previous segment not captured] something is lost in communication"
description = '''Hello, I am investigating strange behavior of one application. The problem from user point of view is described as follow: &quot;There is web application with some form which has two buttons. When user is pressing one of them s(he) suppose to see some dialog. And in some scenario the problem is that it d...'''
date = "2014-01-09T01:57:00Z"
lastmod = "2014-01-10T06:06:00Z"
weight = 28704
keywords = [ "frame", "lost" ]
aliases = [ "/questions/28704" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[TCP Previous segment not captured\] something is lost in communication](/questions/28704/tcp-previous-segment-not-captured-something-is-lost-in-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28704-score" class="post-score" title="current number of votes">0</div><span id="post-28704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am investigating strange behavior of one application. The problem from user point of view is described as follow: "There is web application with some form which has two buttons. When user is pressing one of them s(he) suppose to see some dialog. And in some scenario the problem is that it doesn't happen. Form just does not appear."</p><p>I have two Wireshark's logs, one for problematic scenario and one for successful. I uploaded them here:<br />
</p><p>failure: <a href="http://www.cloudshark.org/captures/d11077f00245">http://www.cloudshark.org/captures/d11077f00245</a> (the stream which i am checking is tcp.stream eq 111) success: <a href="http://www.cloudshark.org/captures/9e4b1c861030">http://www.cloudshark.org/captures/9e4b1c861030</a> (the stream which i am checking is tcp.stream eq 197)</p><p>Pushing the button is resulting in POST request: POST /service/sydney/load.php</p><p>I can see that in problematic scenario there are series of DUP ACKs and retransmit. It seems to me that there is ok-response from server in a form "HTTP/1.1 200 OK", but on some reason i do not see it as an individual trace in wireshark log, i can see it only among [TCP segment of a reassembled PDU] traces if i am checking their content. In successful log there is no any retransmit, there is "200 OK" confirmation and everything looks great. Did i get it correct that some of the ACK was missing or its number was not correct. Could anybody explain why it could be the possible reason for this to happen? Please help me to decrypt this part of traces [4509-4522] because I am not sure my interpretation is correct.</p><p>Thanks a lot in advance, Kristina</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '14, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/4d52cf38901c861ba67866ee6050a496?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris_kh&#39;s gravatar image" /><p><span>Chris_kh</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris_kh has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-28704" class="comments-container"></div><div id="comment-tools-28704" class="comment-tools"></div><div class="clear"></div><div id="comment-28704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28741"></span>

<div id="answer-container-28741" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28741-score" class="post-score" title="current number of votes">1</div><span id="post-28741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks as if your client's TCP stack is not reading the segments hat the server is retransmitting</p><p>filter <code>(tcp.ack == 256889 or tcp.seq == 256889) and tcp.stream==111</code> shows the windows client is asking for (relative) sequence number 256889 which the server is constantly re-transmitting - with increasing intervals but windows TCP is not reading/seeing it. The tcp checksum on the inbound segments is correct so there is no obvios reason to discard those segments.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_027.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '14, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jan '14, 02:38</strong> </span></p></div></div><div id="comments-container-28741" class="comments-container"><span id="28763"></span><div id="comment-28763" class="comment"><div id="post-28763-score" class="comment-score"></div><div class="comment-text"><p>Thank you for you reply! May i ask you what do you think could cause that DUP ACK series which appears in the log before that seq 256889? Could you "translate for me" frame 4509? Is all this situation until the [4558] looks ok?</p></div><div id="comment-28763-info" class="comment-info"><span class="comment-age">(10 Jan '14, 01:06)</span> <span class="comment-user userinfo">Chris_kh</span></div></div><span id="28764"></span><div id="comment-28764" class="comment"><div id="post-28764-score" class="comment-score">1</div><div class="comment-text"><p>Duplicate ACKs are sent for every segment that arrives 'out_of_order'. This is a method to trigger a 'Fast Retransmission' where the sender should immediately retransmit when it receives the 3rd 'duplicate ack'. Frame 4509 is the first packet that arrives out_of_order. The expected sequence number after 4508 was 236025, what arrived was 237329. If you look at the ip.ids of 4508 and 4509 you will recognize that exactly 1 ip packet was lost: 0xd1ae</p></div><div id="comment-28764-info" class="comment-info"><span class="comment-age">(10 Jan '14, 02:37)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="28769"></span><div id="comment-28769" class="comment"><div id="post-28769-score" class="comment-score"></div><div class="comment-text"><p>Thnx a lot for very detailed explanation, i got it now!</p></div><div id="comment-28769-info" class="comment-info"><span class="comment-age">(10 Jan '14, 06:06)</span> <span class="comment-user userinfo">Chris_kh</span></div></div></div><div id="comment-tools-28741" class="comment-tools"></div><div class="clear"></div><div id="comment-28741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

