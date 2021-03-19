+++
type = "question"
title = "use tshark with SSLKEYLOGFILE to get decrypted tls data"
description = '''Hello, i am trying to use tshark from the command line to get unecrypted TLS packets. I want to do this with the SSLKEYLOGFILE of session keys like you would do through the wireshark interface. Does anyone know how to do this? Thanks'''
date = "2017-05-22T10:05:00Z"
lastmod = "2017-05-22T10:33:00Z"
weight = 61543
keywords = [ "tls", "ssl", "tshark" ]
aliases = [ "/questions/61543" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [use tshark with SSLKEYLOGFILE to get decrypted tls data](/questions/61543/use-tshark-with-sslkeylogfile-to-get-decrypted-tls-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61543-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i am trying to use tshark from the command line to get unecrypted TLS packets. I want to do this with the SSLKEYLOGFILE of session keys like you would do through the wireshark interface. Does anyone know how to do this? Thanks</p></div><div id="question-tags" class="tags-container tags">tls ssl tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '17, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/065a89fea561f43cd2ea6afb99d8275b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogidmt&#39;s gravatar image" /><p>yogidmt<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogidmt has no accepted answers">0%</span></p></div></div><div id="comments-container-61543" class="comments-container"></div><div id="comment-tools-61543" class="comment-tools"></div><div class="clear"></div><div id="comment-61543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61544"></span>

<div id="answer-container-61544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61544-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the <a href="https://wiki.wireshark.org/SSL">SSL page</a> on the Wiki, the tshark commands you require are shown there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '17, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61544" class="comments-container"><span id="61545"></span><div id="comment-61545" class="comment"><div id="post-61545-score" class="comment-score"></div><div class="comment-text"><p>Any chance you could provide some more info? I read through that a few times and i'm still kind of confused as to what i should do. I have an SSLKEYLOGFILE with session keys, not an RSA private key.</p></div><div id="comment-61545-info" class="comment-info"><span class="comment-age">(22 May '17, 11:48)</span> yogidmt</div></div><span id="61561"></span><div id="comment-61561" class="comment"><div id="post-61561-score" class="comment-score">1</div><div class="comment-text"><p>So what have you tried?</p><p>Use <code>-o ssl.key_logfile:path/to/keys.log</code> to specify the key log file instead of the <code>ssl.keys_list</code> element.</p></div><div id="comment-61561-info" class="comment-info"><span class="comment-age">(22 May '17, 15:00)</span> grahamb ♦</div></div><span id="61587"></span><div id="comment-61587" class="comment"><div id="post-61587-score" class="comment-score"></div><div class="comment-text"><p>I tried this... tshark -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list: 104.123.15.136,4443,data,C:/users/ben/desktop/sslkeylog.log" -i eth0 -Y "tcp.port == 4443"</p><p>It's saying it can't load key and eth0 isn't a valid interface. Also i assume the ip/port information is for the server sending me data? not the port on my machine data is coming in on?</p></div><div id="comment-61587-info" class="comment-info"><span class="comment-age">(23 May '17, 17:53)</span> yogidmt</div></div><span id="61589"></span><div id="comment-61589" class="comment"><div id="post-61589-score" class="comment-score"></div><div class="comment-text"><p>Looks like you're trying to live-decode traffic by specifying an interface - decoding SSL with a keylogfile only works on recorded traffic (pcap) as far as I know. Both keylog and pcap must be containing the same session details, and then you can read and decoded the pcap using the keylog file.</p></div><div id="comment-61589-info" class="comment-info"><span class="comment-age">(24 May '17, 01:42)</span> Jasper ♦♦</div></div><span id="61592"></span><div id="comment-61592" class="comment"><div id="post-61592-score" class="comment-score"></div><div class="comment-text"><p>I mean i'd prefer to record live traffic, what would be the difference between recording it and decoding as opposed to recording it directly?</p></div><div id="comment-61592-info" class="comment-info"><span class="comment-age">(24 May '17, 05:33)</span> yogidmt</div></div><span id="61595"></span><div id="comment-61595" class="comment not_top_scorer"><div id="post-61595-score" class="comment-score"></div><div class="comment-text"><p>The live packets may come in before the key log file is updated. Wireshark running live can't "go back" in the incoming packet stream.</p></div><div id="comment-61595-info" class="comment-info"><span class="comment-age">(24 May '17, 05:49)</span> grahamb ♦</div></div><span id="61597"></span><div id="comment-61597" class="comment not_top_scorer"><div id="post-61597-score" class="comment-score"></div><div class="comment-text"><p>Is there any way to do what i'm trying to do then? Read incoming TLS packets in somewhat of real time?</p></div><div id="comment-61597-info" class="comment-info"><span class="comment-age">(24 May '17, 06:13)</span> yogidmt</div></div><span id="61599"></span><div id="comment-61599" class="comment not_top_scorer"><div id="post-61599-score" class="comment-score"></div><div class="comment-text"><p>Maybe use a MitM approach e.g. Fiddler?</p></div><div id="comment-61599-info" class="comment-info"><span class="comment-age">(24 May '17, 06:18)</span> grahamb ♦</div></div><span id="61601"></span><div id="comment-61601" class="comment not_top_scorer"><div id="post-61601-score" class="comment-score"></div><div class="comment-text"><p>I am the client though, i wouldn't be trying to intercept packets i just want to read the one's that come to me.</p></div><div id="comment-61601-info" class="comment-info"><span class="comment-age">(24 May '17, 07:03)</span> yogidmt</div></div><span id="61602"></span><div id="comment-61602" class="comment not_top_scorer"><div id="post-61602-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.telerik.com/download/fiddler">Fiddler</a> allows that (on Windows). What OS are you using?</p></div><div id="comment-61602-info" class="comment-info"><span class="comment-age">(24 May '17, 07:45)</span> grahamb ♦</div></div><span id="61608"></span><div id="comment-61608" class="comment not_top_scorer"><div id="post-61608-score" class="comment-score"></div><div class="comment-text"><p>I'll have to check that out. I'm on Win10</p></div><div id="comment-61608-info" class="comment-info"><span class="comment-age">(24 May '17, 11:18)</span> yogidmt</div></div></div><div id="comment-tools-61544" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-61544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

