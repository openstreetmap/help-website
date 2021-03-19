+++
type = "question"
title = "Search for unicode string (UTF-16)"
description = '''When frame contains Unicode string like &quot;select&quot;, it is displayed as &quot;s e l e c t&quot;, the space between characters is the null character &#92;x00 not the space.  if i use the display filter:   frame contains &quot;s e l e c t&quot;  it is not filtered. so, I have to convert the string &quot;select&quot; to hex decimal manual...'''
date = "2016-09-15T13:39:00Z"
lastmod = "2016-09-16T02:35:00Z"
weight = 55570
keywords = [ "tds", "wireshark" ]
aliases = [ "/questions/55570" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Search for unicode string (UTF-16)](/questions/55570/search-for-unicode-string-utf-16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When frame contains Unicode string like "select", it is displayed as "s e l e c t", the space between characters is the null character \x00 not the space.</p><p>if i use the display filter:</p><pre><code> frame contains &quot;s e l e c t&quot;</code></pre><p>it is not filtered.</p><p>so, I have to convert the string "select" to hex decimal manually , and run the display filter:</p><pre><code>frame contains 73:00:65:00:6c:00:65:00:63:00:74:00</code></pre><p>and it's working.</p><p>Also, I tried to use the find tool (in the tool bar) and picked <strong>Wide (UTF-16)</strong> and entered "s e l e c t", but it couldn't find the string.</p><p>I use wireshark v 2.2.0</p><p>My question:</p><ul><li>Is there a simple way to filter for Unicode string direct instead of converting string to hex string</li><li>what i should enter in the find tool when picking Wide (UTF-16) to search for the asci "select" but as a Unicode string</li></ul></div><div id="question-tags" class="tags-container tags">tds wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '16, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/890d84c2eed009483d2d3bee584bfc31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M-Hassan&#39;s gravatar image" /><p>M-Hassan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M-Hassan has no accepted answers">0%</span></p></div></div><div id="comments-container-55570" class="comments-container"></div><div id="comment-tools-55570" class="comment-tools"></div><div class="clear"></div><div id="comment-55570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55587"></span>

<div id="answer-container-55587" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55587-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's Unicode in a <a href="https://en.wikipedia.org/wiki/UTF-16">UTF-16</a> encoding, i.e. 2 bytes per code unit.</p><p>Leave the character encoding selector set to Narrow &amp; Wide and just enter your string with the required characters, i.e. "select". This will search for both UTF-8/ASCII and UTF-16 encodings of the required string.<br />
</p><p>If you really want to find just UTF-16 encodings of the string, set the encoding selector to Wide, but still just enter the actual characters required.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '16, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-55587" class="comments-container"><span id="55590"></span><div id="comment-55590" class="comment"><div id="post-55590-score" class="comment-score"></div><div class="comment-text"><p>Thanks.It's working and find the string, but wireshark highligt last half of the string, review my sample <a href="http://imgur.com/qJtub28">http://imgur.com/qJtub28</a> Is this normal? What the actual character for UTF-16 to enter?</p></div><div id="comment-55590-info" class="comment-info"><span class="comment-age">(16 Sep '16, 04:37)</span> M-Hassan</div></div><span id="55593"></span><div id="comment-55593" class="comment"><div id="post-55593-score" class="comment-score"></div><div class="comment-text"><p>That wasn't the original question though :-)</p><p>Looks like a bug to me when restricting the search to the packet bytes pane, please raise an entry on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-55593-info" class="comment-info"><span class="comment-age">(16 Sep '16, 05:10)</span> grahamb ♦</div></div><span id="55596"></span><div id="comment-55596" class="comment"><div id="post-55596-score" class="comment-score"></div><div class="comment-text"><p>what is the UTF-16 of the string "select" to enter when i pick the character encoding selector wide (UTF-16), so i can enter the display filter {frame contains "the UTF-16 of the the string select"}</p></div><div id="comment-55596-info" class="comment-info"><span class="comment-age">(16 Sep '16, 05:56)</span> M-Hassan</div></div><span id="55597"></span><div id="comment-55597" class="comment"><div id="post-55597-score" class="comment-score">1</div><div class="comment-text"><p>If the data you require is dissected in a field, you can just use the appropriate <code>protocol.field == "mystring"</code> filter.</p><p>If the data isn't in a field, as in your example of a TDS "select" statement, then you'll have to manually convert the string to the appropriate UTF-x equivalent, e.g. "select" encoded as UTF-16LE is 73:00:65:00:6c:00:65:00:63:00:74:00 and this would be used as <code>frame contains 73:00:65:00:6c:00:65:00:63:00:74:00</code>.</p><p>There is an online converter <a href="http://www.mobilefish.com/services/latin_utf_base64_to_hex/latin_utf_base64_to_hex.php#text_hex_output">here</a>, and you likely want to convert from text to UTF-16LE (as used by Windows systems).</p></div><div id="comment-55597-info" class="comment-info"><span class="comment-age">(16 Sep '16, 06:45)</span> grahamb ♦</div></div><span id="55598"></span><div id="comment-55598" class="comment"><div id="post-55598-score" class="comment-score"></div><div class="comment-text"><p>Thanks for help. +10 for the tool convertor UTF-16LE</p></div><div id="comment-55598-info" class="comment-info"><span class="comment-age">(16 Sep '16, 07:13)</span> M-Hassan</div></div><span id="55619"></span><div id="comment-55619" class="comment not_top_scorer"><div id="post-55619-score" class="comment-score"></div><div class="comment-text"><p>@Wireshark Bugzilla. I raised a bug: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12908">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12908</a></p></div><div id="comment-55619-info" class="comment-info"><span class="comment-age">(17 Sep '16, 07:05)</span> M-Hassan</div></div></div><div id="comment-tools-55587" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-55587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

