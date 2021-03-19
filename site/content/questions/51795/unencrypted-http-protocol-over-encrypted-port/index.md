+++
type = "question"
title = "Unencrypted http protocol over encrypted port"
description = '''So I just started using Wireshark and started the capture on my own computer. A few packets that catch my attention include http protocol. It seems to me as if my computer is attempting to logon somewhere with my email address but fails. Below is the TCP Stream and I replaced my email address with x...'''
date = "2016-04-19T09:41:00Z"
lastmod = "2016-04-19T13:25:00Z"
weight = 51795
keywords = [ "unencrypted", "encrypted" ]
aliases = [ "/questions/51795" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unencrypted http protocol over encrypted port](/questions/51795/unencrypted-http-protocol-over-encrypted-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51795-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I just started using Wireshark and started the capture on my own computer. A few packets that catch my attention include http protocol. It seems to me as if my computer is attempting to logon somewhere with my email address but fails. Below is the TCP Stream and I replaced my email address with x's. If anybody as any idea on how I can identify what is the source of this on my computer, I would very much appreciate it.</p><p>GET /sub?cname=xxx%40xxx.com_browsers&amp;seq=1&amp;st=6114460300580000 HTTP/1.1 Host: 72.26.124.29:443 Connection: Close</p><p>HTTP/1.1 200 OK Server: evsnotify Content-Type: text/javascript; charset=utf-8 Date: Tue, 19 Apr 2016 14:50:22 GMT Content-Length: 37 Connection: close</p><p>{"type":"user authentication failed"}</p></div><div id="question-tags" class="tags-container tags">unencrypted encrypted</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '16, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/3ef9c4bca7e33511d7533cba1e0ca838?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chuyrod&#39;s gravatar image" /><p>chuyrod<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chuyrod has no accepted answers">0%</span></p></div></div><div id="comments-container-51795" class="comments-container"></div><div id="comment-tools-51795" class="comment-tools"></div><div class="clear"></div><div id="comment-51795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51798"></span>

<div id="answer-container-51798" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51798-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If anybody as any idea on how I can identify what is the source of this on my computer, I would very much appreciate it.</p></blockquote><p>Run Microsoft Network Monitor. They abandoned it, but it should be downloadable. It will show you the PID of the process that sends certain data.´</p><p>BTW: That behavior looks strange!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-51798" class="comments-container"><span id="51823"></span><div id="comment-51823" class="comment"><div id="post-51823-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tip. I opened Resource Monitor and found under the Network Activity section that the id_service.exe from iDrive has a connection to the ip address above. Now i know what process is triggering this traffice, but I'm still confused because I would think the ip address would be iDrive's ip address. I also did another capture and still get the same results even after logging into the idrive website for my account. I'll keep digging.</p><p>Thanks again for the tip.</p><p>Jesse</p></div><div id="comment-51823-info" class="comment-info"><span class="comment-age">(20 Apr '16, 08:17)</span> chuyrod</div></div><span id="51824"></span><div id="comment-51824" class="comment"><div id="post-51824-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment. Please follow-up with comments instead of answers (see FAQ).</p><blockquote><p>but I'm still confused because I would think the ip address would be iDrive's ip address.</p></blockquote><p>What should confuse you even more is the fact that they send your data over an unencrypted connection. Strange enough that they are using the HTTPS port (443). Who knows what else they send (password, backup data) in other <strong>unencrypted</strong> connections?</p><p>I suggest to contact their support and ask them what the heck this is all about ;-)</p><p>You can direct them to your post. 'Publicity' sometimes helps to speed up things :-)</p><p>Regards<br />
Kurt</p></div><div id="comment-51824-info" class="comment-info"><span class="comment-age">(20 Apr '16, 09:14)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-51798" class="comment-tools"></div><div class="clear"></div><div id="comment-51798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

