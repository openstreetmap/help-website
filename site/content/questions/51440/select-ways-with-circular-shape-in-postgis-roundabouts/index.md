+++
type = "question"
title = "Select ways with circular shape in PostGIS (roundabouts)?"
description = '''Hello. I need to create a PostGIS query that outputs roundabouts from OSM that have no &quot;junction&quot;=&quot;roundabout&quot; tag. Is there a function that returns true if a geometry has a circular shape? I have tried ST_HasArc but it doesn&#x27;t seem to be working. Any other suggestion on how to find roundabouts with...'''
date = "2016-08-16T11:58:00Z"
lastmod = "2017-04-11T18:07:00Z"
weight = 51440
keywords = [ "postgresql", "roundabout", "postgis" ]
aliases = [ "/questions/51440" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Select ways with circular shape in PostGIS (roundabouts)?](/questions/51440/select-ways-with-circular-shape-in-postgis-roundabouts)

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
<span id="post-51440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51440-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I need to create a PostGIS query that outputs roundabouts from OSM that have no "junction"="roundabout" tag. Is there a function that returns true if a geometry has a circular shape? I have tried <a href="http://postgis.net/docs/ST_HasArc.html">ST_HasArc</a> but it doesn't seem to be working. Any other suggestion on how to find roundabouts with missing "junction"="roundabout" tag is welcomed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '16, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0464ec5533673976b9a83b8bfaab3c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manuela_butuc&#39;s gravatar image" />
<p><span>manuela_butuc</span><br />
<span class="score" title="156 reputation points">156</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manuela_butuc has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '16, 13:33</strong> </span></p>
</div>
</div>
<div id="comments-container-51440" class="comments-container">
<span id="51442"></span>
<div id="comment-51442" class="comment">
<div id="post-51442-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could try to search for ways that have a highway tag and the same first and last node. Won't work for roundabouts that consist of multiple ways though.</p>
</div>
<div id="comment-51442-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 14:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51444"></span>
<div id="comment-51444" class="comment">
<div id="post-51444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, i did that already, using ST_IsClosed function, but it's still not enough. I need something that goes more into detail</p>
</div>
<div id="comment-51444-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 15:11)</span> <span class="comment-user userinfo">manuela_butuc</span>
</div>
</div>
<span id="51454"></span>
<div id="comment-51454" class="comment">
<div id="post-51454-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect that this is very hard: there will be far too many edge cases to manage (for instance roundabout entrances &amp; exits mapped to the same node; non-round roundabouts etc.)</p>
</div>
<div id="comment-51454-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 19:01)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51440-form-container" class="comment-form-container">
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

<span id="51490"></span>

