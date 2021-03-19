+++
type = "question"
title = "Should size of file increase when saved on disk after extracting from packets"
description = '''I captured a JFIF image packet of 2817 Bytes. Out of which image was of 2497 Bytes. By using option &quot;export selected packet bytes&quot; in wireshark, i extracted the file to my disk. The disk size is also 2497 bytes. Should not it expand as in network transmission it was compressed by GZIP. How the size ...'''
date = "2011-07-28T07:08:00Z"
lastmod = "2011-07-28T11:11:00Z"
weight = 5341
keywords = [ "disk", "save", "bytes", "file", "size" ]
aliases = [ "/questions/5341" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Should size of file increase when saved on disk after extracting from packets](/questions/5341/should-size-of-file-increase-when-saved-on-disk-after-extracting-from-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5341-score" class="post-score" title="current number of votes">0</div><span id="post-5341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured a JFIF image packet of 2817 Bytes. Out of which image was of 2497 Bytes. By using option "export selected packet bytes" in wireshark, i extracted the file to my disk. The disk size is also 2497 bytes. Should not it expand as in network transmission it was compressed by GZIP. How the size is still the same after decompressing it.</p><p>Or if it is not decompressed at all?</p><p>following is the request responce block ...</p><pre><code>GET /vi/tN23KfbtMIA/default.jpg HTTP/1.1 
Host: i1.ytimg.com 
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18 ( .NET CLR 3.5.30729; .NET4.0E) 
Accept: image/png,image/*;q=0.8,*/*;q=0.5 
Accept-Language: en-gb,en;q=0.5 
Accept-Encoding: gzip,deflate 
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7 
Keep-Alive: 115 
Connection: keep-alive 
Referer: http://www.youtube.com/watch?v=ERTcZV7uTFU&amp;feature=aso

HTTP/1.1 200 OK 
Content-Type: image/jpeg 
Last-Modified: Thu, 01 Jan 1970 00:21:46 GMT 
Date: Wed, 27 Jul 2011 10:46:19 GMT 
Expires: Wed, 27 Jul 2011 16:46:19 GMT 
X-Content-Type-Options: nosniff 
Server: sffe 
Content-Length: 2497 
X-XSS-Protection: 1; mode=block 
Cache-Control: public, max-age=21600 
Age: 19895</code></pre><p>========================================</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disk" rel="tag" title="see questions tagged &#39;disk&#39;">disk</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '11, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/9efda729ccf3d60a6241f17ef05291b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arjun&#39;s gravatar image" /><p><span>Arjun</span><br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arjun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jul '11, 11:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-5341" class="comments-container"></div><div id="comment-tools-5341" class="comment-tools"></div><div class="clear"></div><div id="comment-5341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5342"></span>

<div id="answer-container-5342" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5342-score" class="post-score" title="current number of votes">0</div><span id="post-5342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arjun has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, the file size should be the same. As in this case, you talk about gzip, but the object is JPEG compressed (image) data. What you're seeing is the indication of the capability of the client to accept gzip encoded (compressed) data. It's then up to the server to decide to take the client up on its offer, or not. In this case it makes little sense, so the server chooses not to gzip the JPEG compressed data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '11, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5342" class="comments-container"><span id="5343"></span><div id="comment-5343" class="comment"><div id="post-5343-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap..</p><p>If I take raw bits and save it with extension JPEG will it make an image? This can be done by writting binary data thru C program ...what u suggest?</p><p>Thanks, Arjun</p></div><div id="comment-5343-info" class="comment-info"><span class="comment-age">(28 Jul '11, 08:17)</span> <span class="comment-user userinfo">Arjun</span></div></div><span id="5347"></span><div id="comment-5347" class="comment"><div id="post-5347-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", see the FAQ for details on how to use this site best)</p></div><div id="comment-5347-info" class="comment-info"><span class="comment-age">(28 Jul '11, 11:09)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="5348"></span><div id="comment-5348" class="comment"><div id="post-5348-score" class="comment-score"></div><div class="comment-text"><p>Yes, you can do that through a program after saving "selected packet bytes", however, you can also use "File -&gt; Export -&gt; Objects -&gt; HTTP" :-)</p></div><div id="comment-5348-info" class="comment-info"><span class="comment-age">(28 Jul '11, 11:11)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5342" class="comment-tools"></div><div class="clear"></div><div id="comment-5342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

