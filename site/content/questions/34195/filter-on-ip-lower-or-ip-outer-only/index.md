+++
type = "question"
title = "Filter on IP Lower (or IP Outer) only"
description = '''I would like to run an IP filter that only matches the Lower IP. For example, I have a packet that has Ethernet/IPv4/UDP/GPRS/IPv4/UDP/DNS. I would like to do something like tshark -r file -Y ip -T fields -e ip.src | sort | uniq  when I do this I get something like 10.132.48.16 10.132.48.26 10.132.4...'''
date = "2014-06-25T16:23:00Z"
lastmod = "2014-06-25T17:45:00Z"
weight = 34195
keywords = [ "ip", "outer" ]
aliases = [ "/questions/34195" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter on IP Lower (or IP Outer) only](/questions/34195/filter-on-ip-lower-or-ip-outer-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34195-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to run an IP filter that only matches the Lower IP. For example, I have a packet that has Ethernet/IPv4/UDP/GPRS/IPv4/UDP/DNS. I would like to do something like</p><pre><code>tshark -r file -Y ip -T fields -e ip.src | sort | uniq</code></pre><p>when I do this I get something like</p><pre><code>10.132.48.16
10.132.48.26
10.132.48.26,192.168.185.138
10.132.48.26,192.168.67.7
10.132.48.26,192.168.99.4
10.132.48.26,192.168.15.105
10.132.48.26,192.168.15.130</code></pre><p>What I've been doing is constructing a set of filters based on the first entry only from those results, and this sort of works, at least in the case of all ipv4 or all ipv6. The problem comes when I try to work with mixed ipv4 and ipv6. I can do the two independently, but I can't seem to figure out which is upper and lower in the case of Ethernet/IPv6/UDP/GPRS/IPv4/UDP/DNS or Ethernet/IPv4/UDP/GPRS/IPv6/UDP/DNS</p><p>any suggestions would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">ip outer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/95ccb92e85b56e1b19b7a1262efd06cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wyrmwood&#39;s gravatar image" /><p>wyrmwood<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wyrmwood has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '14, 16:26</p></div></div><div id="comments-container-34195" class="comments-container"></div><div id="comment-tools-34195" class="comment-tools"></div><div class="clear"></div><div id="comment-34195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34198"></span>

<div id="answer-container-34198" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34198-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just add "-E occurrence=l" to your options in tshark, to always give the last field value (in this case, always the inner IP) rather than giving all values for the ip.src field.</p><p>Also since you're piping it out in unix, another non-tshark way to always get the inner would be to pipe it to sed. Something like this, before your uniq would work, to replace all text up to the last comma and leave the last IP value:</p><pre><code>| sed s/.*[,]//g</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 17:45</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '14, 17:56</p></div></div><div id="comments-container-34198" class="comments-container"><span id="34212"></span><div id="comment-34212" class="comment"><div id="post-34212-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the advice but I'm actually looking for the opposite (the lower or outer IP). And it works well in the case of tunneled ip over ip or tunneled ipv6 over ipv6. The problem is where the lower and upper ip are mixed (ipv4 in lower and ipv6 in upper) as the filter produces only one ip. Since it takes two filters, there's really no way of telling when there's only one address whether it is gateway or tunneled.</p></div><div id="comment-34212-info" class="comment-info"><span class="comment-age">(26 Jun '14, 05:48)</span> wyrmwood</div></div><span id="34227"></span><div id="comment-34227" class="comment"><div id="post-34227-score" class="comment-score"></div><div class="comment-text"><p>Oh, if it is just the outer then kill the UDP dissection and you will only see the outside address, whether v4 or v6. A cheaper way would be to decode the port as something other than Gtp, with something like this "-d udp.port==2152,dns". That will break the second IP header from being dissected, so won't get pulled by the -T fields flag.</p></div><div id="comment-34227-info" class="comment-info"><span class="comment-age">(26 Jun '14, 08:50)</span> Quadratic</div></div></div><div id="comment-tools-34198" class="comment-tools"></div><div class="clear"></div><div id="comment-34198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

