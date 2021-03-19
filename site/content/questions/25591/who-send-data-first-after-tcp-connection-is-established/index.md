+++
type = "question"
title = "Who send data first after TCP connection is established?"
description = '''Hello everybody. Maybe is just a silly question but I have no clear answer. When I see examples of TCP three way handshake (even those shown in RFC 793), the device which first send the SYN segment (client) is always the device which, after connection is estableshed, begins sending data to the devic...'''
date = "2013-10-03T07:58:00Z"
lastmod = "2015-04-23T04:30:00Z"
weight = 25591
keywords = [ "handshake" ]
aliases = [ "/questions/25591" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Who send data first after TCP connection is established?](/questions/25591/who-send-data-first-after-tcp-connection-is-established)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25591-score" class="post-score" title="current number of votes">0</div><span id="post-25591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody.</p><p>Maybe is just a silly question but I have no clear answer.</p><p>When I see examples of TCP three way handshake (even those shown in RFC 793), the device which first send the SYN segment (client) is always the device which, after connection is estableshed, begins sending data to the device which was listening (server).</p><p>But is the opposite possible? Can the server begin sending data after connection is estableshed by the client? Is this documented anywhere? Could you provide some samples? I didn't find anything regarding this question.</p><p>Regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '13, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/24d0053e1e34abf5ca1e5fdca76c94c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="selecnor&#39;s gravatar image" /><p><span>selecnor</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="selecnor has no accepted answers">0%</span></p></div></div><div id="comments-container-25591" class="comments-container"></div><div id="comment-tools-25591" class="comment-tools"></div><div class="clear"></div><div id="comment-25591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25594"></span>

<div id="answer-container-25594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25594-score" class="post-score" title="current number of votes">3</div><span id="post-25594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can the server begin sending data after connection is established by the client?</p></blockquote><p>Certainly !</p><p>The sequence of transmissions depends completely upon the programming of the 'client' and the 'server'.</p><p>In fact, the two sides might be 'peers' with each sending data to the other simultaneously.</p><p>IOW: the TCP connection provides two one-way pipes (A--&gt;B &amp; B--&gt;A) which can be used however desired and with whatever co-ordination between the pipes is desired.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-25594" class="comments-container"><span id="25597"></span><div id="comment-25597" class="comment"><div id="post-25597-score" class="comment-score"></div><div class="comment-text"><p>Thank you, clear and short explanations as i needed. By the way, how does awarding point work? ;-)</p></div><div id="comment-25597-info" class="comment-info"><span class="comment-age">(03 Oct '13, 08:56)</span> <span class="comment-user userinfo">selecnor</span></div></div><span id="25600"></span><div id="comment-25600" class="comment"><div id="post-25600-score" class="comment-score">1</div><div class="comment-text"><p>(Hit the 'accept' button (checkmark icon) to the left of the answer to 'accept' the answer; points will be awarded).</p></div><div id="comment-25600-info" class="comment-info"><span class="comment-age">(03 Oct '13, 09:08)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="25604"></span><div id="comment-25604" class="comment"><div id="post-25604-score" class="comment-score"></div><div class="comment-text"><p>by the way, just as an example of the sender sending data after the handshake you could take a look at a passive FTP-DATA session.</p></div><div id="comment-25604-info" class="comment-info"><span class="comment-age">(03 Oct '13, 09:41)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="41722"></span><div id="comment-41722" class="comment"><div id="post-41722-score" class="comment-score"></div><div class="comment-text"><p>But what then happens if, suppose, both the client and server send a message simultaneously — wouldn't the TCP of both sides then wait for ack message, which, of course, never appear because they both are awaiting?</p></div><div id="comment-41722-info" class="comment-info"><span class="comment-age">(23 Apr '15, 01:40)</span> <span class="comment-user userinfo">Hi-Angel</span></div></div><span id="41725"></span><div id="comment-41725" class="comment"><div id="post-41725-score" class="comment-score">1</div><div class="comment-text"><p>Sending and receiving are independently handled and guarded by timers. If the timer expires before a new segment is send an 'empty' TCP packet will be send anyway just to convey the flags and protocol values.</p></div><div id="comment-41725-info" class="comment-info"><span class="comment-age">(23 Apr '15, 04:30)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-25594" class="comment-tools"></div><div class="clear"></div><div id="comment-25594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25614"></span>

<div id="answer-container-25614" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25614-score" class="post-score" title="current number of votes">2</div><span id="post-25614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Other examples include Telnet (which isn't used that much) which will advertise capabilities and a prompt, as well as a modern version SSH. Here you can see after the 3-way handshake, in frame 266, the Server advertises what type of SSH server it is, without input from the client.<img src="https://osqa-ask.wireshark.org/upfiles/ssh-open.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 18:07</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></img></div></div><div id="comments-container-25614" class="comments-container"></div><div id="comment-tools-25614" class="comment-tools"></div><div class="clear"></div><div id="comment-25614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

