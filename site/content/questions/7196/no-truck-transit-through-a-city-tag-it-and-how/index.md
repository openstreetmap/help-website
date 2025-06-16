+++
type = "question"
title = "No truck transit through a city - tag it, and how?"
description = '''Yesterday, while mapping, I came across signs on several major highways approaching a big city (Tbilisi, Georgia), which sais that Trucks on transit are not allowed to drive through the city - they are forced on the eastern bypass instead (which is in a bad state, but that is a different story). Bes...'''
date = "2011-08-19T09:19:00Z"
lastmod = "2011-08-26T12:37:00Z"
weight = 7196
keywords = [ "access", "truck" ]
aliases = [ "/questions/7196" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No truck transit through a city - tag it, and how?](/questions/7196/no-truck-transit-through-a-city-tag-it-and-how)

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
<span id="post-7196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7196-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Yesterday, while mapping, I came across signs on several major highways approaching a big city (Tbilisi, Georgia), which sais that Trucks on transit are not allowed to drive through the city - they are forced on the eastern bypass instead (which is in a bad state, but that is a different story). Besides, there are some bigger routes approaching the city from the west, that will not meet the bypass road - so trucks from there should go through the city, anyway.</p>
<p>It is meant to keep the long haul trucks from Turkey to Azerbaijan or Russia to Armenia out of the city, because the way through the city is much better and faster than the bypass road. Trucks from the smaller routes from the west are not so frequent, anyway.</p>
<p>Should I code it? And how? Making an access-restriction for trucks=destination on all links within the city is lots of work. Besides, it will make a conflict with other, smaller zones, e.g. neighbourhoods, where trucks are not allowed to pass through, if they exist. Is there some kind of easy way out, e.g. a zone coding? Or should I just ignore it for now?</p>
<p>Edit: I can offer a picture of this very sign now. <a href="http://www.facebook.com/media/set/?set=a.251069421593487.109530.100000712939258&amp;l=a7b33d4d84&amp;type=1">http://www.facebook.com/media/set/?set=a.251069421593487.109530.100000712939258&amp;l=a7b33d4d84&amp;type=1</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-truck" rel="tag" title="see questions tagged &#39;truck&#39;">truck</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '11, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Aug '11, 12:35</strong> </span></p>
</div>
</div>
<div id="comments-container-7196" class="comments-container">
&#10;</div>
<div id="comment-tools-7196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7196-form-container" class="comment-form-container">
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

<span id="7201"></span>

<div id="answer-container-7201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7201-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Everywhere you see a traffic sign access restriction, you should add it into OSM, even if it is a lot of work. Have a look in the <a href="https://wiki.openstreetmap.org/wiki/Access">access tags on the wiki</a>. You will see that trucks are tagged with the key "hgv". So, put the "hgv=destination" in all road sections you find this traffic sign.</p>
<p>If at the end, some links to the city remi for a truck, this is because the traffic sign is missing, it's not your fault. The data shall reflect the reality.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '11, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '11, 17:27</strong> </span></p>
</div>
</div>
<div id="comments-container-7201" class="comments-container">
<span id="7202"></span>
<div id="comment-7202" class="comment">
<div id="post-7202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>in that case I have to tag a whole 1,5 million inhabitant city with hgv=destination... I go with Chief Wiggum: "Let Michigan take care of it". :D</p>
</div>
<div id="comment-7202-info" class="comment-info">
<span class="comment-age">(19 Aug '11, 15:50)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="7203"></span>
<div id="comment-7203" class="comment">
<div id="post-7203-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You just have to tag the roads where this sign is on, not every road within the whole city.</p>
<p>Also, please don't add a new answer to your question. Use the comment button instead.</p>
</div>
<div id="comment-7203-info" class="comment-info">
<span class="comment-age">(19 Aug '11, 16:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="7204"></span>
<div id="comment-7204" class="comment not_top_scorer">
<div id="post-7204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see a problem here. This question is much more complicated than it seems.<br />
</p>
<p>I do not know how exactly the traffic signs look like, but from access=destination it is not clear what scope does it have. If you put it on the street where the sign is (segment between two junctions) it would mean you cannot drive to centre with supplies, which is obviously not the case here. From the little I know you can go through any individual street - it is transit through the whole city that is forbidden.<br />
</p>
<p>In this case not only the category of vehicle, but also its purpose is relevant...</p>
</div>
<div id="comment-7204-info" class="comment-info">
<span class="comment-age">(19 Aug '11, 17:03)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="7208"></span>
<div id="comment-7208" class="comment">
<div id="post-7208-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>hgv=designated on the official route around, hgv=destination (if they're allowed to get to a local address, or hgv=no if they're outright banned for all access).</p>
</div>
<div id="comment-7208-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 00:31)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="7213"></span>
<div id="comment-7213" class="comment not_top_scorer">
<div id="post-7213-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Paul</span>, that is what I mean... trucks are allowed to enter the entire city for accessing businesses and so on. Only transit is banned in the city. It would, as I see, require a hgv=destination in the entire metropolis to represent the reality and to have correct guidance by satnav.</p>
</div>
<div id="comment-7213-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 09:45)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="7214"></span>
<div id="comment-7214" class="comment not_top_scorer">
<div id="post-7214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sorry... is it possible for trucks, with your suggested coding, to access adresses in the city if only the first link is tagged hgv=destination?</p>
</div>
<div id="comment-7214-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 09:46)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="7215"></span>
<div id="comment-7215" class="comment">
<div id="post-7215-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Accessing points in the city is always possible with this tag as the name already suggests.</p>
</div>
<div id="comment-7215-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 10:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="7219"></span>
<div id="comment-7219" class="comment not_top_scorer">
<div id="post-7219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe I get it wrong... I was thinking, that the hgv=destination only allows trucks to reach a destination on this very link. Anything that is beyond, they cannot reach, because they must drive through this hgv=destination - zone. Or am I way off now?</p>
</div>
<div id="comment-7219-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 18:13)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="7224"></span>
<div id="comment-7224" class="comment">
<div id="post-7224-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think the destination tag says that you can use this way if there is no other possibility of reaching the destination. That is, either the destination is somewhere on this way or it isn't but using it is the only way to reach the destination at all.</p>
</div>
<div id="comment-7224-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 19:55)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="7250"></span>
<div id="comment-7250" class="comment not_top_scorer">
<div id="post-7250-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thank you all for the info. But there are lots of assumptions and speculations, no real hardcore info. But I appreciate it a lot! What I will do, is to tag the bypass road hgv=designated. the access-tag I will skip for the moment :)</p>
</div>
<div id="comment-7250-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 09:52)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="7271"></span>
<div id="comment-7271" class="comment not_top_scorer">
<div id="post-7271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Paul Johnson</span> : What would be the difference in tagging if transit is forbidden:<br />
a) Through the whole city (as in this case) b) Through a single street (Truck can get to shop that is in that street, not just pass through) c) Street from b) lies in city from a)</p>
</div>
<div id="comment-7271-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 21:17)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="7341"></span>
<div id="comment-7341" class="comment not_top_scorer">
<div id="post-7341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I now added a photo of the sign in my original question... So as you can see, the situation is quite tricky...</p>
<p>I thank you all for your help, and although still a newbie, I am pretty much into osm and enjoy it very much - both fieldworking and tagging :)</p>
<p>What I can do is tag the bypass road as hgv=designated. But for the hgv=destination, I keep my hands off for the moment, if you allow me ;)</p>
</div>
<div id="comment-7341-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 12:37)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-7201" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-7201-form-container" class="comment-form-container">
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

