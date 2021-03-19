+++
type = "question"
title = "Trying to figure out who is closing these sessions"
description = '''The Server seems to be sending FIN Acks for sessions that aren&#x27;t in the trace, goes on for awhile and then the sessions all resume. Thanks in advance. Uploaded here: https://www.cloudshark.org/captures/86369a51b115'''
date = "2017-07-12T10:31:00Z"
lastmod = "2017-07-12T10:31:00Z"
weight = 62714
keywords = [ "tls", "client", "server", "sessions" ]
aliases = [ "/questions/62714" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to figure out who is closing these sessions](/questions/62714/trying-to-figure-out-who-is-closing-these-sessions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62714-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The Server seems to be sending FIN Acks for sessions that aren't in the trace, goes on for awhile and then the sessions all resume.</p><p>Thanks in advance.</p><p>Uploaded here: <a href="https://www.cloudshark.org/captures/86369a51b115">https://www.cloudshark.org/captures/86369a51b115</a></p></div><div id="question-tags" class="tags-container tags">tls client server sessions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '17, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/abb4d610318f8a1823c43c659eebdf55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiskydelta&#39;s gravatar image" /><p>wiskydelta<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiskydelta has no accepted answers">0%</span></p></div></div><div id="comments-container-62714" class="comments-container"><span id="62716"></span><div id="comment-62716" class="comment"><div id="post-62716-score" class="comment-score"></div><div class="comment-text"><p>Can you make the capture at Cloudshark publicly accessible?</p></div><div id="comment-62716-info" class="comment-info"><span class="comment-age">(12 Jul '17, 10:51)</span> sindy</div></div><span id="62717"></span><div id="comment-62717" class="comment"><div id="post-62717-score" class="comment-score"></div><div class="comment-text"><p>Should be accessible now</p></div><div id="comment-62717-info" class="comment-info"><span class="comment-age">(12 Jul '17, 12:00)</span> wiskydelta</div></div><span id="62718"></span><div id="comment-62718" class="comment"><div id="post-62718-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "the sessions all resume"? Strictly speaking, a TCP session cannot "resume" once finished. An application may resume conversation, using a new TCP session.</p><p>Other than that, the first FIN seems to always come from the client side, the server only responds to it.</p><p>Not knowing the application case, it is hard to say anything more. I could imagine many clients behind the same NAT device, all of which keep TCP sessions alive for a while after the last application request has been responded, and then close them gracefully (using FIN) on timeout (which is quite a rational approach given the overhead of setting up and especially tearing down a TCP session). You would have to capture for much longer to see several TCP sessions to be established and closed to make some more useful conclusions.</p><p>I would consider it some kind of attack to the client, where somebody else would send FINs in its name, expecting that the server would respond with its own FIN, but two things contradict that view:</p><ul><li>new sessions from the same client side IP are successfully established,</li><li>there would have to be some specific bug in the TCP stack of the server that it would respond a client's FIN with its own one if the session would not exist.</li></ul><p>But there is also a possibility that it is some security device which forges a FIN in the name of the client and handles the consequences smoothly. Can you capture also at client side in parallel to the server side to prove or deny this?</p></div><div id="comment-62718-info" class="comment-info"><span class="comment-age">(12 Jul '17, 12:27)</span> sindy</div></div><span id="62722"></span><div id="comment-62722" class="comment"><div id="post-62722-score" class="comment-score"></div><div class="comment-text"><p>When I say resume, all communications stops and I see a ton of FIN Acks, when they stop then the sessions start establishing correctly again and working. Working on getting a client capture now.</p></div><div id="comment-62722-info" class="comment-info"><span class="comment-age">(12 Jul '17, 13:24)</span> wiskydelta</div></div></div><div id="comment-tools-62714" class="comment-tools"></div><div class="clear"></div><div id="comment-62714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

