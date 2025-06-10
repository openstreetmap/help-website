+++
type = "question"
title = "Query to exhaustively get all restaurants in a specific city"
description = '''Hi all, What would be the best way to retrieve all the restaurants (or any other business type for that matter) in a specific area? The amenity=restaurant check does not appear to provide nowhere near all restaurants in a designated city, for example. Moreover, I have found an actual restaurant whil...'''
date = "2020-05-11T10:28:00Z"
lastmod = "2020-05-12T13:24:00Z"
weight = 74730
keywords = [ "amenity", "restaurant" ]
aliases = [ "/questions/74730" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query to exhaustively get all restaurants in a specific city](/questions/74730/query-to-exhaustively-get-all-restaurants-in-a-specific-city)

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
<span id="post-74730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74730-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>What would be the best way to retrieve all the restaurants (or any other business type for that matter) in a specific area? The amenity=restaurant check does not appear to provide nowhere near all restaurants in a designated city, for example. Moreover, I have found an actual restaurant while looking for pubs and it had only the amenity=pub assigned to it.</p>
<p>Are there any nodes with multiple amenity types, for example amenity=restaurant;pub;cafe or they have to be retrieved by each amenity type separately? I have to mention that I looked separately for each of these amenities and for all results returned in each case all the nodes had a single amenity value.</p>
<p>Is there any other tag that could provide a node that is in fact a restaurant, but it does not have the proper amenity tag value?</p>
<p>Thanks in advance for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-restaurant" rel="tag" title="see questions tagged &#39;restaurant&#39;">restaurant</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '20, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/79f2ecb8b9f5eeb58cd7d12fecfb6145?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="razvan_bunea&#39;s gravatar image" />
<p><span>razvan_bunea</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="razvan_bunea has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74730" class="comments-container">
<span id="74732"></span>
<div id="comment-74732" class="comment">
<div id="post-74732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(just as a pointer to help you explore while someone provides a full answer)</p>
<p>Have a look at "taginfo" - <a href="https://taginfo.openstreetmap.org/tags/amenity=pub%3Bbar">https://taginfo.openstreetmap.org/tags/amenity=pub%3Bbar</a> shows there are a few with that combination. Use <a href="https://taginfo.openstreetmap.org/keys/amenity#values">https://taginfo.openstreetmap.org/keys/amenity#values</a> to exlore the other values (you can filter using the search box on the right)</p>
</div>
<div id="comment-74732-info" class="comment-info">
<span class="comment-age">(11 May '20, 11:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74730-form-container" class="comment-form-container">
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

<span id="74733"></span>

<div id="answer-container-74733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74733-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You mentioned nodes a few times - you should also check for ways and relations to find restaurants mapped as areas (you may already know that and have been using "nodes" loosely).</p>
<p>You could look for restaurant=yes, there are about 3000 of these mapped worldwide. They are likely to be business that mappers see as not primarily a restaurant but including one as part of the business - perhaps hotels or pubs, but I haven't actually checked this.</p>
<p>The dividing line between a restaurant and other businesses serving meals is not always clear, so certainly investigate amenity=cafe and amenity=pub as you mentioned, and also amenity=fast_food. Even amenity=bar may sometimes sell meals - in theory according to the wiki this tag should be used where the focus is on drinks, but there can be confusion on this point in countries where establishments with "Bar" in the name do serve light meals. Whether you want to count all of these may depend on what exactly you mean by "all restaurants".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '20, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-74733" class="comments-container">
<span id="74752"></span>
<div id="comment-74752" class="comment">
<div id="post-74752-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for all your answers. It seems though that Openstreetmap is not yet as complete as Google Places API. We will make the best of what it offers.</p>
</div>
<div id="comment-74752-info" class="comment-info">
<span class="comment-age">(12 May '20, 07:50)</span> <span class="comment-user userinfo">razvan_bunea</span>
</div>
</div>
<span id="74758"></span>
<div id="comment-74758" class="comment">
<div id="post-74758-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This will largely depend on the country and city you are looking at.</p>
</div>
<div id="comment-74758-info" class="comment-info">
<span class="comment-age">(12 May '20, 13:24)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-74733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74733-form-container" class="comment-form-container">
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

