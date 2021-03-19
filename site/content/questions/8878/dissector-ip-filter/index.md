+++
type = "question"
title = "dissector ip filter"
description = '''Hi, I&#x27;ve written a dissector plugin to filter my protocolls. I&#x27;ve added dissector_add_uint(&quot;tcp.port&quot;, 5001, test_handle); to filter the port, but how can I add a filter of an ip adress? I tried something like dissector_add_string(&quot;ip.src&quot;, 127.0.0.1, test_handle); but this doesn&#x27;t work. What is the...'''
date = "2012-02-07T10:09:00Z"
lastmod = "2012-02-07T20:06:00Z"
weight = 8878
keywords = [ "filter", "ip", "dissector" ]
aliases = [ "/questions/8878" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [dissector ip filter](/questions/8878/dissector-ip-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8878-score" class="post-score" title="current number of votes">0</div><span id="post-8878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've written a dissector plugin to filter my protocolls. I've added dissector_add_uint("tcp.port", 5001, test_handle); to filter the port, but how can I add a filter of an ip adress? I tried something like dissector_add_string("ip.src", 127.0.0.1, test_handle); but this doesn't work. What is the correct way to add an ip to my dissector?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '12, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/ce79034142dc613a1a30949664b84723?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic&#39;s gravatar image" /><p><span>Nic</span><br />
<span class="score" title="14 reputation points">14</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic has no accepted answers">0%</span></p></div></div><div id="comments-container-8878" class="comments-container"></div><div id="comment-tools-8878" class="comment-tools"></div><div class="clear"></div><div id="comment-8878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8881"></span>

<div id="answer-container-8881" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8881-score" class="post-score" title="current number of votes">0</div><span id="post-8881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nic has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(A dissector doesn't filter protocols, it dissects them. Presumably that's what you meant.)</p><p>Most dissector handoffs done with tables such as <code>"tcp.port"</code> use values that are also named protocol fields, in which case the <em>convention</em> is that the table name should be the same as the field name, but it is <em>NOT</em> the case that every named protocol field has a corresponding handoff table; there is, for example, no table named <code>"ip.src"</code>, even though there's a field named <code>"ip.src"</code>, so your <code>dissector_add_string()</code> call doesn't work.</p><p>If you mean that you <em>only</em> want your dissector called for traffic to and from port 5001 <em>that is coming from a particular IP address</em>, the only way to do that would be to make a heuristic dissector and have it check both <code>pinfo-&gt;srcport</code> and <code>pinfo-&gt;dstport</code> and reject the packet if neither of them have the value 5001 and <em>also</em> check whether <code>pinfo-&gt;net_src</code> is equal to the source address in question. (To do that, you could create a (static const) structure of type <code>address</code>, initialize its <code>type</code> value to <code>AT_IPv4</code> or <code>AT_IPV6</code> depending on whether it's an IPv4 or IPv6 address, initialize its <code>len</code> value to 4 or 16, and initialize its <code>data</code> value to point to an (const) array of bytes containing the raw bytes of the IP address, and then compare the addresses with <code>CMP_ADDRESS()</code>. Do <em>NOT</em> assume that the address is an IPv4 address! It could, for example, be an IPv6 address.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '12, 20:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8881" class="comments-container"></div><div id="comment-tools-8881" class="comment-tools"></div><div class="clear"></div><div id="comment-8881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

