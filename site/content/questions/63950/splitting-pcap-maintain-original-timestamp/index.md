+++
type = "question"
title = "Splitting PCAP: Maintain original timestamp?"
description = '''Hi, I&#x27;m trying to split a large PCAP by limiting each output file to 5 million packets using the EditCap CLI. I use command &quot;editcap -c 5000000 inputFilePath outputFilePath&quot; and some sort of split occurs. But when I tshark the resulting files, they each seem to start at index 1 in the first column, ...'''
date = "2017-10-16T18:37:00Z"
lastmod = "2017-10-17T07:38:00Z"
weight = 63950
keywords = [ "editcap", "pcap" ]
aliases = [ "/questions/63950" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Splitting PCAP: Maintain original timestamp?](/questions/63950/splitting-pcap-maintain-original-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63950-score" class="post-score" title="current number of votes">0</div><span id="post-63950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to split a large PCAP by limiting each output file to 5 million packets using the EditCap CLI. I use command "editcap -c 5000000 inputFilePath outputFilePath" and some sort of split occurs. But when I tshark the resulting files, they each seem to start at index 1 in the first column, and at time 0 in the 2nd column. Is there a way to maintain the original values for either of these first two columns? Need the time to be maintained at least constant from the original file.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '17, 18:37</strong></p><img src="https://secure.gravatar.com/avatar/114ef72f685e2f473dc68e1b91dab133?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="someDude&#39;s gravatar image" /><p><span>someDude</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="someDude has no accepted answers">0%</span></p></div></div><div id="comments-container-63950" class="comments-container"></div><div id="comment-tools-63950" class="comment-tools"></div><div class="clear"></div><div id="comment-63950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63956"></span>

<div id="answer-container-63956" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63956-score" class="post-score" title="current number of votes">0</div><span id="post-63956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="someDude has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The index is the index into that particular file, so no, that will always start at 1.</p><p>The time is the time from the previous packet in that particular file, so no, that will always start at 0</p><p>As you remark that the 'time to be maintained at least constant from the original file' I assume you mean that you want to keep the original wall clock timestamps. That in fact is happening, you would have to select the timestamp output to print the wall clock time instead of time since previous packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '17, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63956" class="comments-container"><span id="63961"></span><div id="comment-63961" class="comment"><div id="post-63961-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I'm checking out <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkTimeFormatsSection.html">https://www.wireshark.org/docs/wsug_html_chunked/ChWorkTimeFormatsSection.html</a> regarding timestamp formats. Do you know if the format can be selected after i already have the original pcap file, or is the formatting some setting that needs to be specified prior to capturing the packets? Will accept answer when get these specifics figured out</p></div><div id="comment-63961-info" class="comment-info"><span class="comment-age">(17 Oct '17, 05:20)</span> <span class="comment-user userinfo">someDude</span></div></div><span id="63962"></span><div id="comment-63962" class="comment"><div id="post-63962-score" class="comment-score"></div><div class="comment-text"><p>The time format sets how timestamps are displayed, it does NOT affect the timestamps in the file.</p></div><div id="comment-63962-info" class="comment-info"><span class="comment-age">(17 Oct '17, 05:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63966"></span><div id="comment-63966" class="comment"><div id="post-63966-score" class="comment-score"></div><div class="comment-text"><p>Just add another column for Absolute Time: <em>Edit -&gt; Preferences -&gt; Columns -&gt; + -&gt; Absolute date, as YYYY-MM-DD, and time</em> Rename the column and drag it to whatever location in the list you like. You can have multiple time format columns.</p></div><div id="comment-63966-info" class="comment-info"><span class="comment-age">(17 Oct '17, 06:45)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="63968"></span><div id="comment-63968" class="comment"><div id="post-63968-score" class="comment-score"></div><div class="comment-text"><p>Ok thanks, so I'll check into splitting the file, then rendering the times in Absolute format via <a href="https://ask.wireshark.org/questions/30393/tshark-how-to-output-date-in-iso-format">https://ask.wireshark.org/questions/30393/tshark-how-to-output-date-in-iso-format</a> . Cannot really use the WS UI for this purpose since I need to automate this.</p></div><div id="comment-63968-info" class="comment-info"><span class="comment-age">(17 Oct '17, 07:38)</span> <span class="comment-user userinfo">someDude</span></div></div></div><div id="comment-tools-63956" class="comment-tools"></div><div class="clear"></div><div id="comment-63956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

