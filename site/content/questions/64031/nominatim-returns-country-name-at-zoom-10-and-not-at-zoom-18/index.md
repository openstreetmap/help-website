+++
type = "question"
title = "Nominatim returns country name at zoom 10 and not at zoom 18"
description = '''The below 2 links return slightly different results. At zoom level 10 country code is returned &quot;SN&quot; and country name goes along with it (&quot;Senegal&quot;): https://nominatim.openstreetmap.org/reverse?format=xml&amp;amp;lat=13.35228&amp;amp;lon=-15.67002&amp;amp;zoom=10 At zoom level 18, when it supposed to be a more a...'''
date = "2018-06-05T18:02:00Z"
lastmod = "2018-06-06T20:53:00Z"
weight = 64031
keywords = [ "zoomlevel", "country", "nominatim", "countryname", "zoom" ]
aliases = [ "/questions/64031" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim returns country name at zoom 10 and not at zoom 18](/questions/64031/nominatim-returns-country-name-at-zoom-10-and-not-at-zoom-18)

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
<span id="post-64031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The below 2 links return slightly different results. At zoom level 10 country code is returned "SN" and country name goes along with it ("Senegal"): <a href="https://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=13.35228&amp;lon=-15.67002&amp;zoom=10">https://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=13.35228&amp;lon=-15.67002&amp;zoom=10</a></p>
<p>At zoom level 18, when it supposed to be a more accurate result, it returns country code only "SN" https://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=13.35228&amp;lon=-15.67002&amp;zoom=18 What is odd, is that having country code, it is basically the same information for the country name.</p>
<p>I understand that those are different "place ids" and "osm ids" and "osm types", but still doesn't seem correct to me.</p>
<p>Any suggestions on how to address it would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-countryname" rel="tag" title="see questions tagged &#39;countryname&#39;">countryname</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '18, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/34a9ff282bda047810fdbb874b6671b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Taras%20O&#39;s gravatar image" />
<p><span>Taras O</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Taras O has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64031" class="comments-container">
&#10;</div>
<div id="comment-tools-64031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64031-form-container" class="comment-form-container">
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

<span id="64044"></span>

<div id="answer-container-64044" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64044-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Taras O has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not an expert on Nominatim but as nobody else has answered...</p>
<p>Maybe it is related to the fact that the zoom 18 result is for a way (road) that is partly outside Senegal - see <a href="https://nominatim.openstreetmap.org/details.php?place_id=161282086">https://nominatim.openstreetmap.org/details.php?place_id=161282086</a></p>
<p>Moving the lat/lon slightly so that it is closer to a way that is entirely inside Senegal seems to return the country name, e.g. <a href="https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=13.347182361714394&amp;lon=-15.65073680903879&amp;zoom=18">https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=13.347182361714394&amp;lon=-15.65073680903879&amp;zoom=18</a></p>
<p>That doesn't really explain the difference between country name and country code though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '18, 09:57</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-64044" class="comments-container">
<span id="64046"></span>
<div id="comment-64046" class="comment">
<div id="post-64046-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You're right. In Nominatim every map feature is assigned exactly one country_code during import and data updates. It's tricky (and a limitation of Nominatim) when roads cross country borders. In this case the correct country_code is returned at least. But the road is not completely inside Senegal so the spatial query looking for administrative boundaries sees the country (gray-ed on <a href="https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=422943503)">https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=422943503)</a> but doesn't consider it part of the address. It doesn't happen with a nearby road that doesn't cross the border <a href="https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=422943515">https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=422943515</a> Usually the recommendation is to split the OSM way at the country border. For an unnamed road and since the correct country(code) was assigned I'd say an unnecessary work-around. See also <a href="https://github.com/openstreetmap/Nominatim/issues/844">https://github.com/openstreetmap/Nominatim/issues/844</a></p>
</div>
<div id="comment-64046-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 12:08)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="64064"></span>
<div id="comment-64064" class="comment">
<div id="post-64064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you alan_gr and mtmail! That explains it.</p>
</div>
<div id="comment-64064-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 20:15)</span> <span class="comment-user userinfo">Taras O</span>
</div>
</div>
<span id="64065"></span>
<div id="comment-64065" class="comment">
<div id="post-64065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I actually just discovered something else. I have an older OSM version running on an internal server (2.x) and it returns the JSON for the same query (zoom 18):</p>
<p>{"place_id":"128323717","licence":"Data © OpenStreetMap contributors, ODbL 1.0. http:\/\/www.openstreetmap.org\/copyright","osm_type":"way","osm_id":"301447252","lat":"13.28023","lon":"-15.6339599","place_rank":"26","category":"highway","type":"track","importance":"0.1","addresstype":"road","display_name":"Saré Alkaly - Boghal - Ndiamacouta, Ndiamacouta (Chef lieu de commune), Arrondissement de Bounkiling, Sédhiou, Sédhiou Region, Senegal","name":"Saré Alkaly - Boghal - Ndiamacouta","address":{"road":"Saré Alkaly - Boghal - Ndiamacouta","village":"Ndiamacouta (Chef lieu de commune)","county":"Arrondissement de Bounkiling","state":"Sédhiou","country":"Senegal","country_code":"sn"}}</p>
<p>However, the OSM id seems to be different.</p>
</div>
<div id="comment-64065-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 20:53)</span> <span class="comment-user userinfo">Taras O</span>
</div>
</div>
</div>
<div id="comment-tools-64044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64044-form-container" class="comment-form-container">
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

