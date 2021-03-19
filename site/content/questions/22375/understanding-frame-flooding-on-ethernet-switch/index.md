+++
type = "question"
title = "Understanding Frame Flooding on Ethernet Switch"
description = '''We are seeing an issue on one of our Ethernet switches(Juniper QFX3500) .Ports were shared across the team and each member is complaining that on their captures they are seeing the traffic not intended to them. Further checking the mac table we identified that destination macs were not discovered by...'''
date = "2013-06-26T14:56:00Z"
lastmod = "2013-06-26T15:47:00Z"
weight = 22375
keywords = [ "flooding" ]
aliases = [ "/questions/22375" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Understanding Frame Flooding on Ethernet Switch](/questions/22375/understanding-frame-flooding-on-ethernet-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22375-score" class="post-score" title="current number of votes">0</div><span id="post-22375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are seeing an issue on one of our Ethernet switches(Juniper QFX3500) .Ports were shared across the team and each member is complaining that on their captures they are seeing the traffic not intended to them.</p><p>Further checking the mac table we identified that destination macs were not discovered by the switch and there is an entry i guess that is causing the issue which is shown below.In this case will all (for which dest mac were not discovered) fell in the category of <strong>unknown unicast</strong> and causing the flooding?</p><p>VLAN MAC address Type Age Interfaces</p><p>default * Flood - All-members</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flooding" rel="tag" title="see questions tagged &#39;flooding&#39;">flooding</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-22375" class="comments-container"></div><div id="comment-tools-22375" class="comment-tools"></div><div class="clear"></div><div id="comment-22375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22377"></span>

<div id="answer-container-22377" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22377-score" class="post-score" title="current number of votes">2</div><span id="post-22377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, switches will flood traffic to all ports in the vlan if the destination mac-address was not seen as a source yet.</p><p>See also the answers to <a href="http://ask.wireshark.org/questions/268/seeing-unicast-traffic-on-a-switchport-without-spanning">this question...</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22377" class="comments-container"></div><div id="comment-tools-22377" class="comment-tools"></div><div class="clear"></div><div id="comment-22377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

