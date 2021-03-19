+++
type = "question"
title = "How to filter GSM messages in Wireshark?"
description = '''In my Wireshark Network traffic I get both 2G and 3G data packets (gsm_map). How to filter only 2g or only 3g data packets? We usually concern about AnyTimeInterrogation message in GSM.'''
date = "2013-10-23T05:43:00Z"
lastmod = "2013-10-24T17:55:00Z"
weight = 26321
keywords = [ "filter", "packet-display", "packet", "display-filter" ]
aliases = [ "/questions/26321" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter GSM messages in Wireshark?](/questions/26321/how-to-filter-gsm-messages-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26321-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my Wireshark Network traffic I get both 2G and 3G data packets (gsm_map). How to filter only 2g or only 3g data packets?</p><p>We usually concern about AnyTimeInterrogation message in GSM.</p></div><div id="question-tags" class="tags-container tags">filter packet-display packet display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/4d5a1d4ba48122bcddd239a84b8bf3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pranitkothari&#39;s gravatar image" /><p>pranitkothari<br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pranitkothari has one accepted answer">100%</span></p></div></div><div id="comments-container-26321" class="comments-container"></div><div id="comment-tools-26321" class="comment-tools"></div><div class="clear"></div><div id="comment-26321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="26346"></span>

<div id="answer-container-26346" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26346-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found answer myself.</p><p>In display filter, I need to use,</p><pre><code>gsm_map.ms.sai_Present</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '13, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/4d5a1d4ba48122bcddd239a84b8bf3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pranitkothari&#39;s gravatar image" /><p>pranitkothari<br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pranitkothari has one accepted answer">100%</span></p></div></div><div id="comments-container-26346" class="comments-container"></div><div id="comment-tools-26346" class="comment-tools"></div><div class="clear"></div><div id="comment-26346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26322"></span>

<div id="answer-container-26322" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26322-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It might be possible to filter on AnyTimeInterrogationRes and values in SubscriberInfo like lastRAT-Type but the element is Optional so I'm not sure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '13, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-26322" class="comments-container"><span id="26349"></span><div id="comment-26349" class="comment"><div id="post-26349-score" class="comment-score"></div><div class="comment-text"><p>I got good hint from your answer. Final answer I have posted to my question. Thanks.</p></div><div id="comment-26349-info" class="comment-info"><span class="comment-age">(24 Oct '13, 00:41)</span> pranitkothari</div></div></div><div id="comment-tools-26322" class="comment-tools"></div><div class="clear"></div><div id="comment-26322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26383"></span>

<div id="answer-container-26383" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26383-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Pranitkothari, just make sure that you don't run into cases where the subscriber is reachable by UMTS but the SAI is not included in the ATI return. A few things to note about your approach here:</p><ul><li>ATI/PSIR call flow will at best return the last-known subscriber location. A paging procedure will not be triggered by VMSC just to return a PSIR.</li><li>VMSC does not need to return an SAI. It's optional and is potentially subject to vendor-proprietary logic. For example, an operator may not want SAI-level precision to be available to anything that interrogates their HLR.</li><li>Consider the case of CS Fallback, if your network includes EUTRAN radio access as well as the UMTS cells you're trying to filter for. In that case, a UE can be available in an SAI (by virtue of VMSC -&gt; MME page procedure with a release with redirect back to UMTS), but an SAI could not be returned in ATI query since the subscriber last registered via an ECGI, not an SAI (in which case, at best, last-known location from the perspective of VMSC/HLR would be at the LAI-level).</li></ul><p>Those items might sound like paranoia if you're literally just looking for ATI responsees where the location returned was in UMTS coverage, but depending on your network environment that it's possible to be available in UMTS but not have an SAI included in ATI response to the interrogator. The solution may work for you depending on your case though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '13, 17:55</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '13, 17:58</p></div></div><div id="comments-container-26383" class="comments-container"><span id="26394"></span><div id="comment-26394" class="comment"><div id="post-26394-score" class="comment-score"></div><div class="comment-text"><p>@Quadratic: We are dealing with location related services, and it is ensured from our vendor that we will get SAI in UMTS packet if we request for ATI.</p><p>You really seems to have good in-depth knowledge of GMS/UMTS. We work in location related services, can you please suggest good reference material and forum for GSM and UMTS?</p></div><div id="comment-26394-info" class="comment-info"><span class="comment-age">(24 Oct '13, 23:32)</span> pranitkothari</div></div><span id="26417"></span><div id="comment-26417" class="comment"><div id="post-26417-score" class="comment-score"></div><div class="comment-text"><p>I asked the same question when I started in the mobile space. It's unfortunate, but the best resource out there I've ever been able to find has been the 3GPP whitepapers, with the second best probably being the paid training services of groups like Award Solutions. There's some youtube stuff out there but most is just intro and none that I've seen are very real-world.</p><p>Aside from a lack of strong open training resources out there, there's also no real authority to point to for certifications to validate knowledge in mobile signaling theory, and from that there's a lack of a single sylabus and knowledge base to develop training materials around. For lack of a better analogy, there is no "CCNA of mobile wireless signaling" for everyone to turn to, no way to ask for that validation in an interview, and for those who want to learn you're largely faced with reading the 3GPP whitepapers and RFCs.</p><p>Now, I don't consider myself a very effective teacher most of the time, since I have a hard time considering where the audience is coming from and they get lost in my analogies a lot, but I <em>am</em> trying to do something about this problem. I'm not focused on the UMTS side at the moment, but for the evolved packet core I am trying to complete a decent video series on everything from base call flows to mobility management to policy and credit control. It's been hard to find all the time to get it done on my own time, and another big difficulty is that I'm trying to make it very real-world but NDA agreements prevent most real-world examples or stories I could give, and it's very hard to find packet captures that could be used for that kind of training video exercise which wouldn't be barred by NDAs as well.</p></div><div id="comment-26417-info" class="comment-info"><span class="comment-age">(25 Oct '13, 17:48)</span> Quadratic</div></div></div><div id="comment-tools-26383" class="comment-tools"></div><div class="clear"></div><div id="comment-26383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

