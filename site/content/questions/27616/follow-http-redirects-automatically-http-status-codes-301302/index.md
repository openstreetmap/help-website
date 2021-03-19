+++
type = "question"
title = "Follow HTTP redirects automatically (HTTP status codes 301/302)"
description = '''In the same way &quot;Follow TCP Stream&quot; joins packets for easier analysis. Is there a way to follow HTTP redirects without doing it manually? '''
date = "2013-12-01T11:31:00Z"
lastmod = "2013-12-02T13:46:00Z"
weight = 27616
keywords = [ "redirects", "http" ]
aliases = [ "/questions/27616" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Follow HTTP redirects automatically (HTTP status codes 301/302)](/questions/27616/follow-http-redirects-automatically-http-status-codes-301302)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27616-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the same way "Follow TCP Stream" joins packets for easier analysis.</p><p>Is there a way to follow HTTP redirects without doing it manually?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wanna-also-follow-http-redirects.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">redirects http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '13, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/d65593e3a584ff801c331e387964c69e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elgalu&#39;s gravatar image" /><p>elgalu<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elgalu has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 01 Dec '13, 11:32</p></div></div><div id="comments-container-27616" class="comments-container"></div><div id="comment-tools-27616" class="comment-tools"></div><div class="clear"></div><div id="comment-27616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27672"></span>

<div id="answer-container-27672" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27672-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to follow HTTP redirects without doing it manually?</p></blockquote><p>Wireshark does not provide that functionality and it would be hard to implement for several reasons (see also the comment of @Guy Harris).</p><p>In some cases you will see the redirect and the following request in the same TCP connection, if the client uses HTTP/1.1 <strong>and</strong> it reuses the same connection to the <strong>same</strong> server. However, as shown in your example, there can also be redirects to a different host (request: rubygems.org, redirect: production.s3.rubygems.org), hence the client must use a different TCP connection.</p><p>What you can do is to support the manual process as much as possible, with the features/tools Wireshark provides (and/or tshark)</p><ol><li>Add some columns to show the following values: <code>tcp.stream</code>, <code>http.location</code> and <code>http.request.full_uri</code></li><li>Apply the following display filter: <code>http.response.code == 302 or http.response.code == 301 or http.request</code><br />
</li></ol><p>The whole thing will look like the following screenshot</p><p><img src="https://osqa-ask.wireshark.org/upfiles/screenshot_small_1.png" alt="alt text" /></p><p>The filtered frames will show the redirect and (in most cases) directly following the request to the redirected page. If there is a lot of traffic, you could further filter the requests, based on client IP (ip.addr) and User-Agent header (http.user_agent).</p><p>Then simply take the TCP stream values and build your next filter:</p><blockquote><p>tcp.stream eq 2 or tcp.stream eq 3</p></blockquote><p>Unfortunately you still can't 'follow' both streams at once, but at least you will be able to do the manual analysis a bit faster ;-))</p><p>You can to the same thing with tshark and some scripting!</p><p>As an alternative, you could write a Listener/Tap (in C or Lua) and filter things there, but that's quite some work to do, and probably not worth the time, if you don't have to follow hundreds of redirects per day.</p><blockquote><p><a href="http://wiki.wireshark.org/Lua/Taps">http://wiki.wireshark.org/Lua/Taps</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '13, 13:52</p></div></div><div id="comments-container-27672" class="comments-container"><span id="27673"></span><div id="comment-27673" class="comment"><div id="post-27673-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Wireshark does not provide that functionality.</p></blockquote><p>...because it's a network analyzer, not a Web browser or other Web client. It shows you what happened on the network, and if the program that sent the request that got the redirect didn't follow the redirect, then following-the-redirect didn't happen on the network.</p></div><div id="comment-27673-info" class="comment-info"><span class="comment-age">(02 Dec '13, 13:49)</span> Guy Harris ♦♦</div></div><span id="27677"></span><div id="comment-27677" class="comment"><div id="post-27677-score" class="comment-score"></div><div class="comment-text"><p>Very helpful and detailed small guide! Thanks!!!</p></div><div id="comment-27677-info" class="comment-info"><span class="comment-age">(02 Dec '13, 14:55)</span> elgalu</div></div></div><div id="comment-tools-27672" class="comment-tools"></div><div class="clear"></div><div id="comment-27672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

