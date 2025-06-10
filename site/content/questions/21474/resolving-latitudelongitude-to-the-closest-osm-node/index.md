+++
type = "question"
title = "Resolving latitude/longitude to the closest OSM node?"
description = '''If given a latitude,longitude value, how can I convert this value to an OSM node.'''
date = "2013-04-12T17:07:00Z"
lastmod = "2013-04-12T18:04:00Z"
weight = 21474
keywords = [ "map", "nodes", "osm", "routing" ]
aliases = [ "/questions/21474" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Resolving latitude/longitude to the closest OSM node?](/questions/21474/resolving-latitudelongitude-to-the-closest-osm-node)

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
<span id="post-21474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21474-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If given a latitude,longitude value, how can I convert this value to an OSM node.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '13, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/361e0b98020ca3f3d7db7baa2ec6c590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sadeer&#39;s gravatar image" />
<p><span>Sadeer</span><br />
<span class="score" title="176 reputation points">176</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sadeer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '13, 00:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-21474" class="comments-container">
<span id="21476"></span>
<div id="comment-21476" class="comment">
<div id="post-21476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's <em>similar</em> to <span>reverse geocoding</span> but apparently it is not possible to return a node with Nominatim, if I see correctly. Maybe with XAPI or overpass API.</p>
</div>
<div id="comment-21476-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 17:12)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="21484"></span>
<div id="comment-21484" class="comment">
<div id="post-21484-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you mean "any sort of node at all" or "a node with particular tags"? Not that it makes much of a difference technically, but it might help people imagine what you're trying to do.</p>
</div>
<div id="comment-21484-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 17:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="21486"></span>
<div id="comment-21486" class="comment">
<div id="post-21486-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'm building a route planning system: users will be able to click on a map to set their starting/destination places. A route will then be found between the given locations. Currently, I'm using Leaflet to allow users to set these places, and what it returns is lat/lon value when the user clicks on the map. Now, I'm trying to resolve the returned lat/lon values to the closest osm nodes which are part of some osm way.</p>
<p>Hope that makes sense.</p>
</div>
<div id="comment-21486-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 17:56)</span> <span class="comment-user userinfo">Sadeer</span>
</div>
</div>
<span id="21487"></span>
<div id="comment-21487" class="comment">
<div id="post-21487-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@Sadeer</span>: may it be that you are actually not looking for the closest node (which is part of "some osm way") but instead of the closest point on a way which is tagged with highway=whatever? I strongly think that you should have a look in the existing open source <span>routing solutions</span> for ideas or even code fragments (if the license is compatible). No reason to reinvent the wheel.</p>
</div>
<div id="comment-21487-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 18:04)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21474-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

