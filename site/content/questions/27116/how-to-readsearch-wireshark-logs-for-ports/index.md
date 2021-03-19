+++
type = "question"
title = "How to read/search wireshark logs for ports"
description = '''Hello, I&#x27;m trying to search for a specific product and/or port in a wireshark log that i pulled. I tried to use the filter system but typing the port didnt result in a search, instead i got an error: &quot;6502&quot; isn&#x27;t a valid display filter: &quot;6502&quot; is neither a field nor a protocol name. is there a way t...'''
date = "2013-11-19T13:59:00Z"
lastmod = "2013-11-19T14:31:00Z"
weight = 27116
keywords = [ "port" ]
aliases = [ "/questions/27116" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to read/search wireshark logs for ports](/questions/27116/how-to-readsearch-wireshark-logs-for-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27116-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to search for a specific product and/or port in a wireshark log that i pulled. I tried to use the filter system but typing the port didnt result in a search, instead i got an error: "6502" isn't a valid display filter: "6502" is neither a field nor a protocol name.</p><p>is there a way to search for key words or ports? really need your help please</p></div><div id="question-tags" class="tags-container tags">port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '13, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/701dc2d233a92ccc9fe4bb952ef73d05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xxx4reggie&#39;s gravatar image" /><p>xxx4reggie<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xxx4reggie has no accepted answers">0%</span></p></div></div><div id="comments-container-27116" class="comments-container"></div><div id="comment-tools-27116" class="comment-tools"></div><div class="clear"></div><div id="comment-27116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27117"></span>

<div id="answer-container-27117" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27117-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the protocol uses <a href="http://wiki.wireshark.org/Transmission_Control_Protocol">TCP</a>, then try <code>tcp.port eq 6502</code>; if it uses <a href="http://wiki.wireshark.org/User_Datagram_Protocol">UDP</a>, then try <code>udp.port eq 6502</code>.</p><p>For more information on display filter syntax, refer to the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">Wireshark User Guide</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '13, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27117" class="comments-container"><span id="27119"></span><div id="comment-27119" class="comment"><div id="post-27119-score" class="comment-score"></div><div class="comment-text"><p>oh wow! That helps significantly! Thank you so much, life saver!!</p><p>Another question, is it possible to do a search via name? (I'm also checking the Guide that you posted but just in case you have this info:) )</p></div><div id="comment-27119-info" class="comment-info"><span class="comment-age">(19 Nov '13, 15:16)</span> xxx4reggie</div></div><span id="27122"></span><div id="comment-27122" class="comment"><div id="post-27122-score" class="comment-score"></div><div class="comment-text"><p>If you mean something like this:</p><blockquote><p>tcp.port eq <strong>http</strong></p></blockquote><p>then the answer is: No</p><p>Although in the case of 6502 this filter would be nice</p><blockquote><p>tcp.port eq c64</p></blockquote><p>almost!! ;-))</p></div><div id="comment-27122-info" class="comment-info"><span class="comment-age">(19 Nov '13, 15:31)</span> Kurt Knochner ♦</div></div><span id="27144"></span><div id="comment-27144" class="comment"><div id="post-27144-score" class="comment-score"></div><div class="comment-text"><p>No, c64 would actually be a match for 6510.</p></div><div id="comment-27144-info" class="comment-info"><span class="comment-age">(20 Nov '13, 02:25)</span> grahamb ♦</div></div><span id="27150"></span><div id="comment-27150" class="comment"><div id="post-27150-score" class="comment-score"></div><div class="comment-text"><p>I know. That why I said: almost!! ;-))</p></div><div id="comment-27150-info" class="comment-info"><span class="comment-age">(20 Nov '13, 03:13)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27117" class="comment-tools"></div><div class="clear"></div><div id="comment-27117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

