+++
type = "question"
title = "I want add subtree , a HEX value with 16bytes, but  buf max is 8 bytes"
description = '''I asked this question on the wireshark-dev mailing list and @cmaynard solved it. YOU HAVE HERE:  I want add subtree , a HEX value with 16bytes, but buf max is 8 bytes, when I tried more not works. I tried defining Protofield like a string and it works but I want to show in HEX . Why can do it? local...'''
date = "2016-05-03T02:28:00Z"
lastmod = "2016-05-03T07:12:00Z"
weight = 52165
keywords = [ "lua", "bytes", "subtree", "hex", "protofield" ]
aliases = [ "/questions/52165" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [I want add subtree , a HEX value with 16bytes, but buf max is 8 bytes](/questions/52165/i-want-add-subtree-a-hex-value-with-16bytes-but-buf-max-is-8-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52165-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I asked this question on the <a href="https://www.wireshark.org/lists/wireshark-dev/201604/msg00229.html">wireshark-dev mailing list</a> and @cmaynard solved it. YOU HAVE HERE:</p><blockquote><p>I want add subtree , a HEX value with 16bytes, but buf max is 8 bytes, when I tried more not works. I tried defining Protofield like a string and it works but I want to show in HEX . Why can do it?</p><p>local f_marker = ProtoField.string("myproto.marker", "MARKER", base.HEX)</p><p>subtree = root:add(p_myproto, buf(0)) subtree:add(f_marker, buf(0,16))</p></blockquote></div><div id="question-tags" class="tags-container tags">lua bytes subtree hex protofield</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/0164b3a0b6fca8e2931eb42defb1ebfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="javiguembe&#39;s gravatar image" /><p>javiguembe<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="javiguembe has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '16, 07:06</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-52165" class="comments-container"><span id="52169"></span><div id="comment-52169" class="comment"><div id="post-52169-score" class="comment-score"></div><div class="comment-text"><p>What you should really do is rework your "question" to clearly state the problem, and then add an answer post with the answer and then accept the answer so others can see it's a helpful answer to your question. Then there's no need for the redundant "(SoLVED)" in the question title.</p><p>Please read the FAQ for the site for more information.</p></div><div id="comment-52169-info" class="comment-info"><span class="comment-age">(03 May '16, 03:35)</span> grahamb ♦</div></div><span id="52178"></span><div id="comment-52178" class="comment"><div id="post-52178-score" class="comment-score"></div><div class="comment-text"><p>I've tried to clean it up.</p></div><div id="comment-52178-info" class="comment-info"><span class="comment-age">(03 May '16, 07:13)</span> cmaynard ♦♦</div></div><span id="52216"></span><div id="comment-52216" class="comment"><div id="post-52216-score" class="comment-score"></div><div class="comment-text"><p>Sorry! Thanks!</p></div><div id="comment-52216-info" class="comment-info"><span class="comment-age">(04 May '16, 01:18)</span> javiguembe</div></div></div><div id="comment-tools-52165" class="comment-tools"></div><div class="clear"></div><div id="comment-52165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52177"></span>

<div id="answer-container-52177" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52177-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The intent of sending javiguembe to this site was not to ask and answer <strong>this</strong> question but to make javiguembe aware of the site so that it might be utilized to search for answers to future questions or to ask new questions. But since the question has been asked here, I'll post the relevant part of the answer I gave on the mailing list, which apparently solved the problem:</p><p>Try declaring <code>f_marker</code> like so:</p><pre><code>local f_marker = ProtoField.bytes(&quot;myproto.marker&quot;, &quot;MARKER&quot;)</code></pre><p>Ref: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Proto.html#lua_class_ProtoField">https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Proto.html#lua_class_ProtoField</a>, specifically section 11.6.7.24.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-52177" class="comments-container"></div><div id="comment-tools-52177" class="comment-tools"></div><div class="clear"></div><div id="comment-52177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

