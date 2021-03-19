+++
type = "question"
title = "Problem with creating an ASN1 dissector"
description = '''Hey, I try to create a new ASN1 dissector for the CAM protocol. If i try to compile the whole Wireshark i get the following error: epan/.libs/libireshark.so: undefined refferenc to &#x27;dissect_CAM_PDU&#x27; I do not know where this error comes from.. I have a function call dissect_CAM_PDU in my packet-CAM-t...'''
date = "2014-09-08T01:41:00Z"
lastmod = "2014-09-08T04:23:00Z"
weight = 36062
keywords = [ "asn2wrs", "asn1" ]
aliases = [ "/questions/36062" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with creating an ASN1 dissector](/questions/36062/problem-with-creating-an-asn1-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36062-score" class="post-score" title="current number of votes">0</div><span id="post-36062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I try to create a new ASN1 dissector for the CAM protocol. If i try to compile the whole Wireshark i get the following error: epan/.libs/libireshark.so: undefined refferenc to 'dissect_CAM_PDU'</p><p>I do not know where this error comes from.. I have a function call dissect_CAM_PDU in my packet-CAM-template.c (like its in the older version of the dissector) but i do not find the body of the function.. I thougt it may be a function which is generatet automatically? But it does not seem so..</p><p>Can someone help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn2wrs" rel="tag" title="see questions tagged &#39;asn2wrs&#39;">asn2wrs</span> <span class="post-tag tag-link-asn1" rel="tag" title="see questions tagged &#39;asn1&#39;">asn1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '14, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/f65ac046295141d9f33ce4ac1770b5a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Venturina&#39;s gravatar image" /><p><span>Venturina</span><br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Venturina has no accepted answers">0%</span></p></div></div><div id="comments-container-36062" class="comments-container"></div><div id="comment-tools-36062" class="comment-tools"></div><div class="clear"></div><div id="comment-36062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36064"></span>

<div id="answer-container-36064" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36064-score" class="post-score" title="current number of votes">1</div><span id="post-36064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, It's not so easy to give advice without seeing the actual code. If this is a public protocol and you intend to submit it to Wireshark you could upload it for review trough gerrit.</p><p>In general in the template you will ned a function that "calls" the generated part of the code how this is to be designed depends on the protocol. So probably you need the body of "dissect_CAM_PDU" in the template or .cnf file or possibly if the ASN1 contains CAM-PDU ::= the dissect_CAM_PDU() function should have been generated for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '14, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-36064" class="comments-container"><span id="36066"></span><div id="comment-36066" class="comment"><div id="post-36066-score" class="comment-score"></div><div class="comment-text"><p>Looking at ETSI TS 102 637-2 V1.2.1 (2011-03)</p><p>-- ASN1START CAM-PDU-Descriptions { itu-t (0) identified-organization (4) etsi (0) itsDomain (5) wg1 (1) ts (102637) cam (2) version1 (1) } DEFINITIONS AUTOMATIC TAGS ::= BEGIN IMPORTS ItsPduHeader, VehicleCommonParameters, ProfileParameters, StationID, TimeStamp, ReferencePosition FROM DENM-PDU-Descriptions { itu-t (0) identified-organization (4) etsi (0) itsDomain (5) wg1 (1) ts (102637) denm (3) version2 (2) }; -- The root data frame for cooperative awareness messages CamPdu ::= SEQUENCE { header ItsPduHeader, cam CoopAwareness } :</p><p>It looks like dissect_cam_CamPdu() (or something similar depending on the name you chose for your dissector) should have been automatically generated.</p></div><div id="comment-36066-info" class="comment-info"><span class="comment-age">(08 Sep '14, 04:23)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-36064" class="comment-tools"></div><div class="clear"></div><div id="comment-36064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

