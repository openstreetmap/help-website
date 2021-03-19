+++
type = "question"
title = "xxxx bytes missing in capture file"
description = '''Hello im trying to capture traffic and after saving and uploading pcap file i get this alert on tcp stream: [1285 bytes missing in capture file] thanks in advance for any help. 2x2i'''
date = "2014-08-25T11:33:00Z"
lastmod = "2014-08-26T08:52:00Z"
weight = 35711
keywords = [ "follow.tcp.stream", "pcap", "error" ]
aliases = [ "/questions/35711" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [xxxx bytes missing in capture file](/questions/35711/xxxx-bytes-missing-in-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35711-score" class="post-score" title="current number of votes">0</div><span id="post-35711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello im trying to capture traffic and after saving and uploading pcap file i get this alert on tcp stream:</p><p><code>[1285 bytes missing in capture file]</code></p><p>thanks in advance for any help.</p><p>2x2i</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '14, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/c9eb9c012e62cd9862a31a1406202fe1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="2x2i&#39;s gravatar image" /><p><span>2x2i</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="2x2i has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Aug '14, 08:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-35711" class="comments-container"><span id="35713"></span><div id="comment-35713" class="comment"><div id="post-35713-score" class="comment-score"></div><div class="comment-text"><p>Did you transfer as binary? ftp transfer as ASCII will mangle the file.</p></div><div id="comment-35713-info" class="comment-info"><span class="comment-age">(25 Aug '14, 11:36)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-35711" class="comment-tools"></div><div class="clear"></div><div id="comment-35711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35755"></span>

<div id="answer-container-35755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35755-score" class="post-score" title="current number of votes">0</div><span id="post-35755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This usually indicates that some frames (packets) in a TCP connection weren't captured (and you're doing "follow TCP stream" to view what went back and forth on the socket). Rather than stopping when some bytes are missing, Wireshark continues to show the TCP stream but shows you where the data is incomplete.</p><p>To fix the problem you need to ensure you capture <em>all</em> the packets. Unfortunately this can be quite difficult to achieve in practice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-35755" class="comments-container"><span id="35759"></span><div id="comment-35759" class="comment"><div id="post-35759-score" class="comment-score"></div><div class="comment-text"><p>See the users related question as to why there may be missing bytes\packets: <a href="https://ask.wireshark.org/questions/35714/seeing-packet-size-limited-during-capture-with-ngenius-performance-manager-capture">https://ask.wireshark.org/questions/35714/seeing-packet-size-limited-during-capture-with-ngenius-performance-manager-capture</a></p></div><div id="comment-35759-info" class="comment-info"><span class="comment-age">(26 Aug '14, 08:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-35755" class="comment-tools"></div><div class="clear"></div><div id="comment-35755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

