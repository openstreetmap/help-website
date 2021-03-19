+++
type = "question"
title = "IPhone Resets Mid Transfer"
description = '''Hello, My ability to analyze a capture is limited. So, any help is appreciated. I have a server that is trying to send a .m4v (video) file to an IPhone. It looks to me, like the phone is resetting the connection before the transfer takes place. If that is true, the question is why is it resetting? H...'''
date = "2014-03-21T12:29:00Z"
lastmod = "2014-03-22T05:08:00Z"
weight = 31064
keywords = [ "reset", "iphone", "tcp" ]
aliases = [ "/questions/31064" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [IPhone Resets Mid Transfer](/questions/31064/iphone-resets-mid-transfer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31064-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>My ability to analyze a capture is limited. So, any help is appreciated.</p><p>I have a server that is trying to send a .m4v (video) file to an IPhone. It looks to me, like the phone is resetting the connection before the transfer takes place. If that is true, the question is why is it resetting?</p><p>Here is a copy of my capture file.<br />
<img src="https://osqa-ask.wireshark.org/upfiles/IPhone_m4v_1.png" alt="capture" /></p><p>My Nexus 5 receives the same file without any issues. I hope that the trimmed down capture image contains enough information. I had to trim it down to fit in this message.</p><p>Thanks,</p><p>Dana</p></div><div id="question-tags" class="tags-container tags">reset iphone tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '14, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/4424348054ffcb9cc312dddb9ca08cf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danabaillie&#39;s gravatar image" /><p>danabaillie<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danabaillie has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-31064" class="comments-container"></div><div id="comment-tools-31064" class="comment-tools"></div><div class="clear"></div><div id="comment-31064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31074"></span>

<div id="answer-container-31074" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31074-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The client software decided to close the socket and terminate the transfer prematurely after having read (and inspected) the first 1658 (FIN's ACK#-1) bytes of the m4v file. So you need to ask this question to the client software community (itunes, safari, etc...) to get a more appropriate answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '14, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Mar '14, 01:55</p></div></div><div id="comments-container-31074" class="comments-container"><span id="31075"></span><div id="comment-31075" class="comment"><div id="post-31075-score" class="comment-score"></div><div class="comment-text"><p>Ok. I disabled "Allow subdissector to reassemble TCP streams" and reran the attempt to open the .m4v file in my IPhone. I realized later that I could have used my existing capture and simply disable " "Allow subdissector to reassemble TCP streams" without recreating a capture. I learn slowly.</p><p>Anyway, it now does show the "200 OK". Not seeing that was adding confusion for me.</p><p>I read your response, mrEEde. I suspect that what you said is probably all that the capture file can tell us, so I will reach out to some IOS (Apple) sites.<br />
</p><p>Here is the updated capture file, just in case there is something new or missed.</p><p><a href="https://osqa-ask.wireshark.org/upfiles/IPhone_m4v_2.png">capture file</a></p></div><div id="comment-31075-info" class="comment-info"><span class="comment-age">(22 Mar '14, 08:11)</span> danabaillie</div></div><span id="31089"></span><div id="comment-31089" class="comment"><div id="post-31089-score" class="comment-score">1</div><div class="comment-text"><p>@mrEEde The client received 1658 bytes before closing the connection.</p></div><div id="comment-31089-info" class="comment-info"><span class="comment-age">(22 Mar '14, 17:12)</span> Roland</div></div></div><div id="comment-tools-31074" class="comment-tools"></div><div class="clear"></div><div id="comment-31074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31070"></span>

<div id="answer-container-31070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31070-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>205 is the client, 199 the server. Client is requesting the .m4v file in packet 14.</p><p>Please disable "Allow subdissector to reassemble TCP streams" to see if you get a 200 OK for the request.</p><p>Client closes the connection in packet 20. The RST in packet 23 is because the port is already closed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '14, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span> </br></p></div></div><div id="comments-container-31070" class="comments-container"><span id="31071"></span><div id="comment-31071" class="comment"><div id="post-31071-score" class="comment-score"></div><div class="comment-text"><p>Ahhh. Thanks Roland. I know for a fact that the server is sending a 200 OK, but not seeing it in the capture had me thinking that it was shut down prematurely for some reason. I do as you suggest and let you know what I get.<br />
</p><p>Maybe, it's not as bad as I thought.</p><p>Thanks again.</p><p>Dana</p></div><div id="comment-31071-info" class="comment-info"><span class="comment-age">(21 Mar '14, 15:56)</span> danabaillie</div></div></div><div id="comment-tools-31070" class="comment-tools"></div><div class="clear"></div><div id="comment-31070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

