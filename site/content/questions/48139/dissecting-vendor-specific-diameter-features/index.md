+++
type = "question"
title = "Dissecting vendor specific diameter features"
description = '''Hi, I&#x27;m trying to figure out what&#x27;s the order in which wireshark looks up for things when dissecting diameter packet. Does it look for Application-Id first? Or AVP? What I ultimately need to do, is add a vendor specific feature to the Feature-List-ID 1. Now, if I understand correctly, I should add a...'''
date = "2015-12-01T06:34:00Z"
lastmod = "2016-01-12T00:53:00Z"
weight = 48139
keywords = [ "development", "diameter", "dissection", "avp", "features" ]
aliases = [ "/questions/48139" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting vendor specific diameter features](/questions/48139/dissecting-vendor-specific-diameter-features)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48139-score" class="post-score" title="current number of votes">0</div><span id="post-48139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to figure out what's the order in which wireshark looks up for things when dissecting diameter packet. Does it look for Application-Id first? Or AVP?</p><p>What I ultimately need to do, is add a vendor specific feature to the Feature-List-ID 1. Now, if I understand correctly, I should add a .c file similar to "packet-diameter_3gpp.c" where I can dissect the bits. I shall use this file as a template.</p><p>I already have my own vendor specific dictionary and it works correctly. But in the vendor spec I found out that "Supported-Features" AVP's vendor-id will be set to 3GPP and my-vendor-id. Does this mean I should redefine this AVP and set my own vendor-id in my own dictionary?</p><p>Thanks a lot!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span> <span class="post-tag tag-link-avp" rel="tag" title="see questions tagged &#39;avp&#39;">avp</span> <span class="post-tag tag-link-features" rel="tag" title="see questions tagged &#39;features&#39;">features</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '15, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/a03fa5b340afab78d2e44b63e8dcf3d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aliniel&#39;s gravatar image" /><p><span>Aliniel</span><br />
<span class="score" title="30 reputation points">30</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aliniel has 2 accepted answers">100%</span></p></div></div><div id="comments-container-48139" class="comments-container"><span id="48147"></span><div id="comment-48147" class="comment"><div id="post-48147-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I get it, the avp is 3gpp feature... And the application Id is the vendors application id? I don't have the code handy right now but I think the avp subdissection is done per vendor and a new table(code changes) is needed to add new vendors tables. If your case is as above the avp will be dissected in the 3gpp subdissector and code will be needed there to handle the application Id of your vendor.</p></div><div id="comment-48147-info" class="comment-info"><span class="comment-age">(01 Dec '15, 08:55)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-48139" class="comment-tools"></div><div class="clear"></div><div id="comment-48139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49110"></span>

<div id="answer-container-49110" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49110-score" class="post-score" title="current number of votes">0</div><span id="post-49110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aliniel has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Time to close this one :)</p><p>I had vendor specific flag values for Feature-List-Id AVP when the vendor-id was set to my vendor. Everything else was the same as defined by 3GPP.</p><p>All I had to do, was add some code to the existing function which dissected those flags according to my needs when the vendor-id and feature-list-id were set to certain values. There was no need for a whole another source file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/a03fa5b340afab78d2e44b63e8dcf3d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aliniel&#39;s gravatar image" /><p><span>Aliniel</span><br />
<span class="score" title="30 reputation points">30</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aliniel has 2 accepted answers">100%</span></p></div></div><div id="comments-container-49110" class="comments-container"></div><div id="comment-tools-49110" class="comment-tools"></div><div class="clear"></div><div id="comment-49110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

