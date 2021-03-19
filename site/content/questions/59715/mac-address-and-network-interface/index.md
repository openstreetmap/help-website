+++
type = "question"
title = "MAC address and network interface"
description = '''can Wireshark automatically extract the Network Interface Card vendor from the MAC address alone? and why?'''
date = "2017-02-27T11:09:00Z"
lastmod = "2017-02-27T11:54:00Z"
weight = 59715
keywords = [ "mac-address", "networkinterfaces" ]
aliases = [ "/questions/59715" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAC address and network interface](/questions/59715/mac-address-and-network-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59715-score" class="post-score" title="current number of votes">0</div><span id="post-59715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can Wireshark automatically extract the Network Interface Card vendor from the MAC address alone? and why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span> <span class="post-tag tag-link-networkinterfaces" rel="tag" title="see questions tagged &#39;networkinterfaces&#39;">networkinterfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '17, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/b643b25d9639e9ba34419f16fdbd5517?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ayaa&#39;s gravatar image" /><p><span>ayaa</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ayaa has no accepted answers">0%</span></p></div></div><div id="comments-container-59715" class="comments-container"></div><div id="comment-tools-59715" class="comment-tools"></div><div class="clear"></div><div id="comment-59715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59716"></span>

<div id="answer-container-59716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59716-score" class="post-score" title="current number of votes">2</div><span id="post-59716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ul><li>Can Wireshark automatically extract the Network Interface Card vendor from the MAC address alone?</li></ul><p>Yes, as long as the L/G-bit within the MAC address = 0. If the bit is 0, the address is universally administered and registered at the IEEE Registration Authority:</p><p><a href="https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries">https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries</a></p><p>If the L/G-bit is is 1, the address is locally administered. Please see the link above for a full list of registered OUI's with the IEEE.</p><ul><li>And why?</li></ul><p>See above answer. Basically, a MAC address can be divided into 2 parts. The first half (the first 3 octets) are called the Organizationally Unique Identifier (OUI). The second half (last 3 octets) is the Network Interface Contoller (NIC) specific. So the OUI is registered with the IEEE and defines which organization/company "owns" that block of MAC addresses. The NIC portion is then assigned by that company. If an organization does not expect to use a complete block of an OUI (3 octets), then the OUI can be shared among different companies (MA-M and MA-S).</p><ol><li>MAC Address Block Large (MA-L) = entire OUI is utilized</li><li>MAC Address Block Medium (MA-M) = OUI is shared, first nibble (4-bits) in NIC is unique between companies</li><li>MAC Address Block Small (MA-S) = OUI is shared, first octet (8-bits) in NIC is unique between companies</li></ol><p>By the way, Wireshark provides an OUI look-up tool:</p><p><a href="https://www.wireshark.org/tools/oui-lookup.html">https://www.wireshark.org/tools/oui-lookup.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '17, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-59716" class="comments-container"></div><div id="comment-tools-59716" class="comment-tools"></div><div class="clear"></div><div id="comment-59716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

