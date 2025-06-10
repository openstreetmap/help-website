+++
type = "question"
title = "Bridge highway=motorway classification"
description = '''There seems to have been a certain number of edit wars over the classification of various major bridges in New York City. One of the main criteria for what is a highway=motorway is that it has no intersection controls on the main roadway (such as traffic-signals, rotaries and roundabouts, and stop s...'''
date = "2021-02-26T19:12:00Z"
lastmod = "2021-02-28T04:37:00Z"
weight = 79044
keywords = [ "motorway", "bridge", "classification", "trunk" ]
aliases = [ "/questions/79044" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bridge highway=motorway classification](/questions/79044/bridge-highwaymotorway-classification)

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
<span id="post-79044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79044-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There seems to have been a certain number of edit wars over the classification of various major bridges in New York City.</p>
<p>One of the main criteria for what is a <code>highway=motorway</code> is that it has no intersection controls on the main roadway (such as traffic-signals, rotaries and roundabouts, and stop signs or stop markings). Bridges usually don't have intersections, so that is not useful here. The other two, limited access and roadway separation apply to most of the bridges.</p>
<p>Another important factor is that <code>highway=</code> tags should apply where reasonable to the whole road, not just a segment of it. Many of these bridges were built to carry a major street, but when highways (<code>highway=motorway</code>s) were built later ramps were added only where convenient, resulting in incomplete interchanges with them. Whether the bridges are considered an extension of the highway or the major street might factor in.</p>
<p>I'm hoping we can come up with a reasonable set of criteria for what <code>highway=</code> tag bridges like these should have. Don't worry about what commercial maps have these classified as, they also have a mess.</p>
<p>In the below table I've catalogued some area bridges with varying characteristics. The Carries column gives the street the bridge was built to carry, and its classification. The <code>highway=motorway_link</code> column counts the number of directions on the bridge that can be entered/exited (each counting 1) from a <code>highway=motorway</code>. This ignores that not all lanes/roadways go to all exits or all directions on the connecting motorway etc. Vehicles only is whether bicycles and limited-use motorcycles are banned from the main roadway as indicated by signage.</p>
<table>
<tbody>
<tr>
<th>Bridge</th>
<th>Carries</th>
<th>motorway_link</th>
<th>Separate roadways</th>
<th>Pedestrian separation</th>
<th>Vehicles only</th>
<th>Present tagging</th>
</tr>
&#10;<tr>
<td><a href="https://en.wikipedia.org/wiki/Brooklyn_Bridge">Brooklyn Bridge</a></td>
<td>highway=primary Adams St</td>
<td>3/4</td>
<td>Separate</td>
<td>Separate</td>
<td>Yes</td>
<td><a href="http://osm.mapki.com/history/way.php?id=432550255">highway=trunk</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/Manhattan_Bridge">Manhattan Bridge</a></td>
<td>highway=primary Flatbush Ave Ext</td>
<td>1/4</td>
<td>Separate</td>
<td>Separate</td>
<td>Yes</td>
<td><a href="http://osm.mapki.com/history/way.php?id=46189305">highway=trunk</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/Williamsburg_Bridge">Williamsburg Bridge</a></td>
<td>highway=primary Delancey St</td>
<td>2/4</td>
<td>Separate</td>
<td>Separate</td>
<td>Yes</td>
<td><a href="http://osm.mapki.com/history/way.php?id=40337615">highway=motorway</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/Queensboro_Bridge">Queensboro Bridge</a></td>
<td>highway=primary NY 25/NY 25A</td>
<td>0/4</td>
<td>Separate</td>
<td>Separate</td>
<td>Yes</td>
<td><a href="http://osm.mapki.com/history/way.php?id=198924625">highway=motorway</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/Triborough_Bridge#Harlem_River_lift_bridge_(NY_900G)">Triboro Bridge (Manhattan span)</a></td>
<td>highway=motorway NY 900G (unsigned)</td>
<td>4/4</td>
<td>Separate</td>
<td>Barrier</td>
<td>Yes</td>
<td><a href="http://osm.mapki.com/history/way.php?id=5669174">highway=motorway</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/Willis_Avenue_Bridge">Willis Ave Bridge</a></td>
<td>highway=primary Willis Ave</td>
<td>2/2</td>
<td>One-way</td>
<td>Barrier</td>
<td>No</td>
<td><a href="http://osm.mapki.com/history/way.php?id=5670524">highway=primary</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/145th_Street_Bridge">145th St Bridge</a></td>
<td>highway=secondary 145th St</td>
<td>0/4</td>
<td>No</td>
<td>Curb</td>
<td>No</td>
<td><a href="http://osm.mapki.com/history/way.php?id=5670765">highway=secondary</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/Washington_Bridge">Washington Bridge</a></td>
<td>highway=secondary 181st St</td>
<td>4/4</td>
<td>Median</td>
<td>Barrier</td>
<td>No</td>
<td><a href="http://osm.mapki.com/history/way.php?id=33117565">highway=motorway</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/University_Heights_Bridge">University Heights Bridge</a></td>
<td>highway=primary Fordham Rd</td>
<td>0/4</td>
<td>No</td>
<td>Barrier</td>
<td>No</td>
<td><a href="http://osm.mapki.com/history/way.php?id=19174360">highway=primary</a></td>
</tr>
<tr>
<td><a href="https://en.wikipedia.org/wiki/Broadway_Bridge_(Manhattan)">Broadway Bridge</a></td>
<td>highway=primary US 9</td>
<td>0/4</td>
<td>Median</td>
<td>Curb</td>
<td>No</td>
<td><a href="http://osm.mapki.com/history/way.php?id=126140593">highway=primary</a></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-motorway" rel="tag" title="see questions tagged &#39;motorway&#39;">motorway</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-classification" rel="tag" title="see questions tagged &#39;classification&#39;">classification</span> <span class="post-tag tag-link-trunk" rel="tag" title="see questions tagged &#39;trunk&#39;">trunk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '21, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/5833f68b9cfce6017187678c495b6fc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdejean&#39;s gravatar image" />
<p><span>mdejean</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdejean has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '21, 18:54</strong> </span></p>
</div>
</div>
<div id="comments-container-79044" class="comments-container">
<span id="79045"></span>
<div id="comment-79045" class="comment">
<div id="post-79045-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just for info - you can link to how these objects have changed over time by linking to (for one lane of the Williamsburg Bridge for example) <a href="http://osm.mapki.com/history/way.php?id=40337615">http://osm.mapki.com/history/way.php?id=40337615</a> .</p>
</div>
<div id="comment-79045-info" class="comment-info">
<span class="comment-age">(26 Feb '21, 19:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="79046"></span>
<div id="comment-79046" class="comment">
<div id="post-79046-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> thanks, I've added those links to the last column of the table.</p>
</div>
<div id="comment-79046-info" class="comment-info">
<span class="comment-age">(26 Feb '21, 20:51)</span> <span class="comment-user userinfo">mdejean</span>
</div>
</div>
<span id="79052"></span>
<div id="comment-79052" class="comment">
<div id="post-79052-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's troublesome because there are no legal designation, unlike the origin in UK Motorway. This is more suitable for discussion in forum and elsewhere, than an Q&amp;A format.</p>
<p>You should mention the end connections as well. For example, the Triborough Bridge can be considered as a natural extension of I-278 connecting with FDR Drive, which would strongly be <code>=motorway</code>.</p>
<p>Personally, you should term the "limited-access" as restricted vehicle categories directly. Fundamentally, bridges usually have no driveways, making them "limited-access" already.</p>
</div>
<div id="comment-79052-info" class="comment-info">
<span class="comment-age">(27 Feb '21, 12:21)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="79058"></span>
<div id="comment-79058" class="comment">
<div id="post-79058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For many years, the vehicular ways of the Brooklyn Bridge were tagged as <strong>motorway,</strong> and those on the Manhattan Bridge as <strong>primary</strong>. In 2018 the Manhattan was upgraded to <strong>motorway</strong> to match the Brooklyn. This doesn't seem too offbase, since these two bridges are reasonably similar in nature.</p>
<p>Last year the infamous Fluffy89502 changed them both to <strong>primary</strong> as part of a large brutal re-classification campaign. That's certainly too minor a class, but I felt Fluffy did have a point that <strong>motorway</strong> was perhaps overselling them a bit. So I settled on <strong>trunk</strong> for both of them, based on the wiki's description of "limited access but not high speed."</p>
<p>I haven't given much attention to the other bridges or tunnels, but offhand I doubt that there is a single classification that would accurately describe all the bridges into Manhattan, since some of them directly connect to expressways and some connect surface streets.</p>
</div>
<div id="comment-79058-info" class="comment-info">
<span class="comment-age">(27 Feb '21, 14:31)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="79064"></span>
<div id="comment-79064" class="comment">
<div id="post-79064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That really is quite a nice table.</p>
<p>After a bit of staring at the table, the map, and aerial imagery, I've begun to feel that perhaps the non-GWB Washington Bridge, the Williamsburg, and the Queensboro should be demoted to <strong>trunk</strong>. (Maybe even the Lincoln Tunnel and all of NJ-495, but I guess that's another topic.)</p>
<p>It would be working backwards of course, but I could invent a formula based on this table that would support that demotion. The simplest might to be to tally one point for every motorway link, plus one point for "vehicles only." A score &lt; 5 means the bridge keeps the classification of the "carries" street, 5-8 merits <strong>trunk</strong>, and &gt; 8 merits <strong>motorway</strong>. (Obviously this formula is almost completely arbitrary.)</p>
<p>I don't think any such formula should be binding, but it's interesting to take a look at the outliers.</p>
</div>
<div id="comment-79064-info" class="comment-info">
<span class="comment-age">(27 Feb '21, 22:08)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="79065"></span>
<div id="comment-79065" class="comment not_top_scorer">
<div id="post-79065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a>. I've changed that column name. I've also sent this to the <code>tagging</code> mailing list now, which is maybe a better place to discuss it.</p>
</div>
<div id="comment-79065-info" class="comment-info">
<span class="comment-age">(27 Feb '21, 23:05)</span> <span class="comment-user userinfo">mdejean</span>
</div>
</div>
</div>
<div id="comment-tools-79044" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-79044-form-container" class="comment-form-container">
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

<span id="79066"></span>

<div id="answer-container-79066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79066-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In a conflict, particularly with primary, trunk and motorway tagging, I strongly recommend giving consideration to the lower value in the range that people are talking about. I don't believe every Interstate segment qualifies for motorway, though one-off and extremely extenuating circumstances can give an exception (like the traffic light for the Interstate Drawbridge on I 5). However, I don't think all of I 5 should be a motorway; north of Blaine City Center in Washington and south of I 8 in California is a pretty good case for a trunk since it's basically a freeway but there's pedestrians at both ends and on the Canadian end there's also a bicycle lane that moves from the right to the left side of the roadway, multiple traffic lights, at grade intersections and a big park with people often playing frisbee over the roadway.</p>
<p>I've got zero experience with the bridges in question, though. But there really should be a hesitancy to tag things as motorway when they don't operate like one. Often Trunk or Primary is a better value even if their network or official classification is higher.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '21, 04:37</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '21, 04:39</strong> </span></p>
</div>
</div>
<div id="comments-container-79066" class="comments-container">
&#10;</div>
<div id="comment-tools-79066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79066-form-container" class="comment-form-container">
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

