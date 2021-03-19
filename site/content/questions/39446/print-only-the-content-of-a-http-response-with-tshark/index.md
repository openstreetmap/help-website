+++
type = "question"
title = "Print only the content of a http response with tshark"
description = '''Is tshark able to print only the content of a http response? With &quot;content of a http response&quot; I mean that part, that is normally displayed by the web browser. When I use the command tshark -i lo -x -R &#x27;http.response.code == 200&#x27; -l  the response can occur in several different places:  It can be par...'''
date = "2015-01-27T17:57:00Z"
lastmod = "2015-01-28T20:35:00Z"
weight = 39446
keywords = [ "tshark" ]
aliases = [ "/questions/39446" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Print only the content of a http response with tshark](/questions/39446/print-only-the-content-of-a-http-response-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39446-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is tshark able to print only the content of a http response? With "content of a http response" I mean that part, that is normally displayed by the web browser. When I use the command</p><pre><code>tshark -i lo -x -R &#39;http.response.code == 200&#39; -l</code></pre><p>the response can occur in several different places:</p><ol><li>It can be part of the output that follows the heading "Reassembled TCP". That's that case when I request <a href="http://httpbin.org/html.">http://httpbin.org/html.</a></li><li>It can be part of the output that follows the heading "De-chunked entity body". That's the case when I request httpbin.org/stream-bytes/10.</li><li>It can be part of the output that follows the heading "Uncompressed entity body". That's the case when I request httpbin.org/gzip.</li><li>It can be part of the output that does not follow a heading. That's the case when I request <a href="http://httpbin.org/deny.">http://httpbin.org/deny.</a></li></ol><p>I created a demo for each of these cases at <a href="http://pastebin.com/uEWuHagu">http://pastebin.com/uEWuHagu</a></p><p>In the first case I would like to get that part of "Reassembled TCP" that follows &lt;!DOCTYPE html.</p><p>In the second case I would like to get everything that follows the line "De-chunked entity body (10 bytes):"</p><p>In the third case I would like to get everything that follows the line "Uncompressed entity body (462 bytes):"</p><p>In the fourth case I would like to get everything that belongs to the ascii image and everything that follows that image.</p><p>I am not sure if another situation is possible. I would like to get the described response in any situation. It would be fantastic if that is possible.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '15, 17:57</strong></p><img src="https://secure.gravatar.com/avatar/d35774ec5eb4bae1cb17de194e84a1ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miachino&#39;s gravatar image" /><p>miachino<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miachino has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jan '15, 05:39</p></div></div><div id="comments-container-39446" class="comments-container"></div><div id="comment-tools-39446" class="comment-tools"></div><div class="clear"></div><div id="comment-39446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39464"></span>

<div id="answer-container-39464" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39464-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can get the de-chunked entity body one by printing the "<code>data</code>" field, like this:</p><pre><code>tshark -i lo -Y &#39;http.response.code == 200&#39; -T fields -e data</code></pre><p>For the others, I don't know of a way to get them with tshark alone, but you can use a Lua script to get them.</p><p>For example the script provided <a href="https://ask.wireshark.org/questions/38759/using-tshark-to-save-filtered-packets-to-file?page=1&amp;focusedAnswerId=38799#38799">in this link's answer</a>, with the following tshark command:</p><pre><code># the following is all one command line:
tshark -i lo -Y &#39;http.response.code == 200&#39; -T fields -e extractor.string -X lua_script:extract.lua -X lua_script1:data-text-lines -X lua_script1:json</code></pre><p>I can explain how to modify that script to get the <code>data</code> field as well, if you wish.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '15, 20:35</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39464" class="comments-container"><span id="39523"></span><div id="comment-39523" class="comment"><div id="post-39523-score" class="comment-score"></div><div class="comment-text"><p>@Hadriel Thanx for your answer. Unfortunately I have no idea about Lua. Therefore I am not even able to read your script that you wrote as a reply to the other question. Because of that I am at least sceptical that I would understand your explanations. But of course it would be very kind of you if we could give it a try.</p></div><div id="comment-39523-info" class="comment-info"><span class="comment-age">(31 Jan '15, 10:35)</span> miachino</div></div></div><div id="comment-tools-39464" class="comment-tools"></div><div class="clear"></div><div id="comment-39464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

