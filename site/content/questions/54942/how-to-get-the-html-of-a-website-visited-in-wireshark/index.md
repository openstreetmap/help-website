+++
type = "question"
title = "How to get the HTML of a website visited, in Wireshark?"
description = '''Following is an example of an HTTP response : HTTP/1.1 200 OK Date: Mon, 27 Jul 2009 12:28:53 GMT Server: Apache/2.2.14 (Win32) Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT Content-Length: 88 Content-Type: text/html Connection: Closed &amp;lt;html&amp;gt; &amp;lt;body&amp;gt; &amp;lt;h1&amp;gt;Hello, World!&amp;lt;/h1&amp;gt; &amp;lt;...'''
date = "2016-08-18T03:07:00Z"
lastmod = "2016-08-21T18:32:00Z"
weight = 54942
keywords = [ "sniffing", "packet-capture", "http", "tshark", "wireshark" ]
aliases = [ "/questions/54942" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the HTML of a website visited, in Wireshark?](/questions/54942/how-to-get-the-html-of-a-website-visited-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54942-score" class="post-score" title="current number of votes">0</div><span id="post-54942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Following is an example of an HTTP response :</p><pre><code>HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 88
Content-Type: text/html
Connection: Closed
&lt;html&gt;
&lt;body&gt;
&lt;h1&gt;Hello, World!&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre><p>I am particularly interested in the HTML (of the webpage) appended at the end of the response message. How can I get this HTML of the websites visited, from Wireshark capture data, for example from a .pcap file opened in Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '16, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p><span>Jesss</span><br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Aug '16, 03:10</strong> </span></p></div></div><div id="comments-container-54942" class="comments-container"></div><div id="comment-tools-54942" class="comment-tools"></div><div class="clear"></div><div id="comment-54942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54965"></span>

<div id="answer-container-54965" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54965-score" class="post-score" title="current number of votes">1</div><span id="post-54965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html#ChIOExportObjectsDialog">This section</a> of the users guide may be helpful.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '16, 21:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54965" class="comments-container"><span id="55037"></span><div id="comment-55037" class="comment"><div id="post-55037-score" class="comment-score"></div><div class="comment-text"><p>It is in GUI. I want to do it in commandline interface, i.e. tshark..</p></div><div id="comment-55037-info" class="comment-info"><span class="comment-age">(21 Aug '16, 18:32)</span> <span class="comment-user userinfo">Jesss</span></div></div></div><div id="comment-tools-54965" class="comment-tools"></div><div class="clear"></div><div id="comment-54965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

