+++
type = "question"
title = "How to create a filter for a particular field?"
description = '''Hi, I want to create a display filter for a particular field. Please help me to finish my task. HTTP Header: Hypertext Transfer Protocol  POST / HTTP/1.1&#92;r&#92;n Content-Type: text/xml; charset=utf-8&#92;r&#92;n SOAPAction: &quot;create&quot;&#92;r&#92;n  Here, I want to create filter for the &quot;SOAPAction&quot; field.'''
date = "2011-09-11T08:05:00Z"
lastmod = "2011-09-11T11:19:00Z"
weight = 6270
keywords = [ "http", "soap", "display-filter" ]
aliases = [ "/questions/6270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a filter for a particular field?](/questions/6270/how-to-create-a-filter-for-a-particular-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6270-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I want to create a display filter for a particular field. Please help me to finish my task.</p><p>HTTP Header:</p><pre><code>Hypertext Transfer Protocol

POST / HTTP/1.1\r\n
Content-Type: text/xml; charset=utf-8\r\n
SOAPAction: &quot;create&quot;\r\n</code></pre><p>Here, I want to create filter for the "SOAPAction" field.</p></div><div id="question-tags" class="tags-container tags">http soap display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '11, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/01febacc45af8ecf743c4f575d428326?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JK7&#39;s gravatar image" /><p>JK7<br />
<span class="score" title="31 reputation points">31</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JK7 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Sep '11, 10:43</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6270" class="comments-container"></div><div id="comment-tools-6270" class="comment-tools"></div><div class="clear"></div><div id="comment-6270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6274"></span>

<div id="answer-container-6274" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6274-score" class="post-score" title="current number of votes">7</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://www.wireshark.org/docs/dfref/h/http.html">HTTP field list</a> doesn't include <code>SOAPAction</code>, so <code>SOAPAction</code> is added as a simple text item. You can filter for it in a couple ways:</p><h3 id="option-1-custom-http-header-field">Option 1: Custom HTTP header field</h3><p>Add a custom header field to your HTTP preferences (requires Wireshark restart), which allows you to filter for the field.</p><ol><li>Open menu: <strong>Edit &gt; Preferences &gt; Protocols &gt; HTTP &gt; Custom HTTP headers fields</strong></li><li>Click <strong>New</strong></li><li>For <strong>Header name</strong>, enter <strong>SOAPAction</strong></li><li>For <strong>Field desc</strong>, enter <strong>Intent of SOAP HTTP request</strong> (or whatever)</li><li>Click <strong>OK</strong></li><li>Restart Wireshark.</li><li>In the <em>Display Filter textbox</em>, enter <strong>http.header.SOAPAction</strong>, and click <strong>Apply</strong>. The textbox background should turn green, indicating the display filter syntax is correct (and that our preference changes for the custom field <code>SOAPAction</code> took effect).</li></ol><h3 id="option-2-string-matching-display-filter">Option 2: String matching display filter</h3><p>This display filter scans entire HTTP packets for the string "SOAPAction:". This might be inefficient compared to a custom HTTP header field, but it works well.</p><pre><code>http contains &quot;SOAPAction:&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '11, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Sep '11, 17:15</p></div></div><div id="comments-container-6274" class="comments-container"><span id="6291"></span><div id="comment-6291" class="comment"><div id="post-6291-score" class="comment-score"></div><div class="comment-text"><p>Hi "Helloworld" Thanks.....</p></div><div id="comment-6291-info" class="comment-info"><span class="comment-age">(12 Sep '11, 09:10)</span> JK7</div></div></div><div id="comment-tools-6274" class="comment-tools"></div><div class="clear"></div><div id="comment-6274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

