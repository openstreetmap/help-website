+++
type = "question"
title = "Routing software cannot find a route accross a border post (Sahara)"
description = '''I have been looking into why OpenStreetMap based routing software cannot find a route from the N1 to the N5 across the no mans land border post in the South of Western Sahara. I signed up as an OpenStreetMap user and used the web editing software to identify exactly where it goes wrong and it appear...'''
date = "2015-02-08T11:35:00Z"
lastmod = "2015-02-09T21:19:00Z"
weight = 40858
keywords = [ "border", "mapfactor", "newbie", "routing" ]
aliases = [ "/questions/40858" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Routing software cannot find a route accross a border post (Sahara)](/questions/40858/routing-software-cannot-find-a-route-accross-a-border-post-sahara)

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
<span id="post-40858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40858-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been looking into why OpenStreetMap based routing software cannot find a route from the N1 to the N5 across the no mans land border post in the South of Western Sahara. I signed up as an OpenStreetMap user and used the web editing software to identify exactly where it goes wrong and it appears to be the border post at the Northern end of no mans land. No route can be found from the N1 to the track through the border post.</p>
<p>I have never edited OSM data before and would like help/guidance in identifying the exact cause and applying a fix.</p>
<p>Thanks John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-border" rel="tag" title="see questions tagged &#39;border&#39;">border</span> <span class="post-tag tag-link-mapfactor" rel="tag" title="see questions tagged &#39;mapfactor&#39;">mapfactor</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '15, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/180199b9cea32bfe5acf5f2d3dfdeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrBassMan&#39;s gravatar image" />
<p><span>MrBassMan</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrBassMan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '15, 19:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-40858" class="comments-container">
<span id="40859"></span>
<div id="comment-40859" class="comment">
<div id="post-40859-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Hi John, welcome! Do you mean this location shown there <a href="http://osrm.at/aUj">OSRM</a>/<span>graphopper</span>/<span>the "track" between the border controls on osm.org</span>?</p>
<p>In fact, this <em>seems</em> to be tagged not correct for a connection between two border controls. This <em>may</em> be why your OSM-based routing software (which?) could not find this route: because you may have set it up to not route over "tracks" (small roads for agricultural use). Or your software avoid borders …</p>
</div>
<div id="comment-40859-info" class="comment-info">
<span class="comment-age">(08 Feb '15, 11:48)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40860"></span>
<div id="comment-40860" class="comment">
<div id="post-40860-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>slightly off topic: just while we are at it, country borders at this country generate interesting results in routing: <a href="http://osrm.at/aUk">rather takes the ferry out and back again</a>, <a href="https://graphhopper.com/maps/?point=35.106428%2C-2.254944&amp;point=35.070469%2C-2.128601&amp;layer=OpenStreetMap">found a whatever track</a>. I do not know how reality is there.</p>
</div>
<div id="comment-40860-info" class="comment-info">
<span class="comment-age">(08 Feb '15, 11:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40862"></span>
<div id="comment-40862" class="comment">
<div id="post-40862-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes thats the place. Using navigator 14 trying to route down West africa. Yes i am using bycycle mode on that which should use tracks. I can route song a start point on the track just south of the border post but not route if the start is before the payout and end after. Its as if there is a gap in the road at the border. Help please.</p>
</div>
<div id="comment-40862-info" class="comment-info">
<span class="comment-age">(08 Feb '15, 19:56)</span> <span class="comment-user userinfo">MrBassMan</span>
</div>
</div>
<span id="40867"></span>
<div id="comment-40867" class="comment">
<div id="post-40867-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just for reference: Who is the manufacturer of the software? The name is very unspecific.</p>
</div>
<div id="comment-40867-info" class="comment-info">
<span class="comment-age">(08 Feb '15, 22:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40870"></span>
<div id="comment-40870" class="comment">
<div id="post-40870-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes Mapfactor Navigator 14 - using their latest map data which is updated regularly.</p>
</div>
<div id="comment-40870-info" class="comment-info">
<span class="comment-age">(09 Feb '15, 02:38)</span> <span class="comment-user userinfo">MrBassMan</span>
</div>
</div>
</div>
<div id="comment-tools-40858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40858-form-container" class="comment-form-container">
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

<span id="40866"></span>

<div id="answer-container-40866" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40866-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With those two routing engines <a href="http://osrm.at/aUj">OSRM</a>/<span>graphopper</span> I see no problem. Both usually have very current data (not older than a week). Please could you have a look if your data is <em>up to date</em>? However, the last edit there is from 2014-11-06 and it did not change anything which would be relevant here, if I <a href="https://overpass-api.de/achavi/?changeset=26588536">see</a> correctly. I now have checked with <a href="http://www.yournavigation.org/?flat=21.379144229378&amp;flon=-16.959609984473&amp;tlat=21.321267420071&amp;tlon=-16.943817137793">yournavigation</a> (select bicycle and click "find route"): also no problem, even with its data being from 2014-09-02.</p>
<p>I see no connection problem in our data at the <span>northern border control</span> (you mean this one, don't you?): it is the connection between the "unclassified" road towards the north and the track towards the south.</p>
<p>Other options would be that it does not send you over tracks with <em>special settings</em> (which <span>this track</span> here has currently – you can click them on the linked way page for explanations):</p>
<ul>
<li><code>access=permissive</code></li>
<li><code>smoothness=horrible</code></li>
<li><code>surface=sand</code></li>
</ul>
<p>Or your software simply avoid to cross <em>borders</em>. Please check at other border controls.</p>
<p>Or your software has maps cut into <em>separated</em> countries and cannot route between different countries.</p>
<p>Of course it could just be a software <em>bug</em>. Ask the application developers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '15, 22:23</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '15, 22:35</strong> </span></p>
</div>
</div>
<div id="comments-container-40866" class="comments-container">
<span id="40871"></span>
<div id="comment-40871" class="comment">
<div id="post-40871-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Border crossing is supported by the software.</p>
<p>Routing across countries is fine normally with Mapfactor Navigator</p>
<p>Software bug - I have raised the issue on their forums as well <a href="http://forum.mapfactor.com/discussion/6324/western-sahara-border-routing-using-osm-data">http://forum.mapfactor.com/discussion/6324/western-sahara-border-routing-using-osm-data</a></p>
</div>
<div id="comment-40871-info" class="comment-info">
<span class="comment-age">(09 Feb '15, 02:40)</span> <span class="comment-user userinfo">MrBassMan</span>
</div>
</div>
<span id="40883"></span>
<div id="comment-40883" class="comment">
<div id="post-40883-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>note that the <span>"borked N1 at border"</span> was likely not a routing problem (<span>previous data state – I have dragged the bottom node a bit more to the right to make the connections better visible</span>), it as just like an intersection.</p>
</div>
<div id="comment-40883-info" class="comment-info">
<span class="comment-age">(09 Feb '15, 12:55)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40895"></span>
<div id="comment-40895" class="comment">
<div id="post-40895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also don't think that my change fixed the routing problem. Nevertheless the back and forth was an error that had to be fixed.</p>
</div>
<div id="comment-40895-info" class="comment-info">
<span class="comment-age">(09 Feb '15, 19:40)</span> <span class="comment-user userinfo">Jojo4u</span>
</div>
</div>
<span id="40902"></span>
<div id="comment-40902" class="comment">
<div id="post-40902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10452/jojo4u">@jojo4u</a>: ah, okay, I misunderstood you then, thanks Yes, of course, that zig-zag likely was wrong.</p>
</div>
<div id="comment-40902-info" class="comment-info">
<span class="comment-age">(09 Feb '15, 21:19)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40866-form-container" class="comment-form-container">
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

