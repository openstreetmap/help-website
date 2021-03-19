+++
type = "question"
title = "What may cause zlib decompression to fail?"
description = '''I am trying to analyze HTTP traffic where the HTTP body is zlib encoded. The packet details pane shows: Hypertext Transfer Protocol  POST /xxs/ HTTP/1.1&#92;r&#92;n  Content-Type: text/xml; charset=&quot;utf-8&quot;&#92;r&#92;n  SOAPAction: &#92;r&#92;n  Content-Encoding: zlib&#92;r&#92;n  Text-Length: 550&#92;r&#92;n  Content-Length: 312&#92;r&#92;n  Conn...'''
date = "2013-02-20T09:57:00Z"
lastmod = "2013-02-20T09:57:00Z"
weight = 18778
keywords = [ "zlib", "decompression" ]
aliases = [ "/questions/18778" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What may cause zlib decompression to fail?](/questions/18778/what-may-cause-zlib-decompression-to-fail)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18778-score" class="post-score" title="current number of votes">0</div><span id="post-18778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to analyze HTTP traffic where the HTTP body is zlib encoded. The packet details pane shows:</p><pre><code>Hypertext Transfer Protocol
    POST /xxs/ HTTP/1.1\r\n
    Content-Type: text/xml; charset=&quot;utf-8&quot;\r\n
    SOAPAction: \r\n
    Content-Encoding: zlib\r\n
    Text-Length: 550\r\n
    Content-Length: 312\r\n
    Connection: Close\r\n
    \r\n
    Content-encoded entity body (zlib): 312 bytes [Error: Decompression failed]
        Data (312 bytes)</code></pre><p>So for some reason the decompression of the zlip compressed data is failing. When I export the raw bytes of the HTTP body to a file I can successfully decompress them with a command line tool (openssl zlib -d). That tells me the content is in fact validly zlib encoded.</p><p>What may be causing the zlib decompression to fail in Wireshark? Is there anything further I could try to do to get this to work?</p><p>The problem occurs both in</p><ul><li>the current version 1.8.5 (SVN Rev 47350 from /trunk-1.8) on Windows 7 (zlib1.dll is present in Wireshark folder)</li><li>Version 1.2.15 on CentOS (the only version I was able to get hold of on Linux right now)</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zlib" rel="tag" title="see questions tagged &#39;zlib&#39;">zlib</span> <span class="post-tag tag-link-decompression" rel="tag" title="see questions tagged &#39;decompression&#39;">decompression</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/710a14b2c62659199e7e7453ad873be0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tobias&#39;s gravatar image" /><p><span>tobias</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tobias has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Feb '13, 10:00</strong> </span></p></div></div><div id="comments-container-18778" class="comments-container"></div><div id="comment-tools-18778" class="comment-tools"></div><div class="clear"></div><div id="comment-18778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

