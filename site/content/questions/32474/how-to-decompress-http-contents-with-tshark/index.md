+++
type = "question"
title = "How to decompress http contents with tshark"
description = '''I have pcap files with http contents compressed by gzip, and want to export each stream to a text file. I know wireshark can export the uncompressed contents by GUI, but exporting each file manually is time wasting. I want to do this by tshark automatically. I tried followings: for stream in `tshark...'''
date = "2014-05-03T22:07:00Z"
lastmod = "2014-05-04T08:57:00Z"
weight = 32474
keywords = [ "gzipped", "decompression", "tshark" ]
aliases = [ "/questions/32474" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to decompress http contents with tshark](/questions/32474/how-to-decompress-http-contents-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32474-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have pcap files with http contents compressed by gzip, and want to export each stream to a text file. I know wireshark can export the uncompressed contents by GUI, but exporting each file manually is time wasting. I want to do this by tshark automatically.</p><p>I tried followings:</p><pre><code>for stream in `tshark -r input.pcap -T fields -e tcp.stream -2 -R http | sort -n | uniq`
do
  tshark -q -r input.pcap -o http.decompress_body:TRUE -z follow,tcp,ascii,$stream &gt; $stream.txt
done</code></pre><p>However, "-o http.decompress_body:TRUE" does not seem to work correctly.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags">gzipped decompression tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '14, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/ce5dd061c9114ad81c7189c97507a2a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hseisyu&#39;s gravatar image" /><p>hseisyu<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hseisyu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '14, 23:25</p></div></div><div id="comments-container-32474" class="comments-container"></div><div id="comment-tools-32474" class="comment-tools"></div><div class="clear"></div><div id="comment-32474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32484"></span>

<div id="answer-container-32484" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32484-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>However, "-o http.decompress_body:TRUE" does not seem to work correctly.</p></blockquote><p>the option does work, but the 'Follow TCP stream' function does <strong>not decompress</strong> the HTTP response, neither in Wireshark (GUI) nor in tshark (CLI), as that's not implemented yet. The 'Follow TCP stream' function just shows the contents of the TCP payload as it is transmitted over the wire.</p><p>There is an enhancement request:</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3528">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3528</a><br />
</p></blockquote><p>However, a patch that implemented the feature has never been accepted due to some problems.</p><p>So, if you need to extract the HTTP payload, including uncompressed HTTP responses, your options are:</p><ul><li>implement the feature yourself and submit the code</li><li>wait until the feature gets implemented by somebody</li><li>pay somebody to implement it for you</li><li>use a different tool, like one of those mentioned in the following questions/answers.</li></ul><blockquote><p><a href="http://ask.wireshark.org/questions/10023/command-line-option-for-follow-tcp-stream">http://ask.wireshark.org/questions/10023/command-line-option-for-follow-tcp-stream</a><br />
<a href="http://ask.wireshark.org/questions/23706/capturing-url-from-tcp-packets">http://ask.wireshark.org/questions/23706/capturing-url-from-tcp-packets</a><br />
<a href="http://ask.wireshark.org/questions/31557/how-to-extract-email-files">http://ask.wireshark.org/questions/31557/how-to-extract-email-files</a><br />
<a href="http://ask.wireshark.org/questions/26959/if-tshark-can-support-export-objects-like-wireshark-for-gui">http://ask.wireshark.org/questions/26959/if-tshark-can-support-export-objects-like-wireshark-for-gui</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '14, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-32484" class="comments-container"></div><div id="comment-tools-32484" class="comment-tools"></div><div class="clear"></div><div id="comment-32484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

