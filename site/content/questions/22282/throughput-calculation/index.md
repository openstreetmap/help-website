+++
type = "question"
title = "Throughput calculation"
description = '''Assuming I want to calculate throughputs (using commands) by applying different display filters on same file, I have to calculate capture time from &quot;capinfos -u&quot; and bytes from &quot;tshark -z io,stat,time,filter&quot; Is there any better way that I can get througput directly? I want to specify display filter...'''
date = "2013-06-24T07:51:00Z"
lastmod = "2013-06-24T10:38:00Z"
weight = 22282
keywords = [ "display-filter", "throughput", "tshark", "capinfos" ]
aliases = [ "/questions/22282" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Throughput calculation](/questions/22282/throughput-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22282-score" class="post-score" title="current number of votes">0</div><span id="post-22282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Assuming I want to calculate throughputs (using commands) by applying different display filters on same file, I have to calculate capture time from "capinfos -u" and bytes from "tshark -z io,stat,time,filter"</p><p>Is there any better way that I can get througput directly? I want to specify display filters in single command and get the throughut directly in a single command.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-capinfos" rel="tag" title="see questions tagged &#39;capinfos&#39;">capinfos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '13, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/e007baa1950a507d2163e10837a2861d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajat&#39;s gravatar image" /><p><span>Rajat</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajat has no accepted answers">0%</span></p></div></div><div id="comments-container-22282" class="comments-container"></div><div id="comment-tools-22282" class="comment-tools"></div><div class="clear"></div><div id="comment-22282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22283"></span>

<div id="answer-container-22283" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22283-score" class="post-score" title="current number of votes">2</div><span id="post-22283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about something like <code>'tshark -r ~/Wireshark/pcap/http.cap -qz io,stat,0,tcp.port==50261,tcp.port==50262,tcp.port==50263'</code> ?</p><p>It gives the following output:</p><pre><code>$ tshark -r ~/Wireshark/pcap/http.cap -qz io,stat,0,tcp.port==50261,tcp.port==50262,tcp.port==50263

======================================================================================
| IO Statistics                                                                      |
|                                                                                    |
| Interval size: 50.0 secs (dur)                                                     |
| Col 1: Frames and bytes                                                            |
|     2: tcp.port==50261                                                             |
|     3: tcp.port==50262                                                             |
|     4: tcp.port==50263                                                             |
|------------------------------------------------------------------------------------|
|              |1                 |2               |3               |4               |
| Interval     | Frames |  Bytes  | Frames | Bytes | Frames | Bytes | Frames | Bytes |
|------------------------------------------------------------------------------------|
|  0.0 &lt;&gt; 50.0 |   4654 | 3559316 |     11 |  1964 |     11 |  1965 |     11 |  1949 |
======================================================================================
$</code></pre><p>Now you can use the capture time and the</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '13, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22283" class="comments-container"><span id="22284"></span><div id="comment-22284" class="comment"><div id="post-22284-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark is this? The one I have is a dissector where tshark -z io,stat,0,filter does not specify total capture time.</p></div><div id="comment-22284-info" class="comment-info"><span class="comment-age">(24 Jun '13, 08:28)</span> <span class="comment-user userinfo">Rajat</span></div></div><span id="22292"></span><div id="comment-22292" class="comment"><div id="post-22292-score" class="comment-score"></div><div class="comment-text"><p>The latest official release 1.10, which version are you running?</p></div><div id="comment-22292-info" class="comment-info"><span class="comment-age">(24 Jun '13, 09:27)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="22293"></span><div id="comment-22293" class="comment"><div id="post-22293-score" class="comment-score"></div><div class="comment-text"><p>Sake, what is the relavance of 0 in your t-shark cli?</p><p>Thanks</p></div><div id="comment-22293-info" class="comment-info"><span class="comment-age">(24 Jun '13, 09:52)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="22295"></span><div id="comment-22295" class="comment"><div id="post-22295-score" class="comment-score"></div><div class="comment-text"><p>It is representing the interval over which the statistics are calculated. 0 means "the whole file".</p></div><div id="comment-22295-info" class="comment-info"><span class="comment-age">(24 Jun '13, 10:21)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-22283" class="comment-tools"></div><div class="clear"></div><div id="comment-22283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22296"></span>

<div id="answer-container-22296" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22296-score" class="post-score" title="current number of votes">1</div><span id="post-22296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about this:</p><blockquote><p><code>tshark -nr input.cap -z conv,tcp -q</code><br />
</p></blockquote><p>Then take the <strong>Bytes</strong> value and divide it by the number of seconds (Duration).</p><p>To get only one certain streams, either filter them (option: -R tcp.port eq xxxx) or search for those connections in the output of tshark.</p><pre><code>TCP Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |    Relative    |   Duration   |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |
10.95.119.188:59122  &lt;-&gt; 10.116.11.24:5300          0         0   10507    821508   10507    821508  1407,479330000      1562,6490
10.116.11.24:5300    &lt;-&gt; 10.95.119.188:2424        25      3973       0         0      25      3973     0,000000000      2970,1373</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '13, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jun '13, 10:39</strong> </span></p></div></div><div id="comments-container-22296" class="comments-container"></div><div id="comment-tools-22296" class="comment-tools"></div><div class="clear"></div><div id="comment-22296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

