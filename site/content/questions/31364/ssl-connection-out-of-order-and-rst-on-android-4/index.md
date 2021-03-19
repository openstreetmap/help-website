+++
type = "question"
title = "SSL Connection Out-Of-Order and RST on Android 4"
description = '''Hello all, I&#x27;ve recently moved my website to an all HTTPS after purchasing an EV certificate from Starfield Technologies. Everything seems to go well until recently I discovered that a particular browser from a device (Stock browser from Android 4.x) is unable to access my website, showing the error...'''
date = "2014-04-01T20:59:00Z"
lastmod = "2014-04-03T09:24:00Z"
weight = 31364
keywords = [ "ssl", "https" ]
aliases = [ "/questions/31364" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Connection Out-Of-Order and RST on Android 4](/questions/31364/ssl-connection-out-of-order-and-rst-on-android-4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31364-score" class="post-score" title="current number of votes">0</div><span id="post-31364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I've recently moved my website to an all HTTPS after purchasing an EV certificate from Starfield Technologies.</p><p>Everything seems to go well until recently I discovered that a particular browser from a device (Stock browser from Android 4.x) is unable to access my website, showing the error "Connection PRoblem. A network error occured". Weirdly stock browser from older versions of Android such as 1.x and 2.x works fine.</p><p><img src="http://i.imgur.com/R6HCLZn.png" alt="A network error occured" /></p><p>Initially I thought that it was a certificate chaining problem, and I've included the full bundle provided by my SSL provider but still no go. Even tried changing different cipher, yet still did not fix the problem.</p><p>Someone suggested to capture the handshake from my Android device and analyze the handshake. I've managed to install an app to capture the packets and uploaded the PCAP file to CloudShark. I am seeing a couple of Out-Of-Order and RST flags but don't know how to interpret them.</p><p><a href="https://www.cloudshark.org/captures/3efe30799215">https://www.cloudshark.org/captures/3efe30799215</a></p><p>Can anyone kindly help to take a look at the captured packets and determine what might be the cause for the stock browser from Android 4.x device unable to access my website?</p><p>Thank you all for your time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 20:59</strong></p><img src="https://secure.gravatar.com/avatar/5ebbbdfff17731ce80293114a3528eae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raymondcc&#39;s gravatar image" /><p><span>raymondcc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raymondcc has no accepted answers">0%</span></p></img></div></div><div id="comments-container-31364" class="comments-container"></div><div id="comment-tools-31364" class="comment-tools"></div><div class="clear"></div><div id="comment-31364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31416"></span>

<div id="answer-container-31416" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31416-score" class="post-score" title="current number of votes">2</div><span id="post-31416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, I've spent some time on the trace you provided, a real tough one I admit. The good thing is, TLS Handshake goes through so there is no problem with the certificates. The bad thing I believe is, that the TLS data gets tampered with when retransmission occurs and the encrypted data probably fails to decrypt so android closes the session after having received the first TLS Application data from the server.<br />
</p><p>Quite a wild speculation you might think but I here is some evidence:</p><p><strong>Frame 36</strong> is the Close Notify from android that starts the termination process of session tcp.port==49421</p><p><strong>Frame 24</strong> is a TSL application record <strong>0x170301</strong> with a length of 0x10a0 coming in as tcp.seq==3773 with a tcp.len==1292<br />
<strong>Frame 27</strong> is a Fast Retransmission of tcp.seq==3773 but this time the data portion is no longer a 0x170301 but starts with <strong>0x26992</strong>!</p><p>Same happens for frames 35 and 38 - 38 being a 'retransmission' as well with data not being the same, even the tcp.len of the 'retransmitted' segment is different now!</p><p><a href="https://www.cloudshark.org/captures/3efe30799215?filter=%28tcp.seq%3D%3D3773%20or%20%20tcp.seq%3D%3D8941%29%20and%20tcp.len%20gt%200">filter: (tcp.seq==3773 or tcp.seq==8941) and tcp.len gt 0</a></p><p>Now, who is retransmitting and why?<br />
I don't tink that it is really the server as the retransmissions occur too fast for the RTT! Also the 'Fast Retransmission occurs without any duplicate ACKs being sent in your trace!</p><p>Applying another filter on 'low ip.id' it becomes obvious that all inbound packets come through the same IP stack acting as a proxy: They arrive with a TTL of 16 and have incrementing ip.id even the originate from different servers (ip addresses).</p><p>One more peculiarity is that the inbound SYN_ACKs do NOT HAVE ANY TCP options, not even MSS when they arrive at your android. Also an indication that some <em>not-so-modern</em> TCP stack is faking your real servers. <strong>Added comment:</strong> As only android_4x devices have this problem it might a software device within the android itself that is causing this ...</p><p>I believe you need to fix or bypass this yet to be determined device. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_193.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Apr '14, 13:06</strong> </span></p></div></div><div id="comments-container-31416" class="comments-container"><span id="31453"></span><div id="comment-31453" class="comment"><div id="post-31453-score" class="comment-score"></div><div class="comment-text"><p>Hi mrEEde, thanks for taking the time to analyze the captured packets. I've gone through the process of elimination and found that this error is caused by SPDY from LiteSpeed 5.0 RC1.</p><p>I've reported this bug to the LiteSpeed developers and they claim this will be fixed in RC2.</p><p>I guess it's never good to use Beta or Release Candidate on production servers.</p><p>Thanks again.</p></div><div id="comment-31453-info" class="comment-info"><span class="comment-age">(02 Apr '14, 20:53)</span> <span class="comment-user userinfo">raymondcc</span></div></div><span id="31491"></span><div id="comment-31491" class="comment"><div id="post-31491-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. Glad to hear that you found the culprit. Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-31491-info" class="comment-info"><span class="comment-age">(03 Apr '14, 09:24)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-31416" class="comment-tools"></div><div class="clear"></div><div id="comment-31416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

