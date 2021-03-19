+++
type = "question"
title = "What is the capture filter for a specific IPv4 subnet?"
description = '''What is the capture filter for a specific IPv4 subnet? I had thought that this would do: net 192.168.1.0  However, I don&#x27;t capture any traffic with this filter at all (where I know there is traffic, since I can see some on that subnet when capturing without the filter).'''
date = "2013-05-20T08:18:00Z"
lastmod = "2013-05-22T02:00:00Z"
weight = 21312
keywords = [ "filter", "capture_filter", "ipv4" ]
aliases = [ "/questions/21312" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the capture filter for a specific IPv4 subnet?](/questions/21312/what-is-the-capture-filter-for-a-specific-ipv4-subnet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21312-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the capture filter for a specific IPv4 subnet? I had thought that this would do:</p><pre><code>net 192.168.1.0</code></pre><p>However, I don't capture any traffic with this filter at all (where I know there is traffic, since I can see some on that subnet when capturing without the filter).</p></div><div id="question-tags" class="tags-container tags">filter capture_filter ipv4</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '13, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-21312" class="comments-container"></div><div id="comment-tools-21312" class="comment-tools"></div><div class="clear"></div><div id="comment-21312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21313"></span>

<div id="answer-container-21313" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21313-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to supply the netmask as well, e.g. <code>net 192.168.1.0/24</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 May '13, 08:24</p></div></div><div id="comments-container-21313" class="comments-container"><span id="21371"></span><div id="comment-21371" class="comment"><div id="post-21371-score" class="comment-score"></div><div class="comment-text"><p>see also the following similar question, for IPv6.</p><blockquote><p><a href="http://ask.wireshark.org/questions/12128/capture-filter-for-ipv6-network-prefix">http://ask.wireshark.org/questions/12128/capture-filter-for-ipv6-network-prefix</a></p></blockquote></div><div id="comment-21371-info" class="comment-info"><span class="comment-age">(22 May '13, 05:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-21313" class="comment-tools"></div><div class="clear"></div><div id="comment-21313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21369"></span>

<div id="answer-container-21369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21369-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>I also thought that without a netmask, bpf would default to classfull addresses, but I never ran into it because I had CIDR subnets everywhere.</p><p>Or maybe the behavior has changed over time ... OK, the manpage says it all:</p><pre><code>dst net net
          True if the IPv4/v6 destination address  of  the  packet  has  a
          network  number  of  net.   Net  may  be  either a name from the
          networks database (/etc/networks, etc.) or a network number.  An
          IPv4  network  number  can  be  written  as a dotted quad (e.g.,
          192.168.1.0), dotted triple (e.g., 192.168.1), dotted pair (e.g,
          172.16),   or   single   number   (e.g.,  10);  the  netmask  is
          255.255.255.255 for a dotted quad (which means that it&#39;s  really
          a  host  match),  255.255.255.0 for a dotted triple, 255.255.0.0
          for a dotted pair, or 255.0.0.0 for a single  number.   An  IPv6
          network  number  must  be  written  out  fully;  the  netmask is
          ff:ff:ff:ff:ff:ff:ff:ff, so IPv6 &quot;network&quot;  matches  are  really
          always  host  matches,  and  a  network match requires a netmask
          length.</code></pre><p>So, "net 192.168.1" will also work...</p><p>My "learn-something-new-item" for today :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '13, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21369" class="comments-container"></div><div id="comment-tools-21369" class="comment-tools"></div><div class="clear"></div><div id="comment-21369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

