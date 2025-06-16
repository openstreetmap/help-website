+++
type = "question"
title = "nominatim search for states in viewbox"
description = '''Can I search for a country states(admin level=4) in Viewport via nominatim search? http://nominatim.openstreetmap.org/search?q=district&amp;amp;countrycodes=IL&amp;amp;limit=20&amp;amp;format=xml&amp;amp;email=info&amp;amp;bounded=1&amp;amp;viewbox=34.270278754419145,33.34013,35.876804,29.496639&amp;amp;debug=0&amp;amp;addressdeta...'''
date = "2014-01-02T15:04:00Z"
lastmod = "2014-01-02T16:00:00Z"
weight = 29544
keywords = [ "boundaries", "country", "nominatim" ]
aliases = [ "/questions/29544" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim search for states in viewbox](/questions/29544/nominatim-search-for-states-in-viewbox)

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
<span id="post-29544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29544-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can I search for a country states(admin level=4) in Viewport via nominatim search?</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=district&amp;countrycodes=IL&amp;limit=20&amp;format=xml&amp;email=info&amp;bounded=1&amp;viewbox=34.270278754419145,33.34013,35.876804,29.496639&amp;debug=0&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?q=district&amp;countrycodes=IL&amp;limit=20&amp;format=xml&amp;email=info&amp;bounded=1&amp;viewbox=34.270278754419145,33.34013,35.876804,29.496639&amp;debug=0&amp;addressdetails=1</a></p>
<p>this search return all states in a country. but only if display_name like "District". there is a way to filter results and get only places admin_level=4 ?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '14, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/57fadcd89e00b509fec577a14acc3447?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Izikb&#39;s gravatar image" />
<p><span>Izikb</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Izikb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '14, 15:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-29544" class="comments-container">
&#10;</div>
<div id="comment-tools-29544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29544-form-container" class="comment-form-container">
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

<span id="29547"></span>

<div id="answer-container-29547" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29547-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might want to use the <strong>bbox operator</strong> but there is AFAIK no operator to restrict the admin_level:<br />
<a href="https://wiki.openstreetmap.org/wiki/Nominatim#Parameters">https://wiki.openstreetmap.org/wiki/Nominatim#Parameters</a></p>
<p>So either you are able to prefilter your query by adjusting the state,country, ... addresses or you may use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> instead</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '14, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-29547" class="comments-container">
<span id="29548"></span>
<div id="comment-29548" class="comment">
<div id="post-29548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! the problem is that Overpass API is too slow</p>
</div>
<div id="comment-29548-info" class="comment-info">
<span class="comment-age">(02 Jan '14, 15:49)</span> <span class="comment-user userinfo">Izikb</span>
</div>
</div>
<span id="29550"></span>
<div id="comment-29550" class="comment">
<div id="post-29550-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hmm Qverpass API is one of the fastest ways to work remote with global OSM data. The only alternative would be to do the processing local using OSM planet extracts.</p>
<p>BTW.: All APIs are hosted on donated resources and maintained by volunteers. So they require fair use and are esp. not suitable to do bulk transfers: <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy</a></p>
</div>
<div id="comment-29550-info" class="comment-info">
<span class="comment-age">(02 Jan '14, 15:54)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="29552"></span>
<div id="comment-29552" class="comment">
<div id="post-29552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, maybe you can help me :)</p>
<p>I do this with overpass, I want to get states(admin_level=4) in this bbox. this is my code:</p>
<p><a href="http://overpass-turbo.eu/s/1V7">http://overpass-turbo.eu/s/1V7</a></p>
<p>why it's take a few minutes to return results? in nominatim it's really fast.</p>
<p>I use overpass turbo</p>
<p>Thanks !!</p>
</div>
<div id="comment-29552-info" class="comment-info">
<span class="comment-age">(02 Jan '14, 16:00)</span> <span class="comment-user userinfo">Izikb</span>
</div>
</div>
</div>
<div id="comment-tools-29547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29547-form-container" class="comment-form-container">
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

