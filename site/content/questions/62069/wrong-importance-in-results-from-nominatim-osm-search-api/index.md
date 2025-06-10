+++
type = "question"
title = "[closed] Wrong importance in results from Nominatim OSM Search API"
description = '''When searching for Dubai in the website, it&#x27;s returning a list with the city of Dubai at the top, so I guess the importance of the city in the United Arab Emirates, is the highest. When doing a search request to the Nominatim OSM search API, I&#x27;m getting Uganda as the country with the highest priorit...'''
date = "2018-02-13T10:09:00Z"
lastmod = "2018-02-19T01:02:00Z"
weight = 62069
keywords = [ "api", "nominatim" ]
aliases = [ "/questions/62069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Wrong importance in results from Nominatim OSM Search API](/questions/62069/wrong-importance-in-results-from-nominatim-osm-search-api)

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
<span id="post-62069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62069-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When searching for <code>Dubai</code> in the website, it's returning a list with the city of <code>Dubai</code> at the top, so I guess the importance of the city in the United Arab Emirates, is the highest.</p>
<p>When doing a search request to the Nominatim OSM search API, I'm getting Uganda as the country with the highest priority, which is not right.</p>
<p>These are the results of the API call for <a href="https://nominatim.openstreetmap.org/search?q=Dubai&amp;format=json">https://nominatim.openstreetmap.org/search?q=Dubai&amp;format=json</a></p>
<p><code>[ { "place_id": "226938824", "licence": "Data © OpenStreetMap contributors, ODbL 1.0. </code><a href="https://www.openstreetmap.org/copyright"><code>https://www.openstreetmap.org/copyright",</code></a><code> "osm_type": "node", "osm_id": "5404871640", "boundingbox": [ "2.9270179", "2.9670179", "30.941206", "30.981206" ], "lat": "2.9470179", "lon": "30.961206", "display_name": "Dubai, Arua, Northern Region, Uganda", "class": "place", "type": "village", "importance": 0.17875, "icon": "https://nominatim.openstreetmap.org/images/mapicons/poi_place_village.p.20.png" }, { "place_id": "16284768", "licence": "Data © OpenStreetMap contributors, ODbL 1.0. </code><a href="https://www.openstreetmap.org/copyright"><code>https://www.openstreetmap.org/copyright",</code></a><code> "osm_type": "node", "osm_id": "1404229008", "boundingbox": [ "2.78168", "2.82168", "44.06159", "44.10159" ], "lat": "2.80168", "lon": "44.08159", "display_name": "Dubai, Buurhakaba بورحكب, Buur Hakaba بورحكب, Bay باي, Soomaaliya الصومال", "class": "place", "type": "suburb", "importance": 0.1725, "icon": "https://nominatim.openstreetmap.org/images/mapicons/poi_place_village.p.20.png" }, [...] ]</code></p>
<p>And this is the wesbite results for <code>Dubai</code> as search parameter.</p>
<p><img src="https://user-images.githubusercontent.com/7332540/36143309-6b345ddc-10b3-11e8-890c-c7f17797699c.png" width="713" alt="screen shot 2018-02-13 at 11 45 09" /></p>
<p>There is something clearly wrong with my request or the server because Dubai in UAE should have the highest priority always, unless you are searching from Uganda.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '18, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/4bdb36e27701d86cc80919cba423d4c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="octohedron&#39;s gravatar image" />
<p><span>octohedron</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="octohedron has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '18, 23:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62069" class="comments-container">
<span id="62071"></span>
<div id="comment-62071" class="comment">
<div id="post-62071-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please do not waste everybodies time by asking the same question in multiple places at the same time.</p>
</div>
<div id="comment-62071-info" class="comment-info">
<span class="comment-age">(13 Feb '18, 10:34)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="62166"></span>
<div id="comment-62166" class="comment">
<div id="post-62166-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>: please add a link for people finding this question here.</p>
</div>
<div id="comment-62166-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 23:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62194"></span>
<div id="comment-62194" class="comment">
<div id="post-62194-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See <a href="https://github.com/openstreetmap/Nominatim/issues/916">https://github.com/openstreetmap/Nominatim/issues/916</a></p>
</div>
<div id="comment-62194-info" class="comment-info">
<span class="comment-age">(19 Feb '18, 01:02)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62069-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question (asked on Github too)" by SimonPoole 13 Feb '18, 10:35

</div>

</div>

</div>

