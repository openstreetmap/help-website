+++
type = "question"
title = "Bicycle Directions not using recently entered bike path"
description = '''I recently added a portion of a bike trail in Florissant, MO to OpenStreetMap. When I query for bicycle directions it does not utilize the bike path. What might I have done wrong? directions API query:  http://open.mapquestapi.com/directions/v1/route?outFormat=json&amp;amp;shapeFormat=raw&amp;amp;generalize...'''
date = "2013-03-06T02:50:00Z"
lastmod = "2013-03-07T15:36:00Z"
weight = 20515
keywords = [ "directions", "path", "api", "bicycle", "mapquest" ]
aliases = [ "/questions/20515" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bicycle Directions not using recently entered bike path](/questions/20515/bicycle-directions-not-using-recently-entered-bike-path)

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
<span id="post-20515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20515-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently added a portion of a bike trail in Florissant, MO to OpenStreetMap. When I query for bicycle directions it does not utilize the bike path. What might I have done wrong?</p>
<p>directions API query: <a href="http://open.mapquestapi.com/directions/v1/route?outFormat=json&amp;shapeFormat=raw&amp;generalize=10&amp;from=38.820426%2C-90.336433&amp;unit=m&amp;locale=en_US&amp;enhancedNarrative=false&amp;to=38.790915%2C-90.321824&amp;routeType=bicycle">http://open.mapquestapi.com/directions/v1/route?outFormat=json&amp;shapeFormat=raw&amp;generalize=10&amp;from=38.820426%2C-90.336433&amp;unit=m&amp;locale=en_US&amp;enhancedNarrative=false&amp;to=38.790915%2C-90.321824&amp;routeType=bicycle</a></p>
<p>I would expect the directions to use the sunset trail as seen on the map here: <a href="https://www.openstreetmap.org/?box=yes&amp;bbox=-90.36306%2C38.78717%2C-90.31781%2C38.83089">https://www.openstreetmap.org/?box=yes&amp;bbox=-90.36306%2C38.78717%2C-90.31781%2C38.83089</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-mapquest" rel="tag" title="see questions tagged &#39;mapquest&#39;">mapquest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '13, 02:50</strong></p>
<img src="https://secure.gravatar.com/avatar/fbebd9f68528fcbc38107226b2b81bc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JARinteractive&#39;s gravatar image" />
<p><span>JARinteractive</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JARinteractive has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '13, 11:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span></p>
</div>
</div>
<div id="comments-container-20515" class="comments-container">
<span id="20523"></span>
<div id="comment-20523" class="comment">
<div id="post-20523-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I can get mapquest to use the sunset trail, see <a href="http://mapq.st/YcfYma">http://mapq.st/YcfYma</a> .</p>
<p>Maybe you also have to set advanced routing options for bicycles, as seen on their website ("Favour routes usings trails&amp;paths").</p>
<p>Don't know if they are exposed thru the API, though.</p>
</div>
<div id="comment-20523-info" class="comment-info">
<span class="comment-age">(06 Mar '13, 10:59)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20515-form-container" class="comment-form-container">
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

<span id="20516"></span>

<div id="answer-container-20516" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20516-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I dont know the mapquest routing but I would guess that the routing routines are not so clever that they always choose the cycleway. Most bicycle routers will not choose that trail because it is twisting and turning and all other roads are straighter and shorter and not forbidden to cycle on (at least that is the way it is <a href="http://mijndev.openstreetmap.nl/~ligfietser/fiets/?map=cycleways&amp;zoom=14&amp;lat=38.80868&amp;lon=-90.33169&amp;layers=B00000TFFFFFFFFFFFFFFFT">mapped</a> there), they will always choose the fastest or shortest route to your destination.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '13, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-20516" class="comments-container">
<span id="20543"></span>
<div id="comment-20543" class="comment">
<div id="post-20543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>routeType=bicycle is supposed to prefer bike paths. I also tried adjusting the cyclingRoadFactor parameter and still could not get the API to return a path using the bike route. It seems like there must be something wrong with how I plotted the route.</p>
</div>
<div id="comment-20543-info" class="comment-info">
<span class="comment-age">(07 Mar '13, 01:26)</span> <span class="comment-user userinfo">JARinteractive</span>
</div>
</div>
<span id="20548"></span>
<div id="comment-20548" class="comment">
<div id="post-20548-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, the route is fine, as far as i can see (see <a href="http://mapq.st/YcfYma">http://mapq.st/YcfYma</a> ). Probably mapquest does not expose all the routing options through the free api.</p>
</div>
<div id="comment-20548-info" class="comment-info">
<span class="comment-age">(07 Mar '13, 08:06)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="20565"></span>
<div id="comment-20565" class="comment">
<div id="post-20565-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>MapQuest doesn't even show any of the path that I entered at this point. There was a small portion of the trail already in OSM, which is what is seen in your MapQuest link.</p>
</div>
<div id="comment-20565-info" class="comment-info">
<span class="comment-age">(07 Mar '13, 14:00)</span> <span class="comment-user userinfo">JARinteractive</span>
</div>
</div>
<span id="20566"></span>
<div id="comment-20566" class="comment">
<div id="post-20566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe you should have pointed us to the actual way IDs you are talking about.</p>
</div>
<div id="comment-20566-info" class="comment-info">
<span class="comment-age">(07 Mar '13, 14:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20516-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20567"></span>

<div id="answer-container-20567" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20567-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If MapQuest Open only routes along the earlier added Sunset Trail part but not along the recently added one than maybe their routing data still hasn't been updated. I can't find any information about the date of their routing data so I suggest to wait a few more weeks or try to contact them directly. MapQuest is a commercial company and we don't know very much about their internals.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '13, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20567" class="comments-container">
&#10;</div>
<div id="comment-tools-20567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20567-form-container" class="comment-form-container">
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

