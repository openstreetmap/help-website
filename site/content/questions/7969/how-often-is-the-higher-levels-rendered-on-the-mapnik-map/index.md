+++
type = "question"
title = "How often is the higher levels rendered on the mapnik map?"
description = '''Often when I edit the map and a bit later look at that area on the main website, and zoom in to a lower level (closer to the ground), I see the updated tiles. But when I zoom out, those tiles in the higher levels (e.g. airplane perspective) seem to be rarely updated / rendered. How often are the hig...'''
date = "2011-09-18T13:23:00Z"
lastmod = "2011-09-25T14:46:00Z"
weight = 7969
keywords = [ "map", "updates", "mapnik", "rendering" ]
aliases = [ "/questions/7969" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How often is the higher levels rendered on the mapnik map?](/questions/7969/how-often-is-the-higher-levels-rendered-on-the-mapnik-map)

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
<span id="post-7969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7969-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Often when I edit the map and a bit later look at that area on the main website, and <strong>zoom in</strong> to a lower level (closer to the ground), I see the updated tiles. But when I zoom out, those tiles in the higher levels (e.g. airplane perspective) seem to be rarely updated / rendered. How often are the higher levels updated?</p>
<p>I have read the question <a href="http://help.openstreetmap.org/questions/178/how-often-does-the-main-mapnik-map-get-updated">How often does the main (mapnik) map get updated</a> and it's answer. But I think that is mostly how it works on the lower levels, and not in the higher levels when the map is <strong>zoomed out</strong>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '11, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonas_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '11, 17:19</strong> </span></p>
</div>
</div>
<div id="comments-container-7969" class="comments-container">
&#10;</div>
<div id="comment-tools-7969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7969-form-container" class="comment-form-container">
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

<span id="7976"></span>

<div id="answer-container-7976" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7976-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-7976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jonas_ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are right that the described process is not complete for all zoom levels, but there also seems to be a confusion about how <em>low zoom level</em> is usually referred to in OSM. The <em>lower</em> the number (starting from 0) the <em>lower</em> we call the zoom. So zooming in would be going to higher zoomlevels. The low-zoom-tiles (which show a bigger part of the earth therefore containing much more data) are rendered only from time to time in a batch-like process.</p>
<p>Another specialty is the <a href="http://wiki.openstreetmap.org/wiki/Coastline#Main_Mapnik_layer">coastline process</a>, which makes changes to coastlines take much more time until the modifications actually go in the rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '11, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-7976" class="comments-container">
<span id="7978"></span>
<div id="comment-7978" class="comment">
<div id="post-7978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I know it can be some confusion about the terminology. That's why I also wrote "zoom in" and "zoom out". But now I have updated the question to clarify ("zoom in, closer to the ground" and "zoom out, to airplane perspective").</p>
</div>
<div id="comment-7978-info" class="comment-info">
<span class="comment-age">(18 Sep '11, 17:22)</span> <span class="comment-user userinfo">Jonas_</span>
</div>
</div>
<span id="7981"></span>
<div id="comment-7981" class="comment">
<div id="post-7981-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I suggest you also update the title (lower, not higher) and change lower to higher and vice versa in the question.</p>
</div>
<div id="comment-7981-info" class="comment-info">
<span class="comment-age">(18 Sep '11, 19:41)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="7984"></span>
<div id="comment-7984" class="comment">
<div id="post-7984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have not changed anything, just clarified. I am talking about higher (airplane perspective) as it stands in the title. So everything is correct now.</p>
</div>
<div id="comment-7984-info" class="comment-info">
<span class="comment-age">(18 Sep '11, 20:34)</span> <span class="comment-user userinfo">Jonas_</span>
</div>
</div>
</div>
<div id="comment-tools-7976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7976-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7982"></span>

<div id="answer-container-7982" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7982-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer is not constant. You can see here how many tiles of a certain zoomlevel range are currently rendered in one second and how many it was in the past: <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_zoom.html">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_zoom.html</a></p>
<p>Zoom0-8 are considered "lowest" zoomlevels. In the current year there were rendered in this level an average of 3.85 metatiles per hour. There is a total of 87381 tiles = 1366 metatiles in these zoomlevels, so if the rendered areas are distributed equally you would have every tile rendered newly every 15 days. If you look at the average of this week though, it would take much longer: around 112 days. I guess the answer lies in this range.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '11, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-7982" class="comments-container">
<span id="8131"></span>
<div id="comment-8131" class="comment">
<div id="post-8131-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>From the link it looks like the tiles in level z0-z12 is never rendered. This is a problem in my point of view.</p>
</div>
<div id="comment-8131-info" class="comment-info">
<span class="comment-age">(25 Sep '11, 12:51)</span> <span class="comment-user userinfo">Jonas_</span>
</div>
</div>
<span id="8135"></span>
<div id="comment-8135" class="comment">
<div id="post-8135-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, they are rendered, and you can also see this from the graph. 0-8 is rendered with an average of 0.00105 metatiles per second (which is 3.78 Metatiles per hour) (statistics per year, average).</p>
</div>
<div id="comment-8135-info" class="comment-info">
<span class="comment-age">(25 Sep '11, 14:46)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-7982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7982-form-container" class="comment-form-container">
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

