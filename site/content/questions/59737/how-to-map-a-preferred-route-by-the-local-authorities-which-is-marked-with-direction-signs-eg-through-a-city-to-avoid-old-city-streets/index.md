+++
type = "question"
title = "how to map a preferred route by the local authorities which is marked with direction signs e.g. through a city to avoid old city streets"
description = '''I am not sure if I found a good title for my question, that&#x27;s why it became so long. Please excuse both. (Anyone with a good short expression about what I mean?) Certainly a plot describes it better: Imagine a city with a lot of streets and especially many possibilities to go from A to B and C and D...'''
date = "2017-09-21T08:19:00Z"
lastmod = "2017-09-23T15:54:00Z"
weight = 59737
keywords = [ "directions", "signs", "durchfahrt", "mapping", "routing" ]
aliases = [ "/questions/59737" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to map a preferred route by the local authorities which is marked with direction signs e.g. through a city to avoid old city streets](/questions/59737/how-to-map-a-preferred-route-by-the-local-authorities-which-is-marked-with-direction-signs-eg-through-a-city-to-avoid-old-city-streets)

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
<span id="post-59737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59737-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-59737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am not sure if I found a good title for my question, that's why it became so long. Please excuse both. (Anyone with a good short expression about what I mean?)</p>
<p>Certainly a plot describes it better: Imagine a city with a lot of streets and especially many possibilities to go from A to B and C and D etc. You come from the south and want to cross the city to the north. As the city has a nice little old part in the middle, the local authorities want drivers who only cross the city to drives along some streets in the east of the city. They have thus installed a series of direction signs to guide you respectively. But you would also have the chance to pass through the old city, it would even be better in terms of travel time, since the streets are also broad and without anything slowing you down. Still the signs tell differently and the authorities and the population don't want you to.</p>
<p>How can these direction signs respectively their preference for a route be mapped? Of course primarily to give routing applications the chance and "instruct" them to route according to the signs and target of the local authorities. But not only for the routers (I know we don't map only for the map and certainly not only for the routers ;-)), as the signs also are a part of the reality the exists and should be mapped from my point of view. Any relation to create a route for such? Or something else?</p>
<p>The routing applications will surely calculate on the type of streets and maxspeed, etc. And they don't have any other chance if they don't know about the signs.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-signs" rel="tag" title="see questions tagged &#39;signs&#39;">signs</span> <span class="post-tag tag-link-durchfahrt" rel="tag" title="see questions tagged &#39;durchfahrt&#39;">durchfahrt</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '17, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/123f4fd2a676d8b3d454fc0e6457782a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geohobbes&#39;s gravatar image" />
<p><span>geohobbes</span><br />
<span class="score" title="166 reputation points">166</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geohobbes has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-59737" class="comments-container">
<span id="59739"></span>
<div id="comment-59739" class="comment">
<div id="post-59739-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you looking for the <a href="https://wiki.openstreetmap.org/wiki/Key:destination">destination</a> key?</p>
</div>
<div id="comment-59739-info" class="comment-info">
<span class="comment-age">(21 Sep '17, 08:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="59743"></span>
<div id="comment-59743" class="comment">
<div id="post-59743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing me at this key, which I was not aware of yet! It solves the mapping of the signs, definitely. But as far as I understood, it will not help the routing applications / navigation systems to guide us along these signs. So I would still be interested in how to achieve that.</p>
</div>
<div id="comment-59743-info" class="comment-info">
<span class="comment-age">(21 Sep '17, 14:41)</span> <span class="comment-user userinfo">geohobbes</span>
</div>
</div>
<span id="59749"></span>
<div id="comment-59749" class="comment">
<div id="post-59749-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Technically routers could use the destination key during route calculation. However this will make route calculations (much) more expensive. You will have to determine the cities along the route, i.e. perform regular geocoding. And you will have to calculate the route somehow backwards in order to know which cities you are going to drive through.</p>
</div>
<div id="comment-59749-info" class="comment-info">
<span class="comment-age">(21 Sep '17, 15:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="59772"></span>
<div id="comment-59772" class="comment">
<div id="post-59772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree. That's also why I think some sort of relation would be better for the intention, as in my comment to rorym below. And I think it would even be beneficial for the routers to make calculations less expensive. Instead of that they need to calculate a route through the city themselves, they could first look for an existing relation of that kind and use it, if it exists. I guess the lookup would not be much overhead (would it?) and the benefit would be big, no?</p>
</div>
<div id="comment-59772-info" class="comment-info">
<span class="comment-age">(22 Sep '17, 13:45)</span> <span class="comment-user userinfo">geohobbes</span>
</div>
</div>
<span id="59776"></span>
<div id="comment-59776" class="comment">
<div id="post-59776-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This would require to create relations for all kinds of possible routes. This is not feasible and not maintainable. User rorym already explained why these relations are usually not needed. There might be edge-cases of course, as there always will be.</p>
</div>
<div id="comment-59776-info" class="comment-info">
<span class="comment-age">(22 Sep '17, 14:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="59799"></span>
<div id="comment-59799" class="comment not_top_scorer">
<div id="post-59799-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Routers may go around if the authorities have set the speed restrictions low enough, and we map them!</p>
</div>
<div id="comment-59799-info" class="comment-info">
<span class="comment-age">(23 Sep '17, 15:54)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-59737" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-59737-form-container" class="comment-form-container">
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

<span id="59740"></span>

<div id="answer-container-59740" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59740-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-59740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think there is a relation for that. Usually, in my experience, the outer "ring road" will be a higher road classification than the inner part. There are other ways to map things which routers can use to figure out that they should not route through the middle. I presume the speed limits in the middle will be lower. There will probably also be more traffic lights, pedestrian crossings, and yield/give way junctions. Routers use this sort of data to guess at how fast a route is (lots of traffic lights makes things slower).</p>
<p>You could also map the width of the roads (although that's hard and I don't think any software uses that). Mapping the <a href="https://wiki.openstreetmap.org/wiki/Key:lanes">number of lanes</a> might help the router to figure out what is the 2 lane ring road and which is the 1 lane inner city road. You can also map <a href="https://wiki.openstreetmap.org/wiki/Key:destination">what the destination of the lane is</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '17, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-59740" class="comments-container">
<span id="59746"></span>
<div id="comment-59746" class="comment">
<div id="post-59746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a pity, if there is no possibility. Sure, you are right about all the possibilities by which the routers might decide to take the preferred route. My example is certainly a little over-exaggerated to neglect all difference, as I wanted to make clear what I mean. But I definitely had the case quite some times that the router chose wrongly and in which I was quite sure that it was due to pretty similar road conditions regarding what you mentioned. So I think it would be beneficial for OSM completeness and a being better data source than others, for the local people and for the navigated users, if anything would exist that would offer the possibility. Aren't hiking routing applications using the approach that I am think of, if they chose parts / legs of specified hiking routes in OSM data, instead of the shortest way? Some sort of "direction route relation" or "through traffic relation" or "transit traffic relation" could be used as an offer for routers / navigation systems, to route the users exactly how the signs tell them, what do you think?</p>
</div>
<div id="comment-59746-info" class="comment-info">
<span class="comment-age">(21 Sep '17, 15:03)</span> <span class="comment-user userinfo">geohobbes</span>
</div>
</div>
</div>
<div id="comment-tools-59740" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59740-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59777"></span>

<div id="answer-container-59777" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59777-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In most countries, the roads around the edge of the city would have a higher class (say, <code>highway=primary</code>) and those in the centre of the city a lower class (<code>highway=unclassified</code> or <code>highway=residential</code>). The <code>highway=</code> tag indicates a road's importance in the connected highway network.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '17, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-59777" class="comments-container">
&#10;</div>
<div id="comment-tools-59777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59777-form-container" class="comment-form-container">
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

