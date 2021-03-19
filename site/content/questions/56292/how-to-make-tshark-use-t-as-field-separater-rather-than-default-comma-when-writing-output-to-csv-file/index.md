+++
type = "question"
title = "How to make tshark use &#92;t as field separater, rather than default comma, when writing output to csv file?"
description = '''I have described the problem I face when tshark uses , as a field delimiter in this question when writing output to a .csv file. So I&#x27;d like a way to instruct Tshark to use another character, say &#92;t, as field separator.  The normal Tshark command is something like: tshark -r inputFile.pcap -T fields...'''
date = "2016-10-11T00:06:00Z"
lastmod = "2016-10-11T00:43:00Z"
weight = 56292
keywords = [ "csv", "tshark", "export-to-csv", "wireshark" ]
aliases = [ "/questions/56292" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to make tshark use \\t as field separater, rather than default comma, when writing output to csv file?](/questions/56292/how-to-make-tshark-use-t-as-field-separater-rather-than-default-comma-when-writing-output-to-csv-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56292-score" class="post-score" title="current number of votes">0</div><span id="post-56292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have described the problem I face when tshark uses <code>,</code> as a field delimiter <a href="https://ask.wireshark.org/questions/56289/problem-using-tshark-to-write-fields-to-csv-file-tshark-breaks-a-field-value-into-2-values-if-it-has-a-comma-character">in this question</a> when writing output to a <code>.csv</code> file.</p><p>So I'd like a way to instruct Tshark to use another character, say <code>\t</code>, as field separator.</p><p>The normal Tshark command is something like:</p><pre><code>tshark -r inputFile.pcap -T fields -e fieldA -e fieldB -e fieldC &gt; outputFile.csv</code></pre><p><strong>What do I add to this command to instruct tshark to use <code>\t</code> as field separator, while writing the output to <code>.csv</code> file, rather than the default <code>,</code></strong>?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-export-to-csv" rel="tag" title="see questions tagged &#39;export-to-csv&#39;">export-to-csv</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '16, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p><span>Jesss</span><br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div></div><div id="comments-container-56292" class="comments-container"></div><div id="comment-tools-56292" class="comment-tools"></div><div class="clear"></div><div id="comment-56292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56294"></span>

<div id="answer-container-56294" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56294-score" class="post-score" title="current number of votes">1</div><span id="post-56294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jesss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As per the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark manual</a> or even built-in help; <code>tshark -h</code>:</p><pre><code>  -E&lt;fieldsoption&gt;=&lt;value&gt; set options for output when -Tfields selected:
     bom=y|n               print a UTF-8 BOM
     header=y|n            switch headers on and off
     separator=/t|/s|&lt;char&gt; select tab, space, printable character as separator
     occurrence=f|l|a      print first, last or all occurrences of each field
     aggregator=,|/s|&lt;char&gt; select comma, space, printable character as
                       aggregator</code></pre><p>so, use <code>-E separator=/t</code>, you might also want to consider adding quotes around fields, e.g. <code>-E quote=d</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '16, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '16, 00:44</strong> </span></p></div></div><div id="comments-container-56294" class="comments-container"></div><div id="comment-tools-56294" class="comment-tools"></div><div class="clear"></div><div id="comment-56294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

