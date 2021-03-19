+++
type = "question"
title = "text2pcap is not converting diameter trace"
description = '''Dear Team, I am trying read diameter pcap dump with tshark by filtering with &quot;session ID&quot; and redirected the output to /tmp folder, when i convert this file (HEX or ASCII) to pcap in text2pcap, it is showing wrong protocols.. tshark -x -r InputFile.pcap -V &quot;diameter.Session-Id == &#92;&quot;MMEC78.MMEGI8024&#92;...'''
date = "2017-02-21T06:43:00Z"
lastmod = "2017-03-13T09:29:00Z"
weight = 59581
keywords = [ "text2pcap", "diameter", "tshark" ]
aliases = [ "/questions/59581" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [text2pcap is not converting diameter trace](/questions/59581/text2pcap-is-not-converting-diameter-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59581-score" class="post-score" title="current number of votes">0</div><span id="post-59581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Team, I am trying read diameter pcap dump with tshark by filtering with "session ID" and redirected the output to /tmp folder, when i convert this file (HEX or ASCII) to pcap in text2pcap, it is showing wrong protocols..</p><p>tshark -x -r InputFile.pcap -V "diameter.Session-Id == \"MMEC78.MMEGI8024\" &gt; /tmp/filter (-x used for saving in HEX)</p><p>text2pcap filter outut.pcap ---&gt;here my file is converted but it opens in Ethernet/TDMoP/anyother protocols, instead of Diameter..I found this problem with diameter trace file only as this method works fine for my other protocol trace file example.GSM_MAP trace..</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_VxX9XTi.JPG" alt="alt text" /></p><p>please help...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '17, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/746454f41d14403415dece210aba20d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudheer628&#39;s gravatar image" /><p><span>sudheer628</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudheer628 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-59581" class="comments-container"></div><div id="comment-tools-59581" class="comment-tools"></div><div class="clear"></div><div id="comment-59581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59667"></span>

<div id="answer-container-59667" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59667-score" class="post-score" title="current number of votes">0</div><span id="post-59667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Answer: Got the solution by friend, that my tshark is reading pcap in HEX &amp; non HEX data format, text2pcap is unable to recognize non HEX data..issue resolved by using proper encapsulation type. we used below command which simply consider HEX format only</p><p>text2pcap -l 113 input output.pcap (where 113 represents the encapsulation of Linux trace)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '17, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/746454f41d14403415dece210aba20d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudheer628&#39;s gravatar image" /><p><span>sudheer628</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudheer628 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '17, 00:05</strong> </span></p></div></div><div id="comments-container-59667" class="comments-container"><span id="60034"></span><div id="comment-60034" class="comment"><div id="post-60034-score" class="comment-score"></div><div class="comment-text"><p>Hi, did you attempt for IPv4 or IPv6 ? If IPv6 could you please help with some more details ? thanks in advance</p></div><div id="comment-60034-info" class="comment-info"><span class="comment-age">(13 Mar '17, 09:29)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div></div><div id="comment-tools-59667" class="comment-tools"></div><div class="clear"></div><div id="comment-59667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60031"></span>

<div id="answer-container-60031" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60031-score" class="post-score" title="current number of votes">0</div><span id="post-60031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html"><code>text2pcap</code></a> man page indicates, you can use the <code>-a</code> option:</p><p><em>Enables ASCII text dump identification. It allows to identify the start of the ASCII text dump and not include it in the packet even if it looks like HEX.</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '17, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-60031" class="comments-container"></div><div id="comment-tools-60031" class="comment-tools"></div><div class="clear"></div><div id="comment-60031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

