+++
type = "question"
title = "Bus stations tagged according to new scheme do not appear on map"
description = '''Hello, I recently added some bus stations according to what I understood to be the new scheme, tagging them as public_transport=station and bus=yes. Surprisingly none of them appears on the map, whereas stations tagged with amenity=bus_station are shown. Did I get something wrong and there is someth...'''
date = "2017-03-22T17:47:00Z"
lastmod = "2017-03-23T12:39:00Z"
weight = 55240
keywords = [ "bus_station", "map", "new_scheme", "tagging", "show" ]
aliases = [ "/questions/55240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bus stations tagged according to new scheme do not appear on map](/questions/55240/bus-stations-tagged-according-to-new-scheme-do-not-appear-on-map)

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
<span id="post-55240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55240-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I recently added some bus stations according to what I understood to be the new scheme, tagging them as public_transport=station and bus=yes. Surprisingly none of them appears on the map, whereas stations tagged with amenity=bus_station are shown. Did I get something wrong and there is something missing? I'm tempted to change the tags to the old scheme to make them visible.</p>
<p>Knut</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus_station" rel="tag" title="see questions tagged &#39;bus_station&#39;">bus_station</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-new_scheme" rel="tag" title="see questions tagged &#39;new_scheme&#39;">new_scheme</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-show" rel="tag" title="see questions tagged &#39;show&#39;">show</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '17, 17:47</strong></p>
<img src="https://secure.gravatar.com/avatar/f03c3c74641d9bd0999b9249921f5218?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Knut%20Hildebrandt&#39;s gravatar image" />
<p><span>Knut Hildebr...</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Knut Hildebrandt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55240" class="comments-container">
<span id="55244"></span>
<div id="comment-55244" class="comment">
<div id="post-55244-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For info, there's discussion about the rendering of these on the "standard" map style over at <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/311">https://github.com/gravitystorm/openstreetmap-carto/issues/311</a> . Other map styles may already render them, of course.</p>
</div>
<div id="comment-55244-info" class="comment-info">
<span class="comment-age">(22 Mar '17, 18:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="55246"></span>
<div id="comment-55246" class="comment">
<div id="post-55246-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the hint. As much as I understood, there is a rendering problem with the new scheme that persists for almost 2 1/2 years. And the only viable solution for the moment seems to be double tagging. Thus I won't replace the new tags with the old ones but add these too in the hope the stops and stations will be shown on the maps.</p>
<p>BTW, this problem does not only exist on the Openstreetmap website but also in OsmAnd,the navigator I use.</p>
</div>
<div id="comment-55246-info" class="comment-info">
<span class="comment-age">(22 Mar '17, 21:23)</span> <span class="comment-user userinfo">Knut Hildebr...</span>
</div>
</div>
<span id="55249"></span>
<div id="comment-55249" class="comment">
<div id="post-55249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Related: <a href="/questions/43542/tagging-a-bus-station">tagging a bus station</a>.</p>
</div>
<div id="comment-55249-info" class="comment-info">
<span class="comment-age">(23 Mar '17, 12:01)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="55251"></span>
<div id="comment-55251" class="comment">
<div id="post-55251-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that <code>amenity=bus_station</code> is <em>not</em> for tagging individual bus stops, it is for bus stations, i.e. large installations where many buses stop, typically with service buildings.</p>
</div>
<div id="comment-55251-info" class="comment-info">
<span class="comment-age">(23 Mar '17, 12:15)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="55252"></span>
<div id="comment-55252" class="comment">
<div id="post-55252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/666/sleske">@sleske</a> Thanks for the hints. I know that amenity=bus_station is not for individual stops and I only used it for smaller or bigger bus stations. And I also understood how to use the new scheme but unfortunately stations only tagged according to it, are not shown on the maps ;-(</p>
</div>
<div id="comment-55252-info" class="comment-info">
<span class="comment-age">(23 Mar '17, 12:39)</span> <span class="comment-user userinfo">Knut Hildebr...</span>
</div>
</div>
</div>
<div id="comment-tools-55240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55240-form-container" class="comment-form-container">
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

<span id="55250"></span>

<div id="answer-container-55250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55250-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As mentioned by SomeoneElse's comment, there are currently two schemes for tagging bus stops:</p>
<ul>
<li>the old scheme: put a node where the bus shelter/stop sign is, tag it <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop"><code>highway=bus_stop</code></a></li>
<li>the new scheme, called <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport"><strong>Public Transport scheme</strong></a>: tag the stop position on the road as <code>public_transport=stop_position</code>, <code>bus=yes</code>, and the shelter position as <code>public_transport=platform</code> (and ideally combine them into a relation tagged <code>type=public_transport</code>, <code>public_transport=stop_area</code>).</li>
</ul>
<p>An introduction to the new scheme is under <a href="https://wiki.openstreetmap.org/wiki/Key:public_transport">Key:public_transport</a>.</p>
<hr />
<p>The new Public Transport scheme was introduced to address problems with the old scheme, mainly because the old scheme did not work well for other types of public transport.</p>
<p>However, the OSM main map does not yet render the new scheme - see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/311">issue 311</a> for details.</p>
<p><strong>So, for the time being, the pragmatic solution is to tag according to <em>both</em> schemes</strong> - that means you are compatible with all data consumers. If there is ever a consensus to abandon the old scheme, the old tags can be removed automatically if desired.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '17, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '17, 12:12</strong> </span></p>
</div>
</div>
<div id="comments-container-55250" class="comments-container">
&#10;</div>
<div id="comment-tools-55250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55250-form-container" class="comment-form-container">
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

