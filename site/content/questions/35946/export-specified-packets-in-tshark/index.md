+++
type = "question"
title = "&quot;Export specified packets&quot; in tshark."
description = '''In wireshark there is an option &quot;Export specified packets&quot;. How can I do this in thsark? Is there a command that can export/save filtred packets in a new .pcap file?'''
date = "2014-09-03T01:42:00Z"
lastmod = "2014-09-04T00:59:00Z"
weight = 35946
keywords = [ "save", "export", "tshark", "command-line", "wireshark" ]
aliases = [ "/questions/35946" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# ["Export specified packets" in tshark.](/questions/35946/export-specified-packets-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35946-score" class="post-score" title="current number of votes">1</div><span id="post-35946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In wireshark there is an option "Export specified packets". How can I do this in thsark? Is there a command that can export/save filtred packets in a new .pcap file?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '14, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/d37010d6d63374fe35a5fcfba121dedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anhtuan&#39;s gravatar image" /><p><span>anhtuan</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anhtuan has no accepted answers">0%</span></p></div></div><div id="comments-container-35946" class="comments-container"></div><div id="comment-tools-35946" class="comment-tools"></div><div class="clear"></div><div id="comment-35946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35985"></span>

<div id="answer-container-35985" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35985-score" class="post-score" title="current number of votes">2</div><span id="post-35985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="anhtuan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are tshark commands that can, given a filter in the "display filter" syntax", read a capture file and write out to another file the packets matched by the filter, such as</p><pre><code>tshark -Y {filter} -r {input file} -w {output file}</code></pre><p>and</p><pre><code>tshark -2 -R {filter} -r {input file} -w {output file}</code></pre><p>The second example is more like "Export specified packets" with <code>{filter}</code> as the display filter and with "All packets" and "Displayed" selected, although it's slower as it has to read the file twice.</p><p>You can also use <code>editcap</code> if you want to select the packets using ranges of packet numbers rather than a filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '14, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-35985" class="comments-container"><span id="35988"></span><div id="comment-35988" class="comment"><div id="post-35988-score" class="comment-score"></div><div class="comment-text"><p>Thanks! This solved my problem.</p></div><div id="comment-35988-info" class="comment-info"><span class="comment-age">(04 Sep '14, 00:59)</span> <span class="comment-user userinfo">anhtuan</span></div></div></div><div id="comment-tools-35985" class="comment-tools"></div><div class="clear"></div><div id="comment-35985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

