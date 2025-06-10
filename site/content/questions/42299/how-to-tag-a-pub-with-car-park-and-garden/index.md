+++
type = "question"
title = "How to tag a pub with car park and garden?"
description = '''Tagging a pub as a single node or a building with amenity=pub seems well defined. See http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpub Some pubs, however, have their own car park, a beer garden and other facilities on site. To map these I have created an area that is tagged as landuse=retail and...'''
date = "2015-04-12T17:54:00Z"
lastmod = "2015-04-13T15:23:00Z"
weight = 42299
keywords = [ "amenity", "site", "pub", "area" ]
aliases = [ "/questions/42299" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a pub with car park and garden?](/questions/42299/how-to-tag-a-pub-with-car-park-and-garden)

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
<span id="post-42299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42299-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Tagging a pub as a single node or a building with amenity=pub seems well defined. See <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpub">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpub</a></p>
<p>Some pubs, however, have their own car park, a beer garden and other facilities on site. To map these I have created an area that is tagged as landuse=retail and amenity=pub. This is the whole site. Then the car park is created with a separate area within the site and tagged amenity=parking and access=customers. A service road is added to join the car park to the public road. Separate areas are also created for any garden and the pub building. The best tags for the garden appear to be leisure=garden with access=customers. The best tags for the pub building appear to be building=yes. Schools use amenity=school for the site and building=school for the building, but building=pub isn't in the wiki although it is used over 1200 times. Then entrances to the building are tagged with entrance=main, etc. Any contact information such as website and phone are added to the main site area.</p>
<p>Is this the best approach?</p>
<p>Inspiration: - use of landuse=retail based on planning use classification, e.g. <a href="http://en.wikipedia.org/wiki/Planning_use_classes_in_England#Class_A4_.E2.80.93_Drinking_establishments">http://en.wikipedia.org/wiki/Planning_use_classes_in_England#Class_A4_.E2.80.93_Drinking_establishments</a> - schools use amenity=school for whole site, see <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool</a> - <a href="https://help.openstreetmap.org/questions/1103/should-i-tag-nodes-or-areas-for-amenity-and-tourism">https://help.openstreetmap.org/questions/1103/should-i-tag-nodes-or-areas-for-amenity-and-tourism</a> - use of entrance tag for sites, e.g. <a href="https://help.openstreetmap.org/questions/14078/tagging-large-sites-entrance-area">https://help.openstreetmap.org/questions/14078/tagging-large-sites-entrance-area</a> - use of building=pub see <a href="http://taginfo.openstreetmap.org/tags/building=pub">http://taginfo.openstreetmap.org/tags/building=pub</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-site" rel="tag" title="see questions tagged &#39;site&#39;">site</span> <span class="post-tag tag-link-pub" rel="tag" title="see questions tagged &#39;pub&#39;">pub</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '15, 17:54</strong></p>
<img src="https://secure.gravatar.com/avatar/1c4ffb9bacfef145ef8dedf853b732dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="al_t&#39;s gravatar image" />
<p><span>al_t</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="al_t has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42299" class="comments-container">
<span id="42307"></span>
<div id="comment-42307" class="comment">
<div id="post-42307-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is no reason, not to use building=pub. For the rest it seems fine. As Hendrikklaas wrote, you could add operator, but I would only do that in case you do not have an enclosing polygon for all parts.</p>
</div>
<div id="comment-42307-info" class="comment-info">
<span class="comment-age">(13 Apr '15, 07:11)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="42310"></span>
<div id="comment-42310" class="comment">
<div id="post-42310-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, I also feel meta data like operator and contact information should be just in one place. I was thinking the enclosing polygon as well.</p>
</div>
<div id="comment-42310-info" class="comment-info">
<span class="comment-age">(13 Apr '15, 10:20)</span> <span class="comment-user userinfo">al_t</span>
</div>
</div>
</div>
<div id="comment-tools-42299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42299-form-container" class="comment-form-container">
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

<span id="42312"></span>

<div id="answer-container-42312" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42312-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would take a different approach as I tend to avoid relations where they are not warranted. In this instance I would tag as follows</p>
<p>An outline with building=yes and all building related tags (address, height, roof, year built etc etc)</p>
<p>Inside that, a node with amenity=pub and include all relevant tags beer_garden=yes, wifi=yes, guinness=yes etc etc</p>
<p>Parking would be tagged with a polygon and tagged with parking tags as appropriate</p>
<p>Think of it this way, if there is information related to the pub that you would specifically want to know about that, or any other pub, put it in the pub tag where it belongs</p>
<p>In other words, keep it as simple as possible and think logically.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '15, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
</div>
<div id="comments-container-42312" class="comments-container">
&#10;</div>
<div id="comment-tools-42312" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42312-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42301"></span>

<div id="answer-container-42301" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42301-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi al_t, consider to add brand and / or operator to all the separate items as well together with acces=customers</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '15, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-42301" class="comments-container">
&#10;</div>
<div id="comment-tools-42301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42301-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42303"></span>

<div id="answer-container-42303" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42303-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Apart from visualization, is this the best way to structure the data? If I were to query all pubs which have a garden in a given area, do you think it would be possible this way? A relation for the whole thing might make things easier. Also reminds me of the proposition to allow to tag different amenities within a camping as tags of a camping node. This second approach makes for a much simpler mapping experience (i.e. could be done from Osmand or a dedicated gardenpub app), and easier data consumption. But a less pretty map.</p>
<p>Sorry if that's too philosophical an answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '15, 23:35</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-42303" class="comments-container">
<span id="42306"></span>
<div id="comment-42306" class="comment">
<div id="post-42306-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is the site relation, but that should only be used when one cannot draw a polygon around the area, i.e. when the different parts are physically separated.</p>
</div>
<div id="comment-42306-info" class="comment-info">
<span class="comment-age">(13 Apr '15, 07:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="42311"></span>
<div id="comment-42311" class="comment">
<div id="post-42311-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help. I was modelling my way of tagging pubs on that for schools - <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool</a> So I thought a query like ST_Within ( see <a href="http://postgis.net/docs/manual-2.0/ST_Within.html">http://postgis.net/docs/manual-2.0/ST_Within.html</a> and <a href="http://revenant.ca/www/postgis/workshop/joins.html">http://revenant.ca/www/postgis/workshop/joins.html</a> ) might be the way to query whether a pub has a car park or garden. Do people do that?</p>
</div>
<div id="comment-42311-info" class="comment-info">
<span class="comment-age">(13 Apr '15, 10:27)</span> <span class="comment-user userinfo">al_t</span>
</div>
</div>
</div>
<div id="comment-tools-42303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42303-form-container" class="comment-form-container">
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

