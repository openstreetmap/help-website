+++
type = "question"
title = "Potlatch Intersection Detection"
description = '''How does Potlatch determine intersections? I went through their repo on GitHub, but I don&#x27;t understand ActionScript. I searched the directory for the keyword &quot;intersection,&quot; but there were only two results and they didn&#x27;t seem too promising. From what I&#x27;ve been reading, nodes that are present in mor...'''
date = "2015-06-09T16:48:00Z"
lastmod = "2015-06-10T09:36:00Z"
weight = 43493
keywords = [ "potlatch2", "potlatch", "intersection", "osm", "intersections" ]
aliases = [ "/questions/43493" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Potlatch Intersection Detection](/questions/43493/potlatch-intersection-detection)

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
<span id="post-43493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43493-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How does Potlatch determine intersections? I went through their repo on GitHub, but I don't understand ActionScript. I searched the directory for the keyword "intersection," but there were only two results and they didn't seem too promising.</p>
<p>From what I've been reading, nodes that are present in more than one way are considered intersections, I wanted to see this for myself and to my surprise, there were tons of extraneous points (thousands even in a small city). I thought about considering only the ways that had the "highway" tag on them, but I'm not sure if this is an exhaustive search of all the intersections considered by OSM - can someone please help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-potlatch" rel="tag" title="see questions tagged &#39;potlatch&#39;">potlatch</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-intersections" rel="tag" title="see questions tagged &#39;intersections&#39;">intersections</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '15, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/cf01841ce4fdf36fb184337821994b21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jycai&#39;s gravatar image" />
<p><span>jycai</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jycai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43493" class="comments-container">
<span id="43495"></span>
<div id="comment-43495" class="comment">
<div id="post-43495-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>From reading this question, it seems that you have some problem that you're trying to solve that may not be directly related to Potlatch2. Is that true, and if so, what is it?</p>
</div>
<div id="comment-43495-info" class="comment-info">
<span class="comment-age">(09 Jun '15, 17:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43500"></span>
<div id="comment-43500" class="comment not_top_scorer">
<div id="post-43500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Potlatch 2 can detect intersections, I wondering if anyone knows how they go about doing this and labeling them as intersections since nodes in OSM are not tagged with an intersections tag. I understand that a node that is in 2 or more ways could be considered an intersection, but I am only looking for the intersection of streets - simply doing this search gives us a lot of extraneous information such as the buildings that have borders that intersect, etc.</p>
</div>
<div id="comment-43500-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 07:16)</span> <span class="comment-user userinfo">jycai</span>
</div>
</div>
<span id="43501"></span>
<div id="comment-43501" class="comment">
<div id="post-43501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is no other indicator except for the highway tag. Your approach seems sensible.</p>
</div>
<div id="comment-43501-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 07:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43503"></span>
<div id="comment-43503" class="comment">
<div id="post-43503-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>keep in mind that roads in OSM are split into several lines. For example, a road has to be split in two segments if you want to tag a change in max speed. This is also picked up as a possible intersection in Potlach. Depending on your needs, you might consider only including those nodes that belong to three or more ways tagged as highway=*. Keep in mind that "highway" is also used for footpaths etc, which you might want to exclude too.</p>
</div>
<div id="comment-43503-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 08:19)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="43504"></span>
<div id="comment-43504" class="comment not_top_scorer">
<div id="post-43504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks scai. There are a lot of things going on with the Potlatch database that are very interesting to me - I know the code is open source, but are the databases used by the program open to the public as well?</p>
</div>
<div id="comment-43504-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 08:20)</span> <span class="comment-user userinfo">jycai</span>
</div>
</div>
<span id="43505"></span>
<div id="comment-43505" class="comment not_top_scorer">
<div id="post-43505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>good call joost, I'll keep that in mind</p>
</div>
<div id="comment-43505-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 08:26)</span> <span class="comment-user userinfo">jycai</span>
</div>
</div>
<span id="43506"></span>
<div id="comment-43506" class="comment not_top_scorer">
<div id="post-43506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does anyone know whether or not Potlatch is detecting these intersections, or are users marking them manually? I've seen a couple posts about how to merge ways and mark an intersection - does this mean that users have to mark them in order for Potlatch to display it?</p>
</div>
<div id="comment-43506-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 08:28)</span> <span class="comment-user userinfo">jycai</span>
</div>
</div>
<span id="43507"></span>
<div id="comment-43507" class="comment">
<div id="post-43507-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What "Potlatch database"? Potlatch just uses the regular OSM database which you are free to set up on your own.</p>
</div>
<div id="comment-43507-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 08:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43508"></span>
<div id="comment-43508" class="comment not_top_scorer">
<div id="post-43508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd like to see all of the nodes that Potlatch has tagged as "Intersections." I've already downloaded OSM data, but this tag on nodes does not exist.</p>
</div>
<div id="comment-43508-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 08:36)</span> <span class="comment-user userinfo">jycai</span>
</div>
</div>
<span id="43509"></span>
<div id="comment-43509" class="comment">
<div id="post-43509-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is no "intersection" tag. Potlatch just uses a heuristic for highlighting intersections. This is done by iD, JOSM and most other editors, too. It helps the user editing the map, that's all.</p>
</div>
<div id="comment-43509-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 08:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43510"></span>
<div id="comment-43510" class="comment not_top_scorer">
<div id="post-43510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where could I find this heuristic? I think it could potentially be pretty useful for what I'm trying to do. Thanks a bunch scai!</p>
</div>
<div id="comment-43510-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 08:44)</span> <span class="comment-user userinfo">jycai</span>
</div>
</div>
<span id="43511"></span>
<div id="comment-43511" class="comment not_top_scorer">
<div id="post-43511-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not familiar with Potlatch2's code but this seems to be the relevant code line: <a href="https://github.com/openstreetmap/potlatch2/blob/9cab0567af82bf9e377bc42bfab96cdd9f95c68d/net/systemeD/halcyon/WayUI.as#L359">https://github.com/openstreetmap/potlatch2/blob/9cab0567af82bf9e377bc42bfab96cdd9f95c68d/net/systemeD/halcyon/WayUI.as#L359</a></p>
</div>
<div id="comment-43511-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 09:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43512"></span>
<div id="comment-43512" class="comment not_top_scorer">
<div id="post-43512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks so much scai!</p>
</div>
<div id="comment-43512-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 09:36)</span> <span class="comment-user userinfo">jycai</span>
</div>
</div>
</div>
<div id="comment-tools-43493" class="comment-tools">
<span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-43493-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

