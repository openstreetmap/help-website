+++
type = "question"
title = "New street names in Accra - preserving old name"
description = '''Hi all, The street names in Accra are changing. The page https://wiki.openstreetmap.org/wiki/Key:name suggests that old_name is the right tag to use to preserve the previous name.  Despite the street signs having been changed already, the old names are still widely used. So it makes sense for the ol...'''
date = "2015-10-25T14:22:00Z"
lastmod = "2015-10-26T09:53:00Z"
weight = 46104
keywords = [ "old_name" ]
aliases = [ "/questions/46104" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [New street names in Accra - preserving old name](/questions/46104/new-street-names-in-accra-preserving-old-name)

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
<span id="post-46104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46104-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>The street names in Accra are changing. The page <a href="https://wiki.openstreetmap.org/wiki/Key:name">https://wiki.openstreetmap.org/wiki/Key:name</a> suggests that old_name is the right tag to use to preserve the previous name.</p>
<p>Despite the street signs having been changed already, the old names are still widely used. So it makes sense for the old names to remain visible on the map, alongside the new name. For instance, say for the next 5 years, it would be ideal to see</p>
<p>new name (previously old name)</p>
<p>on the map. If this has an "expiration date", the the name might change to "new name" after that.</p>
<p>Any thoughts on how this should be handled?</p>
<p>Thanks! Bjoern</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-old_name" rel="tag" title="see questions tagged &#39;old_name&#39;">old_name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '15, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ec502848aedb6c84f8a0ffaf9ec54a67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bjohas&#39;s gravatar image" />
<p><span>bjohas</span><br />
<span class="score" title="56 reputation points">56</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bjohas has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46104" class="comments-container">
&#10;</div>
<div id="comment-tools-46104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46104-form-container" class="comment-form-container">
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

<span id="46106"></span>

<div id="answer-container-46106" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46106-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While there is a tag "start_date", this cannot be used for name changes. It is meant for the start of the feature. As long as there is no such tag, you cannot create a map that has the "new name (previously old name)".</p>
<p>Furthermore the current map rendering is only triggered by data changes or style changes, not by times hidden in the data. So it won't work even with a tag indicating the start_date of the new name. Still, such a tag can be useful.</p>
<p>You should still tag the current name in "name" and the previous name in "old_name". Please do not put "new name (previously old name)" in the name tag, as that is NOT the name of the street.</p>
<p>You could propose a tag for the start_date of the current name, but that's about it. What else would you like to do ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '15, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-46106" class="comments-container">
<span id="46108"></span>
<div id="comment-46108" class="comment">
<div id="post-46108-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I'd agree that using "new name (previously old name)" in the name field makes no sense. Renders, routers et al that read the "name" field are perfectly capable of reading the "old name" field too. If a particular renderer doesn't do that and you'd like it to, try and influence the people in charge of the renderer. For OSM's "standard" map that's <a href="https://github.com/gravitystorm/openstreetmap-carto/issues">https://github.com/gravitystorm/openstreetmap-carto/issues</a> .</p>
<p>However, creating map tiles (perhaps based on OSM's "standard" map) isn't that difficult these days, and maintaining such a map for one city wouldn't take a huge server. See <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a> for more details.</p>
</div>
<div id="comment-46108-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 19:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46120"></span>
<div id="comment-46120" class="comment">
<div id="post-46120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you know whether nominatim picks up the old name? At least it's discoverable in that way then, even if it doesn't actually render.</p>
</div>
<div id="comment-46120-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 21:15)</span> <span class="comment-user userinfo">bjohas</span>
</div>
</div>
<span id="46125"></span>
<div id="comment-46125" class="comment">
<div id="post-46125-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A search for "Callow Park" finds <a href="http://www.openstreetmap.org/way/129252704">http://www.openstreetmap.org/way/129252704</a> , so probably.</p>
</div>
<div id="comment-46125-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 23:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46126"></span>
<div id="comment-46126" class="comment">
<div id="post-46126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>according to the <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview">development page</a> it does. You find a list of all "names" that are recognized by Nominatim on that page</p>
</div>
<div id="comment-46126-info" class="comment-info">
<span class="comment-age">(26 Oct '15, 04:16)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-46106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46106-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46128"></span>

<div id="answer-container-46128" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46128-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sounds like <code>old_name</code> is correct to use. Have you considered putting the new names as <code>official_name</code>?</p>
<p>If everyone uses the old name and not the new name for a street, you could make a case for the <code>name</code> tag to be the old name. However you have a problem that the map might look "wrong" for people (since it doesn't have the 'new name'), nor the name "on the ground"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '15, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-46128" class="comments-container">
&#10;</div>
<div id="comment-tools-46128" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46128-form-container" class="comment-form-container">
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

