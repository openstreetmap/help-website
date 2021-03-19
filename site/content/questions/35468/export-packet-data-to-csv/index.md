+++
type = "question"
title = "Export packet data to CSV"
description = '''I am trying to export the packet list information, to include the packet data, to a CSV file. In the Packet Details view, I have right-clicked on the expanded Data element and selected &#x27;Apply as Column&#x27;. - Data (57 bytes)  Data: 39000000000000003152415200000000420d000000000000... &amp;lt;-- this is what...'''
date = "2014-08-13T13:47:00Z"
lastmod = "2014-09-17T17:05:00Z"
weight = 35468
keywords = [ "csv", "export", "payload", "data.data" ]
aliases = [ "/questions/35468" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Export packet data to CSV](/questions/35468/export-packet-data-to-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35468-score" class="post-score" title="current number of votes">1</div><span id="post-35468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to export the packet list information, to include the packet data, to a CSV file. In the Packet Details view, I have right-clicked on the expanded Data element and selected 'Apply as Column'.</p><pre><code>- Data (57 bytes)
    Data: 39000000000000003152415200000000420d000000000000...   &lt;-- this is what I right-clicked
    [Length: 57]</code></pre><p>Looking at the column preferences, I see a new column of Custom type named 'Data' that uses the field name of 'data.data'. Here's what I see in the 'Data' column for the selected packet:</p><pre><code>39000000000000003152415200000000420d000000000000...</code></pre><p>When I export the Packet Dissections as CSV, the 'Data' column has just this exact text, but I really want the full data, i.e., without the ellipsis.</p><p>Is there a way to achieve this? I'm using Wireshark v1.12.0.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-data.data" rel="tag" title="see questions tagged &#39;data.data&#39;">data.data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '14, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/b5c318e3277525e5f18c103ff9cf820d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matt%20Davis&#39;s gravatar image" /><p><span>Matt Davis</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matt Davis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Aug '14, 13:48</strong> </span></p></div></div><div id="comments-container-35468" class="comments-container"><span id="35469"></span><div id="comment-35469" class="comment"><div id="post-35469-score" class="comment-score"></div><div class="comment-text"><p>This question seems to be VERY similar to what I'm asking. <a href="https://ask.wireshark.org/questions/15531/datadata-shows-only-24byte">https://ask.wireshark.org/questions/15531/datadata-shows-only-24byte</a></p></div><div id="comment-35469-info" class="comment-info"><span class="comment-age">(13 Aug '14, 13:50)</span> <span class="comment-user userinfo">Matt Davis</span></div></div><span id="36366"></span><div id="comment-36366" class="comment"><div id="post-36366-score" class="comment-score"></div><div class="comment-text"><p>I am also looking to do something like this. Did you figure out a way to do it?</p></div><div id="comment-36366-info" class="comment-info"><span class="comment-age">(16 Sep '14, 09:45)</span> <span class="comment-user userinfo">adercott</span></div></div></div><div id="comment-tools-35468" class="comment-tools"></div><div class="clear"></div><div id="comment-35468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36409"></span>

<div id="answer-container-36409" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36409-score" class="post-score" title="current number of votes">2</div><span id="post-36409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Matt Davis has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately I have no idea about the GUI issue with the shortened output, but if your main focus is dumping the data into a text/csv file I'd recommend using tshark with the -Tfields option to select and dump the columns of interest and eventually modifying the output to fit your needs.</p><p>e.g. <code>tshark -r trace1.pcap -Tfields -e frame.number -e ip.src -e ip.dst -e data.data &gt; output.txt</code></p><p>will dump the requeted fields (coloumns) into a text file seperated by I think a TAB space. If you want to you can easily change that by adding the -E separator= flag so that the output will be separated by a comma or another character of your choice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '14, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-36409" class="comments-container"><span id="36426"></span><div id="comment-36426" class="comment"><div id="post-36426-score" class="comment-score"></div><div class="comment-text"><p>Thanks, <span></span><span>@Landi</span>. I wish I could get answer about the UI, but in lieu of a better answer (i.e., at least one), I'll accept this one. ;)</p></div><div id="comment-36426-info" class="comment-info"><span class="comment-age">(17 Sep '14, 17:05)</span> <span class="comment-user userinfo">Matt Davis</span></div></div></div><div id="comment-tools-36409" class="comment-tools"></div><div class="clear"></div><div id="comment-36409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

