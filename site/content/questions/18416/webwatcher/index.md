+++
type = "question"
title = "Webwatcher"
description = '''Hello! I&#x27;m new to wireshark, but I am very thankful for the program.  I knew someone was monitoring my PC, but after dozens of anti-viruses came up empty, I turned to wireshark. I quickly recognized an odd IP address sending/receiving data from my computer. Turns out the IP belonged to webwatcher, a...'''
date = "2013-02-07T13:52:00Z"
lastmod = "2013-02-07T15:47:00Z"
weight = 18416
keywords = [ "webwatcher" ]
aliases = [ "/questions/18416" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Webwatcher](/questions/18416/webwatcher)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18416-score" class="post-score" title="current number of votes">0</div><span id="post-18416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I'm new to wireshark, but I am very thankful for the program.<br />
</p><p>I knew someone was monitoring my PC, but after dozens of anti-viruses came up empty, I turned to wireshark. I quickly recognized an odd IP address sending/receiving data from my computer. Turns out the IP belonged to webwatcher, a hidden remote monitoring service.<br />
</p><p>Is there anyway to decode the information contained beyond the IP address. I tried "decode" tool but was pretty lost. Any help would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-webwatcher" rel="tag" title="see questions tagged &#39;webwatcher&#39;">webwatcher</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '13, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/80d009de81b41f85b278c6969380fbd5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbenn&#39;s gravatar image" /><p><span>pbenn</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbenn has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-18416" class="comments-container"></div><div id="comment-tools-18416" class="comment-tools"></div><div class="clear"></div><div id="comment-18416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18421"></span>

<div id="answer-container-18421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18421-score" class="post-score" title="current number of votes">1</div><span id="post-18421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Webwatcher payload data being transferred over IP (presumably using TCP over IP) will be formatted however the application has been designed to format the payload data.</p><p>Wireshark does not have a dissector for webwatcher so there's no further decoding of the payload data that the present Wireshark can do; It can only show the raw data.</p><p>Obviously you can assume that the data includes (in some manner) some or all the stuff mentioned in the webwatcher product description.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '13, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-18421" class="comments-container"><span id="18423"></span><div id="comment-18423" class="comment"><div id="post-18423-score" class="comment-score"></div><div class="comment-text"><p>I appreciate you answering. Thanks.</p></div><div id="comment-18423-info" class="comment-info"><span class="comment-age">(07 Feb '13, 15:47)</span> <span class="comment-user userinfo">pbenn</span></div></div></div><div id="comment-tools-18421" class="comment-tools"></div><div class="clear"></div><div id="comment-18421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

