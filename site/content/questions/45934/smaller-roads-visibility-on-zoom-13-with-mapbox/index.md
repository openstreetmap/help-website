+++
type = "question"
title = "Smaller roads visibility on zoom &lt;13 with mapbox"
description = '''Hey, I&#x27;m trying to show up smallers roads like service, path etc on smaller zooms like &amp;lt;10. Using mapbox and default sources is impossible i think.. #roads[class=&quot;service&quot;]{  [zoom&amp;lt;13]{line-width:1; line-color:red} }  There is any possibility to do it? '''
date = "2015-10-16T09:48:00Z"
lastmod = "2015-10-19T10:49:00Z"
weight = 45934
keywords = [ "roads", "zoom", "mapbox" ]
aliases = [ "/questions/45934" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Smaller roads visibility on zoom \<13 with mapbox](/questions/45934/smaller-roads-visibility-on-zoom-13-with-mapbox)

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
<span id="post-45934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45934-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>I'm trying to show up smallers roads like service, path etc on smaller zooms like &lt;10.</p>
<p>Using mapbox and default sources is impossible i think..</p>
<pre><code>#roads[class=&quot;service&quot;]{
  [zoom&lt;13]{line-width:1; line-color:red}
}</code></pre>
<p>There is any possibility to do it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '15, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d41c90d48f91727f281db7038d633a4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="k0n0pka&#39;s gravatar image" />
<p><span>k0n0pka</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="k0n0pka has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '15, 19:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45934" class="comments-container">
&#10;</div>
<div id="comment-tools-45934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45934-form-container" class="comment-form-container">
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

<span id="45945"></span>

<div id="answer-container-45945" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45945-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If Mapbox Studio's default (vector tile-backed) data source doesn't include small roads at z13, then you have a handful of choices:</p>
<ul>
<li>Set up your own rendering stack: switch2osm.org explains how to set up a traditional raster renderer</li>
<li>Contact an alternative commercial supplier such as <a href="http://www.thunderforest.com/">Thunderforest</a>, who may be able to supply different vector tiles</li>
<li>Create your own vector tiles with a utility like <a href="http://github.com/systemed/tilemaker">Tilemaker</a>, which has the detail you want at these zoom levels, and serve them</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '15, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-45945" class="comments-container">
<span id="45973"></span>
<div id="comment-45973" class="comment">
<div id="post-45973-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"and serve them", how i can import it as source to mapbox studio?</p>
</div>
<div id="comment-45973-info" class="comment-info">
<span class="comment-age">(18 Oct '15, 12:40)</span> <span class="comment-user userinfo">k0n0pka</span>
</div>
</div>
<span id="45988"></span>
<div id="comment-45988" class="comment">
<div id="post-45988-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I believe you can specify a custom tile URL using the 'Change source' option in Mapbox Studio. If you are hosting your own tiles, you will need to serve the tiles to this URL. The mbtileserver.rb tool in Tilemaker is a simple example of how to do this.</p>
<p>If all of this sounds like gobbledegook, it might be worth you contacting either Mapbox or Thunderforest to see if they can meet your needs.</p>
</div>
<div id="comment-45988-info" class="comment-info">
<span class="comment-age">(19 Oct '15, 10:49)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45945-form-container" class="comment-form-container">
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

