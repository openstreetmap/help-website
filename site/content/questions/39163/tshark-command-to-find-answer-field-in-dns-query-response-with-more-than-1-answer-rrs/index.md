+++
type = "question"
title = "tshark command to find answer field in dns query response with more than 1 answer RRs"
description = '''My DNS trace contains more than 1 &#x27;Answer RRs&#x27;. How do I extract &#x27;Name&#x27; (dns.resp.name) and &#x27;Addr&#x27; (dns.resp.addr) field from each response &amp;amp; print it in same line as requested domain name. I tried using -Tfields -e &quot;dns.resp.name&quot; -e &quot;dns.resp.addr&quot; but I don&#x27;t get any response at all.'''
date = "2015-01-15T08:20:00Z"
lastmod = "2015-03-08T09:22:00Z"
weight = 39163
keywords = [ "performance", "tshark", "dns" ]
aliases = [ "/questions/39163" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark command to find answer field in dns query response with more than 1 answer RRs](/questions/39163/tshark-command-to-find-answer-field-in-dns-query-response-with-more-than-1-answer-rrs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39163-score" class="post-score" title="current number of votes">0</div><span id="post-39163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My DNS trace contains more than 1 'Answer RRs'. How do I extract 'Name' (dns.resp.name) and 'Addr' (dns.resp.addr) field from each response &amp; print it in same line as requested domain name. I tried using -Tfields -e "dns.resp.name" -e "dns.resp.addr" but I don't get any response at all.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-39163" class="comments-container"></div><div id="comment-tools-39163" class="comment-tools"></div><div class="clear"></div><div id="comment-39163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40366"></span>

<div id="answer-container-40366" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40366-score" class="post-score" title="current number of votes">0</div><span id="post-40366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>I found issue. It is due to older version I could not print those fields. Thanks to Kali live linux CDs I found newer version !</p><p>After processing data using -T &amp; -e options, I got request / response data on separate lines and then just wrote following bash script to map request &amp; response on the same line.</p><pre><code>#!/bin/bash
for i in `cat Gn_ADNS1.txt`
do
        line=`echo $i`
        response_frame=`echo $line | awk -F&#39;,&#39; &#39;{ print $2}&#39;`
        if [ ${#response_frame} -gt 0 ] ; then
                req=`cat Gn_ADNS1.txt | grep -w &quot;^$response_frame&quot;`
                echo &quot;$req =&gt; $line&quot;
#       else
#               echo &quot;$line !=&quot;
        fi
done</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '15, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Mar '15, 09:24</strong> </span></p></div></div><div id="comments-container-40366" class="comments-container"></div><div id="comment-tools-40366" class="comment-tools"></div><div class="clear"></div><div id="comment-40366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

