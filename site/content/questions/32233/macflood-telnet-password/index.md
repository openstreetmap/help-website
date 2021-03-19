+++
type = "question"
title = "MACflood &amp; Telnet password"
description = '''Hello, I have a problem with captured telnet password using macflood attack. As you can see on the screen, there is no password, just &quot;......&quot;.  When I use another attack (arpspoof, ...), I can see password without problems. Anybody knows where could be a problem? Thanks. '''
date = "2014-04-28T01:41:00Z"
lastmod = "2014-04-29T02:39:00Z"
weight = 32233
keywords = [ "macflood", "capture", "attack", "password", "telnet" ]
aliases = [ "/questions/32233" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MACflood & Telnet password](/questions/32233/macflood-telnet-password)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32233-score" class="post-score" title="current number of votes">0</div><span id="post-32233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a problem with captured telnet password using macflood attack. As you can see on the screen, there is no password, just "......".</p><p>When I use another attack (arpspoof, ...), I can see password without problems. Anybody knows where could be a problem?</p><p>Thanks.</p><p><img src="http://superupload.wz.cz/upload/telnetfck2.png" alt="screen" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macflood" rel="tag" title="see questions tagged &#39;macflood&#39;">macflood</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-attack" rel="tag" title="see questions tagged &#39;attack&#39;">attack</span> <span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/10ec81062e40be12bb5d3c9b81a831f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petersonn&#39;s gravatar image" /><p><span>petersonn</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petersonn has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '14, 04:14</strong> </span></p></div></div><div id="comments-container-32233" class="comments-container"></div><div id="comment-tools-32233" class="comment-tools"></div><div class="clear"></div><div id="comment-32233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32272"></span>

<div id="answer-container-32272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32272-score" class="post-score" title="current number of votes">1</div><span id="post-32272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You either captured only one direction of the communication or you filtered the traffic to show only one direction (dst: 192.168.1.9). So, what you see in the screenshot is only the traffic from the telnet server to the telnet client. Why you only see half of the traffic could be related to your capture method/setup. As you did not tell us anything about that (except 'macflood') it's impossible to give you any advice.</p><p>The reason why you see dots (....) for the password is some ECHO option enabled on the telnet server. With that option it will echo certain pieces of the communication back to the client. In the case of the password, your telnet server apparently does not echo the real password. Instead it uses other characters.</p><blockquote><p><a href="http://tools.ietf.org/html/rfc857">http://tools.ietf.org/html/rfc857</a></p></blockquote><p>The difference to your other capture file is (most certainly) the fact that you've captured both directions in the other capture file and thus you can see the cleartext password sent from the client to the server. You'll have the echoed password as well in the capture file (if it's the same telnet server), but you might not have noticed, as you probably did not know about that feature and thus you ignored the extra characters.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '14, 17:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32272" class="comments-container"><span id="32285"></span><div id="comment-32285" class="comment"><div id="post-32285-score" class="comment-score"></div><div class="comment-text"><p>Yes, you're right, I captured only traffic from telnet server to telnet client. My topology is: <a href="http://s4.postimg.org/x5x0bvirh/telnet_scheme.png">http://s4.postimg.org/x5x0bvirh/telnet_scheme.png</a> I run macof from attacker's PC for a few seconds to fill CAM table. After that I start capturing data on attacker's PC and then I connect Telnet client PC and make telnet connection. But I can see in the Wireshark only telnet traffic captured in one direction. Where can I find the other direction (from client to server)? If necessary, I can upload my .pcap file for you.</p><p>Thank you for answering!</p><p>Peter</p></div><div id="comment-32285-info" class="comment-info"><span class="comment-age">(29 Apr '14, 02:39)</span> <span class="comment-user userinfo">petersonn</span></div></div></div><div id="comment-tools-32272" class="comment-tools"></div><div class="clear"></div><div id="comment-32272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

