+++
type = "question"
title = "Surface for a specific GPS coordinate / GPS coordinates trace"
description = '''We have a bunch of recorded workout traces from runners, as array of GPS coordinates. Now we want to know the surfaces the runners runned on (asphalt, forest way, etc). As I am very new to OSM, I want to ask how this would be possible? I found that the data should be available in some metadata (key:...'''
date = "2017-04-07T13:39:00Z"
lastmod = "2017-04-10T10:41:00Z"
weight = 55521
keywords = [ "overpassapi", "overpass", "osm", "overpass-api" ]
aliases = [ "/questions/55521" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Surface for a specific GPS coordinate / GPS coordinates trace](/questions/55521/surface-for-a-specific-gps-coordinate-gps-coordinates-trace)

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
<span id="post-55521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have a bunch of recorded workout traces from runners, as array of GPS coordinates. Now we want to know the surfaces the runners runned on (asphalt, forest way, etc). As I am very new to OSM, I want to ask how this would be possible? I found that the data should be available in some metadata (key:surface). Is there a service query call to get this information? And, as a next step, is it possible for self hosting an overpass instance for annotating a bigger amount of such traces, preferably directly without remote call for performance reasons?</p>
<p>Thanks a lot</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '17, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/fdb88cdf2f7bf6b46f61bc27ba88e391?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GarrySnail&#39;s gravatar image" />
<p><span>GarrySnail</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GarrySnail has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55521" class="comments-container">
<span id="55542"></span>
<div id="comment-55542" class="comment">
<div id="post-55542-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>, this is exactly what I need. <a href="https://help.openstreetmap.org/users/1725/andy">@andy</a>-mackey, yes the question was about data use.</p>
<p>Thanks a lot guys!</p>
</div>
<div id="comment-55542-info" class="comment-info">
<span class="comment-age">(10 Apr '17, 10:41)</span> <span class="comment-user userinfo">GarrySnail</span>
</div>
</div>
</div>
<div id="comment-tools-55521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55521-form-container" class="comment-form-container">
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

<span id="55528"></span>

<div id="answer-container-55528" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55528-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GarrySnail has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the start:</p>
<p>Some streets/paths in our data have a <a href="https://wiki.openstreetmap.org/wiki/Key:surface">surface</a> <a href="https://wiki.openstreetmap.org/wiki/Tags">tag</a>. Coverage of the surface meta data will vary very much across regions (some may have 0% and some nearly to 100%). Example querys with map visualization: <a href="https://overpass-turbo.eu/s/ocj">https://overpass-turbo.eu/s/ocj</a> or <a href="http://overpass-turbo.eu/s/ock">http://overpass-turbo.eu/s/ock</a> . As far as I know you could query for the closest street (closest to your coordinate point) with overpass (I do not know the details) and get its surface value.</p>
<p>Please have a look at <a href="https://wiki.openstreetmap.org/wiki/Elements">https://wiki.openstreetmap.org/wiki/Elements</a> and <a href="https://wiki.openstreetmap.org/wiki/Develop">https://wiki.openstreetmap.org/wiki/Develop</a> .</p>
<p>Selfhosting overpass is possible (but not simple), see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">https://wiki.openstreetmap.org/wiki/Overpass_API/Installation</a> .</p>
<p>Nearly everything is possible with OSM, because you have access to the raw data (which you do not have with, for example, google maps).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '17, 21:14</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55528" class="comments-container">
&#10;</div>
<div id="comment-tools-55528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55528-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55526"></span>

<div id="answer-container-55526" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55526-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Surface may have been mapped if you are lucky. If not Bing may give a good idea, at least grass dirt and tarmac may be recognisable, gravel may be harder to see. The surface images may be a little out of date. Of course you will only be able to see the aerial images as an editor background.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '17, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-55526" class="comments-container">
<span id="55527"></span>
<div id="comment-55527" class="comment">
<div id="post-55527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>as far as I understand the question it is about data use, not OSM contribution. <a href="https://help.openstreetmap.org/users/13571/garrysnail"></a><a href="https://help.openstreetmap.org/users/13571/garrysnail">@GarrySnail</a>: please could you comment?</p>
</div>
<div id="comment-55527-info" class="comment-info">
<span class="comment-age">(07 Apr '17, 20:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55526-form-container" class="comment-form-container">
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

