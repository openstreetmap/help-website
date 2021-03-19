+++
type = "question"
title = "Continual NTLM Authentication"
description = '''Hi. This is not actually a Wireshark question per se, so, if I&#x27;m out of line for asking it here, please let me know. I will take it like a man :-) I am using Wireshark to analyze/improve the performance of a .NET 2.0 application. It is a WinForms app, which calls an ASMX Web Service. What I have fou...'''
date = "2011-06-14T13:25:00Z"
lastmod = "2011-06-19T14:39:00Z"
weight = 4566
keywords = [ "authentication", "ntlm", ".net" ]
aliases = [ "/questions/4566" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Continual NTLM Authentication](/questions/4566/continual-ntlm-authentication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. This is not actually a Wireshark question per se, so, if I'm out of line for asking it here, please let me know. I will take it like a man :-)</p><p>I am using Wireshark to analyze/improve the performance of a .NET 2.0 application. It is a WinForms app, which calls an ASMX Web Service.</p><p>What I have found is that, for each and every HTTP POST, to MyWebService.asmx, an NTLM Authentication sequence is executed, as follows:<br />
1) Client sends POST, 2) Server responds with '401 Unauthorized', 3) Client sends POST again, but this time with the necessary 'Authorization:' Header, 4) Server responds with '200 OK'.</p><p>This sequence is executed even when the client hits a button that causes 4 consecutive POSTs. Each of these POSTs, from the same client to the same server, causes a NTLM Authentication sequence. This adds an extra round trip for each request, which has a significant impact on performance, since the client and server are separated by a high latency path.</p><p>My "guess" is that one of the following might cure this:</p><p>A) Include the Authorization header in the initial POST, so the server doesn't have to demand it via the 401.</p><p>B) Use a persistent connection, so at least only the first of the four POSTs will have to Authenticate.</p><p>Unfortunately, I am not a .NET programmer - I am a packetologist :-) - so I don't know what the developer needs to change.</p><p>Can anyone tell me if this is fixable with a not-too-complicated code or config change to the .NET app?</p><p>Thx much!</p><p>Feenyman99</p></div><div id="question-tags" class="tags-container tags">authentication ntlm .net</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '11, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span> </br></p></div></div><div id="comments-container-4566" class="comments-container"></div><div id="comment-tools-4566" class="comment-tools"></div><div class="clear"></div><div id="comment-4566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4625"></span>

<div id="answer-container-4625" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4625-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds to me that there is a loadbalancer in between that does not persist a client to one server, so each new loadbalanced tcp stream needs to re-authenticate. I would identify the loadbalancer and add persistency to it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '11, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4625" class="comments-container"></div><div id="comment-tools-4625" class="comment-tools"></div><div class="clear"></div><div id="comment-4625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4615"></span>

<div id="answer-container-4615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4615-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure if you have access to the server, but I would look at the event log on the server they are posting to and see what error is being generated server-side for the failed ntlm authentications. Hope this is helpful, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '11, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4615" class="comments-container"></div><div id="comment-tools-4615" class="comment-tools"></div><div class="clear"></div><div id="comment-4615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

