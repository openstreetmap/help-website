+++
type = "question"
title = "nominatim adress lookup problem (fuzzy search)"
description = '''Hi, we have some problems with our nominatim search. we have updated our europe dump to the latest version und used the latest nominatim version 4.0.1 address example: Luisenhöhe 2, 4963 St. Peter am Inn https://nominatim.openstreetmap.org/search.php?q=Luisenh%C3%B6he%202,%204963%20St.%20Peter%20am%...'''
date = "2022-04-30T12:19:00Z"
lastmod = "2022-05-02T10:54:00Z"
weight = 84317
keywords = [ "nominatim" ]
aliases = [ "/questions/84317" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim adress lookup problem (fuzzy search)](/questions/84317/nominatim-adress-lookup-problem-fuzzy-search)

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
<span id="post-84317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84317-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>we have some problems with our nominatim search.</p>
<p>we have updated our europe dump to the latest version und used the latest nominatim version 4.0.1</p>
<p>address example: Luisenhöhe 2, 4963 St. Peter am Inn</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?q=Luisenh%C3%B6he%202,%204963%20St.%20Peter%20am%20Inn&amp;polygon_geojson=1&amp;format=jsonv2">https://nominatim.openstreetmap.org/search.php?q=Luisenh%C3%B6he%202,%204963%20St.%20Peter%20am%20Inn&amp;polygon_geojson=1&amp;format=jsonv2</a></p>
<p>In Openstreetmap the town is called St. Peter am Hart in austria.</p>
<p>Our instance doesn't find any results for the address - but if we change St. Peter am Inn into St. Peter am Hart it does work. Another exmaple are street names with "Straße" vs. "Str." - We got only correct results if the search request is in the same notation as in the osm postgresl nominatim db.</p>
<p>Are there any options for enabling fuzzy search? Whats the reason for such different results inthe public instance of openstreetmap.org?</p>
<p>Thanks for help or tips</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '22, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/5fe715b8cd71fe51ae4aef488f7aced0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sylphen&#39;s gravatar image" />
<p><span>sylphen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sylphen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84317" class="comments-container">
&#10;</div>
<div id="comment-tools-84317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84317-form-container" class="comment-form-container">
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

<span id="84332"></span>

<div id="answer-container-84332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84332-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-84332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Nominatim servers on osm.org always use the latests development version of the Nominatim software, so differences are always to be expected.</p>
<p>For the particular problem with St. Peter, the difference is that osm.org has the new <a href="https://nominatim.org/release-docs/latest/customize/Tokenizers/#icu-tokenizer">ICU tokenizer</a> configured. The handling of partial terms has changed a little bit, so that it is marginally better at this particular query.</p>
<p>You can already use the new tokenizer with the 4.0.1 release. However, be aware that switching the tokenizer requires a reimport. Also, the ICU tokenizer has seen quite a few improvements and bug fixes since the last release.</p>
<p>'Straße' vs. 'Str' has always worked. The problem there was probably somewhere else.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '22, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-84332" class="comments-container">
<span id="84335"></span>
<div id="comment-84335" class="comment">
<div id="post-84335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>thank you for the tipp - we will try out that with the latest version in our test environment with enabled ICU tokenizer!</p>
<p>kinds regards</p>
</div>
<div id="comment-84335-info" class="comment-info">
<span class="comment-age">(02 May '22, 10:54)</span> <span class="comment-user userinfo">sylphen</span>
</div>
</div>
</div>
<div id="comment-tools-84332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84332-form-container" class="comment-form-container">
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

