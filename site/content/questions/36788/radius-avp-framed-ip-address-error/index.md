+++
type = "question"
title = "RADIUS AVP - Framed-IP-Address error"
description = ''' I have a device sending RADIUS accounting packets to my Firewall. I got raw captures from the device and when I look at the AVP in the packet for Framed-IP-Address I get an error. AVP: l=14 t=Framed-IP-Address(8): [wrong length for IP address] Anyone ever see this and does it mean that the device i...'''
date = "2014-10-02T08:24:00Z"
lastmod = "2014-10-03T07:16:00Z"
weight = 36788
keywords = [ "avp", "radius" ]
aliases = [ "/questions/36788" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [RADIUS AVP - Framed-IP-Address error](/questions/36788/radius-avp-framed-ip-address-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36788-score" class="post-score" title="current number of votes">0</div><span id="post-36788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/radius-acct-avp.PNG" alt="alt text" /></p><p>I have a device sending RADIUS accounting packets to my Firewall. I got raw captures from the device and when I look at the AVP in the packet for Framed-IP-Address I get an error.</p><p>AVP: l=14 t=Framed-IP-Address(8): [wrong length for IP address]</p><p>Anyone ever see this and does it mean that the device is sending an improperly formatted IP in the packet?</p><p>When I export selected backet bytes I get the following output: xx10.15.29.253 (something is in front of the IP shows up as unrecognized characters so I cannot display them in this post but they are where the xx are). Perhaps this is it? I just don't know what this is supposed formatted.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-avp" rel="tag" title="see questions tagged &#39;avp&#39;">avp</span> <span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '14, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/62b1883ad5fa5f6b7b5d4d52d96ee01d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjjohnsto&#39;s gravatar image" /><p><span>tjjohnsto</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjjohnsto has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '14, 08:29</strong> </span></p></div></div><div id="comments-container-36788" class="comments-container"></div><div id="comment-tools-36788" class="comment-tools"></div><div class="clear"></div><div id="comment-36788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36800"></span>

<div id="answer-container-36800" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36800-score" class="post-score" title="current number of votes">1</div><span id="post-36800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tjjohnsto has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As I read RFC <a href="https://tools.ietf.org/html/rfc2865#section-5.8">2865 section 5.8</a>, the device is sending the Framed-IP-Address in the wrong format. It should consist of 6 bytes: 1 byte of Type, 1 byte of Length, and 4 bytes of IP(v4) address.</p><p>It would appear that the device in question mistakenly encoded the IP address in ASCII (12 bytes).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '14, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36800" class="comments-container"><span id="36820"></span><div id="comment-36820" class="comment"><div id="post-36820-score" class="comment-score"></div><div class="comment-text"><p>Jeff,</p><p>This was the correct answer. Thanks a lot. Now they will go back and fix their software.</p></div><div id="comment-36820-info" class="comment-info"><span class="comment-age">(03 Oct '14, 07:16)</span> <span class="comment-user userinfo">tjjohnsto</span></div></div></div><div id="comment-tools-36800" class="comment-tools"></div><div class="clear"></div><div id="comment-36800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

