+++
type = "question"
title = "Search based on country code/suffix"
description = '''Right now, we can search based on geoip country name like the following: ip and not ip.geoip.country == &quot;United States&quot;  Wonder if it&#x27;s possible to search based on country code, for &quot;United States&quot;, it&#x27;s US, for Russian, it&#x27;s RU.  Thanks.'''
date = "2015-10-23T16:53:00Z"
lastmod = "2015-10-24T16:02:00Z"
weight = 46900
keywords = [ "wireshark" ]
aliases = [ "/questions/46900" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Search based on country code/suffix](/questions/46900/search-based-on-country-codesuffix)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46900-score" class="post-score" title="current number of votes">0</div><span id="post-46900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Right now, we can search based on geoip country name like the following:</p><pre><code>ip and not ip.geoip.country == &quot;United States&quot;</code></pre><p>Wonder if it's possible to search based on country code, for "United States", it's US, for Russian, it's RU.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '15, 16:53</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-46900" class="comments-container"></div><div id="comment-tools-46900" class="comment-tools"></div><div class="clear"></div><div id="comment-46900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46903"></span>

<div id="answer-container-46903" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46903-score" class="post-score" title="current number of votes">1</div><span id="post-46903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not currently possible. The GeoIP API appears to have <code>GeoIP_country_code_by_</code> and <code>GeoIP_country_code3_by_</code> routines that could be used in Wireshark, but they're not currently used, so there are no <code>ip.geoip.country_code</code> or <code>ip.geoip.country_code3</code> fields.</p><p>Please file an enhancement request on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '15, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-46903" class="comments-container"><span id="46908"></span><div id="comment-46908" class="comment"><div id="post-46908-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info. I will create an enhancement request on it.</p></div><div id="comment-46908-info" class="comment-info"><span class="comment-age">(24 Oct '15, 16:02)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-46903" class="comment-tools"></div><div class="clear"></div><div id="comment-46903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

