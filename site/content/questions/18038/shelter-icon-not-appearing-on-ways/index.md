+++
type = "question"
title = "Shelter icon not appearing on ways"
description = '''Hi all, I&#x27;m mapping an alpine shelter and I have drawn quite an accurate way for the building, which is very sharp in aerial imagery. Now, if I add the proper shelter tags to the building&#x27;s area, only the name=* tag gets rendered, while elevation and - most important thing - the shelter icon aren&#x27;t ...'''
date = "2012-11-27T21:27:00Z"
lastmod = "2012-11-28T17:19:00Z"
weight = 18038
keywords = [ "shelter", "icon", "area" ]
aliases = [ "/questions/18038" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Shelter icon not appearing on ways](/questions/18038/shelter-icon-not-appearing-on-ways)

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
<span id="post-18038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18038-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm mapping an alpine shelter and I have drawn quite an accurate way for the building, which is very sharp in aerial imagery. Now, if I add the proper shelter tags to the building's area, only the name=* tag gets rendered, while elevation and - most important thing - the shelter icon aren't rendered at all, so that it's difficult in Mapnik to understand that the thing is really a shelter. Placing a node in the centre of the building, and applying the shelter tag to it, instead, makes the shelter icon appear, but the OSM Wiki seems to discourage this practice (One_feature,_one_OSM_element). Any tips? Thanks! Ocirne</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shelter" rel="tag" title="see questions tagged &#39;shelter&#39;">shelter</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '12, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a4578a09fce23a8045795f5c27418958?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ocirne94&#39;s gravatar image" />
<p><span>Ocirne94</span><br />
<span class="score" title="30 reputation points">30</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ocirne94 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18038" class="comments-container">
&#10;</div>
<div id="comment-tools-18038" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18038-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="18044"></span>

<div id="answer-container-18044" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18044-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have <code>amenity=shelter</code> or <code>tourism=alpine_hut</code> on a <code>building=*</code> way then the icon renders on the standard render. It won't though show the elevation as the node shelter does.</p>
<p>You are correct that having two features for one item is discouraged, and filing a change request at <a href="https://trac.openstreetmap.org/">trac.openstreetmap.org</a> is probably the recommended route. <a href="http://lists.openstreetmap.org/pipermail/dev/2012-November/026173.html">I understand that there are currently efforts to redesign the stylesheets</a>, so once that is complete perhaps the outstanding requests can be considered. Examples:</p>
<ul>
<li>what you have done with <a href="https://www.openstreetmap.org/browse/node/2037238281">the node</a> inside <a href="https://www.openstreetmap.org/browse/way/117546967/history">this way</a> can be seen <a href="http://osm.org/go/0CGnqz12r--?m">here</a></li>
<li>another shelter as a building showing the shelter icon does render can be seen <a href="https://www.openstreetmap.org/browse/way/35967327">here</a> - this one is using tourism=alpine_hut</li>
<li>the <a href="https://trac.openstreetmap.org/ticket/1689">trac ticket</a> which added them originally</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '12, 23:57</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-18044" class="comments-container">
&#10;</div>
<div id="comment-tools-18044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18044-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18055"></span>

<div id="answer-container-18055" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18055-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Or you can use a better suited map for that : <a href="http://maps.refuges.info">http://maps.refuges.info</a></p>
<ul>
<li>Mountain buildings shown at zoom 11+</li>
<li>Support for node, relation and way tagging</li>
<li>icone+ele+name</li>
</ul>
<p>Openstreetmap is about data, maps comes next</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '12, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0137f3597f9ca0efbda5c3b1e2678aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sly&#39;s gravatar image" />
<p><span>sly</span><br />
<span class="score" title="290 reputation points">290</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sly has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '12, 20:53</strong> </span></p>
</div>
</div>
<div id="comments-container-18055" class="comments-container">
<span id="18056"></span>
<div id="comment-18056" class="comment">
<div id="post-18056-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Aktet Sly, I reject your vieuw but in your opinion I could stop cartering since I work for a map. I used to work for a rather large database and now I'm contributing to OSM. But Ill consider the result to be as a variant forbidden for your eyes only. Bye</p>
</div>
<div id="comment-18056-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 14:03)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="18058"></span>
<div id="comment-18058" class="comment">
<div id="post-18058-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe I was a little quick in my view ;-) It's is not that I consider the map below data or anything. What I meant is that even before drawing a map, you need to start by the question : "what data do I collect, and how to be consistent"</p>
<p>If you focus too much on the "how should I do to make my alpine_hut appear on one specific map", you'll end with tagging it as an airport to be sure it displays wich brings several new problems.</p>
</div>
<div id="comment-18058-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 14:10)</span> <span class="comment-user userinfo">sly</span>
</div>
</div>
</div>
<div id="comment-tools-18055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18055-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18041"></span>

<div id="answer-container-18041" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18041-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-18041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>HI as claer its not my own answer but out of 2010, but describes a similar situation, Hendrik</p>
<p>The OpenStreetMap-data is used to create many different maps, often by different people and available on different websites. There are maps you can view with your browser and maps for other programs or even mobile devices (like Garmin maps).</p>
<p>Every one of these maps can be very different:</p>
<p>• Not everything that is in the data, is also shown on every map. Some features are only shown on specialized maps, some features aren't shown at all and are only used for other applications, e.g. routing.</p>
<p>• Some maps are updated every minute, others much less often (e.g. once a week or month). Sometimes the tiles (map images) are cached and it will take longer for new or changed stuff to appear. Check if the map you are using shows the update interval or actual date and time.</p>
<p>When you talk about 'the map', you may mean the 'Mapnik'-layer on OpenStreetMap.org. That one should be updated every minute, but you still have to keep in mind that not everything is shown there.</p>
<p>If you checked the points above and you still think your changes should appear, you may indeed have done something wrong. Please consider doing the following:</p>
<p>• Check if your changes were indeed added to the database. You can view a history of all your edits in your profile on OpenStreetMap.org under 'my edits'.</p>
<p>• Check other examples of the features you have added or changed and see if they are mapped the same way. You may also want to check the map features or other wiki pages for the correct tags.</p>
<p>• Ask someone else for help. Provide a link to the area you have edited or the changeset (that you can find in your edit history).</p>
<p>answered 12 Jul '10, 00:41</p>
<p>driver2</p>
<p>Above the name of the original autor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '12, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Nov '12, 23:58</strong> </span></p>
</div>
</div>
<div id="comments-container-18041" class="comments-container">
<span id="18042"></span>
<div id="comment-18042" class="comment">
<div id="post-18042-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Er - you might want to edit that answer a bit for clarity so that bullet points are preserved and so that "link|award points|edit|more" isn't copied over. It's not very legible as it stands.</p>
</div>
<div id="comment-18042-info" class="comment-info">
<span class="comment-age">(27 Nov '12, 22:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="18045"></span>
<div id="comment-18045" class="comment">
<div id="post-18045-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Done, readable ?</p>
</div>
<div id="comment-18045-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 00:00)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="18076"></span>
<div id="comment-18076" class="comment">
<div id="post-18076-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How about a link to the original answer instead of copy'n'pasting it here?</p>
</div>
<div id="comment-18076-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 17:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18041" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18041-form-container" class="comment-form-container">
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

