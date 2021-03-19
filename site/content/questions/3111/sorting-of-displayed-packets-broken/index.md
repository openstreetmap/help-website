+++
type = "question"
title = "sorting of displayed packets broken?"
description = '''previous versions of wireshark (0.99.x) had a sub-sorting with sequential numbers in the displayed packets, if sorting for protocol (for example) was enabled.  Actual versions are messing up this sub sorting and display packets in arbitrary order, if sorting for protocol is selected. Please have a l...'''
date = "2011-03-25T03:59:00Z"
lastmod = "2011-04-01T07:05:00Z"
weight = 3111
keywords = [ "sorting", "display" ]
aliases = [ "/questions/3111" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [sorting of displayed packets broken?](/questions/3111/sorting-of-displayed-packets-broken)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3111-score" class="post-score" title="current number of votes">0</div><span id="post-3111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>previous versions of wireshark (0.99.x) had a sub-sorting with sequential numbers in the displayed packets, if sorting for protocol (for example) was enabled.</p><p>Actual versions are messing up this sub sorting and display packets in arbitrary order, if sorting for protocol is selected.</p><p>Please have a look:</p><p>http://img822.imageshack.us/i/kaputt.png/ (the broken one)</p><p>http://img854.imageshack.us/i/23675117.png/ (good)</p><p>How can I have the sub sorting with increasing numbers on actual versions of wireshark?</p><p>Kind regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sorting" rel="tag" title="see questions tagged &#39;sorting&#39;">sorting</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '11, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/d7072153853bcf7c79f8fc31d7285d8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nico&#39;s gravatar image" /><p><span>nico</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nico has no accepted answers">0%</span></p></div></div><div id="comments-container-3111" class="comments-container"><span id="3206"></span><div id="comment-3206" class="comment"><div id="post-3206-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by <em>actual</em> versions of Wireshark? Even all those in the 0.99.x series were actual versions. Which version of Wireshark are you using?</p></div><div id="comment-3206-info" class="comment-info"><span class="comment-age">(29 Mar '11, 12:35)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="3207"></span><div id="comment-3207" class="comment"><div id="post-3207-score" class="comment-score"></div><div class="comment-text"><p>Chris, since we moved to the "new_packet_list" in version 1.4.0 the sorting is done by GTK and it only allows one column to sort on. So the OP probably meant "recent" instead of "actual" :-)</p><p>(maybe he is dutch, as the dutch word for "recent" is "actueel")</p></div><div id="comment-3207-info" class="comment-info"><span class="comment-age">(29 Mar '11, 12:46)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="3210"></span><div id="comment-3210" class="comment"><div id="post-3210-score" class="comment-score"></div><div class="comment-text"><p>Ah, that makes more sense now. I wasn't sure if <em>actual</em> was meant to refer to stable versions as opposed to development versions. Actually (pun intended), <a href="http://nl.thefreedictionary.com/actueel">This site</a> translates "actueel" to "current" or "present", but either way, the intent is now clear.<br />
</p></div><div id="comment-3210-info" class="comment-info"><span class="comment-age">(29 Mar '11, 13:19)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="3270"></span><div id="comment-3270" class="comment"><div id="post-3270-score" class="comment-score"></div><div class="comment-text"><p>You're right. "recent" is the correct word. Version 1.2.x and 1.4.x (and 1.5.x) are broken, 0.99.x works.</p><p>As suggested, I will open a bug report.</p><p>Nico</p></div><div id="comment-3270-info" class="comment-info"><span class="comment-age">(01 Apr '11, 07:05)</span> <span class="comment-user userinfo">nico</span></div></div></div><div id="comment-tools-3111" class="comment-tools"></div><div class="clear"></div><div id="comment-3111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3208"></span>

<div id="answer-container-3208" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3208-score" class="post-score" title="current number of votes">0</div><span id="post-3208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nico, you better open a bug/enhancement report on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> so that we won't lose track of fixing this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '11, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div></div><div id="comments-container-3208" class="comments-container"></div><div id="comment-tools-3208" class="comment-tools"></div><div class="clear"></div><div id="comment-3208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

