+++
type = "question"
title = "TCP Dissector, detect which endpoint opened the connection?"
description = '''I&#x27;m writing a dissector for a protocol that I have to work with. This protocol runs atop TCP and is stateful.  In order to dissect the fields correctly, I need to identify which endpoint opened the TCP connection (the client). Is there a way to get this info from the tcp dissector? Would I have to w...'''
date = "2011-08-18T13:29:00Z"
lastmod = "2011-11-09T10:30:00Z"
weight = 5746
keywords = [ "lua", "dissector", "tcp" ]
aliases = [ "/questions/5746" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Dissector, detect which endpoint opened the connection?](/questions/5746/tcp-dissector-detect-which-endpoint-opened-the-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5746-score" class="post-score" title="current number of votes">0</div><span id="post-5746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a dissector for a protocol that I have to work with. This protocol runs atop TCP and is stateful.</p><p>In order to dissect the fields correctly, I need to identify which endpoint opened the TCP connection (the client).</p><p>Is there a way to get this info from the tcp dissector? Would I have to write a tap? I'm not so clear on how to do this in lua.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '11, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/ac7d13a55a5d6af18586aea10ed8ef68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Flame&#39;s gravatar image" /><p><span>Flame</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Flame has no accepted answers">0%</span></p></div></div><div id="comments-container-5746" class="comments-container"><span id="5747"></span><div id="comment-5747" class="comment"><div id="post-5747-score" class="comment-score"></div><div class="comment-text"><p>Cross posted to StackOverflow http://stackoverflow.com/questions/7113810/wireshark-lua-dissector-detect-which-endpoint-opened-the-connection.</p></div><div id="comment-5747-info" class="comment-info"><span class="comment-age">(18 Aug '11, 13:38)</span> <span class="comment-user userinfo">Flame</span></div></div></div><div id="comment-tools-5746" class="comment-tools"></div><div class="clear"></div><div id="comment-5746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5755"></span>

<div id="answer-container-5755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5755-score" class="post-score" title="current number of votes">1</div><span id="post-5755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In general, the TCP dissector doesn't, and can't have that information. If you have not captured the initial 3-way handshake, all you have are data segments and ACKs, and there's no way, from just the TCP header, to determine which of the two endpoints opened the connection.</p><p>If this is a protocol where there's a standard server port, you could use the port number. If not, you might be able to have a tap listener for the TCP tap, to look at all the packets and <em>hope</em> at least one of them is a SYN packet so you can see the initial SYN or the SYN+ACK and from that determine which side opened the connection - but if you don't, you're out of luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '11, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-5755" class="comments-container"><span id="5757"></span><div id="comment-5757" class="comment"><div id="post-5757-score" class="comment-score"></div><div class="comment-text"><p>My best bet would be to see who sends data first then. After the handshake it appears that the client always sends data first.</p><p>There are multiple services that speak this protocol, and they each use a different default listening port.</p></div><div id="comment-5757-info" class="comment-info"><span class="comment-age">(18 Aug '11, 18:43)</span> <span class="comment-user userinfo">Flame</span></div></div><span id="5758"></span><div id="comment-5758" class="comment"><div id="post-5758-score" class="comment-score"></div><div class="comment-text"><p>You might be capturing in the middle of a session, and you might happen to start capturing at a point after the client has sent something to the server but before the server has responded. Those periods of time probably constitute a minority of the total time of the session, so there's probably a good, but not 100%, chance that the endpoint that sent the first non-empty TCP segment is the client.</p><p>If you know all the possible listening ports, that's just a general case of "you could use the port number".</p><p>Note also that if it's <em>very</em> stateful, capturing in the middle could lose other info.</p></div><div id="comment-5758-info" class="comment-info"><span class="comment-age">(18 Aug '11, 19:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="7309"></span><div id="comment-7309" class="comment"><div id="post-7309-score" class="comment-score"></div><div class="comment-text"><p>nop. at least SMTP servers do respond with data immediately after handshake. <a href="http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol#SMTP_transport_example">http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol#SMTP_transport_example</a> I guess your milage may vary.</p></div><div id="comment-7309-info" class="comment-info"><span class="comment-age">(08 Nov '11, 20:30)</span> <span class="comment-user userinfo">ShomeaX</span></div></div><span id="7329"></span><div id="comment-7329" class="comment"><div id="post-7329-score" class="comment-score"></div><div class="comment-text"><p>Hence "good, but not 100%". Most protocols don't work the way SMTP does here.</p></div><div id="comment-7329-info" class="comment-info"><span class="comment-age">(09 Nov '11, 10:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-5755" class="comment-tools"></div><div class="clear"></div><div id="comment-5755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

