+++
type = "question"
title = "ipv6 RS / RA messages"
description = '''hi all, Probably an easy question but I cannot figure it out so would appreciate some help.  As per RFC the source address of a RS message can be either the IP address assigned to the sending interface, or unspecified address if no address is assigned to the sending interface. The link-layer address...'''
date = "2015-10-31T13:06:00Z"
lastmod = "2015-10-31T17:13:00Z"
weight = 47118
keywords = [ "ipv6" ]
aliases = [ "/questions/47118" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ipv6 RS / RA messages](/questions/47118/ipv6-rs-ra-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47118-score" class="post-score" title="current number of votes">0</div><span id="post-47118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,</p><p>Probably an easy question but I cannot figure it out so would appreciate some help.</p><p>As per RFC the source address of a RS message can be either the IP address assigned to the sending interface, or <strong>unspecified address</strong> if no address is assigned to the sending interface. The link-layer address of the sender, if known. MUST NOT be included if the Source Address is the unspecified address. Otherwise it SHOULD be included on link layers that have addresses.</p><p>In case the src address of the RS = unspecified address how can I (based on a Wireshark capture) know which Router Advertisement is the response to the RS above ?</p><p>RFC regarding RA messages states:</p><p>"Destination Address Typically the Source Address of an invoking Router Solicitation or the all-nodes multicast address."</p><p>So if the src was unspecified address, the RA will response to the all-nodes multicast address.</p><p>I think I have problems to understand it, because it is unclear for me what is the order of the messages ... I have some Wireshark captures where the src address of a RS = fe80: .. . ( so a link-local address). What would cause a host to send a RS message with src=unspecified ? Is it not the feature of IPv6 (plug and play) that each device will auto generate a link-local address for itself ?</p><p>I know this might be partially a Wireshark question but I hope this question will not be flaged as offtopic.</p><p>Any help is appreciated!</p><p>Best Regards</p><p>Adam<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '15, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-47118" class="comments-container"><span id="47123"></span><div id="comment-47123" class="comment"><div id="post-47123-score" class="comment-score"></div><div class="comment-text"><p>Could you please add the rfc number it is easier to google.</p></div><div id="comment-47123-info" class="comment-info"><span class="comment-age">(31 Oct '15, 16:36)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-47118" class="comment-tools"></div><div class="clear"></div><div id="comment-47118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47124"></span>

<div id="answer-container-47124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47124-score" class="post-score" title="current number of votes">0</div><span id="post-47124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you read the <a href="https://tools.ietf.org/html/rfc3513#page-9">RFC3513</a> and <a href="https://tools.ietf.org/html/rfc3590">RFC 3590</a> they are both talking about an unspecified address.<br />
<br />
<a href="https://tools.ietf.org/html/rfc3590">RFC 3590:</a><br />
</p><pre><code>   5. Source Address Selection Implications
In RFC 2710, MLD Report and Done messages are required to have an
   IPv6 source address that is link-local.  This memo augments that rule
   by allowing these messages to contain the unspecified address (::) as
   the source address.
The behavior of RFC 2710 implementations, when receiving a message
   with a source address of ::, is dependent upon how the implementation
   treats the unspecified address.  That is, these messages will be
   dropped if the implementation does not consider the unspecified
   address to be link-local in scope.
As the unspecified address is only used when there is no link-local
   address, RFC 2710 implementations discarding these packets will have
   no affect on the packet&#39;s sender as the use should only be for
   joining the link-local solicited-node multicast group [RFC 2462].
There is an implication to senders with respect to joining other
   multicast groups prior to the activation of a link-local address.
   The dropping of Reports using the unspecified address as a source
   address could cause a lack of multicast traffic that is expected by
   the node.  This black hole will be temporary until the node can send
   a Report with a valid link-local address.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '15, 17:13</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div></div><div id="comments-container-47124" class="comments-container"></div><div id="comment-tools-47124" class="comment-tools"></div><div class="clear"></div><div id="comment-47124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

