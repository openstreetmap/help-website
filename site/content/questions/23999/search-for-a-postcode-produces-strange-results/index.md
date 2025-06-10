+++
type = "question"
title = "Search for a postcode produces strange results"
description = '''When i am trying to map to a specific postcode openstreetmap returns no results. Any postcode in the edinburgh area appears as in the london area. So if i enter EH7 6EZ it comes back as if i have typed E7 6EZ. If i enter EHH7 6EZ then it shows up as edinburgh? Openstreetmap appears to strip out the ...'''
date = "2013-07-05T10:24:00Z"
lastmod = "2013-07-05T11:57:00Z"
weight = 23999
keywords = [ "nominatim", "postcode" ]
aliases = [ "/questions/23999" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Search for a postcode produces strange results](/questions/23999/search-for-a-postcode-produces-strange-results)

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
<span id="post-23999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23999-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When i am trying to map to a specific postcode openstreetmap returns no results. Any postcode in the edinburgh area appears as in the london area. So if i enter EH7 6EZ it comes back as if i have typed E7 6EZ. If i enter EHH7 6EZ then it shows up as edinburgh? Openstreetmap appears to strip out the second letter which makes the postcode incorrect. Has anyone seen this issue before and know how to fix it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '13, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/855a56572cb67d7728044386d0890168?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbrooks&#39;s gravatar image" />
<p><span>sbrooks</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbrooks has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '13, 10:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-23999" class="comments-container">
<span id="24000"></span>
<div id="comment-24000" class="comment">
<div id="post-24000-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you mean you are unable to enter that postcode for a feature, or that you can enter it but when you search for it you don't get the results you're expecting? If the former, which editor are you using?</p>
</div>
<div id="comment-24000-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 10:26)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="24001"></span>
<div id="comment-24001" class="comment">
<div id="post-24001-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Try searching for it, and things happen as described. But not for say CO15 1AA which goes to the right place. As far as I can tell the postcode isn't currently in OSM (though I may be wrong) so perhaps some issue with nominatim's GB postcode data. In fact, it may be missing the postcode as EH7 6HF returns a postcode result fine.</p>
</div>
<div id="comment-24001-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 10:34)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="24003"></span>
<div id="comment-24003" class="comment">
<div id="post-24003-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, when i enter the postcode EH7 6EZ it shows up as the london area because for some reason the H out of the postcode is getting stripped out.</p>
</div>
<div id="comment-24003-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 10:39)</span> <span class="comment-user userinfo">sbrooks</span>
</div>
</div>
<span id="24005"></span>
<div id="comment-24005" class="comment">
<div id="post-24005-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I get an Edinburgh location with a raw postcode (EH7 6EZ). Did you search with the street name too?</p>
</div>
<div id="comment-24005-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 10:44)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23999-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="24004"></span>

<div id="answer-container-24004" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24004-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like the postcode you're searching for simply isn't in OpenStreetMap, in which case a search using Nominatim, the native OSM search engine, won't find it. On openstreetmap.org a search should still show results from NPEMap / FreeThe Postcode which finds the right area.</p>
<p>If the postcodes you're looking for get added to OpenStreetMap, your search will succeed. You could add these yourself, or offer a bounty to a mapper who correctly adds them if they're important to you.</p>
<p>The reason you're getting what look like strange results from Nominatim is that it's a text-only search engine, and doesn't understand the structure of postcodes. It's finding the closest text match it can to your query, which unfortunately isn't very helpful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '13, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '13, 11:10</strong> </span></p>
</div>
</div>
<div id="comments-container-24004" class="comments-container">
<span id="24008"></span>
<div id="comment-24008" class="comment">
<div id="post-24008-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That seems to make sense although it makes the tool pretty useless to us. We have a map which shows a radius around a set postcode which is sent to the nominatim web service. If it isn't up to date then it's pretty useless. Is there any other web service which is more up to date which can do this? (Other than google maps!)</p>
</div>
<div id="comment-24008-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 11:02)</span> <span class="comment-user userinfo">sbrooks</span>
</div>
</div>
<span id="24009"></span>
<div id="comment-24009" class="comment">
<div id="post-24009-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Not at all -- it's just that those particular postcodes haven't been added to OSM yet, and that's easy to rectify.</p>
</div>
<div id="comment-24009-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 11:10)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="24010"></span>
<div id="comment-24010" class="comment">
<div id="post-24010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But the problem is i could enter a random postcode and it won't find it and i won't have the time to submit the postcode to osm.</p>
</div>
<div id="comment-24010-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 11:13)</span> <span class="comment-user userinfo">sbrooks</span>
</div>
</div>
<span id="24011"></span>
<div id="comment-24011" class="comment">
<div id="post-24011-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But I was once told that Nominatim uses OS CodePoint-Open as a data source (<a href="http://lists.openstreetmap.org/pipermail/talk-gb/2012-October/014073.html">http://lists.openstreetmap.org/pipermail/talk-gb/2012-October/014073.html</a> ), in which case all postcodes should be included. It seems something is not working that should.</p>
</div>
<div id="comment-24011-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 11:57)</span> <span class="comment-user userinfo">sdoerr</span>
</div>
</div>
</div>
<div id="comment-tools-24004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24004-form-container" class="comment-form-container">
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

