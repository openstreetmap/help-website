+++
type = "question"
title = "How to get the start and the endpoint of a route"
description = '''I&#x27;m messing around with OpenStreetMap and Overpass. Now I want to get information about routes. For example the ferry from Krabi to Railey East. It looks perfect on the map. The dotted ferry line goes from the harbor of Krabi to the harbor of Railey East. But when I click the route, only half lights...'''
date = "2016-07-20T23:47:00Z"
lastmod = "2016-08-02T22:14:00Z"
weight = 51006
keywords = [ "overpass", "route", "relations", "ferry" ]
aliases = [ "/questions/51006" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the start and the endpoint of a route](/questions/51006/how-to-get-the-start-and-the-endpoint-of-a-route)

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
<span id="post-51006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51006-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm messing around with OpenStreetMap and Overpass.</p>
<p>Now I want to get information about routes. For example the ferry from Krabi to Railey East. It looks perfect on the map. The dotted ferry line goes from the harbor of Krabi to the harbor of Railey East. But when I click the route, only half lights up. Of course it makes sense. It connects to the other route.</p>
<p><strong>But how do I extract the whole route. How can I programmatic discover the start and the end point of a route?</strong></p>
<p>OSM data layer screenshot with highlighted area: <img src="/upfiles/route_extraction.png" alt="screenshot" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-ferry" rel="tag" title="see questions tagged &#39;ferry&#39;">ferry</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '16, 23:47</strong></p>
<img src="https://secure.gravatar.com/avatar/cbcec43f8f6c9d5b869aa5bdc56eb673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NLAnaconda&#39;s gravatar image" />
<p><span>NLAnaconda</span><br />
<span class="score" title="166 reputation points">166</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NLAnaconda has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '16, 21:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-51006" class="comments-container">
<span id="51098"></span>
<div id="comment-51098" class="comment">
<div id="post-51098-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>cross-posted: <a href="https://stackoverflow.com/questions/38579137/osm-how-to-get-the-start-and-the-endpoint-of-a-route">https://stackoverflow.com/questions/38579137/osm-how-to-get-the-start-and-the-endpoint-of-a-route</a></p>
</div>
<div id="comment-51098-info" class="comment-info">
<span class="comment-age">(26 Jul '16, 07:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51216"></span>
<div id="comment-51216" class="comment">
<div id="post-51216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>when you say "Overpass" you likely mean (at least for the "click" part) <span>Overpass API</span>'s interface "<span>Overpass Turbo</span>".</p>
</div>
<div id="comment-51216-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 21:17)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="51217"></span>
<div id="comment-51217" class="comment">
<div id="post-51217-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I do. :)</p>
</div>
<div id="comment-51217-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 21:19)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
<span id="51218"></span>
<div id="comment-51218" class="comment">
<div id="post-51218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not know which specific ferry route you are talking about. Could you please provide the OSM object id/link or at least location?</p>
</div>
<div id="comment-51218-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 21:23)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="51220"></span>
<div id="comment-51220" class="comment">
<div id="post-51220-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is this route: <a href="http://www.openstreetmap.org/way/130768455">http://www.openstreetmap.org/way/130768455</a> Actually what I want to achieve is to know what destinations can be reached from a harbor (in this case: <span>node 2465989873</span>)</p>
</div>
<div id="comment-51220-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 21:27)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
<span id="51221"></span>
<div id="comment-51221" class="comment not_top_scorer">
<div id="post-51221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: In general, please do not post your questions to several places. That wastes help resources. If you really need to (for whatever reason), please always mentioning it in each post and provide links to the other posts. Once you've got an answer at one place, update all the other places.</p>
</div>
<div id="comment-51221-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 21:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51006" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-51006-form-container" class="comment-form-container">
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

<span id="51219"></span>

<div id="answer-container-51219" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51219-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See our <span>documentation wiki about Tag:route=ferry</span> "connect each end of the ferry route to a way on land". So you should be able to</p>
<ul>
<li>(if it is a <span>relation</span>) look at the relation's first and last member and the node of each member which is not a part of another member of the relation should be the start and end.</li>
<li>(if it is a <span>way</span>) look at the way's first and last node – that should be the start and end.</li>
</ul>
<p>However, the wiki is no law book, and things may have been mapped differently in reality.</p>
<p>So, in your <em>example case</em> <span>way 130768455</span>: this is not a mapping which is like the documentation describes. The western end is in the sea at an Y point. Here you would need to find other ways sharing the same end node and continue your imaginary travel through them (routing algorithms if you search a short travel).</p>
<p>To find locations which can be reaches from <span>node 2465989873</span> you would need to look which ways or relations with route=ferry tags the node is a member of and then find your way until (routing algorithms if you search a short one) you reach land (different for ways or relations and different depending if routes have been mapped not land-to-land – as said before).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '16, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '16, 21:47</strong> </span></p>
</div>
</div>
<div id="comments-container-51219" class="comments-container">
<span id="51222"></span>
<div id="comment-51222" class="comment">
<div id="post-51222-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing me in the right direction!</p>
</div>
<div id="comment-51222-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 22:12)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
<span id="51223"></span>
<div id="comment-51223" class="comment">
<div id="post-51223-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11351/nlanaconda"></a><a href="http://help.openstreetmap.org/users/11351/nlanaconda">@NLAnaconda</a>: thanks for the feedback! :-) Glad to help.</p>
</div>
<div id="comment-51223-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 22:14)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51219-form-container" class="comment-form-container">
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

