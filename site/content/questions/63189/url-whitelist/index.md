+++
type = "question"
title = "URL Whitelist"
description = '''Hi, We&#x27;re using kiosk mode tablets for one of our customers and the tablets are only allowed to access a limited number of websites via a &quot;locked down&quot; browser, one of them being OpenStreetMap. To be specific, we&#x27;re using the Intune Managed Browser to only whitelist apporpriate URLs. I&#x27;ve already wh...'''
date = "2018-04-27T12:15:00Z"
lastmod = "2018-04-30T08:11:00Z"
weight = 63189
keywords = [ "whitelist" ]
aliases = [ "/questions/63189" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [URL Whitelist](/questions/63189/url-whitelist)

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
<span id="post-63189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63189-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, We're using kiosk mode tablets for one of our customers and the tablets are only allowed to access a limited number of websites via a "locked down" browser, one of them being OpenStreetMap. To be specific, we're using the Intune Managed Browser to only whitelist apporpriate URLs. I've already whitelisted https://<em>.openstreetmap.org/</em> + <a href="https://openstreetmap.org/*">https://openstreetmap.org/*</a> but the devices are still not able to load the map on <a href="https://openstreetmap.org">https://openstreetmap.org</a>.</p>
<p>Are there any other URLs that needs to be whitelisted in order to use the map functionality in this situation?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-whitelist" rel="tag" title="see questions tagged &#39;whitelist&#39;">whitelist</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '18, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/77d1014faa2ecce72a46d14dc6b77715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ali%20Njie&#39;s gravatar image" />
<p><span>Ali Njie</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ali Njie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63189" class="comments-container">
<span id="63191"></span>
<div id="comment-63191" class="comment">
<div id="post-63191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hope you're following OSMF Tile Usage Policy:</p>
<p><a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a></p>
</div>
<div id="comment-63191-info" class="comment-info">
<span class="comment-age">(27 Apr '18, 17:14)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
</div>
<div id="comment-tools-63189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63189-form-container" class="comment-form-container">
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

<span id="63195"></span>

<div id="answer-container-63195" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63195-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ali Njie has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Are there any other URLs that needs to be whitelisted in order to use the map functionality in this situation?</p>
</blockquote>
<p>The answer to that's easy - yes!</p>
<p>The tricky bit is working out which, because it depends on what functionality you want your users to have on the site. What are they using it for - to view maps (if so, which ones)?, to calculate routes?, to edit maps?, to access the forum and the wiki, this help site, etc. etc.?</p>
<p>Because there's so much that people could do from the osm website it's probably easiest for you to look at what actual resources the your desired pages within the site request by looking at proxy logs, or if that's not an option the "developer tools" in the various browsers.</p>
<p>It's worth mentioning that if you just want map view and don't want map editing and all the other stuff then setting up your own leaflet-based website would be by far the easiest approach - you'd only need to whitelist your website and (assuming the standard layer) "<code>https://?.tile.openstreetmap.org/*.png</code>" where "<code>?</code>" is a letter a-c and "<code>*</code>" is the rest of the tile path (an example tile is <a href="https://c.tile.openstreetmap.org/9/253/166.png">https://c.tile.openstreetmap.org/9/253/166.png</a>). In $dayjob I do this sort of thing fairly regularly (for one of Intune's competitors) and use an example map site that has everything behind one URL for testing for exactly this reason.</p>
<p>Incidentally, your current whitelist URLs are missing the initial "<code>?</code>" which may be why you see no tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '18, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63195" class="comments-container">
<span id="63229"></span>
<div id="comment-63229" class="comment">
<div id="post-63229-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for your answer. The users only use the OSM site to access and view the map. No route calculations or anything like that.</p>
<p>I will give this a shot!</p>
<p>Thanks again :)</p>
</div>
<div id="comment-63229-info" class="comment-info">
<span class="comment-age">(30 Apr '18, 08:11)</span> <span class="comment-user userinfo">Ali Njie</span>
</div>
</div>
</div>
<div id="comment-tools-63195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63192"></span>

<div id="answer-container-63192" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63192-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Map-tiles are served from a network of cache servers, see <a href="https://hardware.openstreetmap.org/">https://hardware.openstreetmap.org/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '18, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-63192" class="comments-container">
&#10;</div>
<div id="comment-tools-63192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63192-form-container" class="comment-form-container">
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

