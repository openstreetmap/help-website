+++
type = "question"
title = "Trying to understand what a specific ARP request is for"
description = '''Hi sorry if this is the wrong place to ask this, but we just did a wireshark capture on my macbook (10.10.5) and seeing these ARP requests that I am trying to figure out where they are coming from. Source: Congatec_19:aa:12 Destination: Broadcast the reply is: Source: Apple_d2:5b:b2 Destination: con...'''
date = "2015-09-17T10:20:00Z"
lastmod = "2015-09-17T17:25:00Z"
weight = 45926
keywords = [ "arp", "request" ]
aliases = [ "/questions/45926" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to understand what a specific ARP request is for](/questions/45926/trying-to-understand-what-a-specific-arp-request-is-for)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45926-score" class="post-score" title="current number of votes">0</div><span id="post-45926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>sorry if this is the wrong place to ask this, but we just did a wireshark capture on my macbook (10.10.5) and seeing these ARP requests that I am trying to figure out where they are coming from.</p><p>Source: Congatec_19:aa:12 Destination: Broadcast the reply is: Source: Apple_d2:5b:b2 Destination: congatec_19:aa_12</p><p>how do I figure out what this is about? I did not find anything by googling that name</p><p>thanks</p><p>'mark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '15, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/c65b3ac9da4394dfabebe801d749a9cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M_ahlenius&#39;s gravatar image" /><p><span>M_ahlenius</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M_ahlenius has no accepted answers">0%</span></p></div></div><div id="comments-container-45926" class="comments-container"><span id="45928"></span><div id="comment-45928" class="comment"><div id="post-45928-score" class="comment-score"></div><div class="comment-text"><p>please upload a capture file somewhere and post the link here. It's impossible to do any analysis based on your description!</p></div><div id="comment-45928-info" class="comment-info"><span class="comment-age">(17 Sep '15, 12:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-45926" class="comment-tools"></div><div class="clear"></div><div id="comment-45926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45929"></span>

<div id="answer-container-45929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45929-score" class="post-score" title="current number of votes">0</div><span id="post-45929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The ARP request is coming from the device whose Ethernet MAC address is <code>00:13:95:19:aa:12</code>, and the ARP reply is coming from the device whose Ethernet MAC address is one of a number of OUI's that all map to <code>Apple:d2:5b:b2</code>. See <a href="http://standards-oui.ieee.org/oui.txt">IEEE's OUI lookup table</a> for how Wireshark converts the OUI to a name, or use <a href="https://www.wireshark.org/tools/oui-lookup.html">Wireshark's own OUI online lookup tool</a>.</p><p>Anyway, the device with MAC address <code>00:13:95:19:aa:12</code> is trying to find out which device has a specific IP address so that it can send it some data, and the device with MAC address <code>Apple:d2:5b:b2</code> has indicated that it is the device with the IP address that the first device was looking for. Now the first device is able to send its data to the second device.</p><p>For more information on ARP, refer to the <a href="https://en.wikipedia.org/wiki/Address_Resolution_Protocol">ARP Wikipedia article</a> or to <a href="https://tools.ietf.org/html/rfc826">RFC 826</a> directly. Refer also to my answer to <a href="https://ask.wireshark.org/questions/5412/what-does-arp-42-who-has-19216811-tell-192168133-mean">this</a> similar question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '15, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-45929" class="comments-container"><span id="45930"></span><div id="comment-45930" class="comment"><div id="post-45930-score" class="comment-score"></div><div class="comment-text"><p>could be <strong>IPv4 Address Conflict Detection</strong> instead of ARP request/reply, that's why I asked for the pcap file.</p></div><div id="comment-45930-info" class="comment-info"><span class="comment-age">(17 Sep '15, 13:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45932"></span><div id="comment-45932" class="comment"><div id="post-45932-score" class="comment-score"></div><div class="comment-text"><p>Yes, it could be. I went for the most likely scenario.</p></div><div id="comment-45932-info" class="comment-info"><span class="comment-age">(17 Sep '15, 13:10)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="45938"></span><div id="comment-45938" class="comment"><div id="post-45938-score" class="comment-score"></div><div class="comment-text"><p>At this Question some kind of ARP Types are discussed: <a href="https://ask.wireshark.org/questions/45400/ethernet-packet-arp">https://ask.wireshark.org/questions/45400/ethernet-packet-arp</a></p></div><div id="comment-45938-info" class="comment-info"><span class="comment-age">(17 Sep '15, 17:25)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-45929" class="comment-tools"></div><div class="clear"></div><div id="comment-45929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

