+++
type = "question"
title = "What would cause devices not to respond to an IP camera&#x27;s SYN/ACK intermittently?"
description = '''I have an IP camera that uses RTSP for it&#x27;s video/audio feed, and port 80 for it&#x27;s web management service. Intermittently I lose the feed from the camera and can no longer reach it via the management interface. I am on the same LAN segment with firewall or anything in between.  During this time I am...'''
date = "2016-12-21T18:34:00Z"
lastmod = "2016-12-25T16:27:00Z"
weight = 58283
keywords = [ "handshake", "syn+ack", "tcp" ]
aliases = [ "/questions/58283" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What would cause devices not to respond to an IP camera's SYN/ACK intermittently?](/questions/58283/what-would-cause-devices-not-to-respond-to-an-ip-cameras-synack-intermittently)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58283-score" class="post-score" title="current number of votes">0</div><span id="post-58283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an IP camera that uses RTSP for it's video/audio feed, and port 80 for it's web management service. Intermittently I lose the feed from the camera and can no longer reach it via the management interface. I am on the same LAN segment with firewall or anything in between.</p><p>During this time I am still able to receive ping replies from the camera.</p><p>I was able to get a capture from when the feed stops, and also when it is working properly. Now here's the odd part. In capture where the feed is not working, I show my PC sending the SYN, the camera sending the SYN/ACK, but then my PC doesn't ever send the final ACK. The only thing I see is the camera retransmitting the SYN/ACK and eventually my PC sending out a new SYN. If I didn't know any better, I would say it was a problem with my PC not sending the SYN, however I've tested it on multiple devices with the same results. This is the behavior on both port 554 and port 80.</p><p>When I compare the SYN and the SYN/ACKs from the working capture, I don't see anything different from the non working capture, same options, same flags, etc. However, I suspect I'm overlooking something.</p><p>To restore the feed, I simply reboot the camera.</p><p>Any idea what would cause the 3 way handshake to fail like this?</p><p>Thanks for your time!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-syn+ack" rel="tag" title="see questions tagged &#39;syn+ack&#39;">syn+ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '16, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/1fe0682c5a420fabb7dd96133cc3a511?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jasonm&#39;s gravatar image" /><p><span>jasonm</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jasonm has no accepted answers">0%</span></p></div></div><div id="comments-container-58283" class="comments-container"></div><div id="comment-tools-58283" class="comment-tools"></div><div class="clear"></div><div id="comment-58283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58307"></span>

<div id="answer-container-58307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58307-score" class="post-score" title="current number of votes">2</div><span id="post-58307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I see the TCP checksum looks bad in the SYN/ACK packets that are not accepted. Bad TCP stack implementation on the camera? Maybe it calculates the TCP checksum prior to the option, so if the option is present it would be incorrect. There is no intervening device altering the packets? There was nothing obvious, but just be sure there is no other device capable of adding this option in mid stream causing the damage.</p><p>Filter: tcp.checksum.status == "Bad"<img src="https://osqa-ask.wireshark.org/upfiles/2016-12-22_19_29_33-camera-working-then-not-working.pcapng_%5BWireshark_2.2.3_(v2.2.3-0-g57531cd)%5D.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '16, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></img></div></div><div id="comments-container-58307" class="comments-container"><span id="58330"></span><div id="comment-58330" class="comment"><div id="post-58330-score" class="comment-score"></div><div class="comment-text"><p>Good catch, this was the reason the handshake was failing. I must have disabled the option for Wireshark to calculate the TCP checksum so I completely missed that. I seem to recall at one point it was recommended to disabling validation of this checksum because of the TCP offloading that some NICs had and would cause a lot of false positives. Reenabling it clearly highlighted this problem and none of my other TCP sessions were showing up as false positives. Lesson learned!</p></div><div id="comment-58330-info" class="comment-info"><span class="comment-age">(25 Dec '16, 16:27)</span> <span class="comment-user userinfo">jasonm</span></div></div></div><div id="comment-tools-58307" class="comment-tools"></div><div class="clear"></div><div id="comment-58307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58302"></span>

<div id="answer-container-58302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58302-score" class="post-score" title="current number of votes">0</div><span id="post-58302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A tracefile would help. And in this situation a good look at the status of your network connections.</p><p>Try to identify the state of the workstations TCP session with the command <code>netstat -ano</code>. You should find one line for the attepted connection. If the connection is in the state <code>SYN_SEND</code> then the SYN/ACK was never forwarded to your TCP stack.</p><p>Try to disable the firewall from your anti-virus vendor, if present (or disable the Windows firewall). Then re-run the test until the connections fail.</p><p>Don't forget to re-enable the firewall once you are done.</p><p>Good hunting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '16, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-58302" class="comments-container"><span id="58305"></span><div id="comment-58305" class="comment"><div id="post-58305-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the advice, I just disabled the firewall and AV and tried again, but still the same results.</p><p>Netstat shows:</p><p>SYN_SENT but never goes to ESTABLISHED.</p><p>Here is the trace file:</p><p><a href="https://www.cloudshark.org/captures/b28932034bf6">https://www.cloudshark.org/captures/b28932034bf6</a></p><p>My PC is: 192.168.100.253 Camera is: 192.168.100.224</p><p>The first part shows a time period where the camera feed is not working, (no ACKing the SYN/ACK)</p><p>Then there's some successful pinging happening while the feed is still broken.</p><p>I reboot the camera around packet 102. Packet 113 shows the SYN/ACK of the successful handshake after rebooting the camera. (SYN = 105, SYN/ACK = 113, ACK = 114)</p><p>After looking a bit deeper, you can see that the TCP options are different between the SYN/ACKs that weren't ACKed versus the ones that were.</p><p>For example: Packet 92: It's length is 4 bytes longer, because it has the TCP option for Window Scale set.</p><p>The "good" SYN/ACK (packet 113) is missing that option.</p><p>Could that option be the cause?</p></div><div id="comment-58305-info" class="comment-info"><span class="comment-age">(22 Dec '16, 14:40)</span> <span class="comment-user userinfo">jasonm</span></div></div></div><div id="comment-tools-58302" class="comment-tools"></div><div class="clear"></div><div id="comment-58302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

