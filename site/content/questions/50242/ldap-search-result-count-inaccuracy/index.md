+++
type = "question"
title = "LDAP search result count inaccuracy"
description = '''I&#x27;ve noticed that if I take an LDAP packet capture, follow a long conversation, sort the list of packets by &#x27;info&#x27; and scroll through the list of search results, the number of results at the top of the LDAPMessage decode just increments with every packet I look at. It&#x27;s the number in the square brac...'''
date = "2016-02-16T09:51:00Z"
lastmod = "2016-02-16T12:17:00Z"
weight = 50242
keywords = [ "decoder", "ldap" ]
aliases = [ "/questions/50242" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LDAP search result count inaccuracy](/questions/50242/ldap-search-result-count-inaccuracy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50242-score" class="post-score" title="current number of votes">0</div><span id="post-50242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've noticed that if I take an LDAP packet capture, follow a long conversation, sort the list of packets by 'info' and scroll through the list of search results, the number of results at the top of the LDAPMessage decode just increments with every packet I look at. It's the number in the square brackets, like [570 results] or whatever. That number then carries into the next SearchResultDone packet that I look at but if I look at another SearchResultDone packet after that, the number resets to [0 results]. I don't even think that there is a result count in the SearchResultDone LDAPMessage; there doesn't seem to be a field for it.</p><p>I'd recommend changing the LDAP decoder to no longer display a number of results at all for SearchResultDone LDAPMessages and to properly count the number of results in the specific SearchResultEntry LDAPMessage instead of just incrementing the count from the last packet.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decoder" rel="tag" title="see questions tagged &#39;decoder&#39;">decoder</span> <span class="post-tag tag-link-ldap" rel="tag" title="see questions tagged &#39;ldap&#39;">ldap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '16, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/2466539783099db14c917f90c777e9d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tony%20Hammitt&#39;s gravatar image" /><p><span>Tony Hammitt</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tony Hammitt has no accepted answers">0%</span></p></div></div><div id="comments-container-50242" class="comments-container"></div><div id="comment-tools-50242" class="comment-tools"></div><div class="clear"></div><div id="comment-50242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50244"></span>

<div id="answer-container-50244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50244-score" class="post-score" title="current number of votes">0</div><span id="post-50244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That would be an enhancement request that should be filed via <a href="https://bugs.wireshark.org">Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-50244" class="comments-container"></div><div id="comment-tools-50244" class="comment-tools"></div><div class="clear"></div><div id="comment-50244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

