+++
type = "question"
title = "mDNS Protocol filtering"
description = '''I know that for some protocols, such as http, you can just type &quot;http&quot; in the filter box and wireshark will filter it. However, this doesn&#x27;t seem to work for many protocols, including MDNS, which is what I&#x27;m trying to filter on right now. Is there a way to filter on what is ACTUALLY displayed in the...'''
date = "2013-08-02T07:22:00Z"
lastmod = "2013-08-08T02:28:00Z"
weight = 23518
keywords = [ "filter", "mdns", "filtering", "protocol" ]
aliases = [ "/questions/23518" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mDNS Protocol filtering](/questions/23518/mdns-protocol-filtering)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23518-score" class="post-score" title="current number of votes">0</div><span id="post-23518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know that for some protocols, such as http, you can just type "http" in the filter box and wireshark will filter it. However, this doesn't seem to work for many protocols, including MDNS, which is what I'm trying to filter on right now.</p><p>Is there a way to filter on what is ACTUALLY displayed in the PROTOCOL column of the list?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-mdns" rel="tag" title="see questions tagged &#39;mdns&#39;">mdns</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '13, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/cfb47fa5874edfbcb04379b1c97a81d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ev1lr0b0t&#39;s gravatar image" /><p><span>ev1lr0b0t</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ev1lr0b0t has one accepted answer">50%</span> </br></p></div></div><div id="comments-container-23518" class="comments-container"></div><div id="comment-tools-23518" class="comment-tools"></div><div class="clear"></div><div id="comment-23518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23629"></span>

<div id="answer-container-23629" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23629-score" class="post-score" title="current number of votes">1</div><span id="post-23629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>However, this doesn't seem to work for many protocols, including MDNS,</p></blockquote><p>You can only search for those 'fields' that are registered by a dissector. As the DNS dissector (which also handles MDNS), does not register a field "MDNS", you can't search for it.</p><blockquote><p>Is there a way to filter on what is ACTUALLY displayed in the PROTOCOL column of the list?</p></blockquote><p>No, that's currently not possible, as there is no way to do a text search in the columns itself.</p><p>A possible <strong>solution</strong> for your problem is this display filter.</p><blockquote><p>dns and udp.port eq 5353</p></blockquote><p>which is a simple definition for MDNS. You can also include the multicast IP</p><blockquote><p>dns and udp.port eq 5353 and ip.addr eq 224.0.0.0/24</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23629" class="comments-container"></div><div id="comment-tools-23629" class="comment-tools"></div><div class="clear"></div><div id="comment-23629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

