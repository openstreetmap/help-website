+++
type = "question"
title = "store locator"
description = '''Hi there, I am a developer looking to use OSM in conjunction with a store locator plugin for wordpress. I was hoping someone could tell me if it was possible to use OSM with that type of plugin or if there is a different solution that you folks would recommend. The only thing that I would need to te...'''
date = "2012-04-05T18:07:00Z"
lastmod = "2012-04-06T20:50:00Z"
weight = 11751
keywords = [ "locator", "wordpress", "store", "plugin" ]
aliases = [ "/questions/11751" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [store locator](/questions/11751/store-locator)

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
<span id="post-11751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11751-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, I am a developer looking to use OSM in conjunction with a store locator plugin for wordpress. I was hoping someone could tell me if it was possible to use OSM with that type of plugin or if there is a different solution that you folks would recommend.</p>
<p>The only thing that I would need to test wether or not OSM would work with this plugin is the API key. If anyone has any helpful tips for this I would be very grateful!</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-locator" rel="tag" title="see questions tagged &#39;locator&#39;">locator</span> <span class="post-tag tag-link-wordpress" rel="tag" title="see questions tagged &#39;wordpress&#39;">wordpress</span> <span class="post-tag tag-link-store" rel="tag" title="see questions tagged &#39;store&#39;">store</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '12, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/bddc566029f471a0090cb7afc5204234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dommagnifico&#39;s gravatar image" />
<p><span>dommagnifico</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dommagnifico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11751" class="comments-container">
&#10;</div>
<div id="comment-tools-11751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11751-form-container" class="comment-form-container">
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

<span id="11762"></span>

<div id="answer-container-11762" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11762-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no such thing as an API key for OSM. You just specify your user agent (http-style) and you're done.</p>
<p>A store locator should be easy to write using either <a href="http://leaflet.cloudmade.com/">leaflet</a> or <a href="http://www.openlayers.org/">openlayers</a>. Use your own json object for the list of stores, and one of the available tiles for the map background (be sure to respect the <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a>).</p>
<p>There may be ready-made wordpress plugins for that, I don't know.</p>
<p>If your needs are more complex than the simple json-based solution can provide, you'll have to give us more details,</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '12, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-11762" class="comments-container">
<span id="11787"></span>
<div id="comment-11787" class="comment">
<div id="post-11787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Basically what I am trying to do is have the user be able to search by either zipcode or state, when the user hits enter to search for said state or zipcode, the map zooms in to that area automatically.</p>
<p>That's pretty much the bare bones version of what I need and I was hoping there was some way to do that with OSM, I am using leaflet as well.</p>
<p>Thank you both for the quick responses. If there is an example of this out there somewhere for me to take a gander at that would be awesome as well, I have been searching all over but to no avail.</p>
</div>
<div id="comment-11787-info" class="comment-info">
<span class="comment-age">(06 Apr '12, 20:50)</span> <span class="comment-user userinfo">dommagnifico</span>
</div>
</div>
</div>
<div id="comment-tools-11762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11762-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11763"></span>

<div id="answer-container-11763" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11763-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without giving concrete hints about your aims, you can have a look at the OSM wiki at <a href="https://wiki.openstreetmap.org/wiki/Wordpress">Wordpress</a> ... follow all subpages, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '12, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-11763" class="comments-container">
&#10;</div>
<div id="comment-tools-11763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11763-form-container" class="comment-form-container">
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

