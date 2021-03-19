+++
type = "question"
title = "ipv6 hosts name resolution"
description = '''Greetings everyone, I&#x27;m trying to get ipv6 name resolution working using hosts file. It works ok for IPv4 addresses but I&#x27;ve tried many formats for and still can&#x27;t get it to translate IPv6 hosts, see below my attempts: fe80::10:18ff:fe99:9904 Machine1 fe80.0000.0000.0000.0010.18ff.fe99.9904 Machine2...'''
date = "2011-01-06T00:52:00Z"
lastmod = "2011-10-11T07:14:00Z"
weight = 1646
keywords = [ "hosts", "resolution", "name", "ipv6" ]
aliases = [ "/questions/1646" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ipv6 hosts name resolution](/questions/1646/ipv6-hosts-name-resolution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1646-score" class="post-score" title="current number of votes">0</div><span id="post-1646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings everyone,</p><p>I'm trying to get ipv6 name resolution working using hosts file. It works ok for IPv4 addresses but I've tried many formats for and still can't get it to translate IPv6 hosts, see below my attempts:</p><pre><code>fe80::10:18ff:fe99:9904 Machine1
fe80.0000.0000.0000.0010.18ff.fe99.9904 Machine2
fe80::210:18ff:fe96:3f66 Machine3
fe80:0000:0000:0000:0210:18ff:fe96:3f66 Machine4
fe80::21:70ff:fe9b:9925 Machine5
fe.80.00.00.00.00.00.00.00.21.70.ff.fe.9b.99.25 Machine6
fe-80-00-00-00-00-00-00-00-0c-29-ff-fe-c4-2f-f0 Machine7
192.168.1.100 Machine8
2.2.2.1 Machine9
2.2.2.2 Machine10</code></pre><p>Regards - Philippe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '11, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/21718d32b14b13f6e97de1c1c5e1afb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moction&#39;s gravatar image" /><p><span>moction</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moction has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '11, 09:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-1646" class="comments-container"><span id="6847"></span><div id="comment-6847" class="comment"><div id="post-6847-score" class="comment-score"></div><div class="comment-text"><p>Is this still a problem? Just tried that out and works perfectly fine with 1.6.2</p></div><div id="comment-6847-info" class="comment-info"><span class="comment-age">(11 Oct '11, 07:14)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-1646" class="comment-tools"></div><div class="clear"></div><div id="comment-1646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1660"></span>

<div id="answer-container-1660" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1660-score" class="post-score" title="current number of votes">2</div><span id="post-1660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to the prefix fe80, these are all IPv6 link-local addresses. You should use the global or site-local addresses instead.</p><p>In an IPv4 address, the subnet mask specifies which part of the address is the network ID. A multi-homed system will have a different network ID for each interface. IPv6 link-local addresses, on the other hand, all have the same prefix. Therefore, the address by itself, is not sufficient to determine which interface should be used for link-local traffic.</p><p>See <a href="http://en.wikipedia.org/wiki/IPv6_address#Link-local_addresses_and_zone_indices">IPv6 address - Link-local addresses and zone indices</a> which has a brief explanation of why the IPv6 address of an interface by itself is not sufficient for the local computer to make a routing decision and discusses the use of a zone ID to differentiate the interfaces.</p><p>Also see <a href="http://technet.microsoft.com/en-us/library/bb727005.aspx">TCP/IP Fundamentals for Microsoft Windows Chapter 7 - Host Name Resolution</a>. Microsoft states "For IPv6 entries, the address in the Hosts file entry is a global or site-local IPv6 address expressed in colon hexadecimal notation."</p><p>Then there is an example of a Hosts file with both IPv4 and IPv6 entries (but no link-local addresses).</p><p>Followed by "You should not place entries for link-local addresses in the Hosts file because you cannot specify the zone ID for those addresses."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '11, 20:13</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '11, 23:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-1660" class="comments-container"><span id="1662"></span><div id="comment-1662" class="comment"><div id="post-1662-score" class="comment-score"></div><div class="comment-text"><p>Jaragon, the original poster is trying to do reverse-lookup with wireshark. These will be the addresses he is seeing (which is what you will see on a network that doesn't have a IPv6 router configured - it will only have link-local addresses)</p></div><div id="comment-1662-info" class="comment-info"><span class="comment-age">(06 Jan '11, 22:48)</span> <span class="comment-user userinfo">martyvis</span></div></div></div><div id="comment-tools-1660" class="comment-tools"></div><div class="clear"></div><div id="comment-1660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

