+++
type = "question"
title = "how to add IP address to TreeItem in Lua?"
description = '''How can I add an IP address to a TreeItem? I&#x27;m using the following Lua: sourceIpAddr = ProtoField.uint32(&quot;asc_sccp.sourceIpAddr&quot;, &quot;sourceIpAddr&quot;, base.HEX) subtree:add (sourceIpAddr, buffer(72,4))  As a result, I see: sourceIpAddr: 0  But I would like to see: sourceIpAddr: 0.0.0.0  How can I get thi...'''
date = "2012-05-23T05:19:00Z"
lastmod = "2012-05-23T06:35:00Z"
weight = 11249
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/11249" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to add IP address to TreeItem in Lua?](/questions/11249/how-to-add-ip-address-to-treeitem-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11249-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I add an IP address to a <code>TreeItem</code>?</p><p>I'm using the following Lua:</p><pre><code>sourceIpAddr = ProtoField.uint32(&quot;asc_sccp.sourceIpAddr&quot;, &quot;sourceIpAddr&quot;, base.HEX)
subtree:add (sourceIpAddr, buffer(72,4))</code></pre><p>As a result, I see:</p><pre><code>sourceIpAddr: 0</code></pre><p>But I would like to see:</p><pre><code>sourceIpAddr: 0.0.0.0</code></pre><p>How can I get this result?</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '12, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/a637cbdbbb00c38a1643b374a0833e9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olga&#39;s gravatar image" /><p>Olga<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olga has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 May '12, 06:37</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11249" class="comments-container"></div><div id="comment-tools-11249" class="comment-tools"></div><div class="clear"></div><div id="comment-11249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11255"></span>

<div id="answer-container-11255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11255-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>ProtoField</code> supports several field types other than <code>uint32</code>, including <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_fn_ProtoField_ipv4_abbr___name____desc__">IPv4</a> and <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_fn_ProtoField_ipv6_abbr___name____desc__">IPv6</a>. Try <code>ProtoField.ipv4()</code>:</p><pre><code>sourceIpAddr = ProtoField.ipv4(&quot;asc_sccp.sourceIpAddr&quot;, &quot;sourceIpAddr&quot;)
subtree:add(sourceIpAddr, buffer(72,4))</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '12, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-11255" class="comments-container"></div><div id="comment-tools-11255" class="comment-tools"></div><div class="clear"></div><div id="comment-11255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

