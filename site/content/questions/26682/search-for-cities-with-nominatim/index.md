+++
type = "question"
title = "Search for cities with nominatim"
description = '''Hi, i try to build an autocomplete textbox which should display countries and cities. Because the list should also care for variant names of cities and countries and different languages (like i.e. &quot;Cologne&quot; or &quot;Köln&quot;) I thought about using nominatim. Unfortunately I cannot find any help on how to fi...'''
date = "2013-09-24T15:27:00Z"
lastmod = "2013-09-26T08:35:00Z"
weight = 26682
keywords = [ "autocomplete", "nominatim" ]
aliases = [ "/questions/26682" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Search for cities with nominatim](/questions/26682/search-for-cities-with-nominatim)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26682-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, i try to build an autocomplete textbox which should display countries and cities. Because the list should also care for variant names of cities and countries and different languages (like i.e. "Cologne" or "Köln") I thought about using nominatim. Unfortunately I cannot find any help on how to filter the resultset to just cities and countries. Any help is highly appreciated :-).</p>
<p>your's felix</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-autocomplete" rel="tag" title="see questions tagged &#39;autocomplete&#39;">autocomplete</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '13, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/fa409a3ed5b92587476720eae0558a16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="felixhelix&#39;s gravatar image" />
<p><span>felixhelix</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="felixhelix has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26682" class="comments-container">
&#10;</div>
<div id="comment-tools-26682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26682-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26688"></span>

<div id="answer-container-26688" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26688-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take a look at the <a href="http://wiki.openstreetmap.org/wiki/Nominatim#Parameters">parameters</a>. If you want to limit your search to cities and countries only then just set the <em>city</em> or <em>country</em> parameter, e.g.</p>
<p><a href="http://nominatim.openstreetmap.org/search?city=Köln">http://nominatim.openstreetmap.org/search?city=Köln</a></p>
<p>and</p>
<p><a href="http://nominatim.openstreetmap.org/search?country=Croatia">http://nominatim.openstreetmap.org/search?country=Croatia</a></p>
<p>Setting both at the same time only works if both are actually part of the address. In this example it won't work because there is no city named Köln in Croatia.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '13, 17:09</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26688" class="comments-container">
<span id="26759"></span>
<div id="comment-26759" class="comment">
<div id="post-26759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Scai: Then I could build two queries and merge the results - this can be a solution - but with an overhead.</p>
</div>
<div id="comment-26759-info" class="comment-info">
<span class="comment-age">(26 Sep '13, 08:28)</span> <span class="comment-user userinfo">felixhelix</span>
</div>
</div>
</div>
<div id="comment-tools-26688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26688-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26730"></span>

<div id="answer-container-26730" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26730-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe a look at <a href="http://wiki.openstreetmap.org/wiki/Photon">Photon</a> can be helpful?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '13, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-26730" class="comments-container">
<span id="26760"></span>
<div id="comment-26760" class="comment">
<div id="post-26760-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, maybe I'll give it a Iook - the description sounds very promising. But I have to set photon and nominatim up on my own - haven't I? I guess that exceeds my skills by now. I just want to simply fire a request and get results - lazy guy that I am.</p>
</div>
<div id="comment-26760-info" class="comment-info">
<span class="comment-age">(26 Sep '13, 08:35)</span> <span class="comment-user userinfo">felixhelix</span>
</div>
</div>
</div>
<div id="comment-tools-26730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26730-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

