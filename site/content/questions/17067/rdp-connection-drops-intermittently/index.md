+++
type = "question"
title = "RDP connection drops intermittently"
description = '''Hey Guys Thanks for reading my questions, this forum is my last resort as I am out of ideas. We have users that connect to a remote server outside of our network to perform some admin tasks and everything has been working fine until a few weeks ago. Users started complaining that their RDP session k...'''
date = "2012-12-19T09:07:00Z"
lastmod = "2012-12-20T02:50:00Z"
weight = 17067
keywords = [ "rdp" ]
aliases = [ "/questions/17067" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RDP connection drops intermittently](/questions/17067/rdp-connection-drops-intermittently)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17067-score" class="post-score" title="current number of votes">0</div><span id="post-17067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey Guys</p><p>Thanks for reading my questions, this forum is my last resort as I am out of ideas.</p><p>We have users that connect to a remote server outside of our network to perform some admin tasks and everything has been working fine until a few weeks ago. Users started complaining that their RDP session keeps freezing then drops completely with the error message "Your remote desktop services session has ended. The connection to the remote computer was lost, possibly due to network connectivity problems." I have tested this from multiple PCs and from multiple locations with the same result. The following was captured with Wireshark hopefully someone can shed some light on what's going on.</p><pre><code>4145    213.992742000   source(my pc)   destination (remote server) TPKT    71  Continuation
4146    213.998031000   source(my pc)   destination (remote server) TPKT    981 [TCP Retransmission] Continuation
4167    219.778181000   source(my pc)   destination (remote server) TPKT    85  Continuation
4191    224.575355000   source(my pc)   destination (remote server) TPKT    1354    [TCP Retransmission] Continuation
4246    238.663506000   source(my pc)   destination (remote server) TCP 54  49322 &gt; ms-wbt-server [RST, ACK] Seq=173138 Ack=27613 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '12, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/54e1db98ddba54a3add9130395cc7dbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlevin&#39;s gravatar image" /><p><span>tlevin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlevin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Dec '12, 09:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-17067" class="comments-container"></div><div id="comment-tools-17067" class="comment-tools"></div><div class="clear"></div><div id="comment-17067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17086"></span>

<div id="answer-container-17086" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17086-score" class="post-score" title="current number of votes">0</div><span id="post-17086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, 5 packets out of a complete stream is not a lot to go by when trying to find the source of the problem. But here goes anyway :-)</p><p>Assuming you captured near the client and that your capture and display filters did not filter out the packets coming from the server (you did see server packets earlier in the trace, didn't you?), then I would say that indeed the connection to the RDP server is interrupted. The client keeps sending data and retransmitting it, but it does not get a response (not even by an ACK at the TCP level) and finally shuts down the connection, which results in a TCP RST in frame 4246.</p><p>You might want to capture data on both the client side and the server side to verify that all packets do arrive at the RDP server.</p><p>I suspect there might be a statefull device (Firewall or LoadBalancer or similar) that might have dropped the session and now blocks traffic. What devices are on the path from the client to the RDP server?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '12, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17086" class="comments-container"></div><div id="comment-tools-17086" class="comment-tools"></div><div class="clear"></div><div id="comment-17086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

