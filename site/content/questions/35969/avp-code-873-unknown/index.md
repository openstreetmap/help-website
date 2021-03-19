+++
type = "question"
title = "AVP Code 873 Unknown"
description = '''Hello, I am doing some troubleshooting for a diameter integration but AVP 873 appears as unkown with the following message: &quot;if you know what this is you can add it to dictionary.xml&quot; Is there any new dictionary that already has this AVP defined that i can use?'''
date = "2014-09-03T12:45:00Z"
lastmod = "2014-09-04T15:51:00Z"
weight = 35969
keywords = [ "diameter", "avp873" ]
aliases = [ "/questions/35969" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [AVP Code 873 Unknown](/questions/35969/avp-code-873-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35969-score" class="post-score" title="current number of votes">0</div><span id="post-35969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am doing some troubleshooting for a diameter integration but AVP 873 appears as unkown with the following message: "if you know what this is you can add it to dictionary.xml"</p><p>Is there any new dictionary that already has this AVP defined that i can use?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-avp873" rel="tag" title="see questions tagged &#39;avp873&#39;">avp873</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '14, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/e6ce6d244513167221a35bd9f4ce028a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AMM91249&#39;s gravatar image" /><p><span>AMM91249</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AMM91249 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Sep '14, 06:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-35969" class="comments-container"><span id="35977"></span><div id="comment-35977" class="comment"><div id="post-35977-score" class="comment-score"></div><div class="comment-text"><p>Is this a 3GPP AVP (is the V-bit set with a Vendor-ID of 3GPP)?</p><p>What version are you using?</p><p>AVP code 873 for Vendor-ID of 3GPP has been in Wireshark for quite a while. (OTOH AVP code of 873 for other vendor IDs--including no vendor-ID--isn't supported any version.)\</p><p>If in doubt can you post the capture somewhere (e.g., cloudshark.org)?</p></div><div id="comment-35977-info" class="comment-info"><span class="comment-age">(03 Sep '14, 16:58)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-35969" class="comment-tools"></div><div class="clear"></div><div id="comment-35969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36013"></span>

<div id="answer-container-36013" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36013-score" class="post-score" title="current number of votes">0</div><span id="post-36013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark 1.12.0 decodes this as 3GPP's Service-Information AVP provided that the Vendor ID field for the AVP is 10415 and that the Vendor-Specific bit is set. For example, this is a hexadecimal stream of an AVP I just correctly decoded this way: <strong>00000369</strong> <strong>c0</strong>00000c<strong>000028af</strong></p><p>I bolded the AVP code, AVP flags and Vendor ID fields containing those values respectively.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '14, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-36013" class="comments-container"></div><div id="comment-tools-36013" class="comment-tools"></div><div class="clear"></div><div id="comment-36013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