<div id="answer-container-51490" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51490-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-51490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After 2 days of trials, I think I have found a way around this problem. This is what I did:</p>
<ul>
<li><p>selected only navigable roads (highways without pedestrian, footway, etc)</p></li>
<li><p>used the ST_IsClosed function to find only closed ways</p></li>
<li><p>selected only those ways that have between 7 and 40 nodes</p></li>
<li><p>selected only ways that have less than 500 m in length (could have gone lower, probably)</p></li>
<li><p>I created a centroid for each of the remaining ways with ST_Centroid function</p></li>
<li><p>I calculated the distance between each centroid and the nodes on the corresponding way</p></li>
<li><p>I calculated the standard deviation for the distances (centroid-&gt;nodes) and got numbers between 0.0001 and 0.267</p></li>
<li><p>I chose only the ways that have a standard deviation of maximum 0.08 (this is just a number I came up with after surveying the results)</p></li>
</ul>
<p>I don't have a clean script to post right now, as I used many intermediate tables, but I plan to make one and post it on Github if anyone else is interested in finding roundabouts :) If you have suggestion of any other filters I could use to make the output even more accurate, i'm happy to read them!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '16, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0464ec5533673976b9a83b8bfaab3c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manuela_butuc&#39;s gravatar image" />
<p><span>manuela_butuc</span><br />
<span class="score" title="156 reputation points">156</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manuela_butuc has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '16, 13:21</strong> </span></p>
</div>
</div>
<div id="comments-container-51490" class="comments-container">
<span id="51495"></span>
<div id="comment-51495" class="comment not_top_scorer">
<div id="post-51495-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will also calculate the distance between nodes of the way to see if they are similar, because the standard deviation for the distance between centroid&amp;nodes is not enough to find roundabouts, it outputs ways like this one: <a href="https://postimg.org/image/l9ncwfo2x/">https://postimg.org/image/l9ncwfo2x/</a></p>
</div>
<div id="comment-51495-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 14:26)</span> <span class="comment-user userinfo">manuela_butuc</span>
</div>
</div>
<span id="51500"></span>
<div id="comment-51500" class="comment">
<div id="post-51500-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Impressed with the ingenuity!</p>
<p>I wonder if <a href="http://postgis.net/docs/ST_MinimumBoundingCircle.html">http://postgis.net/docs/ST_MinimumBoundingCircle.html</a> might be useful as well.</p>
</div>
<div id="comment-51500-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 17:24)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="51501"></span>
<div id="comment-51501" class="comment">
<div id="post-51501-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Years ago, I played with ST_Azimuth to find the maximum angle between three points. Underlying assumption was that roundabouts shouldn't have e.g. 90 degree angles in there. The idea is to choose some cut off maximum angle when querying data. Code is here: <a href="http://pastebin.com/nvZ3YrEF">http://pastebin.com/nvZ3YrEF</a></p>
</div>
<div id="comment-51501-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 18:53)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="51503"></span>
<div id="comment-51503" class="comment">
<div id="post-51503-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/12617/manuela_butuc">@manuela_butuc</a> I've accepted this as an answer on your behalf (since you can't accept your own answers). Hope this is OK...</p>
</div>
<div id="comment-51503-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 19:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="51513"></span>
<div id="comment-51513" class="comment">
<div id="post-51513-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5/richard">@Richard</a> ♦ I read what that function does but I don't think it can help me with the roundabouts. Anyways, good to know it exists!</p>
<p><a href="https://help.openstreetmap.org/users/8708/mmd">@mmd</a> Thanks for the code snippet, it actually helped a lot!</p>
</div>
<div id="comment-51513-info" class="comment-info">
<span class="comment-age">(18 Aug '16, 08:59)</span> <span class="comment-user userinfo">manuela_butuc</span>
</div>
</div>
<span id="51517"></span>
<div id="comment-51517" class="comment">
<div id="post-51517-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Great piece of work. Would love to see it written up in a bit more detail (specifically with images of what gets selected &amp; what gets rejected).</p>
</div>
<div id="comment-51517-info" class="comment-info">
<span class="comment-age">(18 Aug '16, 10:17)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="51661"></span>
<div id="comment-51661" class="comment not_top_scorer">
<div id="post-51661-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wouldn't it make more sense to just treat it as a polygon and then calculate perimeter/sqrt(area) ratio? If it's close to minimal theoretical value (and has &gt;=6 nodes), then you probably have a circle.</p>
<p>Consider also, that roundabouts may get divided into multiple ways for route relations.</p>
</div>
<div id="comment-51661-info" class="comment-info">
<span class="comment-age">(23 Aug '16, 00:29)</span> <span class="comment-user userinfo">RicoElectrico</span>
</div>
</div>
</div>
<div id="comment-tools-51490" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-51490-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55568"></span>

<div id="answer-container-55568" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55568-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's a PostGIS script doing just that: <a href="https://github.com/TelenavMapping/useful-postgis-queries/blob/master/sql-queries/detect_possible_roundabouts.sql">https://github.com/TelenavMapping/useful-postgis-queries/blob/master/sql-queries/detect_possible_roundabouts.sql</a> Enjoy!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '17, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/e26832004245996d0586eb01f4716fdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manuelab_telenav&#39;s gravatar image" />
<p><span>manuelab_tel...</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manuelab_telenav has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55568" class="comments-container">
&#10;</div>
<div id="comment-tools-55568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55568-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51653"></span>

<div id="answer-container-51653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51653-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many of us, vector map-makers, do this roundabout recognition, and we do it from the times even before the OSM has been born. There are at least two basic reasons to that:</p>
<ul>
<li>to provide more complete and safer turn-by-turn navigation network; and</li>
<li>when creating the vector scale levels, roundabouts quickly transform to ordinary nodes.</li>
</ul>
<p>In addition to the answer and comments already provided I would rather add some hints/suggestions based on experience running data-preparation on OSM dumps though the numbers are some months old (I do not register them for every run/OSM dump).</p>
<p>The preparation-tool runs separately on any of the road classes (motorway, trunk, primary, secondary, tertiary, living-street and street) and detects way classes RAC (ways tagged as roundabout) and ORC (the rest or the ordinary roads, not tagged as roundabouts).</p>
<p>Within RAC, we create the roundabout (RA) class (single circular ways or end-to-end connected ways creating circular ways). Now, for the RA class we detect some 5-7 (average/statistical) parameters like the number of edges, the length of the edge, the convexity, the diameter and so on. Finally, within the RAC we detect:</p>
<ul>
<li>The safe roundabout (SRA) class (253480 objects for all road classes). These are elements of RA having parameters close to the average values;</li>
<li>The unsafe roundabout (URA) class (6875), those from RA having at least one parameter far from the average value (outside the tolerance). This unsafe class of RA contains roundabouts wit anomalies as well (with self-crossings, more than one round between the start and end nodes, isolated, having more than one section between two nodes, zig-zag consecutive edges and so on);</li>
<li>The geo-rec based (GRA) class (708). This are created from the incomplete roundabouts where adding one or two short poly-line sections we create a safe roundabout; finally</li>
<li>The erroneous objects in RAC (2195). These are ways recognized as ordinary/feeding roads obviously tagged as roundabouts by mistake. This road segments are missing sections in ORC and therefor they are added to the ORC before further processing.<br />
-Within the ORC we detect circular single ways that closely (perfectly) match the corresponding safe SRA parameters. There were totally 101803 such cases, let us say, ordinary road roundabouts (ORRA).<br />
-Finally, in a similar way as for GRA we detect some 19547 geo-rec based roundabouts (GORRA) from the ORC class (with high probability also roundabouts).</li>
</ul>
<p>Within any of the mentioned road types, we merge the described five roundabout classes to a final set of roundabouts. These are the input to further preparation, data generalisation, rooting …</p>
<p>Note that the last two roundabout sets (ORRA and GORRA) contain large number of turning-circles. Visual inspection on a large sample shows that mappers are having dilemma how to tag/upload these kinds of objects. At the same time qualifying turning-circles as roundabouts should not confuse robust line-following/rooting systems.</p>
<p>If interested, some more details can be found from my earlier OSM-dev and OSM-rooting forum discussions/posts here <a href="https://drive.google.com/open?id=0B6qGm3k2qWHqRVVXVVFwbVdtN1E">https://drive.google.com/open?id=0B6qGm3k2qWHqRVVXVVFwbVdtN1E</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '16, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '16, 08:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-51653" class="comments-container">
&#10;</div>
<div id="comment-tools-51653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51653-form-container" class="comment-form-container">
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

