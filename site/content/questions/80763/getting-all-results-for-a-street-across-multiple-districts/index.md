+++
type = "question"
title = "Getting all results for a street across multiple districts"
description = '''With this query I get one match for the street (Leipzig, Germany) with no hint it persists into the next southern district. With a slight to modification I get matches for the next district (Connewitz). I&#x27;m wondering how I can find all matches for the street, regardless of the district. Or how I can...'''
date = "2021-06-28T17:03:00Z"
lastmod = "2021-06-30T16:39:00Z"
weight = 80763
keywords = [ "search", "street", "district", "nominatim" ]
aliases = [ "/questions/80763" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting all results for a street across multiple districts](/questions/80763/getting-all-results-for-a-street-across-multiple-districts)

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
<span id="post-80763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80763-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>With <a href="https://nominatim.openstreetmap.org/ui/search.html?q=karl+liebknecht+stra%C3%9Fe+leipzig">this query</a> I get one match for the street (Leipzig, Germany) with no hint it persists into the next southern district. With a slight to <a href="https://nominatim.openstreetmap.org/ui/search.html?q=karl+liebknecht+stra%C3%9Fe+connewitz+leipzig">modification</a> I get matches for the next district (Connewitz).</p>
<p>I'm wondering how I can find all matches for the street, regardless of the district. Or how I can start from the first response to request information about the street in the next district.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-district" rel="tag" title="see questions tagged &#39;district&#39;">district</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '21, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d4f6fdeb11b94cdb270a90623caa8c1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JonasDoe&#39;s gravatar image" />
<p><span>JonasDoe</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JonasDoe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '21, 09:24</strong> </span></p>
</div>
</div>
<div id="comments-container-80763" class="comments-container">
<span id="80771"></span>
<div id="comment-80771" class="comment">
<div id="post-80771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I doubt it Nominatim has much of a notion of streets spanning districts (addresses &amp; postal codes likely change). OSM itself has no notion except for some major roads where individual parts of the road are grouped in a relation.</p>
</div>
<div id="comment-80771-info" class="comment-info">
<span class="comment-age">(29 Jun '21, 10:22)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="80776"></span>
<div id="comment-80776" class="comment">
<div id="post-80776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> Well, it would even help if the first query would return the results of the second query, too, given the second query appears to be a subset of the first one. But I figure it's not that easy as one might think.</p>
</div>
<div id="comment-80776-info" class="comment-info">
<span class="comment-age">(29 Jun '21, 16:33)</span> <span class="comment-user userinfo">JonasDoe</span>
</div>
</div>
<span id="80778"></span>
<div id="comment-80778" class="comment">
<div id="post-80778-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know the context of what you are trying to do, but maybe Overpass Turbo queries would be more suited to what you are trying to do than the Nominatim search engine?</p>
</div>
<div id="comment-80778-info" class="comment-info">
<span class="comment-age">(30 Jun '21, 09:21)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="80785"></span>
<div id="comment-80785" class="comment">
<div id="post-80785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14272/alan_gr"></a><a href="https://help.openstreetmap.org/users/14272/alan_gr">@alan_gr</a> I don't even know whether my results bear streets or not. But in case they do I'ld like to get all of them where the search string matches their names. I mean, I don't even understand why the results of the second query won't appear in the first one at all. But I guess there's just no way to achieve that, so I figure I've got to live with that or - in case the result set contains streets - run subsequent queries with Overpass. (I assume that I'ld get at least one street in case the name matches, so I could that take as a hint to dive deeper via Overpass.) Not sure I really want to go that route, but thanks for nudging me in that direction anyway!</p>
</div>
<div id="comment-80785-info" class="comment-info">
<span class="comment-age">(30 Jun '21, 16:39)</span> <span class="comment-user userinfo">JonasDoe</span>
</div>
</div>
</div>
<div id="comment-tools-80763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80763-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

