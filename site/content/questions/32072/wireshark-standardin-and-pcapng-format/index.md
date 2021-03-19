+++
type = "question"
title = "wireshark standardin and pcapng format."
description = '''I&#x27;m trying to send a pcapng format file to wireshark standard in or a named pipe, but I continue to get an error &quot;unrecognized libcap format. Is there still a problem reading this type file through this interface?  My command looks like this: cat capture_NG.pcap | wireshark -k -i - I&#x27;ve also tried: ...'''
date = "2014-04-22T16:54:00Z"
lastmod = "2014-04-23T11:53:00Z"
weight = 32072
keywords = [ "pipe", "input", "pcapng", "standard" ]
aliases = [ "/questions/32072" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark standardin and pcapng format.](/questions/32072/wireshark-standardin-and-pcapng-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32072-score" class="post-score" title="current number of votes">0</div><span id="post-32072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to send a pcapng format file to wireshark standard in or a named pipe, but I continue to get an error "unrecognized libcap format. Is there still a problem reading this type file through this interface?</p><p>My command looks like this:</p><p>cat capture_NG.pcap | wireshark -k -i -</p><p>I've also tried:</p><p>wireshark -k -i &lt;(cat capture_NG.pcap)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-input" rel="tag" title="see questions tagged &#39;input&#39;">input</span> <span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-standard" rel="tag" title="see questions tagged &#39;standard&#39;">standard</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '14, 16:54</strong></p><img src="https://secure.gravatar.com/avatar/1607659be497d8c263c7061a0dd9159b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="siber&#39;s gravatar image" /><p><span>siber</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="siber has no accepted answers">0%</span></p></div></div><div id="comments-container-32072" class="comments-container"></div><div id="comment-tools-32072" class="comment-tools"></div><div class="clear"></div><div id="comment-32072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32115"></span>

<div id="answer-container-32115" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32115-score" class="post-score" title="current number of votes">0</div><span id="post-32115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the wireshark man page: <a href="http://www.wireshark.org/docs/man-pages/wireshark.html">http://www.wireshark.org/docs/man-pages/wireshark.html</a></p><pre><code>Data read from pipes must be in standard libpcap format.</code></pre><p>Wireshark cannot read pcap-ng files from STDIN (or pipes in general). So, please convert your pcan-ng capture file to libpcap format (you can use <a href="http://www.wireshark.org/docs/man-pages/editcap.html">editcap</a>). Then you should be able to pipe the file into Wireshark.</p><p><strong>However:</strong> The way you are using the file, you don't need a pipe at all. You can just read the capture file directly into Wireshark.</p><blockquote><p>wireshark -nr capture_NG.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '14, 11:53</strong> </span></p></div></div><div id="comments-container-32115" class="comments-container"></div><div id="comment-tools-32115" class="comment-tools"></div><div class="clear"></div><div id="comment-32115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

