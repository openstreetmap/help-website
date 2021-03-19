+++
type = "question"
title = "The transmission window is now completely full"
description = '''I have run into the TCP Window Full message and want to be clear about which side the issue is on. I am running a capture on a server and it is capturing traffic being sent from a remote site over a site to site VPN. When I see the message the packet its in is showing source as the server and destin...'''
date = "2015-03-11T03:04:00Z"
lastmod = "2015-03-12T15:06:00Z"
weight = 40461
keywords = [ "zero-window", "tcp" ]
aliases = [ "/questions/40461" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [The transmission window is now completely full](/questions/40461/the-transmission-window-is-now-completely-full)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40461-score" class="post-score" title="current number of votes">0</div><span id="post-40461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have run into the TCP Window Full message and want to be clear about which side the issue is on. I am running a capture on a server and it is capturing traffic being sent from a remote site over a site to site VPN. When I see the message the packet its in is showing source as the server and destination as the remote site firewall... Does this mean the server is running dry and processing power and reporting its buffer is full. I note I see a TCP update window a few packets later from the firewall sending it to the server which then confuses me, maybe its unrelated to the buffer being full on the server. Also is this the same as a zero windows condition? Thanks I'd like to get as much info as possible around this : ) thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zero-window" rel="tag" title="see questions tagged &#39;zero-window&#39;">zero-window</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '15, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/68ce515bc08f1da09ed2200c8aca252c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Costello&#39;s gravatar image" /><p><span>Costello</span><br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Costello has no accepted answers">0%</span></p></div></div><div id="comments-container-40461" class="comments-container"><span id="40465"></span><div id="comment-40465" class="comment"><div id="post-40465-score" class="comment-score"></div><div class="comment-text"><p>It's near to impossible to do network troubleshooting based on a text description of what you are seeing.</p><p>Can you please upload the capture file somewhere (google drive, dropbox, cloudshark.org), possibly anonymized with tracewrangler.com, and then post the link here?</p></div><div id="comment-40465-info" class="comment-info"><span class="comment-age">(11 Mar '15, 03:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-40461" class="comment-tools"></div><div class="clear"></div><div id="comment-40461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40477"></span>

<div id="answer-container-40477" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40477-score" class="post-score" title="current number of votes">2</div><span id="post-40477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Costello has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Window Full" from Wireshark means that Wireshark has calculated that the current packet will fill the receiver's buffer. In order to calculate this correctly, Wireshark has to have captured the TCP three-way handshake so that it knows if window scaling is in use, and if so, what the scale factor is. Window Full is normally, but not always, followed by zero window from the receiver.</p><p>The receiver's window is filling up because the application is not reading the data out of the receive buffer as fast as it is coming in from the network. The application is not keeping up. Sometimes Window Full might not be followed by zero window because right at that point the application swoops in and starts reading data out of the receive buffer while the packet with the Window Full message is in transit, so the receive buffer doesn't actually fill up, although it comes close.</p><p>However, most of the time, Window Full will be followed by zero window. If you see a lot of Window Full messages, and they are <em>not</em> followed by zero window, and you didn't capture the three-way handshake, then that is a clue that window scaling is in use and the Window Full message is wrong, because Wireshark is not able to calculate the true window size.</p><p>When you're analyzing TCP, always try to capture the communication from the beginning, so that you have the three-way handshake in the trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '15, 14:26</strong> </span></p></div></div><div id="comments-container-40477" class="comments-container"><span id="40504"></span><div id="comment-40504" class="comment"><div id="post-40504-score" class="comment-score"></div><div class="comment-text"><p>This is really great information thank you very much.</p></div><div id="comment-40504-info" class="comment-info"><span class="comment-age">(12 Mar '15, 01:06)</span> <span class="comment-user userinfo">Costello</span></div></div></div><div id="comment-tools-40477" class="comment-tools"></div><div class="clear"></div><div id="comment-40477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40467"></span>

<div id="answer-container-40467" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40467-score" class="post-score" title="current number of votes">1</div><span id="post-40467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "[TCP Window Full]" message from Wireshark means that the system sending this TCP segment has filled up the receive window of the other end with the tcp segment in this packet.</p><p>Or put differently: the last received window size of the other end is equal to the length of the tcp segment in this packet.</p><p>What it means for your connection can only be determined when seeing the surrounding packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40467" class="comments-container"><span id="40472"></span><div id="comment-40472" class="comment"><div id="post-40472-score" class="comment-score"></div><div class="comment-text"><p>If I don't see a zero window condition after a TCP full, this indicate anything?</p></div><div id="comment-40472-info" class="comment-info"><span class="comment-age">(11 Mar '15, 07:59)</span> <span class="comment-user userinfo">Costello</span></div></div><span id="40476"></span><div id="comment-40476" class="comment"><div id="post-40476-score" class="comment-score"></div><div class="comment-text"><p>That all depends on your capture point (near the sender or near the receiver) and the other packets surrounding this packet. So the answer would be: "It depends" ;-)</p></div><div id="comment-40476-info" class="comment-info"><span class="comment-age">(11 Mar '15, 09:41)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="40522"></span><div id="comment-40522" class="comment"><div id="post-40522-score" class="comment-score"></div><div class="comment-text"><p>Wow wireshark sure is tricky. I'm only learning but it seems to be difficult to be confident when identifying an issue. There are so many other factors that come into play (lots of red herrings!). I'm using the chappellU videos but is there any where else worth looking at to upskill. I've met quite a few people that have a knowledge of wireshark functionality but none that were confident to pinpoint problems and provide wireshark data to back it up : )</p></div><div id="comment-40522-info" class="comment-info"><span class="comment-age">(12 Mar '15, 15:06)</span> <span class="comment-user userinfo">Costello</span></div></div></div><div id="comment-tools-40467" class="comment-tools"></div><div class="clear"></div><div id="comment-40467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

