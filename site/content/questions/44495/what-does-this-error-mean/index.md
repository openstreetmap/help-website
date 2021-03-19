+++
type = "question"
title = "What does this error mean?"
description = '''Hello. When I want to run Telegram on my Windows OS, Telegram Can&#x27;t connect to the internet. I use Wireshark for Capture it and Please see the Attachment and let me know your idea. Thank you.'''
date = "2015-07-26T07:53:00Z"
lastmod = "2015-07-27T05:33:00Z"
weight = 44495
keywords = [ "and", "telegram", "wireshark" ]
aliases = [ "/questions/44495" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does this error mean?](/questions/44495/what-does-this-error-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44495-score" class="post-score" title="current number of votes">0</div><span id="post-44495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. When I want to run Telegram on my Windows OS, Telegram Can't connect to the internet. I use Wireshark for Capture it and Please see the Attachment and let me know your idea.</p><p>Thank you.<img src="https://osqa-ask.wireshark.org/upfiles/wireshark_1S1dX3c.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-telegram" rel="tag" title="see questions tagged &#39;telegram&#39;">telegram</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '15, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/1f1d393403ea997213960ee852d8f897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hack3rcon&#39;s gravatar image" /><p><span>hack3rcon</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hack3rcon has no accepted answers">0%</span></p></img></div></div><div id="comments-container-44495" class="comments-container"><span id="44502"></span><div id="comment-44502" class="comment"><div id="post-44502-score" class="comment-score"></div><div class="comment-text"><p>It means that the RST Bit is set and this leads to a session termination. But the root cause, why the RST Bit is set here can't be seen at this screenshot. Maybe it is application related.</p></div><div id="comment-44502-info" class="comment-info"><span class="comment-age">(26 Jul '15, 10:34)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44505"></span><div id="comment-44505" class="comment"><div id="post-44505-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us the whole traced session at dropbox or cloudshark?</p></div><div id="comment-44505-info" class="comment-info"><span class="comment-age">(26 Jul '15, 11:41)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44513"></span><div id="comment-44513" class="comment"><div id="post-44513-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p><p><a href="https://www.cloudshark.org/captures/52649d30c0f7">https://www.cloudshark.org/captures/52649d30c0f7</a></p></div><div id="comment-44513-info" class="comment-info"><span class="comment-age">(26 Jul '15, 22:57)</span> <span class="comment-user userinfo">hack3rcon</span></div></div><span id="44519"></span><div id="comment-44519" class="comment"><div id="post-44519-score" class="comment-score"></div><div class="comment-text"><p>I can't see any RST Packet in the trace. But also I can't see any syn/ack packet in the trace. Maybe a firewall rule blocks the syn. Can you ping these addreses?</p></div><div id="comment-44519-info" class="comment-info"><span class="comment-age">(27 Jul '15, 03:43)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44522"></span><div id="comment-44522" class="comment"><div id="post-44522-score" class="comment-score"></div><div class="comment-text"><p>I ping the addresses and the result is :</p><p><a href="https://www.cloudshark.org/captures/f5a81dc6424e">https://www.cloudshark.org/captures/f5a81dc6424e</a></p><p>What is your idea?</p></div><div id="comment-44522-info" class="comment-info"><span class="comment-age">(27 Jul '15, 05:33)</span> <span class="comment-user userinfo">hack3rcon</span></div></div></div><div id="comment-tools-44495" class="comment-tools"></div><div class="clear"></div><div id="comment-44495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44503"></span>

<div id="answer-container-44503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44503-score" class="post-score" title="current number of votes">1</div><span id="post-44503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the context of you trying to reach a server on TCP port 445, based on the relative sequence number it looks like the application is running and some data has been exchanged, but very early on the server is abruptly killing the TCP session, likely due to application-level error.</p><p>Note, I'm assuming that packet came from the server based on the source mac being Cisco and the destination being more likely to be a PC. That and the source port is in the well-known range, so likely the service port reached by the client.</p><p>Also note, a 'reset' is a warning because it MIGHT be a problem. Some applications are just written such that they kill TCP sessions this way in normal conditions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '15, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jul '15, 11:23</strong> </span></p></div></div><div id="comments-container-44503" class="comments-container"><span id="44504"></span><div id="comment-44504" class="comment"><div id="post-44504-score" class="comment-score"></div><div class="comment-text"><p>I use a TMG Server and this problem occur on clients. My TMG server run Telegram without any problem.In TMG I use some rules and the PCs that want to use Telegram are NAT (Use a TMG rule that let them connect to internet directly). This problem suddenly happened :(.</p></div><div id="comment-44504-info" class="comment-info"><span class="comment-age">(26 Jul '15, 11:40)</span> <span class="comment-user userinfo">hack3rcon</span></div></div></div><div id="comment-tools-44503" class="comment-tools"></div><div class="clear"></div><div id="comment-44503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

