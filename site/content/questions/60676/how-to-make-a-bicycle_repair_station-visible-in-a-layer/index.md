+++
type = "question"
title = "How to make a bicycle_repair_station visible in a layer?"
description = '''I have added a bicycle_repair_station but it will not become visible in standard or bicycle layer of OSM. It is contained only in the map data. There might be not a symbol available for such a station or did I make an error?'''
date = "2017-11-18T15:37:00Z"
lastmod = "2017-11-20T13:05:00Z"
weight = 60676
keywords = [ "repair", "station", "bicycle", "visibility" ]
aliases = [ "/questions/60676" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to make a bicycle_repair_station visible in a layer?](/questions/60676/how-to-make-a-bicycle_repair_station-visible-in-a-layer)

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
<span id="post-60676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60676-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have added a bicycle_repair_station but it will not become visible in standard or bicycle layer of OSM. It is contained only in the map data. There might be not a symbol available for such a station or did I make an error?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-repair" rel="tag" title="see questions tagged &#39;repair&#39;">repair</span> <span class="post-tag tag-link-station" rel="tag" title="see questions tagged &#39;station&#39;">station</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-visibility" rel="tag" title="see questions tagged &#39;visibility&#39;">visibility</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '17, 15:37</strong></p>
<img src="https://secure.gravatar.com/avatar/795348c8807b1e6ebf965297a4f7c88b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DerNavigator&#39;s gravatar image" />
<p><span>DerNavigator</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DerNavigator has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60676" class="comments-container">
&#10;</div>
<div id="comment-tools-60676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60676-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="60713"></span>

<div id="answer-container-60713" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60713-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-60713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>I have added a bicycle_repair_station but it will not become visible in standard or bicycle layer of OSM. It is contained only in the map data.</p>
</blockquote>
<p>Yes, that is the expected behaviour. The map layers on <a href="http://openstreetmap.org/">http://openstreetmap.org/</a> do not show all information available in the database - this is intentional, because the map strikes a balance between showing information and not becoming too cluttered.</p>
<p>As far as I can tell, a bicycle repair station is too specialized for inclusion in the standard map layer (the default layer). It <em>might</em> make sense for the cycle map layer. The cycle map layer is part of the project <a href="https://wiki.openstreetmap.org/wiki/OpenCycleMap">OpenCycleMap</a>. The project's ticket system already has a ticket about showing repair stations: <a href="https://trac.openstreetmap.org/ticket/5286">Render "bicycle repair stations" on OpenCycleMap</a>. If you have more information to add, you can add it to this ticket.</p>
<p>Apart from that, there's nothing you can do to make the stations show up on the map. However, even without being visible on the map, the stations are still useful - they are searchable, and there are many other users of OSM data beside the main map, so for e.g. bicycle navigation systems of specialised maps, the stations can be useful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '17, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-60713" class="comments-container">
&#10;</div>
<div id="comment-tools-60713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60713-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60683"></span>

<div id="answer-container-60683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60683-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-60683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Go to <a href="https://taginfo.openstreetmap.org/tags/amenity=bicycle_repair_station">taginfo</a> and search for "<code>bicycle_repair_station</code>". Click "Overpass turbo". Move the map to your area of interest and click "run". You'll get a map like <a href="https://overpass-turbo.eu/s/t4H">this</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '17, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '17, 20:13</strong> </span></p>
</div>
</div>
<div id="comments-container-60683" class="comments-container">
&#10;</div>
<div id="comment-tools-60683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60683-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60715"></span>

<div id="answer-container-60715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60715-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bicycle repair stations mapped in OSM are shown on cycle.travel: for example, <a href="http://cycle.travel/map?lat=33.4534&amp;lon=-112.073&amp;zoom=17">http://cycle.travel/map?lat=33.4534&amp;lon=-112.073&amp;zoom=17</a></p>
<p>(Note that cycle.travel covers Western Europe and North America, and is updated from OSM data approximately once a month.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '17, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-60715" class="comments-container">
&#10;</div>
<div id="comment-tools-60715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60715-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60681"></span>

<div id="answer-container-60681" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I did a search for bike repair and got several. These work so maybe thats the way to map one. <a href="http://www.openstreetmap.org/way/344904107">http://www.openstreetmap.org/way/344904107</a> <a href="https://www.openstreetmap.org/node/3465734855">https://www.openstreetmap.org/node/3465734855</a></p>
<p>Sorry it seems you are not looking for businesses (shops) more of a self repair amenity see links below.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '17, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '17, 22:48</strong> </span></p>
</div>
</div>
<div id="comments-container-60681" class="comments-container">
<span id="60682"></span>
<div id="comment-60682" class="comment">
<div id="post-60682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Those are both bicycle shops - "bicycle repair stations" are (as I understand it) not shops, although they may be associated with them.</p>
</div>
<div id="comment-60682-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 20:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60684"></span>
<div id="comment-60684" class="comment">
<div id="post-60684-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sorry OK. They both render as repair shops but i guess most shops could fit brake blocks and tyres but may not be able to rebuild a wheel or a hub gear. Work shop is also sometimes shortened to shop, which is also confusing.</p>
</div>
<div id="comment-60684-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 22:29)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="60685"></span>
<div id="comment-60685" class="comment">
<div id="post-60685-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The picture on <a href="https://wiki.openstreetmap.org/wiki/Tag%3Aamenity%3Dbicycle_repair_station">https://wiki.openstreetmap.org/wiki/Tag%3Aamenity%3Dbicycle_repair_station</a> is the sort of thing that this is about, I think. They're pretty rare in the UK, and I had no idea what they were either until they were discussed on one of the mailing lists.</p>
</div>
<div id="comment-60685-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 22:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60686"></span>
<div id="comment-60686" class="comment">
<div id="post-60686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ho thanks while you were doing that i have been googling and got this <a href="https://transportation.uiowa.edu/bicycle-repair-stations">https://transportation.uiowa.edu/bicycle-repair-stations</a></p>
</div>
<div id="comment-60686-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 22:41)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="60707"></span>
<div id="comment-60707" class="comment">
<div id="post-60707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is a close up of one type. It seems there are quite a lot of designs. Here is one that can have various tools secured to steel flexi cables. The "Repair Station" is, i think quite a nice idea. <a href="https://www.bikefixation.com/product/public-work-stand">https://www.bikefixation.com/product/public-work-stand</a></p>
</div>
<div id="comment-60707-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 23:21)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-60681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60681-form-container" class="comment-form-container">
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

