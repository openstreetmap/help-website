+++
type = "question"
title = "No &quot;ACK&quot; from receiver, failed to send data"
description = '''Hi,  I encountered a problem where receiver did not &quot;ACK&quot; back to sender after both sender and receiver successfully established connection and send &quot;PSH, ACK&quot; to receiver. From the log, I can see connection established, and lots of TCP Transmission&quot;.  What could be the problem. Anyone can help? tha...'''
date = "2017-04-27T00:42:00Z"
lastmod = "2017-05-01T12:47:00Z"
weight = 61065
keywords = [ "tcp" ]
aliases = [ "/questions/61065" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No "ACK" from receiver, failed to send data](/questions/61065/no-ack-from-receiver-failed-to-send-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61065-score" class="post-score" title="current number of votes">0</div><span id="post-61065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I encountered a problem where receiver did not "ACK" back to sender after both sender and receiver successfully established connection and send "PSH, ACK" to receiver. From the log, I can see connection established, and lots of TCP Transmission".<br />
</p><p>What could be the problem. Anyone can help?</p><p>thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '17, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/6ac9523ee599a263b575498bd2ebdc24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbw&#39;s gravatar image" /><p><span>tbw</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbw has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-61065" class="comments-container"><span id="61073"></span><div id="comment-61073" class="comment"><div id="post-61073-score" class="comment-score"></div><div class="comment-text"><p><em>Maybe</em> if you make a capture file available somewhere such as cloudshark, dropbox, pastebin, etc., someone might be able to help.</p></div><div id="comment-61073-info" class="comment-info"><span class="comment-age">(27 Apr '17, 06:48)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="61083"></span><div id="comment-61083" class="comment"><div id="post-61083-score" class="comment-score"></div><div class="comment-text"><p>thanks for the suggestion. Uploaded the capture file to dropbox. Appreciate anyone can help to find out why there is no "ACK" from the receiver.</p><p><a href="https://www.dropbox.com/s/915h8yngooi4u31/tan_0427.pcap?dl=0">https://www.dropbox.com/s/915h8yngooi4u31/tan_0427.pcap?dl=0</a></p><p>thank you very much</p></div><div id="comment-61083-info" class="comment-info"><span class="comment-age">(27 Apr '17, 20:41)</span> <span class="comment-user userinfo">tbw</span></div></div></div><div id="comment-tools-61065" class="comment-tools"></div><div class="clear"></div><div id="comment-61065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61109"></span>

<div id="answer-container-61109" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61109-score" class="post-score" title="current number of votes">0</div><span id="post-61109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Except for the 20 TCP ACK packets from 169.254.1.108, every other TCP packet that host sends contains an invalid TCP checksum. As such, they are never ACK'd by 169.254.239.8.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '17, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-61109" class="comments-container"><span id="61110"></span><div id="comment-61110" class="comment"><div id="post-61110-score" class="comment-score"></div><div class="comment-text"><p>thank you very much, appreciate your help. The invalid TCP checksum, is it because of the Header Checksum which supposes to be set to 0000?</p><p>thanks again,</p></div><div id="comment-61110-info" class="comment-info"><span class="comment-age">(28 Apr '17, 19:04)</span> <span class="comment-user userinfo">tbw</span></div></div><span id="61142"></span><div id="comment-61142" class="comment"><div id="post-61142-score" class="comment-score"></div><div class="comment-text"><p>No, and there are no TCP checksums with the value of 0x0000, at least in the capture file you provided. Try applying a display filter of <code>tcp.checksum == 0x0000</code>; you won't find any.</p><p>The invalid TCP checksum values vary; they are not simply 0x0000. It would seem that they are simply being improperly computed by the sending host, in this case, 169.254.1.108.</p><p>Assuming you have the TCP preference <em>"Validate the TCP checksum if possible"</em> enabled, you can apply the following filter to find those with valid checksums: <code>tcp.stream eq 0 and ip.src eq 169.254.1.108 and tcp.checksum.status == "Good"</code> vs. those with invalid checksums: <code>tcp.stream eq 0 and ip.src eq 169.254.239.8 and tcp.checksum.status == "Bad"</code>.</p></div><div id="comment-61142-info" class="comment-info"><span class="comment-age">(01 May '17, 12:47)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-61109" class="comment-tools"></div><div class="clear"></div><div id="comment-61109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

