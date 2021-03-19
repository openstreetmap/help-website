+++
type = "question"
title = "I have a pcap file and I&#x27;m trying to find out the client system?"
description = '''Hello,   I have a pcap file and I&#x27;m trying to figure out a way to determine the operating system used by the client system? I think from the data it is a Dell machine running a Microsoft operation system but I&#x27;m not sure which(2000,XP, Vista, Window 7, etc). Also, how do I determine the client’s IP ...'''
date = "2011-01-29T09:57:00Z"
lastmod = "2011-02-01T07:28:00Z"
weight = 2009
keywords = [ "machine", "os", "client", "pcap", "file" ]
aliases = [ "/questions/2009" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I have a pcap file and I'm trying to find out the client system?](/questions/2009/i-have-a-pcap-file-and-im-trying-to-find-out-the-client-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a pcap file and I'm trying to figure out a way to determine the operating system used by the client system? I think from the data it is a Dell machine running a Microsoft operation system but I'm not sure which(2000,XP, Vista, Window 7, etc).</p><p>Also, how do I determine the client’s IP address and MAC address?</p></div><div id="question-tags" class="tags-container tags">machine os client pcap file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '11, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/8d0620f05fbf6a443b3e2c560c26e779?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gamer5k&#39;s gravatar image" /><p>gamer5k<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gamer5k has no accepted answers">0%</span></p></div></div><div id="comments-container-2009" class="comments-container"></div><div id="comment-tools-2009" class="comment-tools"></div><div class="clear"></div><div id="comment-2009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2019"></span>

<div id="answer-container-2019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2019-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try to find an HTTP request if you can, those usually have OS information fields in their headers like this:</p><p><code>Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)</code></p><p>This one would be from a Windows XP machine, because "Windows NT 5.1" is Windows XP, while "5.0" would be Windows 2000, "6.0" is Vista, "6.1" is Windows 7.</p><p>Regarding client IP and MAC: this might be a bit more difficult to determine depending on where the capture was taken - you might not be able to see the MAC address at all if it hidden behind a router. Usually the client is the one where the connection is established from, so look for which machine has the most SYN packets send out by filtering on <code>tcp.flags=0x02</code> and then looking at Statistics/Conversations/TCP. One of them might be the client you're looking for, often the one with the most connections.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '11, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2019" class="comments-container"><span id="28518"></span><div id="comment-28518" class="comment"><div id="post-28518-score" class="comment-score"></div><div class="comment-text"><p>Hello, i did this and now i have 1820 TCP connections. How can i filter these?</p><p>Or should i open them one for one and examine?</p></div><div id="comment-28518-info" class="comment-info"><span class="comment-age">(01 Jan '14, 23:20)</span> kweerd63</div></div></div><div id="comment-tools-2019" class="comment-tools"></div><div class="clear"></div><div id="comment-2019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2069"></span>

<div id="answer-container-2069" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2069-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try to find a smb session setup request, use filter: <code>smb.cmd == 0x73</code><br />
In the smb session request you'll find the field Native OS: <code>smb.native_os</code><br />
more details found on msdn <a href="http://msdn.microsoft.com/en-us/library/ff469879(v=PROT.13).aspx">Session Setup andX</a>, <a href="http://msdn.microsoft.com/en-us/library/ecd51ae2-478c-455b-8669-254b74208d3b(v=PROT.13)#id45">Client Details</a><br />
This only valid with smb/cifs</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '11, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/0dcd1df1e0bf3e031f35cf0571297889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="melsvizzer&#39;s gravatar image" /><p>melsvizzer<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="melsvizzer has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-2069" class="comments-container"><span id="51460"></span><div id="comment-51460" class="comment"><div id="post-51460-score" class="comment-score"></div><div class="comment-text"><p>Thank you Melsvizzer. You save my time :)</p></div><div id="comment-51460-info" class="comment-info"><span class="comment-age">(07 Apr '16, 03:26)</span> ho minh dat</div></div></div><div id="comment-tools-2069" class="comment-tools"></div><div class="clear"></div><div id="comment-2069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

