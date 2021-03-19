+++
type = "question"
title = "filter expression (eth.ig == 0) appears to always be true"
description = '''Trying to get better at filtering in wireshark and understand the subtleties. Looking at ways to filter based on Ethernet address (MAC). First thing is separating bcast/mcast from normal addresses.  I used the IG bit line under Destination under Ethernet and did Apply As Filter -&amp;gt; Selected. This ...'''
date = "2014-04-02T12:20:00Z"
lastmod = "2014-04-02T12:36:00Z"
weight = 31417
keywords = [ "filter", "ethernet", "mac" ]
aliases = [ "/questions/31417" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filter expression (eth.ig == 0) appears to always be true](/questions/31417/filter-expression-ethig-0-appears-to-always-be-true)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31417-score" class="post-score" title="current number of votes">0</div><span id="post-31417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to get better at filtering in wireshark and understand the subtleties. Looking at ways to filter based on Ethernet address (MAC). First thing is separating bcast/mcast from normal addresses.</p><p>I used the IG bit line under Destination under Ethernet and did Apply As Filter -&gt; Selected. This produces eth.ig == 1 (which appears to work). Choosing Not Selected produces !(eth.ig == 1), which also works.</p><p>My first thought (before playing with Not Selected, etc.) was to use eth.ig == 0 to screen out bcast/mcast. It appears to always evaluate to true.</p><p>Why is !(eth.ig == 1) not equivalent to eth.ig == 0?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '14, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/9a382605a4cb750db4973f5a35ff2783?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="artswri&#39;s gravatar image" /><p><span>artswri</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="artswri has no accepted answers">0%</span></p></div></div><div id="comments-container-31417" class="comments-container"></div><div id="comment-tools-31417" class="comment-tools"></div><div class="clear"></div><div id="comment-31417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31418"></span>

<div id="answer-container-31418" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31418-score" class="post-score" title="current number of votes">3</div><span id="post-31418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's probably because you always have <strong>two</strong> ethernet addresses in a frame, one for the source, one for the destination.</p><p>"!(eth.ig=1)" says "none of the two MACs may have a 1", which means both must be zero.</p><p>"eth.ig=0" says "one of the MACs must have a 0", which is only false when both have a one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Apr '14, 12:26</strong> </span></p></div></div><div id="comments-container-31418" class="comments-container"><span id="31419"></span><div id="comment-31419" class="comment"><div id="post-31419-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it's now obvious to me what's going on! So what I really wanted was eth.dst.ig == 0 (which is not a legal expression AFAICT - the wireshark I'm using does not like it). But I can live with the alternative ways to express...</p></div><div id="comment-31419-info" class="comment-info"><span class="comment-age">(02 Apr '14, 12:31)</span> <span class="comment-user userinfo">artswri</span></div></div><span id="31422"></span><div id="comment-31422" class="comment"><div id="post-31422-score" class="comment-score"></div><div class="comment-text"><p>Yes, it looks like Wireshark does not allow to specify the MAC for which you want the value to be checked. You could enter an enhancement request at <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a> if you like :-)</p></div><div id="comment-31422-info" class="comment-info"><span class="comment-age">(02 Apr '14, 12:36)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-31418" class="comment-tools"></div><div class="clear"></div><div id="comment-31418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

