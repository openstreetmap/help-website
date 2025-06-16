+++
type = "question"
title = "get address string like in Nominatim using Overpass API"
description = '''I am trying to build up an address string like OSM Nominatim does using the overpass API, when all I have is the ID of e.g. a way:  https://www.openstreetmap.org/way/4979228 Target would be to get a string shown as when you are searching for &#x27;Aachener Weiher&quot; on Nominatim  Aachener Weiher, Frieda-Fis...'''
date = "2017-12-10T20:01:00Z"
lastmod = "2017-12-11T12:31:00Z"
weight = 61125
keywords = [ "overpass", "nominatim", "osm", "way", "address" ]
aliases = [ "/questions/61125" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [get address string like in Nominatim using Overpass API](/questions/61125/get-address-string-like-in-nominatim-using-overpass-api)

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
<span id="post-61125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61125-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to build up an address string like OSM Nominatim does using the overpass API, when all I have is the ID of e.g. a way:</p>
<p><a href="https://www.openstreetmap.org/way/4979228">https://www.openstreetmap.org/way/4979228</a></p>
<p>Target would be to get a string shown as when you are <a href="https://www.openstreetmap.org/search?query=aachener%20weiher#map=18/50.93526/6.92739&amp;layers=H" title="searching for &#39;Aachener Weiher&quot; on Nominatim">searching for 'Aachener Weiher" on Nominatim</a></p>
<p><code>Aachener Weiher, Frieda-Fischer-Weg, Neustadt/Süd, Innenstadt, Köln, Regierungsbezirk Köln, Nordrhein-Westfalen, 50674, Deutschland</code></p>
<p>I guess this can maybe be done using the <code>is_in</code> or recurse up <code>&lt;&lt;;</code> functions, but I am stuck n how to use them properly. All examples I found show how to get features in a given area, not the area around a given feature.</p>
<p>Can someone please point me into the right direction? Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '17, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ee68f452c4ceca4ab5d477241fe75ce2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osm-noob&#39;s gravatar image" />
<p><span>osm-noob</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osm-noob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61125" class="comments-container">
<span id="61131"></span>
<div id="comment-61131" class="comment">
<div id="post-61131-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Why do you want to do that with Overpass API? Overpass API is not a geocoder, you won't achieve the same results as with Nominatim because they work quite differently.</p>
</div>
<div id="comment-61131-info" class="comment-info">
<span class="comment-age">(11 Dec '17, 08:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="61134"></span>
<div id="comment-61134" class="comment">
<div id="post-61134-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - I found Nominatim's reverse Geocoding feature - which can get the address details, but does not include the OSM IDs of the features. My approach was kind of a polyfill for getting IDs with names. But as I learned today, the OSM IDs are far from persistent... I think I have to read more about the underlying tech and understand it better.</p>
</div>
<div id="comment-61134-info" class="comment-info">
<span class="comment-age">(11 Dec '17, 12:31)</span> <span class="comment-user userinfo">osm-noob</span>
</div>
</div>
</div>
<div id="comment-tools-61125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61125-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

