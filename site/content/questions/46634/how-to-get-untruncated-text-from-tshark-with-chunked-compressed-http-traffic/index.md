+++
type = "question"
title = "How to get untruncated text from tshark with chunked, compressed http traffic"
description = '''I have some http traffic which happens to be served compressed, chunked and encrypted. I have the client master-secrete and CLIENT_RANDOM, so I am using that to decrypt the traffic. I&#x27;m using a bleeding edge build (win32-2.1.0-132-g3ef2fd6) as it seems to supports combined dechunking, decompression ...'''
date = "2015-10-16T14:05:00Z"
lastmod = "2015-10-19T16:35:00Z"
weight = 46634
keywords = [ "encryption", "tshark", "compression" ]
aliases = [ "/questions/46634" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get untruncated text from tshark with chunked, compressed http traffic](/questions/46634/how-to-get-untruncated-text-from-tshark-with-chunked-compressed-http-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46634-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some http traffic which happens to be served compressed, chunked and encrypted. I have the client master-secrete and CLIENT_RANDOM, so I am using that to decrypt the traffic.</p><p>I'm using a bleeding edge build (win32-2.1.0-132-g3ef2fd6) as it seems to supports combined dechunking, decompression and decryption well. Everything works in the wireshark GUI, but it would be convenient to be able to export the plain text of the HTTP request and response using <code>tshark</code>. I can get the full ASCII text in the GUI by going:</p><p><code>Uncompressed Entity Body -&gt; Line-based text data -&gt; right click -&gt; Copy -&gt; ...As printable text</code></p><p>However, with <code>tshark</code>, I can only get the first few bytes of that text by using:</p><p><code>tshark.exe -Y "http" -o ssl.keylog_file:"{key_file}" -r "{input_file}" -T fields -e text</code></p><p>Which returns something like:</p><pre><code>Source GeoIP: Unknown,Destination GeoIP: Unknown,GET / HTTP/1.1\r\n,\r\n
Source GeoIP: Unknown,Destination GeoIP: Unknown,HTTP/1.1 200 OK\r\n,\r\n,HTTP chunked response,Data
 chunk (7516 octets),Data chunk (8192 octets),Data chunk (4307 octets),End of chunked encoding,\r\n,
Content-encoded entity body (gzip): 20015 bytes -&gt; 107148 bytes, [truncated] The first few bytes of the http
response. If I keep going on and on and on and on and on and on and on and on and on and on and on</code></pre><p>Is there a way to get the non-truncated text using <code>tshark</code>?</p></div><div id="question-tags" class="tags-container tags">encryption tshark compression</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '15, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/87d59b2f90fcd8644828f5662aad806f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dishesmolasse&#39;s gravatar image" /><p>dishesmolasse<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dishesmolasse has no accepted answers">0%</span></p></div></div><div id="comments-container-46634" class="comments-container"></div><div id="comment-tools-46634" class="comment-tools"></div><div class="clear"></div><div id="comment-46634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46731"></span>

<div id="answer-container-46731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46731-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please see my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/43023/want-to-use-tshark-to-decode-a-specific-packet-and-do-not-truncate-lines">https://ask.wireshark.org/questions/43023/want-to-use-tshark-to-decode-a-specific-packet-and-do-not-truncate-lines</a><br />
</p></blockquote><p>I did not try, but maybe the 'follow' option might work as well in 2.1.0 incl. decompression (as I said, <strong>not</strong> tested, just speculation).</p><blockquote><p>tshark -nr input.pcap ... -z follow,tcp,ascii,1</p></blockquote><p>Please replace 1 with the correct TCP stream number.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Oct '15, 16:49</p></div></div><div id="comments-container-46731" class="comments-container"></div><div id="comment-tools-46731" class="comment-tools"></div><div class="clear"></div><div id="comment-46731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

