+++
type = "question"
title = "Gre Decapsulation"
description = '''Is there a version of wireshark that can decapsulate a gre tunnel? I&#x27;ve set up a gre tunnel between two endpoint and traversing a middle box. I am trying to sniffer at the middle box and inspect the data stream. The version of wireshark suggested on the &quot;wishes&quot; wiki. 0.10.8 does not work, the data ...'''
date = "2011-02-23T12:24:00Z"
lastmod = "2011-02-24T09:22:00Z"
weight = 2532
keywords = [ "gre" ]
aliases = [ "/questions/2532" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Gre Decapsulation](/questions/2532/gre-decapsulation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2532-score" class="post-score" title="current number of votes">0</div><span id="post-2532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a version of wireshark that can decapsulate a gre tunnel?</p><p>I've set up a gre tunnel between two endpoint and traversing a middle box. I am trying to sniffer at the middle box and inspect the data stream.</p><p>The version of wireshark suggested on the "wishes" wiki. 0.10.8 does not work, the data within the gre frame is not decoded.</p><p>the data is stacked, application/ip/ppp/gre/ip/enet</p><p>It would also be great if I could decode what was within the ppp frame as well.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gre" rel="tag" title="see questions tagged &#39;gre&#39;">gre</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '11, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/9cfb21851200396681dfa46bb00597fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kylewh&#39;s gravatar image" /><p><span>kylewh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kylewh has no accepted answers">0%</span></p></div></div><div id="comments-container-2532" class="comments-container"></div><div id="comment-tools-2532" class="comment-tools"></div><div class="clear"></div><div id="comment-2532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2533"></span>

<div id="answer-container-2533" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2533-score" class="post-score" title="current number of votes">0</div><span id="post-2533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Where is this really old version suggested? I think the current version of Wireshark (1.4.3 stable or 1.5.0 development) will be able to display all layers correctly. If not, are you able to share a small capture file with these packets?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '11, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2533" class="comments-container"><span id="2550"></span><div id="comment-2550" class="comment"><div id="post-2550-score" class="comment-score"></div><div class="comment-text"><p>http://wiki.wireshark.org/WishList</p><p>this page mentions in the dissector details section that version 0.10.8 would decapsulate gre, but i've tried version 0.10.8 and it does not decapsulate GRE.</p><p>I've tried with the latest version of wireshark as well, and the data within the gre packets is not detailed.</p><p>Unfortunately I cannot share a file capture in this forum.</p></div><div id="comment-2550-info" class="comment-info"><span class="comment-age">(24 Feb '11, 06:57)</span> <span class="comment-user userinfo">kylewh</span></div></div><span id="2554"></span><div id="comment-2554" class="comment"><div id="post-2554-score" class="comment-score"></div><div class="comment-text"><p>Is it possible for you to share some kind of screenshot (preferably with 1.4.3 or 1.5 version? )</p><p>I feel you need to decode packets to GRE. Try it and let us know...</p></div><div id="comment-2554-info" class="comment-info"><span class="comment-age">(24 Feb '11, 08:23)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div><span id="2555"></span><div id="comment-2555" class="comment"><div id="post-2555-score" class="comment-score"></div><div class="comment-text"><p>As the wishlist says, there is a dissector for GRE encapsulation type 0x8881 (is that what you are using too?), but it is not complete as reassembly is not implemented.</p><p>A screenshot showing the GRE details or the hex data of one or two packets would make it easier to see what's going on in your situation.</p></div><div id="comment-2555-info" class="comment-info"><span class="comment-age">(24 Feb '11, 09:22)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-2533" class="comment-tools"></div><div class="clear"></div><div id="comment-2533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

