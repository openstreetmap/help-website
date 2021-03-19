+++
type = "question"
title = "Change default header name when converting .pcap to .csv"
description = '''I convert .pcap file to .csv using following command: tshark -r %s -T fields -E separator=, -e frame.number -e frame.time_epoch -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e tcp.seq -e tcp.stream -e frame.len -e tcp.flags -e _ws.col.Info -E header=y -E quote=d -E occurrence=f &amp;gt; %s.csv How ...'''
date = "2017-08-16T09:02:00Z"
lastmod = "2017-08-16T12:19:00Z"
weight = 63474
keywords = [ "header", "csv", "tshark" ]
aliases = [ "/questions/63474" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Change default header name when converting .pcap to .csv](/questions/63474/change-default-header-name-when-converting-pcap-to-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63474-score" class="post-score" title="current number of votes">0</div><span id="post-63474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I convert .pcap file to .csv using following command:</p><p><code>tshark -r %s -T fields -E separator=, -e frame.number -e frame.time_epoch -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e tcp.seq -e tcp.stream -e frame.len -e tcp.flags -e _ws.col.Info -E header=y -E quote=d -E occurrence=f  &gt; %s.csv</code></p><p>How can I change header name?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '17, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/1595a24111dff7d0376d456e91895399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zahra&#39;s gravatar image" /><p><span>Zahra</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zahra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Aug '17, 09:02</strong> </span></p></div></div><div id="comments-container-63474" class="comments-container"></div><div id="comment-tools-63474" class="comment-tools"></div><div class="clear"></div><div id="comment-63474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63476"></span>

<div id="answer-container-63476" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63476-score" class="post-score" title="current number of votes">1</div><span id="post-63476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Zahra has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way is probably to rename them in Wireshark first and then re-run your <code>tshark</code> command. If you don't want to change the default column names in Wireshark, you could create a new profile for this purpose where you can specify the new column names and then just have <code>tshark</code> use that profile via the <code>-C</code> <code></code>&lt;<code>profile</code>&gt; option.</p><p>Alternatively, you could make use of the <code>"gui.column.format:...</code>" option to specify and name each column however you wish. Run <code>tshark -G column-formats</code> for more help with that.</p><p>See the <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark man page</code></a> for more information on all <code>tshark</code> options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '17, 12:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-63476" class="comments-container"></div><div id="comment-tools-63476" class="comment-tools"></div><div class="clear"></div><div id="comment-63476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

