+++
type = "question"
title = "autosuggest with nominatim"
description = '''Hi, I&#x27;ve got a leaflet map with mapbox map layer under it. For geocoding I used nominatim, but since they don&#x27;t allow autocomplete (for a good reason) I&#x27;m using the mapbox geocoding. The function works well but the poi results are often way off (up to hundred meters) and often show results from poi&#x27;...'''
date = "2019-12-16T14:16:00Z"
lastmod = "2019-12-20T22:44:00Z"
weight = 72116
keywords = [ "autocomplete", "nominatim", "geocoding" ]
aliases = [ "/questions/72116" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [autosuggest with nominatim](/questions/72116/autosuggest-with-nominatim)

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
<span id="post-72116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72116-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I've got a leaflet map with mapbox map layer under it. For geocoding I used nominatim, but since they <a href="https://operations.osmfoundation.org/policies/nominatim/">don't allow</a> autocomplete (for a good reason) I'm using the mapbox geocoding. The function works well but the poi results are often way off (up to hundred meters) and often show results from poi's who are moved years ago.</p>
<p>So I'd like to go back to Nominatim (web version) and was thinking if it is possible to get permission to autosuggest if I can build in a big delay? For example send an autosuggest from the text in the text field every 0,5 seconds, or after a certain amount of digits etc?</p>
<p>My main goal is to not have the user push the search button every time, so any ideas on that would be great.</p>
<p>Or any ideas where to ask this?</p>
<p>thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-autocomplete" rel="tag" title="see questions tagged &#39;autocomplete&#39;">autocomplete</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '19, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/89858e1d0e500ae658bf8cf7fc4964c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tijmenheid&#39;s gravatar image" />
<p><span>tijmenheid</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tijmenheid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '19, 14:20</strong> </span></p>
</div>
</div>
<div id="comments-container-72116" class="comments-container">
&#10;</div>
<div id="comment-tools-72116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72116-form-container" class="comment-form-container">
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

<span id="72118"></span>

<div id="answer-container-72118" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72118-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-72118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tijmenheid has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim isn't good at autocomplete (incomplete/partial) queries. Searching for "New Yor" doesn't return New York. Consider using <a href="https://photon.komoot.de/">https://photon.komoot.de/</a> which uses Nominatim processed database as input.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '19, 14:24</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-72118" class="comments-container">
<span id="72121"></span>
<div id="comment-72121" class="comment">
<div id="post-72121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>looks good, thanks!</p>
</div>
<div id="comment-72121-info" class="comment-info">
<span class="comment-age">(16 Dec '19, 17:52)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
<span id="72183"></span>
<div id="comment-72183" class="comment">
<div id="post-72183-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again, it works! Just one small extra question (maybe you'Re familiar with Photon) When searching for a Poi I get the name, address etc, but I would like to get other info too, f.e. website, phonenumber, so it shows up with the icon when it's shown on the map. I know they use 'osm_value' and 'osm_tag', but just can'T find a way to get more out of it. Any ideas?</p>
</div>
<div id="comment-72183-info" class="comment-info">
<span class="comment-age">(20 Dec '19, 21:41)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
<span id="72185"></span>
<div id="comment-72185" class="comment">
<div id="post-72185-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Photon doesn't have that in their searchindex (<a href="https://github.com/komoot/photon/issues/395).">https://github.com/komoot/photon/issues/395).</a> You could query Nominatim using the osmtype and osmid (<a href="http://nominatim.org/release-docs/latest/api/Lookup/">http://nominatim.org/release-docs/latest/api/Lookup/</a> <a href="https://nominatim.openstreetmap.org/lookup?osm_ids=N762657373&amp;extratags=1&amp;format=json)">https://nominatim.openstreetmap.org/lookup?osm_ids=N762657373&amp;extratags=1&amp;format=json)</a> but then you could run into the 1 query per second limit again.</p>
</div>
<div id="comment-72185-info" class="comment-info">
<span class="comment-age">(20 Dec '19, 22:44)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-72118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72118-form-container" class="comment-form-container">
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

