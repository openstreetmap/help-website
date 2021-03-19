+++
type = "question"
title = "how to calculate service response time for SAML ?"
description = '''I need to calculate the service response time between an appliance (if this is of interest for you: a Google Search Appliance) and our internal SAML identity provider. There are some restrictions / conditions I have to live with:  I can&#x27;t run a dumper on the appliance  itself, neither on the network...'''
date = "2015-01-29T06:08:00Z"
lastmod = "2015-01-29T09:41:00Z"
weight = 39480
keywords = [ "filter", "response", "tcp", "times" ]
aliases = [ "/questions/39480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to calculate service response time for SAML ?](/questions/39480/how-to-calculate-service-response-time-for-saml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39480-score" class="post-score" title="current number of votes">0</div><span id="post-39480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to calculate the service response time between an appliance (if this is of interest for you: a Google Search Appliance) and our internal SAML identity provider.</p><p>There are some restrictions / conditions I have to live with:</p><ul><li>I can't run a dumper on the appliance itself, neither on the network between the appliance and the IDP or the IDP itself</li><li>the appliance is able to run tcpdump for me but I can't influence the command line (one exception below)</li><li>the appliance allows me to enter an ip restriction that it will then send to tcpdump which will then create a .cap file for me which I will then be able to download later</li><li>the cap file is limited to 1 GB in size (should be sufficient to log a lot of transactions)</li><li>I am not able to decrypt the traffic because I don't have access to the keys</li></ul><p>I read some posts about http response times but this can't be used for http over tlsv1. What looks most promising to me is this: because the SAML process consists of one single https URL being processed I would be able to calculate the response time by calculating time between first packet and last packet. Having a look at an example trace I downloaded it should be possible to "group" all tcp packages that belong to one transaction by using for example <code>tcp.stream eq 4</code>. In addition to this I enabled <code>Edit -&gt; Preferences -&gt; Protocols -&gt; TCP -&gt; Calculate conversation timestamps</code> and added <code>tcp.time_delta</code> and <code>tcp.time_relative</code> to my displayed columns.</p><p>The figures of <code>tcp.time_relative</code> for the last package in the transaction look good, this seems to be the time elapsed between first and last packet. I tried a filter like <code>tcp.time_relative &gt; 0.5</code> but I am not able to express &amp;&amp; <code>packet is final packet</code>.</p><p>Can you tell me if my approach is correct ? And how to specify the filter ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-times" rel="tag" title="see questions tagged &#39;times&#39;">times</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '15, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/24aaaba3c6140eaef24f9ed711644033?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marged&#39;s gravatar image" /><p><span>marged</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marged has no accepted answers">0%</span></p></div></div><div id="comments-container-39480" class="comments-container"></div><div id="comment-tools-39480" class="comment-tools"></div><div class="clear"></div><div id="comment-39480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39484"></span>

<div id="answer-container-39484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39484-score" class="post-score" title="current number of votes">0</div><span id="post-39484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are on the right track, but there is no filter for the last packet in the TCP stream, so you would need to find another anchor point. Here are some options:</p><ul><li>If all SAML sessions are closed by a TCP FIN, you can use <code>ip.src==&lt;server-ip&gt; and tcp.flags.fin==1</code> as anchor</li><li>If the response from the server fits in one frame, then you could use the ApplicationData packet from the server as anchor with <code>ip.src==&lt;server-ip&gt; and ssl.record.content_type == 23</code></li></ul><p>Hope this helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '15, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39484" class="comments-container"></div><div id="comment-tools-39484" class="comment-tools"></div><div class="clear"></div><div id="comment-39484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

