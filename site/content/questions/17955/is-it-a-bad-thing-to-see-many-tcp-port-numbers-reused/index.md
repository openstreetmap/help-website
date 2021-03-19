+++
type = "question"
title = "Is it a bad thing to see many [TCP Port numbers reused]?"
description = '''Here is a Wireshark capture that contains many [TCP Port numbers reused] packets. You&#x27;ll notice that the reused port messages begin at frame 47727 and continue on for the rest of the capture. Understandably, every stream that contains a reused port message has a corresponding stream that occurred pr...'''
date = "2013-01-25T14:13:00Z"
lastmod = "2013-01-25T15:29:00Z"
weight = 17955
keywords = [ "reused", "port", "tcp", "numbers" ]
aliases = [ "/questions/17955" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is it a bad thing to see many \[TCP Port numbers reused\]?](/questions/17955/is-it-a-bad-thing-to-see-many-tcp-port-numbers-reused)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17955-score" class="post-score" title="current number of votes">0</div><span id="post-17955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is a <a href="http://cloudshark.org/captures/94b48873562a">Wireshark capture</a> that contains many <code>[TCP Port numbers reused]</code> packets.</p><p>You'll notice that the reused port messages begin at frame 47727 and continue on for the rest of the capture.</p><p>Understandably, every stream that contains a reused port message has a corresponding stream that occurred prior and that has the same client side port number.</p><p>For example:</p><p>The first frame that reports a reused port is 47727 (contained in <strong>stream 3952</strong>) where the reused port number is 2242 (foliocorp). Using the <code>tcp.port == 2242</code> filter, I discovered that <strong>stream 0</strong> uses port 2242 as well.</p><p>What caught my attention is the fact that all the streams that contain a <code>TCP Port numbers reused</code> message, are popping up because a duplicate port number (client side) was used aproximately 2 hours prior to the error message - and in sequential order.</p><p>It's as if the client computer sets aside a certain amount of port numbers that will be used and then when the port numbers have all been used, the first port number is reused again and so on.</p><p>My question is, given that the same port number is NOT being used simultaneously, but rather is simply being reused in the sense that it was used some time in the past (2 hours in my case), can I ignore the <code>TCP Port numbers reused</code> messages? Or is there something occurring that shouldn't be? If so, how to I go about fixing the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reused" rel="tag" title="see questions tagged &#39;reused&#39;">reused</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-numbers" rel="tag" title="see questions tagged &#39;numbers&#39;">numbers</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '13, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p><span>KTM</span><br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jan '13, 14:16</strong> </span></p></div></div><div id="comments-container-17955" class="comments-container"></div><div id="comment-tools-17955" class="comment-tools"></div><div class="clear"></div><div id="comment-17955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17956"></span>

<div id="answer-container-17956" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17956-score" class="post-score" title="current number of votes">1</div><span id="post-17956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="KTM has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It can happen when you have a long running capture of a single client-server relation where the client keeps opening new TCP sessions all the time, like in your case (several hours of captured packets). What happens is that the client uses a temporary port (also called "ephemeral port") and connects to the server port (which is usually a fixed port, like port 80 for HTTP).</p><p>Windows up until Windows XP uses port 1025 to 5000 as ephemeral ports (it doesn't matter if it connects to the same server or another, it always increases by 1), and when it gets to 5000 it will start at 1025 again. You can see this text book behaviour in frame 33150 (SYN from port 5000) and the next SYN is in 33162 coming from port 1025 again. Since your capture started after the client had already opened and closed some connections you do not see 1025 twice, but in your case 2242 was the first port number you captured. When it loops around 5000 back to 1025 it is only a matter of time until you get a "port number reused".</p><p>"Port number reused" <strong>might</strong> indicate a problem, but only if the ports are reused very shortly again - which is not the case in your trace. Final verdict: yes, port number reused, but in a long running trace, and thus not a problem. The time distance is about 7880 seconds between the reuse, so you're safe.</p><p>BTW, starting with Vista, Microsoft changed the ephemeral port range to 49152 up to 65535. See also <a href="http://en.wikipedia.org/wiki/Ephemeral_port">http://en.wikipedia.org/wiki/Ephemeral_port</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '13, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17956" class="comments-container"></div><div id="comment-tools-17956" class="comment-tools"></div><div class="clear"></div><div id="comment-17956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

