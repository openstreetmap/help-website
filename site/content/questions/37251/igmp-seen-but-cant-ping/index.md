+++
type = "question"
title = "IGMP seen but can&#x27;t ping"
description = '''Hello I see on Wireshark an embedded board on which I want to connect. I successful connect to the board if its cable is connected after its startup. However if the cable is connected during the startup process, I can not ping it. This seems to happen only on some configurations (with a moxa hub on ...'''
date = "2014-10-21T12:32:00Z"
lastmod = "2014-10-26T15:36:00Z"
weight = 37251
keywords = [ "ping", "igmp" ]
aliases = [ "/questions/37251" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IGMP seen but can't ping](/questions/37251/igmp-seen-but-cant-ping)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37251-score" class="post-score" title="current number of votes">0</div><span id="post-37251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I see on Wireshark an embedded board on which I want to connect. I successful connect to the board if its cable is connected after its startup. However if the cable is connected during the startup process, I can not ping it. This seems to happen only on some configurations (with a moxa hub on which POE devices are connected). Using wireshark I can see that the board is sending 2 IGMP messages in both configuration ( cable connected at startup and cable connected after startup).</p><p>IGMP message show the correct ip address in both case</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-igmp" rel="tag" title="see questions tagged &#39;igmp&#39;">igmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/de92ed7ac90822fad0847bbdb46800f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J%C3%A9r%C3%A9mie%20Guillot&#39;s gravatar image" /><p><span>Jérémie Guillot</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jérémie Guillot has no accepted answers">0%</span></p></div></div><div id="comments-container-37251" class="comments-container"></div><div id="comment-tools-37251" class="comment-tools"></div><div class="clear"></div><div id="comment-37251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37277"></span>

<div id="answer-container-37277" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37277-score" class="post-score" title="current number of votes">1</div><span id="post-37277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>However if the cable is connected during the startup process, <strong>I can not ping it</strong>.</p></blockquote><p>If you cannot ping the board, there could be several reasons, like:</p><ul><li>The embedded board is not answering ARP requests</li><li>Your client (somehow) has the wrong MAC address in its ARP cache</li><li>There is a problem with the initialization of either the NIC or the IP stack within the embedded board</li></ul><p>So, to rule out some possible problems, please do the following:</p><ul><li>start Wireshark</li><li>ping the system</li><li>stop Wireshark</li><li>check the captured data for: ARP request/response, ICMP ECHO request/response (ping), the correct MAC address in those frames.</li></ul><p>If you see the ICMP ECHO request being sent to the correct MAC address, but you don't see any answer, it's a problem with the board (either NIC or IP stack). Then Wireshark can't help you any further.</p><p>If you don't see an ICMP ECHO request, you client does not know where to send it, so it does not get an answer for it's ARP request (check that in the capture file as well). Again: probably a problem within the embedded board.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37277" class="comments-container"><span id="37334"></span><div id="comment-37334" class="comment"><div id="post-37334-score" class="comment-score"></div><div class="comment-text"><p>Hello kurt and thanks for your help.</p><p>You're right there's no answer to the arp request. So it seems there's a problem with the embedded board. The strange thing is that IGMPv2 message is received...</p></div><div id="comment-37334-info" class="comment-info"><span class="comment-age">(24 Oct '14, 03:46)</span> <span class="comment-user userinfo">Jérémie Guillot</span></div></div><span id="37361"></span><div id="comment-37361" class="comment"><div id="post-37361-score" class="comment-score"></div><div class="comment-text"><p>If it's a bug, the behaviour will likely be 'strange', so the fact that the systems <strong>sends</strong> out frames does not mean it is also able to <strong>receive</strong> frames ;-))</p></div><div id="comment-37361-info" class="comment-info"><span class="comment-age">(26 Oct '14, 15:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-37277" class="comment-tools"></div><div class="clear"></div><div id="comment-37277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

