+++
type = "question"
title = "Extracting ip addresses from dns answer section with tshark"
description = '''I am trying to extract the ip addresses from a standard dns query response using &quot;-e dns.resp.addr&quot;. Unfortunately, I also get the ip addresses from &quot;additional records&quot; section because the fieldname is the same: &quot;dns.resp.addr&quot; When I query www.bfh.ch I would expect to get the A record.  tshark -i ...'''
date = "2012-09-04T07:00:00Z"
lastmod = "2012-09-13T17:57:00Z"
weight = 14033
keywords = [ "extraction", "section", "addresses", "dns", "response" ]
aliases = [ "/questions/14033" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting ip addresses from dns answer section with tshark](/questions/14033/extracting-ip-addresses-from-dns-answer-section-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14033-score" class="post-score" title="current number of votes">0</div><span id="post-14033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to extract the ip addresses from a standard dns query response using "-e dns.resp.addr". Unfortunately, I also get the ip addresses from "additional records" section because the fieldname is the same: "dns.resp.addr"<br />
When I query <a href="http://www.bfh.ch">www.bfh.ch</a> I would expect to get the A record.</p><pre><code>tshark -i eth0 port 53 -R &quot;dns.flags.response == 1&quot; -T fields -E separator=\; -E quote=s -e frame.time -e dns.qry.name -e dns.resp.addr

&#39;www.bfh.ch&#39;;&#39;147.87.250.111,147.87.250.20,78.47.48.102,80.238.203.210,147.87.254.20&#39;</code></pre><p>Instead, I also get the ip addresses of their four nameservers.</p><p>I used the display filter reference for dns but couldn't find a solution: <a href="http://www.wireshark.org/docs/dfref/d/dns.html">http://www.wireshark.org/docs/dfref/d/dns.html</a></p><p>Is there a way to extract the addresses from the answer section only?</p><p>Thanks Luke</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-extraction" rel="tag" title="see questions tagged &#39;extraction&#39;">extraction</span> <span class="post-tag tag-link-section" rel="tag" title="see questions tagged &#39;section&#39;">section</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '12, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/a03d81e69280744e9ef6b7ce4b1cd230?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WireLuke&#39;s gravatar image" /><p><span>WireLuke</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WireLuke has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-14033" class="comments-container"></div><div id="comment-tools-14033" class="comment-tools"></div><div class="clear"></div><div id="comment-14033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14036"></span>

<div id="answer-container-14036" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14036-score" class="post-score" title="current number of votes">1</div><span id="post-14036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try also specifying <code>-E occurrence=f</code>. That will cause <code>tshark</code> to only display the first occurrence of the desired fields, rather than all occurrences, which is the default. Refer to the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-14036" class="comments-container"><span id="14156"></span><div id="comment-14156" class="comment"><div id="post-14156-score" class="comment-score"></div><div class="comment-text"><p>This works for domains which return only one address. For names with multiple addresses, I only get the first one. I would like to get the complete answer section without the "additional records" section.</p><p>Thanks anyway!</p></div><div id="comment-14156-info" class="comment-info"><span class="comment-age">(10 Sep '12, 01:43)</span> <span class="comment-user userinfo">WireLuke</span></div></div></div><div id="comment-tools-14036" class="comment-tools"></div><div class="clear"></div><div id="comment-14036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14161"></span>

<div id="answer-container-14161" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14161-score" class="post-score" title="current number of votes">1</div><span id="post-14161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to get the complete answer section <strong>without</strong> the "additional records" section.</p></blockquote><p>Unfortunately that is not possible with tshark field extraction, as the fields in the additional records are also accessed by dns.resp.name and/or dns.resp.addr.</p><p>What you can do is this:</p><blockquote><p><code>tshark -nr input.cap -R "dns" -V</code><br />
</p></blockquote><p>This will print the DNS packets in full detail, like this one:</p><pre><code>   Queries
       www.mircrosoft.com: type A, class IN
           Name: www.mircrosoft.com
           Type: A (Host address)
           Class: IN (0x0001)
   Answers
       www.mircrosoft.com: type CNAME, class IN, cname mircrosoft.com
           Name: www.mircrosoft.com
           Type: CNAME (Canonical name for an alias)
           Class: IN (0x0001)
           Time to live: 1 hour
           Data length: 2
           Primaryname: mircrosoft.com
       mircrosoft.com: type A, class IN, addr 64.4.6.100
           Name: mircrosoft.com
           Type: A (Host address)
           Class: IN (0x0001)
           Time to live: 1 hour
           Data length: 4
           Addr: 64.4.6.100 (64.4.6.100)
       mircrosoft.com: type A, class IN, addr 65.55.39.10
           Name: mircrosoft.com
           Type: A (Host address)
           Class: IN (0x0001)
           Time to live: 1 hour
           Data length: 4
           Addr: 65.55.39.10 (65.55.39.10)
   Authoritative nameservers
       mircrosoft.com: type NS, class IN, ns ns3.msft.net
           Name: mircrosoft.com
           Type: NS (Authoritative name server)
           Class: IN (0x0001)</code></pre><p>Then you extract only the required information from that output (addrs in the Answers section) with a script. Use your preferred language for that (perl/python/lua/ruby).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '12, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14161" class="comments-container"><span id="14253"></span><div id="comment-14253" class="comment"><div id="post-14253-score" class="comment-score"></div><div class="comment-text"><p><em>Unfortunately that is not possible with tshark field extraction, as the fields in the additional records are also accessed by dns.resp.name and/or dns.resp.addr.</em></p><p>This could be changed though so that different filters are used. I would suggest filing a DNS enhancement bug report requesting this.</p></div><div id="comment-14253-info" class="comment-info"><span class="comment-age">(13 Sep '12, 17:57)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-14161" class="comment-tools"></div><div class="clear"></div><div id="comment-14161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

