+++
type = "question"
title = "capture filter for ipv6 network prefix"
description = '''hello. I want to write a filter to capture all IPv6 packets that match the net prefix with a subnet id. With ipv4 is simple: net 192.168.5 but with ipv6 this not works for me: net fec0:abcd:1234:: How can i capture the packets that match with network prefix? Thanks and sorry for my poor english'''
date = "2012-06-22T01:17:00Z"
lastmod = "2012-06-22T02:04:00Z"
weight = 12128
keywords = [ "filter", "capture", "ipv6" ]
aliases = [ "/questions/12128" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter for ipv6 network prefix](/questions/12128/capture-filter-for-ipv6-network-prefix)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12128-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello.</p><p>I want to write a filter to capture all IPv6 packets that match the net prefix with a subnet id. With ipv4 is simple: net 192.168.5 but with ipv6 this not works for me: net fec0:abcd:1234::</p><p>How can i capture the packets that match with network prefix?</p><p>Thanks and sorry for my poor english</p></div><div id="question-tags" class="tags-container tags">filter capture ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '12, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/91b30842fb38f3b72d2a75dfd732043d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorpoz&#39;s gravatar image" /><p>jorpoz<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorpoz has no accepted answers">0%</span></p></div></div><div id="comments-container-12128" class="comments-container"></div><div id="comment-tools-12128" class="comment-tools"></div><div class="clear"></div><div id="comment-12128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12129"></span>

<div id="answer-container-12129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12129-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>For IPv6 you must specify the mask length, as there is no implicit definition as with IPv4. See <a href="http://www.manpagez.com/man/7/pcap-filter/">man page of pcap-filter</a></p><pre><code>dst net net
              True if the IPv4/v6 destination address of the packet has a net-
              work  number of net.  Net may be either a name from the networks
              database (/etc/networks, etc.) or a  network  number.   An  IPv4
              network   number   can  be  written  as  a  dotted  quad  (e.g.,
              192.168.1.0), dotted triple (e.g., 192.168.1), dotted pair (e.g,
              172.16),   or   single   number   (e.g.,  10);  the  netmask  is
              255.255.255.255 for a dotted quad (which means that it&#39;s  really
              a  host  match),  255.255.255.0 for a dotted triple, 255.255.0.0
              for a dotted pair, or 255.0.0.0 for a single  number.   An  IPv6
              network  number  must  be  written  out  fully;  the  netmask is
              ff:ff:ff:ff:ff:ff:ff:ff, so IPv6 &quot;network&quot;  matches  are  really
              always  host  matches,  and  a  network match requires a netmask
              length.</code></pre><p>So, the filter would be something like: <strong><code>net fec0:abcd:1234::/64</code></strong> (or whatever mask len makes sense for your needs).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '12, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jun '12, 02:05</p></div></div><div id="comments-container-12129" class="comments-container"><span id="12132"></span><div id="comment-12132" class="comment"><div id="post-12132-score" class="comment-score"></div><div class="comment-text"><p>ok, i thought that i've tried that option, but it is obviously i didn't. It works. Thanks.</p></div><div id="comment-12132-info" class="comment-info"><span class="comment-age">(22 Jun '12, 05:45)</span> jorpoz</div></div></div><div id="comment-tools-12129" class="comment-tools"></div><div class="clear"></div><div id="comment-12129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

