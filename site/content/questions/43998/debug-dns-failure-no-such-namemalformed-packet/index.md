+++
type = "question"
title = "debug dns failure No such name[Malformed Packet]"
description = '''why is this packet send what cloud be the possible reason of this failure ? 74866 0.000 192.168.2.103(iphone) 192.168.2.1(routerdns) DNS 51 Standard query 0x004f SOA local 74945 0.018 192.168.2.1(routerdns) 192.168.2.103(iphone) DNS 540 Standard query response 0x004f No such name[Malformed Packet]'''
date = "2015-07-09T00:25:00Z"
lastmod = "2015-07-10T02:07:00Z"
weight = 43998
keywords = [ "dns", "dnsquery" ]
aliases = [ "/questions/43998" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [debug dns failure No such name\[Malformed Packet\]](/questions/43998/debug-dns-failure-no-such-namemalformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43998-score" class="post-score" title="current number of votes">0</div><span id="post-43998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>why is this packet send what cloud be the possible reason of this failure ?</p><p><code>74866   0.000   192.168.2.103(iphone)   192.168.2.1(routerdns)     DNS 51          Standard query 0x004f  SOA local</code></p><p><code>74945   0.018   192.168.2.1(routerdns)  192.168.2.103(iphone)      DNS 540         Standard query response 0x004f No such name[Malformed Packet]</code></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-dnsquery" rel="tag" title="see questions tagged &#39;dnsquery&#39;">dnsquery</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '15, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/5871f5c99fa7f6589884321bf9976ad3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="terrance&#39;s gravatar image" /><p><span>terrance</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="terrance has no accepted answers">0%</span></p></div></div><div id="comments-container-43998" class="comments-container"><span id="44003"></span><div id="comment-44003" class="comment"><div id="post-44003-score" class="comment-score"></div><div class="comment-text"><p>Can you upload the packet to <a href="https://cloudshark.org/?">https://cloudshark.org/?</a> It is hard to tell what went wrong here without a capture.</p></div><div id="comment-44003-info" class="comment-info"><span class="comment-age">(09 Jul '15, 03:13)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="44031"></span><div id="comment-44031" class="comment"><div id="post-44031-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/5f96876e2668">https://www.cloudshark.org/captures/5f96876e2668</a></p></div><div id="comment-44031-info" class="comment-info"><span class="comment-age">(09 Jul '15, 22:57)</span> <span class="comment-user userinfo">terrance</span></div></div></div><div id="comment-tools-43998" class="comment-tools"></div><div class="clear"></div><div id="comment-43998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44033"></span>

<div id="answer-container-44033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44033-score" class="post-score" title="current number of votes">1</div><span id="post-44033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a normal DNS query of Apple devices. Apple is using the TLD (top level domain) <strong>.local</strong> for internal purposes. It's related to mDNS, Bonjour. etc. (see <a href="https://en.wikipedia.org/wiki/.local).">https://en.wikipedia.org/wiki/.local).</a> Apple devices ask for the SOA record of .local to figure out if there is an Apple server running on the network. Your DNS server responds with a "no such name", as it does not have any information about .local. Why the answer packet is flagged as <strong>malformed</strong>, I don't know, but that's not relevant here anyway.</p><p>So, nothing to worry about and nothing you can change.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '15, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44033" class="comments-container"><span id="44035"></span><div id="comment-44035" class="comment"><div id="post-44035-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Why the answer packet is flagged as malformed, I don't know</p></blockquote><p>Because it's too short. All the RRSIG records in the packet <em>claim</em> to be 158 bytes long, based on the data length, but, at the end, there's only room for a 74-byte record, so the packet is too short to have the 158-byte RRSIG at the end - much less the 6th authority RR or the additional RR that the record counts claim should be there.</p></div><div id="comment-44035-info" class="comment-info"><span class="comment-age">(10 Jul '15, 00:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="44038"></span><div id="comment-44038" class="comment"><div id="post-44038-score" class="comment-score"></div><div class="comment-text"><p>thanks for checking that. I did not look into it ;-)</p></div><div id="comment-44038-info" class="comment-info"><span class="comment-age">(10 Jul '15, 02:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-44033" class="comment-tools"></div><div class="clear"></div><div id="comment-44033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

