+++
type = "question"
title = "Should an Interface on Laptop running WireShark have an IP Address"
description = '''Just curious to know if I should assign an IP Address to my laptop (running wireshark) interface connected to the SPAN destination port on my cisco swich? i have noticed that when i don&#x27;t assign an address to my laptop&#x27;s interface (Wireshark capturing interface) connected to SPAN destination port on...'''
date = "2012-03-22T07:34:00Z"
lastmod = "2012-03-22T07:53:00Z"
weight = 9699
keywords = [ "interface", "to", "wireshark", "capture", "address" ]
aliases = [ "/questions/9699" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should an Interface on Laptop running WireShark have an IP Address](/questions/9699/should-an-interface-on-laptop-running-wireshark-have-an-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9699-score" class="post-score" title="current number of votes">0</div><span id="post-9699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just curious to know if I should assign an IP Address to my laptop (running wireshark) interface connected to the SPAN destination port on my cisco swich?</p><p>i have noticed that when i don't assign an address to my laptop's interface (Wireshark capturing interface) connected to SPAN destination port on my cisco switch, wireshark captures only DNS, DHCP &amp; NBNS packets.</p><p>i have also noticed that when i assign any address to my laptop's interface (Wireshark capturing interface) connected to SPAN destination port on my cisco switch, wireshark then captures everything.</p><p>is it normal behavior?</p><p>Thanks Fahmeed</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '12, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/31622a3bbbbf992f90124b64273c466f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fbaig&#39;s gravatar image" /><p><span>fbaig</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fbaig has no accepted answers">0%</span></p></div></div><div id="comments-container-9699" class="comments-container"></div><div id="comment-tools-9699" class="comment-tools"></div><div class="clear"></div><div id="comment-9699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9701"></span>

<div id="answer-container-9701" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9701-score" class="post-score" title="current number of votes">0</div><span id="post-9701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I never have an IP address assigned on my laptop card I capture with, just because I want it to be completely passive and prevent it from injecting packets into my capture on its own.</p><p>What's strange is that you say you can't capture anything beyond broadcast packets when you do not assign an IP address. Usually it works just fine and makes no difference (except that without an IP you are passive, as I already said). Promiscuous mode should force your card to accept all frames, even if they're not for your card (you have promiscuous mode checked in your capture settings, don't you?), no matter if an IP is assigned or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9701" class="comments-container"></div><div id="comment-tools-9701" class="comment-tools"></div><div class="clear"></div><div id="comment-9701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

