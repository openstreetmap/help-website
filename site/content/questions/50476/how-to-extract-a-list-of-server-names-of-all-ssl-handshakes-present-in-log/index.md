+++
type = "question"
title = "How to extract a list of server names of all SSL Handshakes present in log?"
description = '''Hi! I have a pcap file with requests over SSL. Under:  SSL TLSv1.2 Record Layer: Handshake Protocol: Client Hello Handshake Protocol: Client Hello Extension: server_name Server Name Indication extension Server Name  I find the host name of the involved server. I would like to extract all values of t...'''
date = "2016-02-24T09:47:00Z"
lastmod = "2016-02-24T11:14:00Z"
weight = 50476
keywords = [ "wireshark" ]
aliases = [ "/questions/50476" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to extract a list of server names of all SSL Handshakes present in log?](/questions/50476/how-to-extract-a-list-of-server-names-of-all-ssl-handshakes-present-in-log)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50476-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I have a pcap file with requests over SSL.</p><p>Under:</p><ol><li>SSL</li><li>TLSv1.2 Record Layer: Handshake Protocol: Client Hello</li><li>Handshake Protocol: Client Hello</li><li>Extension: server_name</li><li>Server Name Indication extension</li><li>Server Name</li></ol><p>I find the host name of the involved server.</p><p>I would like to extract all values of this type into a list.</p><p>Do I have to resort to a programmatic solution using an external library with Python f.x. or is there a built in feature which would allow me to accomplish that or something equivalent?</p><p>Kind Regards</p><p>Raffael</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '16, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/c44e61d34981ed01ab4bc25c3df52fc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raffael1984&#39;s gravatar image" /><p>Raffael1984<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raffael1984 has no accepted answers">0%</span></p></div></div><div id="comments-container-50476" class="comments-container"></div><div id="comment-tools-50476" class="comment-tools"></div><div class="clear"></div><div id="comment-50476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50481"></span>

<div id="answer-container-50481" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50481-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use tshark from the command line, specificying that you only want the server name field, e.g.</p><pre><code>tshark -r path\to\your\capture -T fields -e ssl.handshake.extensions_server_name -R ssl.handshake.extensions_server_name</code></pre><p>Depending on your OS, you may need to provide the path to tshark and use "/" as the path separator.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '16, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50481" class="comments-container"></div><div id="comment-tools-50481" class="comment-tools"></div><div class="clear"></div><div id="comment-50481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

