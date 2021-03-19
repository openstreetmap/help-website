+++
type = "question"
title = "wireshark giving error  undefined symbol: csnStreamDissector"
description = '''Hello i&#x27;m currently using wireshark-1.10.2 and i&#x27;m writing code for my own plugin by taking the existing reference code from wireshark i.e./epan/dissectors/packet-gsm_rlcmac.c and i&#x27;m using all API&#x27;s which they are using in packet-gsm_rlcmac.c and i&#x27;ve included corresponding.h file in my code code i...'''
date = "2014-06-20T05:23:00Z"
lastmod = "2014-06-23T05:48:00Z"
weight = 33988
keywords = [ "to", "wireshark-undefined", "refernce", "csnstreamdissetor" ]
aliases = [ "/questions/33988" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark giving error undefined symbol: csnStreamDissector](/questions/33988/wireshark-giving-error-undefined-symbol-csnstreamdissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33988-score" class="post-score" title="current number of votes">0</div><span id="post-33988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello i'm currently using wireshark-1.10.2 and i'm writing code for my own plugin by taking the existing reference code from wireshark i.e./epan/dissectors/packet-gsm_rlcmac.c and i'm using all API's which they are using in packet-gsm_rlcmac.c and i've included corresponding.h file in my code code is compiled but after starting wireshark its giving above mentioned error because its not able to get the definition of this function (csnStreamDissector()) in which definition is available in packet-csn1.c,this epan/dissectors is not creating any .so but my code is creating .so but able to get the definition if any one has idea about how to resolve the isssue please post comments here or any one can send there responses to my mail id :<span class="__cf_email__" data-cfemail="81eaf2e0e6e0f3b2b3b0c1e6ece0e8edafe2eeec">[email protected]</span> ,please try to help us by resolving this issue..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span> <span class="post-tag tag-link-wireshark-undefined" rel="tag" title="see questions tagged &#39;wireshark-undefined&#39;">wireshark-undefined</span> <span class="post-tag tag-link-refernce" rel="tag" title="see questions tagged &#39;refernce&#39;">refernce</span> <span class="post-tag tag-link-csnstreamdissetor" rel="tag" title="see questions tagged &#39;csnstreamdissetor&#39;">csnstreamdissetor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '14, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/7596daf4fb3556a397822344b20e2362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagar&#39;s gravatar image" /><p><span>sagar</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagar has no accepted answers">0%</span></p></div></div><div id="comments-container-33988" class="comments-container"></div><div id="comment-tools-33988" class="comment-tools"></div><div class="clear"></div><div id="comment-33988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33996"></span>

<div id="answer-container-33996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33996-score" class="post-score" title="current number of votes">0</div><span id="post-33996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Those functions needs to be exported to be available by plugins on Windows. You could try a built in dissector instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '14, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-33996" class="comments-container"><span id="34056"></span><div id="comment-34056" class="comment"><div id="post-34056-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I will try the built in dissector method. But in general, is it possible to write a custom plugin based on CSN.1 encoding using the APIs provided by packet-csn1.</p></div><div id="comment-34056-info" class="comment-info"><span class="comment-age">(23 Jun '14, 00:50)</span> <span class="comment-user userinfo">sagar</span></div></div><span id="34067"></span><div id="comment-34067" class="comment"><div id="post-34067-score" class="comment-score"></div><div class="comment-text"><p>how to decode a message which is not mentioned in decode as and my message was compiled and it is showing in wireshark enable protocols but it is not mentioned the decode as filter,can any body help me..</p></div><div id="comment-34067-info" class="comment-info"><span class="comment-age">(23 Jun '14, 05:18)</span> <span class="comment-user userinfo">sagar</span></div></div><span id="34069"></span><div id="comment-34069" class="comment"><div id="post-34069-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Thanks, I will try the built in dissector method. But in general, is &gt;it possible to write a custom plugin based on CSN.1 encoding using &gt;the APIs provided by packet-csn1.</p></blockquote><p>Currently not as the API isn't exported. I think that is solved by adding WS_DLL_PUBLIC to the needed functions. This makes a plugin problematic as the Wireshark base for the plugin will have to have the changes incorporated and if you need a released version of Wireshark you will have to wait untill a released version with this changes are available.</p><blockquote><p>how to decode a message which is not mentioned in decode as and my &gt;message was compiled and it is showing in wireshark enable protocols &gt;but it is not mentioned the decode as filter,can any body help me..</p></blockquote><p>That depends on how your dissector is called, via a TCP/UDP/SCTP port or? The decode as API has been greatly improved in the uppcomming 1.12 release. You may be better off working with that.</p><p>Have you considered contributing your code to Wireshark which would make all of this much simpler...</p></div><div id="comment-34069-info" class="comment-info"><span class="comment-age">(23 Jun '14, 05:48)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-33996" class="comment-tools"></div><div class="clear"></div><div id="comment-33996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

