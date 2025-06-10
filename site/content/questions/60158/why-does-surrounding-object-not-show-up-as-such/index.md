+++
type = "question"
title = "why does surrounding object not show up as such?"
description = '''Hi, referring to the site at  https://www.openstreetmap.org/#map=16/46.6548/11.1634 In the center is an industrial zone, which imho is a well defined multipolygon. Also the area is colored to be an industrial zone - so I would think there is no mistake with the area as such. However, when using the ...'''
date = "2017-10-17T20:59:00Z"
lastmod = "2017-10-18T20:52:00Z"
weight = 60158
keywords = [ "surrounding", "multipolygon", "relation", "query", "area" ]
aliases = [ "/questions/60158" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [why does surrounding object not show up as such?](/questions/60158/why-does-surrounding-object-not-show-up-as-such)

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
<span id="post-60158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60158-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>referring to the site at <a href="https://www.openstreetmap.org/#map=16/46.6548/11.1634">https://www.openstreetmap.org/#map=16/46.6548/11.1634</a></p>
<p>In the center is an industrial zone, which imho is a well defined multipolygon. Also the area is colored to be an industrial zone - so I would think there is no mistake with the area as such. However, when using the object query tool on the buildings standing on the industrial zone, the latter will not show in the surrounding objects. When querying close the border of the industrial zone, the multipolygon surrounding it will show in the nearby objects. I did not find differences to other industrial zones nearby, where query works fine. - the ways making up the multipolygon exist and their endpoints are connected and form a ring (one of the ways is defined counterclockwise, the other 3 clockwise, though. - The industrial zone does not have a name (most others in the region do, so this might be an issue) - some other areas defined by the same user also have the same problem (e.g. the orchard right next to the industrial zone. I really think there is nothing wrong with the definitions - so maybe somehow a failed changeset? - The relation does have the &lt;tag k="landuse" v="industrial"/&gt; ande &lt;tag k="type" v="multipolygon"/&gt;</p>
<p>Note that the issue propagates when exporting the data via osm2pgsql; the buildings will not show to be part of the industrial zone.</p>
<p>So do these multipolygon require a name to show in the surrounding objects or can someone find another issue?</p>
<p>Thank you,</p>
<p>Andi</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-surrounding" rel="tag" title="see questions tagged &#39;surrounding&#39;">surrounding</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '17, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad88a06505395064766e7ef833f6bdc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="achrist1&#39;s gravatar image" />
<p><span>achrist1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="achrist1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60158" class="comments-container">
<span id="60163"></span>
<div id="comment-60163" class="comment">
<div id="post-60163-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could the problem be that (as you observed) one of the ways is counterclockwise and the other three are clockwise? I realise that <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Usage">the wiki</a> states direction of ways shouldn't matter, but perhaps the renderer's implementation does assume that the endpoint of way N is the startpoint of way N+1.</p>
</div>
<div id="comment-60163-info" class="comment-info">
<span class="comment-age">(17 Oct '17, 23:51)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="60174"></span>
<div id="comment-60174" class="comment">
<div id="post-60174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I think dkiselev's answer is actually spot on. Thanks for your suggestion, though</p>
</div>
<div id="comment-60174-info" class="comment-info">
<span class="comment-age">(18 Oct '17, 20:34)</span> <span class="comment-user userinfo">achrist1</span>
</div>
</div>
</div>
<div id="comment-tools-60158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60158-form-container" class="comment-form-container">
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

<span id="60164"></span>

<div id="answer-container-60164" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60164-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can open dev console and check the networking tab, there are three querries:</p>
<p><a href="https://www.openstreetmap.org/query?lat=46.65684&amp;lon=11.16265&amp;xhr=1">https://www.openstreetmap.org/query?lat=46.65684&amp;lon=11.16265&amp;xhr=1</a> this one seems to generate the template foe the answer translated onto the right language.</p>
<p>Next two are actual data requests made to Overpass API</p>
<p>The closest objects</p>
<pre><code>[timeout:10][out:json];
(
  node(around:22.5,46.65684,11.16265);
  way(around:22.5,46.65684,11.16265)
);
out tags geom(46.65114479792893,11.154974699020386,46.65802297900334,11.171818971633911);
relation(around:22.5,46.65684,11.16265);
out geom(46.65114479792893,11.154974699020386,46.65802297900334,11.171818971633911);</code></pre>
<p>and surrounding objects:</p>
<pre><code>[timeout:10][out:json];
is_in(46.65684,11.16265)-&gt;.a;
way(pivot.a);
out tags bb;
out ids geom(46.65114479792893,11.154974699020386,46.65802297900334,11.171818971633911);
relation(pivot.a);
out tags bb;</code></pre>
<p>Here is the description for Overpass QL is_in statement <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29</a></p>
<p>The important part:</p>
<p><strong>Area creation depends on some specific extraction rules, there's no area counterpart for each and very OSM way or relation!</strong></p>
<p>And here are some details of how the areas for Overpass API are produced <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Areas">http://wiki.openstreetmap.org/wiki/Overpass_API/Areas</a></p>
<p>In the nut shell, <strong>it should be named multypoligon/administartive boundary or postal_code area</strong>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '17, 03:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ba776c365d041c46b17224fcb4bc196d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dkiselev&#39;s gravatar image" />
<p><span>dkiselev</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dkiselev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60164" class="comments-container">
<span id="60173"></span>
<div id="comment-60173" class="comment">
<div id="post-60173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but oh boy, this does nowhere show up in the wiki, e.g. <a href="https://wiki.openstreetmap.org/wiki/Talk:Relation:multipolygon">https://wiki.openstreetmap.org/wiki/Talk:Relation:multipolygon</a> has even wrong examples, which suggest that the multipolygon tag alone is sufficient to create an area...(or, as always possible, I again prove that I cannot read properly) Have you got any idea why the name would be so important to define an area? I mean, I would not be so sure that all industrial zone (all being areas) even have a name. On the other hand I would not think that it is out of the question that a multipolygon road could have a name. So for distinction purposes the name is not so strong. Do you know where I could suggest this to be thought over? Thanks,</p>
<p>Andreas</p>
</div>
<div id="comment-60173-info" class="comment-info">
<span class="comment-age">(18 Oct '17, 20:32)</span> <span class="comment-user userinfo">achrist1</span>
</div>
</div>
<span id="60176"></span>
<div id="comment-60176" class="comment">
<div id="post-60176-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's enough to create multypoligon to create an area in OSM terms, but Overpass is actually is separate project it's closely related to OSM but Overpass treats areas little bit different. So it's enough to create multypoligon from OSM perspective but it wouldn't be imported to Overpass database. I know that it's sounds confusing but OSM is more like a collaboration of different projects instead of one solid project.</p>
</div>
<div id="comment-60176-info" class="comment-info">
<span class="comment-age">(18 Oct '17, 20:52)</span> <span class="comment-user userinfo">dkiselev</span>
</div>
</div>
</div>
<div id="comment-tools-60164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60164-form-container" class="comment-form-container">
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

