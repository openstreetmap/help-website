+++
type = "question"
title = "Vlan tags in captures"
description = '''Hi,  I am using wireshark with HP elitebook 8470p. When I try to capture double tagged packets, I see only one vlan, and when I try to capture single tagged packets, I see no vlan. I think I must do some configuration change on wireshark or ethernet card but couldnt find. Could you please help me? T...'''
date = "2014-07-02T11:02:00Z"
lastmod = "2014-07-08T08:49:00Z"
weight = 34358
keywords = [ "capture", "single", "vlan", "tag", "qinq" ]
aliases = [ "/questions/34358" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Vlan tags in captures](/questions/34358/vlan-tags-in-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34358-score" class="post-score" title="current number of votes">0</div><span id="post-34358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using wireshark with HP elitebook 8470p. When I try to capture double tagged packets, I see only one vlan, and when I try to capture single tagged packets, I see no vlan. I think I must do some configuration change on wireshark or ethernet card but couldnt find. Could you please help me?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-single" rel="tag" title="see questions tagged &#39;single&#39;">single</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-qinq" rel="tag" title="see questions tagged &#39;qinq&#39;">qinq</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '14, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/47af8cc898768e577d1a6de20ab3e7d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Halil%20Burak%20Y%C4%B1lmaz&#39;s gravatar image" /><p><span>Halil Burak ...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Halil Burak Yılmaz has no accepted answers">0%</span></p></div></div><div id="comments-container-34358" class="comments-container"><span id="34368"></span><div id="comment-34368" class="comment"><div id="post-34368-score" class="comment-score"></div><div class="comment-text"><p>What operating system are you running on your PC? Windows, Linux, some flavor of BSD, or something else? And what version of that operating system are you running? You might have to make some configuration change to the driver (Wireshark isn't involved in dropping the VLAN tags; it just gets what the OS hands it).</p></div><div id="comment-34368-info" class="comment-info"><span class="comment-age">(02 Jul '14, 16:03)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="34374"></span><div id="comment-34374" class="comment"><div id="post-34374-score" class="comment-score"></div><div class="comment-text"><p>Thanks for help. I am using windows 7 and my Network Interface Card is Intel 82579LM. I heard that it is configurable on RegEdit at somewhere like below: HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Class{4D36E972-E325-11CE-BFC1-08002BE10318}\00nn</p></div><div id="comment-34374-info" class="comment-info"><span class="comment-age">(03 Jul '14, 01:03)</span> <span class="comment-user userinfo">Halil Burak ...</span></div></div></div><div id="comment-tools-34358" class="comment-tools"></div><div class="clear"></div><div id="comment-34358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34468"></span>

<div id="answer-container-34468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34468-score" class="post-score" title="current number of votes">0</div><span id="post-34468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See my answers (and comments) to the following questions:</p><blockquote><p><a href="http://ask.wireshark.org/questions/15524/vlan-tagging-intel-82579lm-and-wireshark-183">http://ask.wireshark.org/questions/15524/vlan-tagging-intel-82579lm-and-wireshark-183</a><br />
<a href="http://ask.wireshark.org/questions/17251/vlan-tag-with-intel-82579lm">http://ask.wireshark.org/questions/17251/vlan-tag-with-intel-82579lm</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-34468" class="comments-container"></div><div id="comment-tools-34468" class="comment-tools"></div><div class="clear"></div><div id="comment-34468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

