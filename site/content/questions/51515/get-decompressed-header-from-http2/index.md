+++
type = "question"
title = "Get decompressed header from http2"
description = '''Anyone knows a way to get just the decompressed headers for http2 from a capture with tshark? So far I got this command: tshark -r somefile.pcap -o &quot;ssl.keylog_file:sslkeylog.log&quot; -x -Y &quot;http2&quot; &amp;gt; output.txt But this gives me the Hexdumb and Ascii of the frame, the decrypted ssl data and the decom...'''
date = "2016-04-08T07:44:00Z"
lastmod = "2016-04-12T04:14:00Z"
weight = 51515
keywords = [ "decompressed_headers", "tshark", "https", "ssl_decrypt" ]
aliases = [ "/questions/51515" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get decompressed header from http2](/questions/51515/get-decompressed-header-from-http2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51515-score" class="post-score" title="current number of votes">0</div><span id="post-51515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anyone knows a way to get just the decompressed headers for http2 from a capture with tshark? So far I got this command:<br />
tshark -r somefile.pcap -o "ssl.keylog_file:sslkeylog.log" -x -Y "http2" &gt; output.txt<br />
But this gives me the Hexdumb and Ascii of the frame, the decrypted ssl data and the decompressed header inside the ssl data. Now I would like to just get the decompressed headers, cause the rest is not readable anyways (for most of the part).</p><p>Thanks for any help in advance :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decompressed_headers" rel="tag" title="see questions tagged &#39;decompressed_headers&#39;">decompressed_headers</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '16, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/1683ee6ee87a65cb866ff23869f5de45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monkey521&#39;s gravatar image" /><p><span>monkey521</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monkey521 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-51515" class="comments-container"></div><div id="comment-tools-51515" class="comment-tools"></div><div class="clear"></div><div id="comment-51515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51517"></span>

<div id="answer-container-51517" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51517-score" class="post-score" title="current number of votes">1</div><span id="post-51517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="monkey521 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The decompressed headers for HTTP/2 need to be interpreted in a special way. You can obtain the full, verbose HTTP/2 interpretation with:</p><pre><code>tshark -r somefile.pcap -o ssl.keylog_file:sslkeylog.log -Y http2 -O http2</code></pre><p>Alternatively, you can select the fields (and post-process them to pair header names and values):</p><pre><code>tshark -r somefile.pcap -o ssl.keylog_file:sslkeylog.log -Y http2 -Tfields -e http2.header.name -e http2.header.value</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '16, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-51517" class="comments-container"><span id="51591"></span><div id="comment-51591" class="comment"><div id="post-51591-score" class="comment-score"></div><div class="comment-text"><p>thank you very much! :)</p></div><div id="comment-51591-info" class="comment-info"><span class="comment-age">(12 Apr '16, 04:14)</span> <span class="comment-user userinfo">monkey521</span></div></div></div><div id="comment-tools-51517" class="comment-tools"></div><div class="clear"></div><div id="comment-51517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

