+++
type = "question"
title = "tshark http dissection of captured dump"
description = '''Hi,  please I have the following challenges using Tshark, though I have achieved it in wireshark, but it cost me too many time. So want to autorun tshark to do same. But I have been having difficulty achieving any.  merge and filter series of dumped traffic for sequence of IP addressed (example 10.1...'''
date = "2013-08-22T21:22:00Z"
lastmod = "2013-08-25T10:10:00Z"
weight = 23971
keywords = [ "http", "csv", "request", "tshark", "dissection" ]
aliases = [ "/questions/23971" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark http dissection of captured dump](/questions/23971/tshark-http-dissection-of-captured-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23971-score" class="post-score" title="current number of votes">0</div><span id="post-23971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>please I have the following challenges using Tshark, though I have achieved it in wireshark, but it cost me too many time. So want to autorun tshark to do same. But I have been having difficulty achieving any.</p><ol><li>merge and filter series of dumped traffic for sequence of IP addressed (example 10.1.1.2, 10.2.4.12, 10.5.3.6 and so on), combined with same argument (as in "http.request.method==GET or ((tcp.flag.syn==1 &amp;&amp; tcp.flag.ack==0 &amp;&amp; tcp.port==443) or (tcp.flag.syn==1 &amp;&amp; tcp.flag.ack==0 &amp;&amp; tcp.port==22) ).</li><li>export this filtered output as a .csv file.</li></ol><p>Please how can I do it... in tshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '13, 21:22</strong></p><img src="https://secure.gravatar.com/avatar/981f5e7be0c0e73e3f429d0038fb3eed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hunted&#39;s gravatar image" /><p><span>Hunted</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hunted has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Aug '13, 01:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-23971" class="comments-container"></div><div id="comment-tools-23971" class="comment-tools"></div><div class="clear"></div><div id="comment-23971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23997"></span>

<div id="answer-container-23997" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23997-score" class="post-score" title="current number of votes">1</div><span id="post-23997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The display filter part would be the same for Wireshark and Tshark. You can set the display filter for tshark with the option "-Y" (or "-R" in versions up to 1.8):</p><pre><code>tshark -r &lt;file&gt; -Y &quot;(ip.addr==10.1.1.2 or ip.addr==10.2.4.12 or ip.addr==10.5.3.6) and (&quot;http.request.method==GET or (tcp.flag.syn==1 &amp;&amp; tcp.flag.ack==0 &amp;&amp; tcp.port==443) or (tcp.flag.syn==1 &amp;&amp; tcp.flag.ack==0 &amp;&amp; tcp.port==22) )&quot;</code></pre><p>As for the CSV output, have a look at the -T field options of tshark:</p><pre><code>  -T pdml|ps|psml|text|fields
                           format of text output (def: text)
  -e &lt;field&gt;               field to print if -Tfields selected (e.g. tcp.port, col.Info);
                           this option can be repeated to print multiple fields
  -E&lt;fieldsoption&gt;=&lt;value&gt; set options for output when -Tfields selected:
     header=y|n            switch headers on and off
     separator=/t|/s|&lt;char&gt; select tab, space, printable character as separator
     occurrence=f|l|a      print first, last or all occurrences of each field
     aggregator=,|/s|&lt;char&gt; select comma, space, printable character as
                           aggregator
     quote=d|s|n           select double, single, no quotes for values</code></pre><p>(from "tshark -h")</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23997" class="comments-container"><span id="24026"></span><div id="comment-24026" class="comment"><div id="post-24026-score" class="comment-score"></div><div class="comment-text"><p>thanks, its now working...</p><p>tshark -r &lt;file&gt; -Y "(ip.addr==10.1.1.2 or ip.addr==10.2.4.12 or ip.addr==10.5.3.6) and ("http.request.method==GET" or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==443) or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==22) )"</p><p>However, I have another challenge. when i attempt to autorun this code using batch file process (using windows), I discovered that it does not accept it, rather it attempts to capture the traffic on my network. I want it to dissect the specified file. Is there a way to instruct it (tshark) to dissect the given file, and not to capture another traffic..?</p><p>Thanks in anticipation of your response.</p></div><div id="comment-24026-info" class="comment-info"><span class="comment-age">(25 Aug '13, 09:38)</span> <span class="comment-user userinfo">Hunted</span></div></div><span id="24029"></span><div id="comment-24029" class="comment"><div id="post-24029-score" class="comment-score"></div><div class="comment-text"><p>Your other challenge has been converted into a separate question; that's how a Q&amp;A site such as this should work (Q&amp;A sites aren't forums).</p></div><div id="comment-24029-info" class="comment-info"><span class="comment-age">(25 Aug '13, 10:10)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-23997" class="comment-tools"></div><div class="clear"></div><div id="comment-23997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

