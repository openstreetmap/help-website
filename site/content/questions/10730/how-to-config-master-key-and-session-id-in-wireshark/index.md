+++
type = "question"
title = "how to config Master-key and Session-ID in wireshark"
description = '''i read the &quot;Follow SSL stream using Master-key and Session-ID&quot;(http://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id) but i don&#x27;t knew how to config in wireshark, Edit-&amp;gt; preference-&amp;gt;protocols-&amp;gt;ssl, but where to set RSA Session-ID:xxxx Master-Key:xxxx,????'''
date = "2012-05-07T06:55:00Z"
lastmod = "2012-05-07T07:06:00Z"
weight = 10730
keywords = [ "session-id", "ssl", "master-key" ]
aliases = [ "/questions/10730" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to config Master-key and Session-ID in wireshark](/questions/10730/how-to-config-master-key-and-session-id-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10730-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i read the "Follow SSL stream using Master-key and Session-ID"(<a href="http://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id)">http://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id)</a> but i don't knew how to config in wireshark, Edit-&gt; preference-&gt;protocols-&gt;ssl, but where to set RSA Session-ID:xxxx Master-Key:xxxx,????</p></div><div id="question-tags" class="tags-container tags">session-id ssl master-key</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/ecce11d45d4a07d3a4e0f745af860fb0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="endofkok3&#39;s gravatar image" /><p>endofkok3<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="endofkok3 has no accepted answers">0%</span></p></div></div><div id="comments-container-10730" class="comments-container"></div><div id="comment-tools-10730" class="comment-tools"></div><div class="clear"></div><div id="comment-10730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10732"></span>

<div id="answer-container-10732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10732-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Within the SSL preferences, there should be a text box called</p><blockquote><p><code>(Pre)-Master-Secret log filename</code></p></blockquote><p>There you define the name of the file that contains the required information.</p><p>Sample, based on data from the link you posted:</p><blockquote><p><code>c:\rsa.log</code><br />
<code>RSA Session-ID:B5AEB800F43F96A9BAD007A5D26423E43479B904166FA72A4789DEA15A830E26</code><br />
<code>Master-Key:454AD3030F0AE8234508DF959EF533675E225BBB388EE5F80A20A007BAB63E1ABB972F39401796FB02F27AF95AB083A4</code></p></blockquote><p>BTW: If the text box is not there, you're probably using an older version of wireshark. In that case, please upgrade to the lastest version.</p><p>Please also check the SSL Decryption Wiki, for a different way to decrypt SSL, by using the RSA secret key of the server.</p><blockquote><p><strong><code>http://wiki.wireshark.org/SSL</code></strong></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 May '12, 07:08</p></div></div><div id="comments-container-10732" class="comments-container"><span id="10778"></span><div id="comment-10778" class="comment"><div id="post-10778-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, but now, I found another two questions: 1.I have to access ssl server through and http proxy, but openssl s_client can not support proxy. 2.I found that every time I run the openssl s_client command I got the different Session-Id and Master-Key, I don't know how to config them in rsa.log file.</p></div><div id="comment-10778-info" class="comment-info"><span class="comment-age">(08 May '12, 05:35)</span> endofkok3</div></div><span id="10779"></span><div id="comment-10779" class="comment"><div id="post-10779-score" class="comment-score"></div><div class="comment-text"><p>1.) openssl does not support a proxy (to my knowledge). Maybe proxytunnel can help you: <strong><a href="http://proxytunnel.sourceforge.net/intro.php">http://proxytunnel.sourceforge.net/intro.php</a></strong></p><p><strong>EDIT3</strong>: Additionally there is a patch available for proxy support in openssl: <strong><a href="http://goo.gl/Ea0LB">http://goo.gl/Ea0LB</a></strong></p><p>2.) As it's a new SSL session, you will get a new Session-ID. I'll have to check if one can use multiple entries in the session log.</p><p><strong>EDIT</strong>: According to the SSL debug log, Wireshark reads all line in that file and tries to find a matching Session-ID.</p><p><strong>EDIT2</strong>: Just tested it with serveral Session-IDs in one file. It works.</p></div><div id="comment-10779-info" class="comment-info"><span class="comment-age">(08 May '12, 06:23)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-10732" class="comment-tools"></div><div class="clear"></div><div id="comment-10732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

