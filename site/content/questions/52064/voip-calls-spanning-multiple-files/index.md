+++
type = "question"
title = "VoIP calls spanning multiple files"
description = '''When trying to look at VoIP calls that span across files, I see the call using telephony&amp;gt;VoIP calls in the capture containing the start of the call, and obviously as it contains the call set up, however I can not see the continuation of that call by doing the same thing in subsequent files. I kno...'''
date = "2016-04-28T15:59:00Z"
lastmod = "2016-04-29T10:27:00Z"
weight = 52064
keywords = [ "voipcalls" ]
aliases = [ "/questions/52064" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VoIP calls spanning multiple files](/questions/52064/voip-calls-spanning-multiple-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52064-score" class="post-score" title="current number of votes">0</div><span id="post-52064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When trying to look at VoIP calls that span across files, I see the call using telephony&gt;VoIP calls in the capture containing the start of the call, and obviously as it contains the call set up, however I can not see the continuation of that call by doing the same thing in subsequent files. I know I have to manually filter to see (and listen) to it, but can not find any information on how to do this. Related,,is there anyway to "splice" two files (i.e. ring buffered) files together to make one continuous? Thanks....</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-voipcalls" rel="tag" title="see questions tagged &#39;voipcalls&#39;">voipcalls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '16, 15:59</strong></p><img src="https://secure.gravatar.com/avatar/75f910be5d288574d1febbf2b6cc9992?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Templedogs&#39;s gravatar image" /><p><span>Templedogs</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Templedogs has no accepted answers">0%</span></p></div></div><div id="comments-container-52064" class="comments-container"></div><div id="comment-tools-52064" class="comment-tools"></div><div class="clear"></div><div id="comment-52064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52066"></span>

<div id="answer-container-52066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52066-score" class="post-score" title="current number of votes">0</div><span id="post-52066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use Mergecap, which is distributed and installed with Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '16, 19:50</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-52066" class="comments-container"><span id="52068"></span><div id="comment-52068" class="comment"><div id="post-52068-score" class="comment-score"></div><div class="comment-text"><p>Or drop multiple capture files onto the Wireshark window (does this even work with the Qt version?)</p></div><div id="comment-52068-info" class="comment-info"><span class="comment-age">(29 Apr '16, 00:38)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52074"></span><div id="comment-52074" class="comment"><div id="post-52074-score" class="comment-score"></div><div class="comment-text"><p>This doesn't quite work on the Qt version.....it does however still work on the Legacy version.</p></div><div id="comment-52074-info" class="comment-info"><span class="comment-age">(29 Apr '16, 06:23)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="52075"></span><div id="comment-52075" class="comment"><div id="post-52075-score" class="comment-score"></div><div class="comment-text"><p>Indeed, there's still an <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12129">open bug</a> on Qt for that.</p></div><div id="comment-52075-info" class="comment-info"><span class="comment-age">(29 Apr '16, 07:02)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52076"></span><div id="comment-52076" class="comment"><div id="post-52076-score" class="comment-score"></div><div class="comment-text"><p>Thanks...did not even realize there was a merge under files...Lots to learn...thank you so much for your reply. Will play with it today....</p></div><div id="comment-52076-info" class="comment-info"><span class="comment-age">(29 Apr '16, 07:35)</span> <span class="comment-user userinfo">Templedogs</span></div></div><span id="52079"></span><div id="comment-52079" class="comment"><div id="post-52079-score" class="comment-score"></div><div class="comment-text"><p>The method Jaap and I are talking about, is to open the Legacy version of Wireshark, then select all the files you wish to merge, and then simply drag-and-drop them into the open Wireshark window. The files will be merged in chronological order. You can then save this as a merged file using the FILE | SAVE AS.</p><p>Please don't forget to Accept this answer if it answered your question.</p></div><div id="comment-52079-info" class="comment-info"><span class="comment-age">(29 Apr '16, 08:51)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="52086"></span><div id="comment-52086" class="comment not_top_scorer"><div id="post-52086-score" class="comment-score"></div><div class="comment-text"><p><code>File-&gt;Merge</code> works even in Qt :-) But after each merge, you have to save the merged captures as a new file before merging in another file.</p></div><div id="comment-52086-info" class="comment-info"><span class="comment-age">(29 Apr '16, 10:27)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52066" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-52066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

