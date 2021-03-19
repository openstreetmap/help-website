+++
type = "question"
title = "Anyone know what Cspuni is?"
description = '''Hi I am trying to send files with FTPS (SSL/TLS) but it&#x27;s not working that well. When I do a wireshark trace I see that source port are 2806 (cspuni)  1.1.1.2 3.3.3.4 TCP cspuni &amp;gt; ftps [SYN] Seq=0 Win=65535 Len=0 MSS=1460 Source port: cspuni (2806) Destination port: ftps (990) I havent heard of c...'''
date = "2012-08-23T01:36:00Z"
lastmod = "2012-08-23T01:50:00Z"
weight = 13837
keywords = [ "cspuni", "wireshark" ]
aliases = [ "/questions/13837" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Anyone know what Cspuni is?](/questions/13837/anyone-know-what-cspuni-is)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13837-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am trying to send files with FTPS (SSL/TLS) but it's not working that well. When I do a wireshark trace I see that source port are 2806 (cspuni) 1.1.1.2 3.3.3.4 TCP cspuni &gt; ftps [SYN] Seq=0 Win=65535 Len=0 MSS=1460 Source port: cspuni (2806) Destination port: ftps (990)</p><p>I havent heard of cspuni before, anyone have an idea what that is. Or do this appear when something is wrong, for example the certificate doesn't match?</p><p>/ P</p></div><div id="question-tags" class="tags-container tags">cspuni wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '12, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/c5bca1ef893b080de1d75bef26c2d22f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ph13&#39;s gravatar image" /><p>ph13<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ph13 has no accepted answers">0%</span></p></div></div><div id="comments-container-13837" class="comments-container"></div><div id="comment-tools-13837" class="comment-tools"></div><div class="clear"></div><div id="comment-13837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13839"></span>

<div id="answer-container-13839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13839-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know what it is, but you don't have to worry about it. Wireshark tries to lookup well known ports in the services table, for example to be able to replace port 80 with "http". Unfortunately, Wireshark also does this for epheremal ports (which are used by clients), confusing lots of users with protocol names they don't even use.</p><p>As you may know clients use ephemeral ports for creating each new connection. For example Windows XP starts at port 1025 and goes up to 5000, only to start at 1025 again. Wireshark replaces these ports just like it does with server ports, and you'll see lots of funny protocol names. The list of protocols can be found in the Wireshark installation directory in a file called "services". In there you'll see that cspuni is a protocol using port 2806, which is a typical ephemeral port of a client.</p><p>You can disable the replacement of ports by disabling it at "View" -&gt; "Name Resolution" -&gt; "Transport Layer" (which would be temporary), or completely in the preferences dialog at the name resolution pane. That way Wireshark will show port number instead of protocol names.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '12, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13839" class="comments-container"><span id="13840"></span><div id="comment-13840" class="comment"><div id="post-13840-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I was just confused when I saw that in Wireshark, thought it had something to do with the communication problem I have, that it used that port then.</p></div><div id="comment-13840-info" class="comment-info"><span class="comment-age">(23 Aug '12, 02:34)</span> ph13</div></div></div><div id="comment-tools-13839" class="comment-tools"></div><div class="clear"></div><div id="comment-13839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

