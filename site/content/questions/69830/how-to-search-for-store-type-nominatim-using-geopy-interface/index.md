+++
type = "question"
title = "How to search for &quot;store type&quot; Nominatim (using GeoPy interface)"
description = '''Hi - I am trying to find the best way to search for &quot;All butchers in England&quot; or &quot;All butchers in Germany&quot;. I notice that when I do a search for a butcher via Nominatim in Geopy where I already know the coordinates, Nominatim indeed seems to know it is a butcher: location = geolocator.reverse(&quot;50.89...'''
date = "2019-07-01T19:20:00Z"
lastmod = "2019-07-02T07:45:00Z"
weight = 69830
keywords = [ "geopy", "nominatim" ]
aliases = [ "/questions/69830" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to search for "store type" Nominatim (using GeoPy interface)](/questions/69830/how-to-search-for-store-type-nominatim-using-geopy-interface)

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
<span id="post-69830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi - I am trying to find the best way to search for "All butchers in England" or "All butchers in Germany". I notice that when I do a search for a butcher via Nominatim in Geopy where I already know the coordinates, Nominatim indeed seems to know it is a butcher:</p>
<p>location = geolocator.reverse("50.8907671, 12.4256231") locaton.raw {'place_id': ...other stuff. 'address': {<strong>'butcher':</strong> 'Fleischerei Hanns', 'house_number': '6', 'road': 'Am Löschkenberg'...</p>
<p>If I try an unstructured search I get very few results (should be in the thousands)</p>
<blockquote>
<blockquote>
<blockquote>
<p>location = geolocator.geocode("butcher in germany", exactly_one=False, limit=None) len(location) 10</p>
</blockquote>
</blockquote>
</blockquote>
<p>And I know you can do structured searches in Nominatim. So how would I structure a search here to return all the addresses that Nominatim thinks is a butcher?</p>
<p>PS - I do the same search on Overpass-turbo and get around 5900 entries, but the addresses do not routinely have a CITY and that's what I'm looking for. They only have what people might have entered. I can run the Overpass lat/long through Nominatim reverse search to get the city information, which works but it feels inefficient. If I can answer my first question I'll have a solution.</p>
<p>Thanks for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geopy" rel="tag" title="see questions tagged &#39;geopy&#39;">geopy</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '19, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/48c7e49d3c1e3f81518abde5e8944a9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthpau&#39;s gravatar image" />
<p><span>matthpau</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthpau has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '19, 19:23</strong> </span></p>
</div>
</div>
<div id="comments-container-69830" class="comments-container">
&#10;</div>
<div id="comment-tools-69830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69830-form-container" class="comment-form-container">
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

<span id="69831"></span>

<div id="answer-container-69831" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69831-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="matthpau has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim can only find POIs (shop, restaurant, hospital) in a short radius. Even then the list can be incomplete. Overpass or filtering a *.osm file with other tools is the better systematic approach for a whole country.</p>
<p>Nominatim support batch requests with <a href="http://nominatim.org/release-docs/latest/api/Lookup/">http://nominatim.org/release-docs/latest/api/Lookup/</a> The limit is set to 50 on nominatim.osm.org (configurable if you have your own installation). It might seem inefficient but the only option would be direct database access to a Nominatim installation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '19, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-69831" class="comments-container">
<span id="69834"></span>
<div id="comment-69834" class="comment">
<div id="post-69834-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Super, thanks for the explanation.</p>
</div>
<div id="comment-69834-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 07:45)</span> <span class="comment-user userinfo">matthpau</span>
</div>
</div>
</div>
<div id="comment-tools-69831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69831-form-container" class="comment-form-container">
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

