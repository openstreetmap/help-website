+++
type = "question"
title = "Specific IP address display filter using tshark"
description = '''I&#x27;m running into issues regarding the use of ip.src as a display filter argument in tshark. The filter works perfectly fine when used with wireshark, I&#x27;m not sure if I&#x27;m missing something for it&#x27;s use with tshark though. In wireshark: ip.src==192.168.0.10 tshark: tshark -r example.pcap -T fields -e ...'''
date = "2015-08-27T13:11:00Z"
lastmod = "2015-08-27T14:18:00Z"
weight = 45418
keywords = [ "tshark", "ip.src" ]
aliases = [ "/questions/45418" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Specific IP address display filter using tshark](/questions/45418/specific-ip-address-display-filter-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45418-score" class="post-score" title="current number of votes">1</div><span id="post-45418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running into issues regarding the use of ip.src as a display filter argument in tshark. The filter works perfectly fine when used with wireshark, I'm not sure if I'm missing something for it's use with tshark though.</p><p>In wireshark: <code>ip.src==192.168.0.10</code></p><p>tshark: <code>tshark -r example.pcap -T fields -e frame.time -e ip.src==192.168.0.10 http or http2</code></p><p>The tshark command works fine when just using ip.src to filter the source IP addresses(<code>tshark -r example.pcap -T fields -e frame.time -e ip.src http or http2</code>), it's only when used in order to filter a specific IP address.</p><p>I've also tried: <code>tshark -r example.pcap -T fields -e frame.time -e ip.src==192.168.0.0/24 http or http2</code></p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-ip.src" rel="tag" title="see questions tagged &#39;ip.src&#39;">ip.src</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '15, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/6706dcd3c17a4d870b3a0d633c541c92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbm&#39;s gravatar image" /><p><span>tbm</span><br />
<span class="score" title="29 reputation points">29</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '15, 13:11</strong> </span></p></div></div><div id="comments-container-45418" class="comments-container"></div><div id="comment-tools-45418" class="comment-tools"></div><div class="clear"></div><div id="comment-45418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45422"></span>

<div id="answer-container-45422" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45422-score" class="post-score" title="current number of votes">2</div><span id="post-45422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tbm has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't apply a filter to a <code>-e</code> field output specification, in addition to supply a display filter you must use the <code>-Y</code> option</p><p>To print out the ip.src field and filter for ip.src you need something like (untested):</p><pre><code>... -e ip.src -Y &quot;ip.src == 192.168.0.10 and (http or http2)&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45422" class="comments-container"><span id="45425"></span><div id="comment-45425" class="comment"><div id="post-45425-score" class="comment-score"></div><div class="comment-text"><p>Thanks! Works perfectly!</p></div><div id="comment-45425-info" class="comment-info"><span class="comment-age">(27 Aug '15, 14:18)</span> <span class="comment-user userinfo">tbm</span></div></div></div><div id="comment-tools-45422" class="comment-tools"></div><div class="clear"></div><div id="comment-45422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

