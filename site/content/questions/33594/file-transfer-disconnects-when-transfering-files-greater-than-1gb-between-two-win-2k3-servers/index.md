+++
type = "question"
title = "File transfer disconnects when transfering files greater than 1Gb between two Win 2k3 servers"
description = '''Hello Wireshark Gurus, I am having a problem where file transfers between two windows server machines are failing mid way sometimes when the file exceeds 1/2Gb in size.  I have attached a link that points to the pcap: https://dl.dropboxusercontent.com/u/11187256/172.26.44.18.pcapng source is 192.168...'''
date = "2014-06-09T14:02:00Z"
lastmod = "2014-06-09T14:31:00Z"
weight = 33594
keywords = [ "windows", "transfer", "server", "disconnect", "error" ]
aliases = [ "/questions/33594" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [File transfer disconnects when transfering files greater than 1Gb between two Win 2k3 servers](/questions/33594/file-transfer-disconnects-when-transfering-files-greater-than-1gb-between-two-win-2k3-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33594-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Wireshark Gurus,</p><p>I am having a problem where file transfers between two windows server machines are failing mid way sometimes when the file exceeds 1/2Gb in size.</p><p>I have attached a link that points to the pcap:</p><p><a href="https://dl.dropboxusercontent.com/u/11187256/172.26.44.18.pcapng">https://dl.dropboxusercontent.com/u/11187256/172.26.44.18.pcapng</a></p><p>source is 192.168.141.131 dst is 172.26.44.18</p><p>I am seeing errors at the end of the file and trying to explain to Microsoft has gotten me no where. Can you please take a look and assist if you can.</p></div><div id="question-tags" class="tags-container tags">windows transfer server disconnect error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '14, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/621f3ca32033b5d34582bb03a6c67bad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sigma55&#39;s gravatar image" /><p>Sigma55<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sigma55 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '14, 04:47</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33594" class="comments-container"></div><div id="comment-tools-33594" class="comment-tools"></div><div class="clear"></div><div id="comment-33594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33595"></span>

<div id="answer-container-33595" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33595-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks to me like 192.168.141.131 stops sending data in the middle of a 61440 byte sized data chunk. Since the other PC with IP 172.26.44.18 does not receive any further data it resets the session in packet 282192, after close to 30 seconds of "silence" - probably a timeout.</p><p>Next step: capture next to 192.168.141.131 to find out if it really stops sending or if the packets just do not make it through anymore.</p><p>Two tips here:</p><ol><li>Capturing on one of the affected systems isn't optimal, see <a href="http://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">http://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a></li><li>Putting 300+ MB file up for download only makes sense if you really need all the payload. In your case you could probably greatly reduce the size by only capturing the first 256 bytes of each packet, which should include all SMB headers. There is an option in the capture settings where you can limit how much bytes are kept for each packet.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '14, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33595" class="comments-container"><span id="33617"></span><div id="comment-33617" class="comment"><div id="post-33617-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick response.</p><p>I have read the article and it sheds some light on why you shouldn't do it. Should I instead to the capture on a system connected to the same network off a switchport?</p><p>I will also look into limiting the size of the capture as you mentioned.</p><p>Feedback to follow.</p><p>Joe</p></div><div id="comment-33617-info" class="comment-info"><span class="comment-age">(10 Jun '14, 08:01)</span> Sigma55</div></div><span id="33637"></span><div id="comment-33637" class="comment"><div id="post-33637-score" class="comment-score"></div><div class="comment-text"><p>Yes, capturing on an additional system connected to a SPAN port would help avoiding those problems. Of course that requires that the switch can do SPAN ports.</p></div><div id="comment-33637-info" class="comment-info"><span class="comment-age">(11 Jun '14, 00:34)</span> Jasper ♦♦</div></div><span id="33725"></span><div id="comment-33725" class="comment"><div id="post-33725-score" class="comment-score"></div><div class="comment-text"><p>OK. did some more testing. turns out, that server is the only server that has problems copying the files. All the other servers can copy the files without error on the same network. I will use the SPAN port to monitor further but it seems to be a software problem.</p><p>Thank you very much for your time sir.</p></div><div id="comment-33725-info" class="comment-info"><span class="comment-age">(12 Jun '14, 10:27)</span> Sigma55</div></div></div><div id="comment-tools-33595" class="comment-tools"></div><div class="clear"></div><div id="comment-33595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

