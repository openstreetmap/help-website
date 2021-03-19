+++
type = "question"
title = "measuring round trip time,"
description = '''Hi everybody,  Just now i have started using the wireshark, i got to know how to capture the traffic flowing through network, but i am trying to get the round trip time of packets , how do i get to know that ??  i can just see the window of showing the packet no, src, dest, protocol, etc, please hel...'''
date = "2011-05-24T23:16:00Z"
lastmod = "2011-05-30T07:33:00Z"
weight = 4210
keywords = [ "rtt" ]
aliases = [ "/questions/4210" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [measuring round trip time,](/questions/4210/measuring-round-trip-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4210-score" class="post-score" title="current number of votes">0</div><span id="post-4210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody, Just now i have started using the wireshark, i got to know how to capture the traffic flowing through network, but i am trying to get the round trip time of packets , how do i get to know that ?? i can just see the window of showing the packet no, src, dest, protocol, etc, please help me out in finding the roundtrip time.</p><p>Thanks &amp; regards Sagar</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtt" rel="tag" title="see questions tagged &#39;rtt&#39;">rtt</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '11, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/257c9f9e498193d7ddde57090efe094a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagu072&#39;s gravatar image" /><p><span>sagu072</span><br />
<span class="score" title="35 reputation points">35</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagu072 has no accepted answers">0%</span></p></div></div><div id="comments-container-4210" class="comments-container"></div><div id="comment-tools-4210" class="comment-tools"></div><div class="clear"></div><div id="comment-4210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4213"></span>

<div id="answer-container-4213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4213-score" class="post-score" title="current number of votes">3</div><span id="post-4213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should make sure you have a column showing the "relative time" (I also recommend adding the "delta time displayed" column while you're at it): see preferences/columns.</p><p>Usually, you determine round trip time by selecting at the outgoing packet and setting a "time reference" by using the popup menu. Next, look for the incoming answer packet and use the relative time column to read the time that it took for the answer to arrive. Important: this only works if you capture very very close to the client (or, more generally, the machine that is sending the question).</p><p>A special case is measuring RTT for TCP sessions, which can be done by finding the initial SYN, and then (after setting a time reference on it) looking at the relative time of the ACK (third packet in the TCP three way handshake). If you do that you don't have to worry about the placement of the capturing machine, because all parts of the round trip distance is included.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '11, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4213" class="comments-container"><span id="4215"></span><div id="comment-4215" class="comment"><div id="post-4215-score" class="comment-score"></div><div class="comment-text"><p>jasper, thank you, there s no column with name relative time, i am not really getting what all u said as m new to wireshark, i may get it once i go through wireshark n read this again, thank you.</p></div><div id="comment-4215-info" class="comment-info"><span class="comment-age">(25 May '11, 00:18)</span> <span class="comment-user userinfo">sagu072</span></div></div><span id="4223"></span><div id="comment-4223" class="comment"><div id="post-4223-score" class="comment-score"></div><div class="comment-text"><p>Go to Edit -&gt; Preferences -&gt; User Interface -&gt; Columns. Click "Add", name it "Relative Time" and select "Relative Time" as Field Type.</p></div><div id="comment-4223-info" class="comment-info"><span class="comment-age">(25 May '11, 01:16)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="4226"></span><div id="comment-4226" class="comment"><div id="post-4226-score" class="comment-score"></div><div class="comment-text"><p>hi, i hv added the relative time column but its values are as same as time column. what exactly the relative time represents, and how do i identify outgoing packet, Ack n all.</p></div><div id="comment-4226-info" class="comment-info"><span class="comment-age">(25 May '11, 01:42)</span> <span class="comment-user userinfo">sagu072</span></div></div><span id="4227"></span><div id="comment-4227" class="comment"><div id="post-4227-score" class="comment-score"></div><div class="comment-text"><p>true, if you have default wireshark settings your time column is probably set to "relative time", but since it can be changed to something else I like to have an extra column for relative time.</p><p>Regardin the outgoing packet - you need to know the protocol and what kind of packet contains outgoing data. If you are unfamiliar with the protocol you can only revert to the Three Way Handshake process I mentioned earlier.</p></div><div id="comment-4227-info" class="comment-info"><span class="comment-age">(25 May '11, 02:36)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="4228"></span><div id="comment-4228" class="comment"><div id="post-4228-score" class="comment-score"></div><div class="comment-text"><p>(answer converted to comment)</p></div><div id="comment-4228-info" class="comment-info"><span class="comment-age">(25 May '11, 02:40)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-4213" class="comment-tools"></div><div class="clear"></div><div id="comment-4213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4290"></span>

<div id="answer-container-4290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4290-score" class="post-score" title="current number of votes">0</div><span id="post-4290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What kind of WLANcard you are using sagu072 and what level of accuracy for your RTT need? I ask this question because there are different ways and different time elements which you can do this with.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '11, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/559f374efd2eaeaafac5616bbec62008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AminGho&#39;s gravatar image" /><p><span>AminGho</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AminGho has no accepted answers">0%</span></p></div></div><div id="comments-container-4290" class="comments-container"></div><div id="comment-tools-4290" class="comment-tools"></div><div class="clear"></div><div id="comment-4290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

