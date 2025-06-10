+++
type = "question"
title = "Map preview on facebook"
description = '''Hello, is possible to make preview maps when i post link on facebook ? Some map providers ( mapy.cz ) can do this. Look. https://imgur.com/a/2JjIBhl'''
date = "2019-05-11T14:03:00Z"
lastmod = "2019-05-14T11:18:00Z"
weight = 69160
keywords = [ "facebook", "share" ]
aliases = [ "/questions/69160" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Map preview on facebook](/questions/69160/map-preview-on-facebook)

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
<span id="post-69160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69160-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, is possible to make preview maps when i post link on facebook ? Some map providers ( mapy.cz ) can do this. Look.</p>
<p><a href="https://imgur.com/a/2JjIBhl">https://imgur.com/a/2JjIBhl</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-facebook" rel="tag" title="see questions tagged &#39;facebook&#39;">facebook</span> <span class="post-tag tag-link-share" rel="tag" title="see questions tagged &#39;share&#39;">share</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '19, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/4388bfc57cdcb698acc16a9bc787b948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pschonmann&#39;s gravatar image" />
<p><span>pschonmann</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pschonmann has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69160" class="comments-container">
<span id="69161"></span>
<div id="comment-69161" class="comment">
<div id="post-69161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you provide a bit more information about what you'd actually like to happen? Not everyone is familiar with Facebook and I'm not sure exactly what you mean by a "preview map".</p>
</div>
<div id="comment-69161-info" class="comment-info">
<span class="comment-age">(11 May '19, 15:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69162"></span>
<div id="comment-69162" class="comment">
<div id="post-69162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you paste link in comment field, you can see something like thumbnail, preview of your link. If you paste osm link you see only link to osm.org and big icon. Would be nice to see part of map instead.</p>
</div>
<div id="comment-69162-info" class="comment-info">
<span class="comment-age">(11 May '19, 16:45)</span> <span class="comment-user userinfo">pschonmann</span>
</div>
</div>
</div>
<div id="comment-tools-69160" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69160-form-container" class="comment-form-container">
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

<span id="69185"></span>

<div id="answer-container-69185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69185-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-69185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Preview maps like this are indicated to Facebook by a series of 'meta tags' in the HEAD of an HTML document, for example:</p>
<pre><code>&lt;meta property=&#39;og:title&#39; content=&quot;Charlbury-Lechlade&quot;&gt;
&lt;meta property=&#39;og:description&#39; content=&quot;A 20mi cycle route planned on cycle.travel.&quot;&gt;
&lt;meta property=&#39;og:image&#39; content=&#39;http://cycle.travel/generated/cards/101313.jpg&#39;&gt;</code></pre>
<p>(The "OG" stands for "Open Graph".)</p>
<p>Only one image can be supplied, whereas OSM maps are actually made up of many images tiled together. We wouldn't want to get into specially rendering images just for Facebook previews, so I doubt we'd want to supply a composite image for this purpose. <em>However</em>, it might be an acceptable substitute to (for example) simply supply the tile corresponding to the centre point of the map, zoomed out one or two levels.</p>
<p>If you think this would be a worthwhile change, the place to suggest it is at <a href="https://github.com/openstreetmap/openstreetmap-website/issues">https://github.com/openstreetmap/openstreetmap-website/issues</a> , or better still, supply working code at <a href="https://github.com/openstreetmap/openstreetmap-website/pulls">https://github.com/openstreetmap/openstreetmap-website/pulls</a> . I'd recommend you include a link to this question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '19, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-69185" class="comments-container">
&#10;</div>
<div id="comment-tools-69185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69185-form-container" class="comment-form-container">
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

