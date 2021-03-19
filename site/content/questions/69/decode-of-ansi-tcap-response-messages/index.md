+++
type = "question"
title = "Decode of ANSI TCAP response messages"
description = '''Greeings! I&#x27;m attempting to use Wireshark to decode (among other protocols) some ss7/sigtran tcap/map messaging. My protocol stacks are (from the inside out):  ansi_map - ansi_tcap - sccp - mtp3 - mtp2 peer adaptation - sctp - ip  I&#x27;m not much of an ss7 so I kind of fumble with some of the lower lay...'''
date = "2010-09-14T12:18:00Z"
lastmod = "2010-09-15T17:41:00Z"
weight = 69
keywords = [ "ansi_map", "decoding", "sigtran" ]
aliases = [ "/questions/69" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decode of ANSI TCAP response messages](/questions/69/decode-of-ansi-tcap-response-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-69-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-69-score" class="post-score" title="current number of votes">0</div><span id="post-69-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greeings!</p><p>I'm attempting to use Wireshark to decode (among other protocols) some ss7/sigtran tcap/map messaging. My protocol stacks are (from the inside out):<br />
</p><pre><code>ansi_map - ansi_tcap - sccp - mtp3 - mtp2 peer adaptation - sctp - ip</code></pre><p>I'm not much of an ss7 so I kind of fumble with some of the lower layers. (Yes, I have set MTP3 standard to ANSI in my preferences.)</p><p>I'm in the wireless ansi world so I have "simple" map transactions such as LOCREQ and locreq response messages and then I have WIN transactions such as ORREQ and orreq responses messages.<br />
</p><p>All the versions of Wireshark I've tried support decoding the initial commands (e.g. LOCREQ and ORREQ). However, none of the versions will decode the response messages (locreq or orreq).<br />
</p><p>What gets even more curious is that Ethereal v0.99.0 of will decode the ORREQ, orreq and locreq. However, it does not decode LOCREQ. I have ZERO desire to run Ethereal, but I would like to be able to decode my messages.<br />
</p><p>I've searched a bit and have found references to some issues that were being dealt with a couple of years back with (I think) some ss7 decoding issues. Unfortunately, I did find the final resolution to that issue.<br />
</p><p>Should I be able to decode my ansi map and win messages with the current version of Wireshark?<br />
</p><p>Have I missed a preference setting somewhere?<br />
</p><p>Any and all help would be most appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ansi_map" rel="tag" title="see questions tagged &#39;ansi_map&#39;">ansi_map</span> <span class="post-tag tag-link-decoding" rel="tag" title="see questions tagged &#39;decoding&#39;">decoding</span> <span class="post-tag tag-link-sigtran" rel="tag" title="see questions tagged &#39;sigtran&#39;">sigtran</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '10, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/55f8cae6add9cffdcead3632a91d15db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmyhre&#39;s gravatar image" /><p><span>jmyhre</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmyhre has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-69" class="comments-container"><span id="132"></span><div id="comment-132" class="comment"><div id="post-132-score" class="comment-score">1</div><div class="comment-text"><p>"Ethereal" is the name that the program now called "Wireshark" used to have; what</p><p>All the versions of Wireshark I've tried support decoding the initial commands (e.g. LOCREQ and ORREQ). However, none of the versions will decode the response messages (locreq or orreq). What gets even more curious is that Ethereal v0.99.0 of will decode the ORREQ, orreq and locreq. However, it does not decode LOCREQ.</p><p>really means is "it could decode orreq and locreq in 0.99.0, but, at some point after 0.99.0, it couldn't decode them". That's a bug; file it at bugs.wireshark.org (with a capture if possible).</p></div><div id="comment-132-info" class="comment-info"><span class="comment-age">(15 Sep '10, 17:41)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-69" class="comment-tools"></div><div class="clear"></div><div id="comment-69-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="73"></span>

<div id="answer-container-73" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-73-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-73-score" class="post-score" title="current number of votes">0</div><span id="post-73-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you have aprintout like "Dissector for ANSI TCAP NATIONAL code:0 not implemented. Contact Wireshark developers if you want this supported" chanses are that the problem is as decribed in https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4466 "As ANSI TCAP responses does not contain a operation code Wireshark tries to match Responses to Invokes based on Source Destination and Identifier"</p><p>This has to be fixed in the code or change to GSM/UMTS/LTE :-))</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '10, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span> </br></br></p></div></div><div id="comments-container-73" class="comments-container"></div><div id="comment-tools-73" class="comment-tools"></div><div class="clear"></div><div id="comment-73-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="74"></span>

<div id="answer-container-74" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-74-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-74-score" class="post-score" title="current number of votes">0</div><span id="post-74-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the response. I'd hoped it'd be an issue with something I had (or had not configured). Unfortunately, it sounds like an issue with the complexity of the ansi tcap/map specification.<br />
</p><p>Looks like I'll just have to keep ethereal around for when I need help in decoding a response message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '10, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/55f8cae6add9cffdcead3632a91d15db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmyhre&#39;s gravatar image" /><p><span>jmyhre</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmyhre has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-74" class="comments-container"></div><div id="comment-tools-74" class="comment-tools"></div><div class="clear"></div><div id="comment-74-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

