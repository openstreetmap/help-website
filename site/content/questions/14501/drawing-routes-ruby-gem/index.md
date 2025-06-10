+++
type = "question"
title = "[closed] drawing routes, ruby gem"
description = '''Hello. I&#x27;ve created ruby gem for drawing routes on OpenStreetMap maps. Hope it would be useful. https://github.com/akwiatkowski/gpx2exif How to use:  - Cli:  gpx2png -g spec/fixtures/sample.gpx -s 800x600 -o map.png # image size gpx2png -g spec/fixtures/sample.gpx -z 11 -o map.png # zoom    Ruby cod...'''
date = "2012-07-23T12:36:00Z"
lastmod = "2012-07-24T16:26:00Z"
weight = 14501
keywords = [ "ruby" ]
aliases = [ "/questions/14501" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] drawing routes, ruby gem](/questions/14501/drawing-routes-ruby-gem)

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
<span id="post-14501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14501-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-14501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>I've created ruby gem for drawing routes on OpenStreetMap maps. Hope it would be useful. <a href="https://github.com/akwiatkowski/gpx2exif">https://github.com/akwiatkowski/gpx2exif</a></p>
<p>How to use: - Cli:</p>
<blockquote>
<pre><code>gpx2png -g spec/fixtures/sample.gpx    -s 800x600 -o map.png # image size
gpx2png -g spec/fixtures/sample.gpx    -z 11 -o map.png # zoom</code></pre>
</blockquote>
<ul>
<li>Ruby code:</li>
</ul>
<blockquote>
<pre><code>g = GpxUtils::TrackImporter.new
g.add_file(&#39;sample.gpx&#39;)
e = Gpx2png::Osm.new
e.coords = g.coords
e.zoom = 8
e.save(&#39;output.png&#39;)</code></pre>
</blockquote>
<p>more <a href="https://github.com/akwiatkowski/gpx2exif/blob/master/spec/gpx2png/osm_spec.rb">https://github.com/akwiatkowski/gpx2exif/blob/master/spec/gpx2png/osm_spec.rb</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ruby" rel="tag" title="see questions tagged &#39;ruby&#39;">ruby</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '12, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/9c980de1d89c9eda9cbe366c24562978?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobik314&#39;s gravatar image" />
<p><span>bobik314</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobik314 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>24 Jul '12, 17:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-14501" class="comments-container">
<span id="14544"></span>
<div id="comment-14544" class="comment">
<div id="post-14544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What about publishing your code even in the OSM wiki, the OSM forum or to one or more of the OSM mailing lists?</p>
<p>Because this is "only" an FAQ site ...</p>
</div>
<div id="comment-14544-info" class="comment-info">
<span class="comment-age">(24 Jul '12, 16:26)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-14501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14501-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Not a question. Please use the mailing list, forum, wiki or irc to announce your tool." by scai 24 Jul '12, 17:31

</div>

</div>

</div>

