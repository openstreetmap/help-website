+++
type = "question"
title = "Not sure how to fix bridge mapping for side street"
description = '''Greetings, Fairly new to OSM and I found a bug that I don&#x27;t quite know how to fix. I have been reading about the different ways of mapping a bridge, but I don&#x27;t see what is wrong. Here is the issue: http://www.openstreetmap.org/#map=17/38.93105/-94.64582 Lets say you are leaving Roe Avenue to go wes...'''
date = "2015-09-19T18:34:00Z"
lastmod = "2015-09-20T15:41:00Z"
weight = 45401
keywords = [ "bridge", "routing", "bug" ]
aliases = [ "/questions/45401" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not sure how to fix bridge mapping for side street](/questions/45401/not-sure-how-to-fix-bridge-mapping-for-side-street)

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
<span id="post-45401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45401-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings,</p>
<p>Fairly new to OSM and I found a bug that I don't quite know how to fix. I have been reading about the different ways of mapping a bridge, but I don't see what is wrong.</p>
<p>Here is the issue: <a href="http://www.openstreetmap.org/#map=17/38.93105/-94.64582">http://www.openstreetmap.org/#map=17/38.93105/-94.64582</a></p>
<p>Lets say you are leaving Roe Avenue to go west bound on 435. There is a on-ramp that has a divider between the on-ramp and the highway; This is the northern most highway traveling west bound on the map. That on ramp is shown correctly on the map that it goes under Nall Avenue then merges.</p>
<p>However, if using the route calculation it /really/ wants you to exit at Nall, sit at the light, then merge back onto the on-ramp before merging onto 435.</p>
<p>It is like it doesn't see and or recognize that instead of taking the right exit, you can (and should!) go straight under the bridge.</p>
<p>I poked around at the map and looked at the documentation, but I completly fail to see why this exit is an issue.</p>
<p>Can anyone provide any feedback on the issue and how to fix it?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '15, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/3ba5c35d5f9cd72422c5a37a5c3cce99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StackKorora&#39;s gravatar image" />
<p><span>StackKorora</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StackKorora has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45401" class="comments-container">
<span id="45402"></span>
<div id="comment-45402" class="comment">
<div id="post-45402-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A screenshot + sketch would be nice to see what routing you try to avoid :-/</p>
</div>
<div id="comment-45402-info" class="comment-info">
<span class="comment-age">(19 Sep '15, 19:55)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="45411"></span>
<div id="comment-45411" class="comment">
<div id="post-45411-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/upfiles/OSMScreenshot.png">Sure!</a> Hope this helps.</p>
<p>Red is the path it takes me (Off the highway, to a light, then back on the highway). Green is the path it should take me.</p>
<p>Thanks!</p>
</div>
<div id="comment-45411-info" class="comment-info">
<span class="comment-age">(20 Sep '15, 04:23)</span> <span class="comment-user userinfo">StackKorora</span>
</div>
</div>
<span id="45412"></span>
<div id="comment-45412" class="comment">
<div id="post-45412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The route seems to be correct on the <a href="http://map.project-osrm.org/?hl=en&amp;loc=38.939358,-94.705307&amp;loc=38.935165,-94.728989&amp;z=15&amp;center=38.937259,-94.721545&amp;alt=0&amp;df=0&amp;re=0&amp;ly=-1171809665">osrm website</a>, perhaps the data was changed recently ?</p>
</div>
<div id="comment-45412-info" class="comment-info">
<span class="comment-age">(20 Sep '15, 06:17)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="45415"></span>
<div id="comment-45415" class="comment">
<div id="post-45415-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5390/escada"></a><a href="http://help.openstreetmap.org/users/5390/escada">@escada</a>: That's a different location, isn't it? <a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=38.93251%2C-94.64314%3B38.93097%2C-94.65697#map=17/38.93177/-94.65006">Here</a> is the one from the screenshot and the route seems fine. So the issue is not the data.</p>
<p><a href="http://help.openstreetmap.org/users/11490/stackkorora"></a><a href="http://help.openstreetmap.org/users/11490/stackkorora">@StackKorora</a>: Which "route calculation" are you talking about? The OSM website? A specific app or device?</p>
</div>
<div id="comment-45415-info" class="comment-info">
<span class="comment-age">(20 Sep '15, 09:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45417"></span>
<div id="comment-45417" class="comment not_top_scorer">
<div id="post-45417-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a>, you're right, ti should have been <a href="http://osrm.at/ftE">this</a>. I tried a few in the area and copied the wrong one, sorry</p>
</div>
<div id="comment-45417-info" class="comment-info">
<span class="comment-age">(20 Sep '15, 14:43)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="45418"></span>
<div id="comment-45418" class="comment">
<div id="post-45418-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you both for looking at this. I am glad in knowing that I wasn't crazy thinking it was correct. :-)</p>
<p>The App I use is OSMAnd from f-droid: <a href="https://f-droid.org/wiki/page/net.osmand.plus">https://f-droid.org/wiki/page/net.osmand.plus</a></p>
<p>It has route calcuation in it. I just checked and I am updated on both the app and the map.</p>
<p>It seems this may not be an OSM issue but perhaps a OSMAnd app issue?</p>
<p>Thank you again!</p>
</div>
<div id="comment-45418-info" class="comment-info">
<span class="comment-age">(20 Sep '15, 15:12)</span> <span class="comment-user userinfo">StackKorora</span>
</div>
</div>
<span id="45419"></span>
<div id="comment-45419" class="comment not_top_scorer">
<div id="post-45419-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it seems to be an issue of OSMAnd itself. There haven't been any recent edits on this roads so I guess it has the same data as other routers.</p>
</div>
<div id="comment-45419-info" class="comment-info">
<span class="comment-age">(20 Sep '15, 15:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45401" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-45401-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

