+++
type = "question"
title = "SSL Dissector - TLSv1 versus SSL"
description = '''I have two separate PCAP files. Both of these PCAP files contain a ClientHello of protocol TLS version 1.0. How come one of the captures says the ClientHello packet is &quot;SSL&quot; protocol, and the other capture says the ClientHello is &quot;TLSv1&quot; protocol?'''
date = "2012-11-16T16:40:00Z"
lastmod = "2012-11-19T11:12:00Z"
weight = 15995
keywords = [ "tls", "ssl" ]
aliases = [ "/questions/15995" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Dissector - TLSv1 versus SSL](/questions/15995/ssl-dissector-tlsv1-versus-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15995-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two separate PCAP files. Both of these PCAP files contain a ClientHello of protocol TLS version 1.0.</p><p>How come one of the captures says the ClientHello packet is "SSL" protocol, and the other capture says the ClientHello is "TLSv1" protocol?</p></div><div id="question-tags" class="tags-container tags">tls ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '12, 16:40</strong></p><img src="https://secure.gravatar.com/avatar/3eec6f1f3686c586936115d9ba692bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shauer&#39;s gravatar image" /><p>shauer<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shauer has no accepted answers">0%</span></p></div></div><div id="comments-container-15995" class="comments-container"><span id="16000"></span><div id="comment-16000" class="comment"><div id="post-16000-score" class="comment-score"></div><div class="comment-text"><p>can you post those two conversations on <a href="http://cloudshark.org">cloudshark.org</a> (or similar)?</p></div><div id="comment-16000-info" class="comment-info"><span class="comment-age">(17 Nov '12, 14:07)</span> Kurt Knochner ♦</div></div><span id="16064"></span><div id="comment-16064" class="comment"><div id="post-16064-score" class="comment-score"></div><div class="comment-text"><p>Here are the two captures.</p><p>Shows up as "TLSv1": <a href="http://cloudshark.org/captures/a5f13d33adcd">http://cloudshark.org/captures/a5f13d33adcd</a></p><p>Shows up as "SSL": <a href="http://cloudshark.org/captures/40569e71513">http://cloudshark.org/captures/40569e71513</a></p></div><div id="comment-16064-info" class="comment-info"><span class="comment-age">(19 Nov '12, 09:48)</span> shauer</div></div><span id="16066"></span><div id="comment-16066" class="comment"><div id="post-16066-score" class="comment-score"></div><div class="comment-text"><p>I see in the uploaded files that both PCAP dumps show the ClientHello as "SSL". This is not what I am seeing in the desktop version of Wireshark.</p></div><div id="comment-16066-info" class="comment-info"><span class="comment-age">(19 Nov '12, 09:54)</span> shauer</div></div><span id="16067"></span><div id="comment-16067" class="comment"><div id="post-16067-score" class="comment-score"></div><div class="comment-text"><p>Desktop version is 1.8.3 (SVN 45256). Desktop is Windows 7 x64.</p></div><div id="comment-16067-info" class="comment-info"><span class="comment-age">(19 Nov '12, 09:58)</span> shauer</div></div><span id="16076"></span><div id="comment-16076" class="comment"><div id="post-16076-score" class="comment-score"></div><div class="comment-text"><p>the link for the second capture file does not work.</p><p>UPDATE: I found it myself: <a href="http://cloudshark.org/captures/40569e715137">http://cloudshark.org/captures/40569e715137</a></p></div><div id="comment-16076-info" class="comment-info"><span class="comment-age">(19 Nov '12, 11:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15995" class="comment-tools"></div><div class="clear"></div><div id="comment-15995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16078"></span>

<div id="answer-container-16078" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16078-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at both capture files, you will see, that the one marked as TLSv1 contains ciphers with Diffie Hellman Key Exchange (<em><em>DHE</em></em>). Furthermore there is an Extension available:</p><blockquote><p><code>Extension: SessionTicket TLS</code><br />
</p></blockquote><p>Wireshark starts SSL/TLS dissection by setting the Protocol field to "SSL". Later in the process it will update it, if there are more/other signs regarding the SSL/TLS version.</p><p>packet-ssl.c:</p><p><code>     / Initialize the protocol column; we'll set it later when we      * figure out what flavor of SSL it is (assuming we don't      * throw an exception before we get the chance to do so). /     col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, "SSL");</code></p><p>I have not checked your sample in detail in the code, but I believe the TLS Extension (and possibly also the DHE ciphers) lead to an update from <strong>SSL</strong> to <strong>TLSv1</strong> in the protocol field.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '12, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '12, 11:13</p></div></div><div id="comments-container-16078" class="comments-container"></div><div id="comment-tools-16078" class="comment-tools"></div><div class="clear"></div><div id="comment-16078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

