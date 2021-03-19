+++
type = "question"
title = "How can I get Spanning Tree Protocol&#x27;s &quot;Originating Vlan (PVID):&quot; section to appear???"
description = ''' Team,  How can I get the field &quot;Originating VLAN (PVID)&quot; to appear on my version of Wireshark? I am currently running 1.10.6 and a person who is running 1.12.1 gave me the file below and his capture does display such field. Does this have something to do with the version? Or is this something I can...'''
date = "2015-06-30T17:02:00Z"
lastmod = "2015-07-02T04:32:00Z"
weight = 43757
keywords = [ "spanning", "vlan", "spanningtree" ]
aliases = [ "/questions/43757" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get Spanning Tree Protocol's "Originating Vlan (PVID):" section to appear???](/questions/43757/how-can-i-get-spanning-tree-protocols-originating-vlan-pvid-section-to-appear)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43757-score" class="post-score" title="current number of votes">0</div><span id="post-43757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/wsQUESTION_LDv9IWP.png" alt="alt text" /></p><p>Team, How can I get the field "Originating VLAN (PVID)" to appear on my version of Wireshark? I am currently running 1.10.6 and a person who is running 1.12.1 gave me the file below and his capture does display such field. Does this have something to do with the version? Or is this something I can modify on Wireshark? Thanks in advance!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-spanning" rel="tag" title="see questions tagged &#39;spanning&#39;">spanning</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-spanningtree" rel="tag" title="see questions tagged &#39;spanningtree&#39;">spanningtree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '15, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/e0b5d3204af69b366bdd90facf703aa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaby8a&#39;s gravatar image" /><p><span>gaby8a</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaby8a has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43757" class="comments-container"><span id="43766"></span><div id="comment-43766" class="comment"><div id="post-43766-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us the the trace at dropbox or cloudshark?</p></div><div id="comment-43766-info" class="comment-info"><span class="comment-age">(30 Jun '15, 22:03)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="43778"></span><div id="comment-43778" class="comment"><div id="post-43778-score" class="comment-score"></div><div class="comment-text"><p>I will put it on a dropbox soon.</p></div><div id="comment-43778-info" class="comment-info"><span class="comment-age">(01 Jul '15, 05:30)</span> <span class="comment-user userinfo">gaby8a</span></div></div><span id="43784"></span><div id="comment-43784" class="comment"><div id="post-43784-score" class="comment-score"></div><div class="comment-text"><p>Here is the trace: <a href="https://www.dropbox.com/s/bc7n63mgxa3zjnd/from%20sw1%20to%20sw2.pcapng?dl=0">https://www.dropbox.com/s/bc7n63mgxa3zjnd/from%20sw1%20to%20sw2.pcapng?dl=0</a></p><p>thank you!</p></div><div id="comment-43784-info" class="comment-info"><span class="comment-age">(01 Jul '15, 06:59)</span> <span class="comment-user userinfo">gaby8a</span></div></div></div><div id="comment-tools-43757" class="comment-tools"></div><div class="clear"></div><div id="comment-43757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43770"></span>

<div id="answer-container-43770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43770-score" class="post-score" title="current number of votes">2</div><span id="post-43770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You basically gave the answer yourself. The main difference in BPDU dissection between 1.10 and 1.12 is this field. So moving on to 1.12 would help you in this regard.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '15, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-43770" class="comments-container"><span id="43779"></span><div id="comment-43779" class="comment"><div id="post-43779-score" class="comment-score"></div><div class="comment-text"><p>thank you guys. I had suspected it was a version issue, but I was not sure. Jaap, would you kindly direct me to where I can find this information? I want to know where I can find these things. I am still sort of a newbie with wireshark. Thanks.</p></div><div id="comment-43779-info" class="comment-info"><span class="comment-age">(01 Jul '15, 05:31)</span> <span class="comment-user userinfo">gaby8a</span></div></div><span id="43811"></span><div id="comment-43811" class="comment"><div id="post-43811-score" class="comment-score"></div><div class="comment-text"><p>Well, usually from release notes, but as stated for 1.12.0:</p><pre><code> 2.6. Updated Protocol Support
 Too many protocols have been updated to list here.</code></pre><p>It's hard to figure out. So, we go back to the source: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-bpdu.c;h=d57133f8fca436929154d030ddb5d86fed406371;hb=3dac78778cca8a7838350c67d322c90053977d8a">packet-bpdu.c v1.10.6</a> vs <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-bpdu.c;h=a8151876c32abda9cf8323497363ae52b177532c;hb=01b65bf3a8e3d2f856471b0bb5a7e38dabf815f3">packet-bpdu.c v1.12.1</a></p></div><div id="comment-43811-info" class="comment-info"><span class="comment-age">(02 Jul '15, 04:31)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="43812"></span><div id="comment-43812" class="comment"><div id="post-43812-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-43812-info" class="comment-info"><span class="comment-age">(02 Jul '15, 04:32)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-43770" class="comment-tools"></div><div class="clear"></div><div id="comment-43770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

