+++
type = "question"
title = "How decode a gzip url"
description = '''Hi, I used wireshark to capture some traffic between a closed-program and a server. The program request some URL with this format: GET /m_back/page.php?a5bXBpYyBHYW1lcy0mYXBwdmVyc2lvxNzImcm5kdmFsPTEzNDQ4NTM2ODE= HTTP/1.1 Host: xxx.xxx.xxx.xxx Connection: Keep-Alive User-Agent: My User Agent Accept-E...'''
date = "2012-08-14T11:03:00Z"
lastmod = "2012-08-14T11:45:00Z"
weight = 13622
keywords = [ "gzip", "url", "http" ]
aliases = [ "/questions/13622" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How decode a gzip url](/questions/13622/how-decode-a-gzip-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13622-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I used wireshark to capture some traffic between a closed-program and a server.</p><p>The program request some URL with this format:</p><p><strong>GET /m_back/page.php?a5bXBpYyBHYW1lcy0mYXBwdmVyc2lvxNzImcm5kdmFsPTEzNDQ4NTM2ODE= HTTP/1.1</strong></p><p>Host: xxx.xxx.xxx.xxx</p><p>Connection: Keep-Alive</p><p>User-Agent: My User Agent</p><p>Accept-Encoding: gzip</p><p>Looks like the parameter is gzipped, but wireshark can not decoded it.</p><p>The answer from the server is coded with GZIP and wireshark can decoded it easily, I can see it under tab "uncompress entity body"</p><p>How can I unzip the passing parameter? It should be a XML-file o JSON-parameter . I have tried coping it to a plain .gz file and using gzip command, but it didn't work.</p><p>Any idea?</p><p>(with a little help from google Translate, sorry for my english)</p></div><div id="question-tags" class="tags-container tags">gzip url http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/74f23a1b06d41f7930e8b3676f214dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vwpolo&#39;s gravatar image" /><p>vwpolo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vwpolo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Aug '12, 11:15</p></div></div><div id="comments-container-13622" class="comments-container"></div><div id="comment-tools-13622" class="comment-tools"></div><div class="clear"></div><div id="comment-13622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13627"></span>

<div id="answer-container-13627" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13627-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like it's base64 encoded. Likely to be a binary blob.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13627" class="comments-container"><span id="13630"></span><div id="comment-13630" class="comment"><div id="post-13630-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your ideas.</p><p>Now I have processed the data as base64 and it works!</p><p>At this web: <a href="http://www.base64decode.org">www.base64decode.org</a> I can decode the parameter.</p><p>Thanks!!!</p></div><div id="comment-13630-info" class="comment-info"><span class="comment-age">(14 Aug '12, 12:21)</span> vwpolo</div></div><span id="13632"></span><div id="comment-13632" class="comment"><div id="post-13632-score" class="comment-score"></div><div class="comment-text"><p>Can you accept the answer for the benefit of others by clicking the check mark icon next to the answer.</p></div><div id="comment-13632-info" class="comment-info"><span class="comment-age">(14 Aug '12, 13:13)</span> grahamb ♦</div></div></div><div id="comment-tools-13627" class="comment-tools"></div><div class="clear"></div><div id="comment-13627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

