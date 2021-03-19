+++
type = "question"
title = "Wireshark Release 2.2.1 and 2.1.0 export csv problem"
description = '''Hi, I was using wireshark 1.11.2 version and when i try to save data to CSV file, it crashed. I installed version 2.2.1 and later 2.1.0. It does not crash now but this time,when i chose File -&amp;gt; Export Packet Dissections -&amp;gt; As &quot;CSV&quot; and then checking the &quot;Packet bytes&quot;, i can not see any byte i...'''
date = "2016-10-26T06:46:00Z"
lastmod = "2016-10-26T13:28:00Z"
weight = 56693
keywords = [ "csv", "export" ]
aliases = [ "/questions/56693" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Release 2.2.1 and 2.1.0 export csv problem](/questions/56693/wireshark-release-221-and-210-export-csv-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56693-score" class="post-score" title="current number of votes">0</div><span id="post-56693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was using wireshark 1.11.2 version and when i try to save data to CSV file, it crashed. I installed version 2.2.1 and later 2.1.0. It does not crash now but this time,when i chose File -&gt; Export Packet Dissections -&gt; As "CSV" and then checking the "Packet bytes", i can not see any byte information on CSV file. It records just headings. Should i do anything else to see bytes? or these versions also have a bug about that.</p><p>And Also i have a dissector to use interpret my own protocol. I want to see interpretted data on CSV. Is that possible? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '16, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/fa0d88356c0486c4477fc7892b2de25e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saniye&#39;s gravatar image" /><p><span>saniye</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saniye has no accepted answers">0%</span></p></div></div><div id="comments-container-56693" class="comments-container"></div><div id="comment-tools-56693" class="comment-tools"></div><div class="clear"></div><div id="comment-56693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56711"></span>

<div id="answer-container-56711" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56711-score" class="post-score" title="current number of votes">0</div><span id="post-56711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've just double-checked, the <code>File -&gt; Export Packet Dissections -&gt; As CSV...</code> only exports the information shown in the packet list pane. So by adding some packet fields as custom columns of the packet list, you can have them saved as csv, but to my knowledge packet bytes cannot be referred to as a field of the <code>frame</code> "protocol". The settings controlling the output contents in the generic "Export Packet Dissections" are largely ignored for Export as CSV.</p><p>As for the other part of your question, if your own dissector is written properly and creates proper protocol fields into the dissection tree rather than just text labels, then these fields are handled the same way as the fields generated by any "embedded" dissector. So you can use them in display filters, make them columns in packet list, ask tshark to print them using the <code>-T fields -e field_name</code> command line parameters, they are exported into the PDML format, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '16, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56711" class="comments-container"><span id="56713"></span><div id="comment-56713" class="comment"><div id="post-56713-score" class="comment-score"></div><div class="comment-text"><p><span>@saniye</span>, just to make sure the info reaches you, your comment hasn't vanished spontaneously from the other Question, I've removed it from there as you've properly replaced it with this Question.</p></div><div id="comment-56713-info" class="comment-info"><span class="comment-age">(26 Oct '16, 13:28)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-56711" class="comment-tools"></div><div class="clear"></div><div id="comment-56711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

