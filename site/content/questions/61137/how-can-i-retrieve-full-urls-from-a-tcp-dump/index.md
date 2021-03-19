+++
type = "question"
title = "How can I retrieve (full) urls from a tcp dump?"
description = '''Dear all I want to check the URLs, which are opened from inside my private network in order to check if anything is requested that shouldn&#x27;t be. As some of the URLs seem to be opened via https, tcpdump comes afaik to its limits. A google search led me to WireShark and the recommendation to analyze t...'''
date = "2017-05-01T07:05:00Z"
lastmod = "2017-05-01T10:53:00Z"
weight = 61137
keywords = [ "url", "name-resolving", "host_name", "https", "ssl" ]
aliases = [ "/questions/61137" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I retrieve (full) urls from a tcp dump?](/questions/61137/how-can-i-retrieve-full-urls-from-a-tcp-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61137-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all</p><p>I want to check the URLs, which are opened from inside my private network in order to check if anything is requested that shouldn't be. As some of the URLs seem to be opened via https, tcpdump comes afaik to its limits. A google search led me to WireShark and the recommendation to analyze the dump file.</p><p>However, when I open that file I get some information about packets, including source and destination IPs. For whatever reason, resolving the host names does not work. I already enabled external name resolving, but nothing changes. Even if I would get host names, I am not sure that this would include the specific URLs.</p><p>Could you be so kind and help me out? I am not that much into these technical details, so that I do not understand every further recommendation from the net.</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">url name-resolving host_name https ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '17, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/bbeb1f4bb639ba728273f2928cc9c324?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HabakukTibatong&#39;s gravatar image" /><p>HabakukTibatong<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HabakukTibatong has no accepted answers">0%</span></p></div></div><div id="comments-container-61137" class="comments-container"></div><div id="comment-tools-61137" class="comment-tools"></div><div class="clear"></div><div id="comment-61137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61139"></span>

<div id="answer-container-61139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61139-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unless you have the pre-master session key you won't be able to decrypt HTTPS traffic. Therefore to getting the URLs of HTTPS traffic will not be feasible for you.</p><p>To get the hosts of HTTPS URLs you can use the servername extension of the TLS handshake (display filter: <code>ssl.handshake.extensions_server_name</code>).</p><p>For HTTP traffic to get the full URL use the display filter <code>http.request.full_uri</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '17, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-61139" class="comments-container"><span id="61140"></span><div id="comment-61140" class="comment"><div id="post-61140-score" class="comment-score"></div><div class="comment-text"><p>Thanks. About that pre-master session key: Can I get that when I have direct access to the device on my network, which is establishing a https connection? If yes, is this some kine of stable key that I can just export?</p><p>About http.request.full_uri: I do not really understand how to use that, as you said before that I won't be able to get the URLs.</p><p>Either way, thanks for your reply.</p></div><div id="comment-61140-info" class="comment-info"><span class="comment-age">(01 May '17, 11:38)</span> HabakukTibatong</div></div><span id="61141"></span><div id="comment-61141" class="comment"><div id="post-61141-score" class="comment-score"></div><div class="comment-text"><p>For HTTP (unencrypted) traffic <code>http.request.full_uri</code> lists the value of a HTTP request.</p><p>To the get the pre-master key, keyword to search for is 'SSLKEYLOGFILE' (e.g. here or on Google).</p></div><div id="comment-61141-info" class="comment-info"><span class="comment-age">(01 May '17, 12:02)</span> Uli</div></div><span id="61164"></span><div id="comment-61164" class="comment"><div id="post-61164-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I will try that.</p></div><div id="comment-61164-info" class="comment-info"><span class="comment-age">(02 May '17, 09:44)</span> HabakukTibatong</div></div></div><div id="comment-tools-61139" class="comment-tools"></div><div class="clear"></div><div id="comment-61139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

