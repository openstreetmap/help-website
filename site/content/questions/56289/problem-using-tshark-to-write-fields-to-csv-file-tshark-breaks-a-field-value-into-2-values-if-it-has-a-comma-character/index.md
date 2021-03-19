+++
type = "question"
title = "Problem using Tshark to write fields to csv file: Tshark breaks a field value into 2 values if it has a comma character"
description = '''I have some network traffic in the form of a .pcap file. It has around 5000 packets. I have to read some 50 fields from it (like Arrival time, Source IP, Destination IP) etc. and dump them into a MySQL database.  The method I have tried to use is using Tshark to extract the fields I am interested in...'''
date = "2016-10-10T21:31:00Z"
lastmod = "2016-10-10T22:18:00Z"
weight = 56289
keywords = [ "field", "csv", "tshark", "export-to-csv", "wireshark" ]
aliases = [ "/questions/56289" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem using Tshark to write fields to csv file: Tshark breaks a field value into 2 values if it has a comma character](/questions/56289/problem-using-tshark-to-write-fields-to-csv-file-tshark-breaks-a-field-value-into-2-values-if-it-has-a-comma-character)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56289-score" class="post-score" title="current number of votes">0</div><span id="post-56289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some network traffic in the form of a <code>.pcap</code> file. It has around 5000 packets. I have to read some 50 fields from it (like Arrival time, Source IP, Destination IP) etc. and dump them into a <code>MySQL</code> database.</p><p>The method I have tried to use is using Tshark to extract the fields I am interested in, and write them into a <code>.csv</code> file. Then I could use <a href="http://dev.mysql.com/doc/refman/5.7/en/load-data.html">a single <code>SQL</code> query</a> to dump the contents of <code>.csv</code> file into the database. So the command looks something like</p><pre><code>tshark -r my-file.pcap -T fields -e frame.time ... -e ip.src -e ip.dst &gt; outputfile.csv</code></pre><p><strong>The problem with this is that tshark does not parse the values of fields properly when putting them into the <code>.csv</code> file.</strong> For example, when it finds a comma (<code>,</code>) character occuring within a value, it breaks the value there, puts the part of the value occurring before the <code>,</code> into that field, and puts the rest of the value (i.e. the part occuring next to <code>,</code>) into the next field, and so the actual value of the next field goes into the field next to the next field, and so on...</p><p>For example if there are two fields: <code>frame.time</code> with a value of <code>Jun 23, 2016 08:15:00.844245000</code> and <code>ip.src</code> with a value of <code>X.X.X.X</code>, then this is what <code>.csv</code> file looks like:</p><pre><code>frame.time        src.ip
Jun 23            2016 08:15:00.844245000        X.X.X.X</code></pre><p>and this is how it turns out in the database table:</p><pre><code>__________________________________________________
|| frame.time    ||    src.ip                   ||
|| Jun 23        ||    2016 08:15:00.844245000  ||
|| X.X.X.X       ||    NULL                     ||</code></pre><p><strong>The question is that how do I fix this?</strong> Any tips/suggestions/advice is welcome.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-export-to-csv" rel="tag" title="see questions tagged &#39;export-to-csv&#39;">export-to-csv</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '16, 21:31</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p><span>Jesss</span><br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Oct '16, 22:06</strong> </span></p></div></div><div id="comments-container-56289" class="comments-container"></div><div id="comment-tools-56289" class="comment-tools"></div><div class="clear"></div><div id="comment-56289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56290"></span>

<div id="answer-container-56290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56290-score" class="post-score" title="current number of votes">0</div><span id="post-56290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not that tshark creates two instances of the field, it's that tshark does not treat fields which contain the comma symbol specially, so the commas from inside the fields are indistinguishable from the commas separating the instances of the same field for the application processing the csv.</p><p>Look at the <code>-E</code> command line option at <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>. You can change the separator of same field instances from comma to something else, and you can ask Wireshark to add quoting characters to each field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '16, 22:18</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56290" class="comments-container"></div><div id="comment-tools-56290" class="comment-tools"></div><div class="clear"></div><div id="comment-56290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

