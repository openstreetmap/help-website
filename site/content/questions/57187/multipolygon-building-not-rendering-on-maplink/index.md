+++
type = "question"
title = "multipolygon building not rendering on maplink"
description = '''It&#x27;s about this building: http://www.openstreetmap.org/relation/7367542#map=19/48.01331/16.79028 My main goals for this building was to test 3D buildings and try to include the building as accurate as possible. The problem now ist that the building does not render on maplink and I don&#x27;t know why. It...'''
date = "2017-07-19T21:15:00Z"
lastmod = "2017-10-10T08:17:00Z"
weight = 57187
keywords = [ "building", "maplink", "3d" ]
aliases = [ "/questions/57187" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [multipolygon building not rendering on maplink](/questions/57187/multipolygon-building-not-rendering-on-maplink)

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
<span id="post-57187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57187-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It's about this building: <a href="http://www.openstreetmap.org/relation/7367542#map=19/48.01331/16.79028">http://www.openstreetmap.org/relation/7367542#map=19/48.01331/16.79028</a></p>
<p>My main goals for this building was to test 3D buildings and try to include the building as accurate as possible.</p>
<p>The <em>problem</em> now ist that the building does not render on maplink and I don't know why. It does show up on f4map ( <a href="http://demo.f4map.com/#lat=48.0134937&amp;lon=16.7904739&amp;zoom=20&amp;camera.theta=74.099&amp;camera.phi=-8.251">http://demo.f4map.com/#lat=48.0134937&amp;lon=16.7904739&amp;zoom=20&amp;camera.theta=74.099&amp;camera.phi=-8.251</a> ) even it's missing the name tag.</p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-maplink" rel="tag" title="see questions tagged &#39;maplink&#39;">maplink</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '17, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/978afd5e16d64335ba23eb3227f2cfd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TBKMrt&#39;s gravatar image" />
<p><span>TBKMrt</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TBKMrt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57187" class="comments-container">
<span id="57189"></span>
<div id="comment-57189" class="comment">
<div id="post-57189-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you give us a pointer to "maplink*?</p>
</div>
<div id="comment-57189-info" class="comment-info">
<span class="comment-age">(19 Jul '17, 22:38)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57187-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="57195"></span>

<div id="answer-container-57195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57195-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is probably a browser cache issue: I can see the building.</p>
<p>There is no need to use a relation for Simple 3d buildings. It is completely unnecessary as all the relevant information is already contained in the tags and geometries. The principal developers of the S3DB tagging are also authors of some of the visualisation tools (but not f4). <a href="https://forum.openstreetmap.org/viewtopic.php?id=56857">They agreed</a> some time ago that use of relations made data consumption more difficult for gains which were, at best, marginal. Consequently the use of relations is now deprecated (I.e., not recommended).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '17, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '17, 17:39</strong> </span></p>
</div>
</div>
<div id="comments-container-57195" class="comments-container">
<span id="57197"></span>
<div id="comment-57197" class="comment">
<div id="post-57197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For me, the link shows a +-shaped building outline but there is no darker shade filling the outline, as there is for nearby buildings.</p>
</div>
<div id="comment-57197-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 12:10)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57198"></span>
<div id="comment-57198" class="comment">
<div id="post-57198-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try F5 or CTRL+F5 or CTRL+Shift+R in your browser.</p>
</div>
<div id="comment-57198-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 12:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="57204"></span>
<div id="comment-57204" class="comment">
<div id="post-57204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No change.</p>
</div>
<div id="comment-57204-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 15:25)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57207"></span>
<div id="comment-57207" class="comment">
<div id="post-57207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a>, on the Simple 3D wiki page it says "A relation tagged with type=building groups building outline and all building parts together. It is highly recommended to use the relation if there is at least one building part." Is this no longer accurate? <a href="http://wiki.openstreetmap.org/wiki/Simple_3D_buildings#Building_relation">http://wiki.openstreetmap.org/wiki/Simple_3D_buildings#Building_relation</a></p>
</div>
<div id="comment-57207-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 17:12)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="57208"></span>
<div id="comment-57208" class="comment">
<div id="post-57208-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Discussion here <a href="https://forum.openstreetmap.org/viewtopic.php?id=56857.">https://forum.openstreetmap.org/viewtopic.php?id=56857.</a> I've never used a relation for S3DB mapping &amp; never had problems.</p>
</div>
<div id="comment-57208-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 17:37)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="57209"></span>
<div id="comment-57209" class="comment not_top_scorer">
<div id="post-57209-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/595/neuhausr">@neuhausr</a> should add the subforum really is where most critical discussion takes place.</p>
</div>
<div id="comment-57209-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 17:38)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="57210"></span>
<div id="comment-57210" class="comment not_top_scorer">
<div id="post-57210-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> thanks. In the forum thread you linked to they discussed changing the Simple 3D wiki page, but apparently never got around to doing it? Maybe I'll give it a go.</p>
</div>
<div id="comment-57210-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 17:49)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="60035"></span>
<div id="comment-60035" class="comment not_top_scorer">
<div id="post-60035-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I somewhat have to agree and disgree here. My first try was way less complicated, but it didn't show up on the map at all - for whatever reason. Simple 3D buildings on the osm.wiki says that the outline should be "a closed way or multipolygon tagged with building=*" and that "Building attributes (e.g., address, name, overall height, operator, etc.) must be tagged on the building outline." So in my opinion it is highly over complicated, but what the wiki says to do.</p>
<p>The building has to be split in two parts, because they don't look the same. It is like File:Minlevel.svg (again on the osm wiki). If S3DB would accept combined areas as building outline this could be done with one relation that includes the whole building. Moreover many of the 3D buildings in OSM which you can find as example use relations very heavily.</p>
<p>On the map itself, I kept a close look at it and it seemed like a maplink error. When you had the full zoom, the building wouldn't render correctly. If you zoomed out a little bit,the uilding was displayed correctly.</p>
</div>
<div id="comment-60035-info" class="comment-info">
<span class="comment-age">(10 Oct '17, 08:11)</span> <span class="comment-user userinfo">TBKMrt</span>
</div>
</div>
</div>
<div id="comment-tools-57195" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-57195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57202"></span>

<div id="answer-container-57202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, you actually have two multipolygons for this building,</p>
<p>relation #7367544 (which contains most of the structural details (but no name)). This area is not the whole outline of the building :- <a href="http://www.openstreetmap.org/relation/7367544#map=19/48.01331/16.79062">http://www.openstreetmap.org/relation/7367544#map=19/48.01331/16.79062</a></p>
<p>and relation #7367542 (less detail but has the building name) This outline is of the whole building :- <a href="http://www.openstreetmap.org/relation/7367542#map=19/48.01331/16.79062">http://www.openstreetmap.org/relation/7367542#map=19/48.01331/16.79062</a></p>
<p>I would imagine there must be a conflict as the details are spread over two relations. I would suggest removing one of the relations consolidating all information on the remaining relation.</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '17, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-57202" class="comments-container">
<span id="60036"></span>
<div id="comment-60036" class="comment">
<div id="post-60036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are even more relations here. The building is a relation, the outline is a relation, the part of the building that has a lower floor is a relation and the part of the building that only has an upper floor is a relation. I thought about having two areas for the building and one line on the outside. But then you wouldn't really be able to select the outline that easy. So I used ways which are connected to areas using a relation.</p>
<p>I did the best I could to follow the guidelines on <a href="https://wiki.openstreetmap.org/wiki/Simple_3D_buildings,">https://wiki.openstreetmap.org/wiki/Simple_3D_buildings,</a> but I'm not really happy with the result since - in my opinion - it is highly overcomplicated.</p>
<p>A simple version of this building using just one relation to connect all the areas together and using both building part areas as outline resulted in an incorrect render (aka nothing showed up on the map).</p>
</div>
<div id="comment-60036-info" class="comment-info">
<span class="comment-age">(10 Oct '17, 08:17)</span> <span class="comment-user userinfo">TBKMrt</span>
</div>
</div>
</div>
<div id="comment-tools-57202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57202-form-container" class="comment-form-container">
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

