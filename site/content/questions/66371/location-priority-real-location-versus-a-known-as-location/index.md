+++
type = "question"
title = "Location Priority: Real Location versus a Known-As Location"
description = '''I have been experimenting with geolocation, and the geolocation API, and I ran into a strange issue that I have not been able to work around other than to use a different provider (Yandex in this case because it too does not require an API key). I was encoding about 60 named locations in the format ...'''
date = "2018-10-17T15:27:00Z"
lastmod = "2018-10-23T15:24:00Z"
weight = 66371
keywords = [ "geolocation", "duplicate" ]
aliases = [ "/questions/66371" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Location Priority: Real Location versus a Known-As Location](/questions/66371/location-priority-real-location-versus-a-known-as-location)

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
<span id="post-66371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66371-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been experimenting with geolocation, and the geolocation API, and I ran into a strange issue that I have not been able to work around other than to use a different provider (Yandex in this case because it too does not require an API key). I was encoding about 60 named locations in the format "city state", such as "buffalo new york", and ran into a problem. For the places I was encoding, the few I verified appeared to be correct when referencing the first returned geolocation record except for a place called "Middleville, New York". Middleville, New York is a village in upstate New York, in the county of Herkimer with a ZIP code of 13406. However, the first record returned from the OpenStreetMaps.org web site and the geolocation is API is for a small place here on Long Island that is named "Middleville" but is really in Fort Solonga, NY with a ZIP code of 11768. If I were to send mail to Middleville, NY it would go to upstate New York not here on Long Island.</p>
<p><em>My question is</em> why does OpenStreetMaps give priority to a non-postal location over and official postal location? When I check Google, Bing and Mapquest for Middleville, NY, the first record returned if the official postal location. When I go to OpenStreetMaps.org, the first location returned is the Fort Solonga location here on Long Island. Is there any way to alter the priority of the returned data when only the city and state are queried?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '18, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1c872bd45ff7b3017cb34a3ba96edab5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aardvark&#39;s gravatar image" />
<p><span>Aardvark</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aardvark has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '18, 18:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66371" class="comments-container">
<span id="66402"></span>
<div id="comment-66402" class="comment">
<div id="post-66402-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>note that it is OpenStreetMap but not OpenStreetMap<em>s</em>! :-)</p>
</div>
<div id="comment-66402-info" class="comment-info">
<span class="comment-age">(20 Oct '18, 18:44)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="66430"></span>
<div id="comment-66430" class="comment">
<div id="post-66430-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've asked the Nominatim dev for input on this, but please make your question title more descriptive of the actual question (result priority in Nominatim).</p>
<p>Note that there is no prioritisation based on if the location has a post code added in OSM or not (that would also likely not make sense), but it could be expected that place=village would take precedence over a place=hamlet (that could have unexpected consequences though).</p>
</div>
<div id="comment-66430-info" class="comment-info">
<span class="comment-age">(23 Oct '18, 15:24)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66371-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

