+++
type = "question"
title = "High NFS READ latency from SLES10 client to EMC Clarion filer"
description = '''I have a tshark trace dump and want to see the human readable time stamps between NFS READ procedure calls/packets. I understand frame.time_delta might be a good filter expression?  Can anyone provide a command line example on how to do this running tshark. I have the  RTT stats and READ procedure h...'''
date = "2011-01-26T18:04:00Z"
lastmod = "2011-02-07T09:49:00Z"
weight = 1962
keywords = [ "read", "frame.time.delta", "nfs", "tshark" ]
aliases = [ "/questions/1962" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [High NFS READ latency from SLES10 client to EMC Clarion filer](/questions/1962/high-nfs-read-latency-from-sles10-client-to-emc-clarion-filer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1962-score" class="post-score" title="current number of votes">0</div><span id="post-1962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a tshark trace dump and want to see the human readable time stamps between NFS READ procedure calls/packets. I understand frame.time_delta might be a good filter expression?</p><p>Can anyone provide a command line example on how to do this running tshark. I have the RTT stats and READ procedure has very heavy latency so I want to drill down and see if I can understand which file handle(s) might be responsible.</p><p>Any help is very much appreciated.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-read" rel="tag" title="see questions tagged &#39;read&#39;">read</span> <span class="post-tag tag-link-frame.time.delta" rel="tag" title="see questions tagged &#39;frame.time.delta&#39;">frame.time.delta</span> <span class="post-tag tag-link-nfs" rel="tag" title="see questions tagged &#39;nfs&#39;">nfs</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '11, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/80ec40e1e7b5c00d1bdfa2f15021dc3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="debugme&#39;s gravatar image" /><p><span>debugme</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="debugme has no accepted answers">0%</span></p></div></div><div id="comments-container-1962" class="comments-container"><span id="2199"></span><div id="comment-2199" class="comment"><div id="post-2199-score" class="comment-score"></div><div class="comment-text"><p>hi</p><p>Thank you for your response. I will use your filter and see what the results are. Thank you again.</p></div><div id="comment-2199-info" class="comment-info"><span class="comment-age">(07 Feb '11, 09:49)</span> <span class="comment-user userinfo">debugme</span></div></div></div><div id="comment-tools-1962" class="comment-tools"></div><div class="clear"></div><div id="comment-1962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1977"></span>

<div id="answer-container-1977" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1977-score" class="post-score" title="current number of votes">2</div><span id="post-1977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I used the following before to get a grasp on which NFS calls were taking a lot of time:</p><pre><code>tshark -o tcp.desegment_tcp_streams:FALSE -nlr nfs.cap -R rpc -qzio,stat,300,\
    &quot;COUNT(rpc.time)rpc.time&amp;&amp;rpc.procedure==1&quot;,\
    &quot;AVG(rpc.time)rpc.time&amp;&amp;rpc.procedure==1&quot;,\
    &quot;MAX(rpc.time)rpc.time&amp;&amp;rpc.procedure==1&quot;,\
    &quot;COUNT(rpc.time)rpc.time&amp;&amp;rpc.procedure==2&quot;,\
    &quot;AVG(rpc.time)rpc.time&amp;&amp;rpc.procedure==2&quot;,\
    &quot;MAX(rpc.time)rpc.time&amp;&amp;rpc.procedure==2&quot;,\
    [...]
    &quot;COUNT(rpc.time)rpc.time&amp;&amp;rpc.procedure==21&quot;,\
    &quot;AVG(rpc.time)rpc.time&amp;&amp;rpc.procedure==21&quot;,\
    &quot;MAX(rpc.time)rpc.time&amp;&amp;rpc.procedure==21&quot;</code></pre><p>If you want to drill down, you might want to use something like:</p><pre><code>tshark -nlr nfs.cap -R &quot;rpc.time&gt;0.5&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '11, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1977" class="comments-container"></div><div id="comment-tools-1977" class="comment-tools"></div><div class="clear"></div><div id="comment-1977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

