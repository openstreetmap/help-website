+++
type = "question"
title = "Follow TCP Stream - Stream Content Empty"
description = '''On running a capture between a client and a webserver I&#x27;ve noticed that there are 4 TCP handshakes between the two devices. I sort of get this due to the way web browsers handle chunked data (Google sort of explained this to me). What I don&#x27;t get is: once the first handshake has completed and the co...'''
date = "2015-11-06T04:05:00Z"
lastmod = "2015-11-09T15:12:00Z"
weight = 47333
keywords = [ "tcp.stream" ]
aliases = [ "/questions/47333" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Follow TCP Stream - Stream Content Empty](/questions/47333/follow-tcp-stream-stream-content-empty)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47333-score" class="post-score" title="current number of votes">0</div><span id="post-47333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On running a capture between a client and a webserver I've noticed that there are 4 TCP handshakes between the two devices. I sort of get this due to the way web browsers handle chunked data (Google sort of explained this to me).</p><p>What I don't get is: once the first handshake has completed and the connection has been established, If I follow this TCP stream then I can see what's going on between the client and the server.</p><p>However, any subsequent connections' TCP streams, and there are 3 of these, are empty. My question, at this point, is, why are the other 3 TCP streams empty?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp.stream" rel="tag" title="see questions tagged &#39;tcp.stream&#39;">tcp.stream</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '15, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/b5939fd3d8d129ff53ff4a8870f6789f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joewoody&#39;s gravatar image" /><p><span>joewoody</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joewoody has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-47333" class="comments-container"><span id="47445"></span><div id="comment-47445" class="comment"><div id="post-47445-score" class="comment-score"></div><div class="comment-text"><p>There is another interesting thing in the trace. But it is a little bit out of topic, I think. The client does not advertise a MSS in the SYN packet. Fot that kind no Ethernet Frame is larger than 590 byte.</p></div><div id="comment-47445-info" class="comment-info"><span class="comment-age">(09 Nov '15, 15:12)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-47333" class="comment-tools"></div><div class="clear"></div><div id="comment-47333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47336"></span>

<div id="answer-container-47336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47336-score" class="post-score" title="current number of votes">0</div><span id="post-47336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My question, at this point, is, why are the other 3 TCP streams empty?</p></blockquote><p>most certainly because the was no data transmitted in those streams. But it's hard to tell without a pcap file. Is it possible to upload the file somewhere (google drive, dropbox) and to post the link here?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '15, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47336" class="comments-container"><span id="47430"></span><div id="comment-47430" class="comment"><div id="post-47430-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/file/d/0B6vUPsqTPCf8ay1vcG1tZXlLZDg/view?usp=sharing">https://drive.google.com/file/d/0B6vUPsqTPCf8ay1vcG1tZXlLZDg/view?usp=sharing</a></p><p>Tried to replicate today. The file in the link above, if my undersatnding is correct, contains 3 TCP handshakes - 2 of whose TCP streams appear to be empty. If the streams contain no data, then why would the connection attempts take place in the first place? This, unless i'm completely wrong, doesn't seem correct.....</p><p>Regards JW</p></div><div id="comment-47430-info" class="comment-info"><span class="comment-age">(09 Nov '15, 05:15)</span> <span class="comment-user userinfo">joewoody</span></div></div><span id="47442"></span><div id="comment-47442" class="comment"><div id="post-47442-score" class="comment-score"></div><div class="comment-text"><p>As I thought, there no data in the TCP streams, except 'tcp.stream eq 0'. The other streams contain the 3-way handshake (SYN,SYN-ACK,ACK) only.</p><blockquote><p>then why would the connection attempts take place in the first place?</p></blockquote><p>Wireshark is a network troubleshooting tool that can help you to show <strong>what</strong> is on the network. It has no magic inside to tell you <strong>why</strong> something happens ;-)</p><p>From what I can see in the capture file:</p><ul><li>There is a Watchguard Firewall involved</li><li>There are 5 TCP connections</li><li>4 of these connections contain only a 3-way handshake.</li><li>source ports are counting up</li></ul><blockquote><p>This, unless i'm completely wrong, doesn't seem correct....</p></blockquote><p>Maybe or maybe not. I can only speculate:</p><ul><li>If you have taken the network capture <strong>on</strong> the Firewall and the firewall has something like hardware offloading/acceleration you will only see those frames that hit the CPU, which is usually the 3-way handshake. I can't tell you why it's different for the first stream, because I don't know your environment.</li><li>the external system might have opened several connections but in 4 of them it did not send any data (GET/POST request). Reason unknown.</li><li>Something is wrong with the capturing system, so it only captured the 3-way handshake</li><li>The rest of the TCP streams data took a different route and thus the capturing system did not see it. However I can't tell you why, because I don't know your environment.</li><li>There is some kind of service check configured on the firewall, that tries to figure out if port 80 is still reachable on 172.16.1.11 and it uses a 3-way handshake to check that</li><li>Any other possible reason ;-)</li></ul><p>Regards<br />
Kurt</p></div><div id="comment-47442-info" class="comment-info"><span class="comment-age">(09 Nov '15, 14:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47336" class="comment-tools"></div><div class="clear"></div><div id="comment-47336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

