+++
type = "question"
title = "Running TShark in a batch file with -r attempts to capture traffic rather than reading the file"
description = '''tshark -r &amp;lt;file&amp;gt; -Y &quot;(ip.addr==10.1.1.2 or ip.addr==10.2.4.12 or ip.addr==10.5.3.6) and (&quot;http.request.method==GET&quot; or (tcp.flags.syn==1 &amp;amp;&amp;amp; tcp.flags.ack==0 &amp;amp;&amp;amp; tcp.port==443) or (tcp.flags.syn==1 &amp;amp;&amp;amp; tcp.flags.ack==0 &amp;amp;&amp;amp; tcp.port==22) )&quot;  When i attempt to autorun...'''
date = "2013-08-25T09:36:00Z"
lastmod = "2013-08-26T06:25:00Z"
weight = 24025
keywords = [ "tshark" ]
aliases = [ "/questions/24025" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Running TShark in a batch file with -r attempts to capture traffic rather than reading the file](/questions/24025/running-tshark-in-a-batch-file-with-r-attempts-to-capture-traffic-rather-than-reading-the-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24025-score" class="post-score" title="current number of votes">0</div><span id="post-24025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>tshark -r &lt;file&gt; -Y &quot;(ip.addr==10.1.1.2 or ip.addr==10.2.4.12 or ip.addr==10.5.3.6) and (&quot;http.request.method==GET&quot; or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==443) or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==22) )&quot;</code></pre><p>When i attempt to autorun this code using batch file process, I discovered that it does not accept it, rather it attempts to capture the traffic on my network. I want it to dissect the specified file. Is there a way to instruct it (tshark) to dissect the given file, and not to capture traffic..?</p><p>Thanks in anticipation of your response.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '13, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/981f5e7be0c0e73e3f429d0038fb3eed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hunted&#39;s gravatar image" /><p><span>Hunted</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hunted has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>25 Aug '13, 10:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-24025" class="comments-container"><span id="24028"></span><div id="comment-24028" class="comment"><div id="post-24028-score" class="comment-score"></div><div class="comment-text"><p>You say "batch file", which is a term used more on Windows than on UN*X; is this on Windows or on UN*X (note: Linux and OS X are versions of UN*X)?</p><p>What are the exact contents of the batch file in question?</p></div><div id="comment-24028-info" class="comment-info"><span class="comment-age">(25 Aug '13, 10:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-24025" class="comment-tools"></div><div class="clear"></div><div id="comment-24025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24044"></span>

<div id="answer-container-24044" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24044-score" class="post-score" title="current number of votes">0</div><span id="post-24044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you put "&lt;file&gt;" literally in your batch file? The word "&lt;file&gt;" should be replaced by the name of the packet capture file that you want to analyze.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '13, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '13, 16:30</strong> </span></p></div></div><div id="comments-container-24044" class="comments-container"></div><div id="comment-tools-24044" class="comment-tools"></div><div class="clear"></div><div id="comment-24044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24060"></span>

<div id="answer-container-24060" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24060-score" class="post-score" title="current number of votes">0</div><span id="post-24060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tshark -r &lt;file&gt; -Y "(ip.addr==10.1.1.2 or ip.addr==10.2.4.12 or ip.addr==10.5.3.6) and (<strong>"http.request.method==GET"</strong> or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==443) or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==22) )"<br />
When i attempt to autorun this code using batch file process, <strong>I discovered that it does not accept it</strong></p></blockquote><p>The reason is the wrong number of quotes " in the argument string. Your shell will get confused by the additional quotes around <strong>http.request.method</strong>.</p><p>Please try this</p><blockquote><p>tshark -r &lt;file&gt; -Y "(ip.addr==10.1.1.2 or ip.addr==10.2.4.12 or ip.addr==10.5.3.6) and (http.request.method==GET or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==443) or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==22) )"</p></blockquote><p>or this (single quotes)</p><blockquote><blockquote><p>tshark -r &lt;file&gt; -Y '(ip.addr==10.1.1.2 or ip.addr==10.2.4.12 or ip.addr==10.5.3.6) and (http.request.method==GET or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==443) or (tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.port==22) )'</p></blockquote></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '13, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Aug '13, 06:26</strong> </span></p></div></div><div id="comments-container-24060" class="comments-container"></div><div id="comment-tools-24060" class="comment-tools"></div><div class="clear"></div><div id="comment-24060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

