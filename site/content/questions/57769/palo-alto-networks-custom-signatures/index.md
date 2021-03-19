+++
type = "question"
title = "Palo Alto Networks Custom Signatures"
description = '''I work with PAN products doing pro services. I have been really trying to correlate the Palo Alto context for custom signatures and what we find in Wireshark Display filters. Being somewhat new to this whole process, I thought I&#x27;d post a question here and see where it goes. My apologies if this is n...'''
date = "2016-12-01T12:15:00Z"
lastmod = "2016-12-02T06:15:00Z"
weight = 57769
keywords = [ "signature" ]
aliases = [ "/questions/57769" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Palo Alto Networks Custom Signatures](/questions/57769/palo-alto-networks-custom-signatures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57769-score" class="post-score" title="current number of votes">0</div><span id="post-57769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I work with PAN products doing pro services. I have been really trying to correlate the Palo Alto context for custom signatures and what we find in Wireshark Display filters. Being somewhat new to this whole process, I thought I'd post a question here and see where it goes. My apologies if this is not the correct forum for this type of question.</p><p>What I am trying to do is to understand how a Palo Alto context matches with something you would find decoded or dissected by Wireshark ( I assume decoder and dissector are synonymous ?)</p><p>So.. as an example I want to write a PAN Custom Signature. I obtain a packet capture. I can dig through and find some unique field or string i want to match on. Then the real work, or the real question is, how do I relate that to what Palo Alto defines as context? They have documentation that roughly equates to something you may see in Wireshark.</p><p>For example an integer context defined by Palo Alto would be such dnp3-req-object-type</p><p>I can find nothing that really matches in a display filter. Unless i have Palo Alto's reference material and some clue as to where I may find this integer, i really dont see how else I would create a custom signature.</p><p>I type dnp3. in Wireshark display filter and I get a possible list of filters that might get me to the field or value I am looking for. But these references dont match anything near what PAN is suggesting.</p><p>Perhaps there is a reason PAN just doesn't use the same filter syntax or perhaps I'm not getting something.</p><p>Does anybody have experience writing custom sigs with PANOS ?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-signature" rel="tag" title="see questions tagged &#39;signature&#39;">signature</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '16, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/705d4a9044e157d49ea31624c27a2b00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dlammon&#39;s gravatar image" /><p><span>dlammon</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dlammon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Dec '16, 13:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-57769" class="comments-container"></div><div id="comment-tools-57769" class="comment-tools"></div><div class="clear"></div><div id="comment-57769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57783"></span>

<div id="answer-container-57783" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57783-score" class="post-score" title="current number of votes">0</div><span id="post-57783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark display filter strings are essentially random, added as a dissector author's personal preference with little if any reference to external standards. Certainly that's the case with dnp3, where I personally added a lot of those fields and I used abbreviations that made sense to me.</p><p>Note also that these field names may change at any point in time if a dissector is modified, although we don't like changing them as it causes issues for users with previously prepared filters.</p><p>As to what PAN use for the context names, unless they religiously track what the fields are in Wireshark dissectors, I think any correlation with Wireshark is just coincidence.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '16, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57783" class="comments-container"><span id="57789"></span><div id="comment-57789" class="comment"><div id="post-57789-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the response, makes total sense. For me I guess its a matter of just correlating what PAN uses with something I can find in a packet trace. Paying "attention" ( for me ) is probably the operative word :-) It is good to know also that if some field can be used to match something with a Palo Alto Signature at some point in time it may not, if the dissector changes .</p></div><div id="comment-57789-info" class="comment-info"><span class="comment-age">(02 Dec '16, 06:15)</span> <span class="comment-user userinfo">dlammon</span></div></div></div><div id="comment-tools-57783" class="comment-tools"></div><div class="clear"></div><div id="comment-57783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

