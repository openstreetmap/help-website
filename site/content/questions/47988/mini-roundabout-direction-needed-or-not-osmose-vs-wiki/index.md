+++
type = "question"
title = "Mini-roundabout direction - needed or not? Osmose vs wiki."
description = '''NB: I&#x27;m based in the UK, where (mini-)roundabouts go clockwise. I thought I&#x27;d fix some local map bugs though osmose. I notice that osmose flags this:  direction = clockwise  highway = mini_roundabout  with: Reverse roundabout Mini roundabout direction in this country is &quot;clockwise&quot; by default, usele...'''
date = "2016-02-07T09:44:00Z"
lastmod = "2016-02-11T15:08:00Z"
weight = 47988
keywords = [ "osmose", "roundabout" ]
aliases = [ "/questions/47988" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Mini-roundabout direction - needed or not? Osmose vs wiki.](/questions/47988/mini-roundabout-direction-needed-or-not-osmose-vs-wiki)

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
<span id="post-47988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47988-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>NB: I'm based in the UK, where (mini-)roundabouts go clockwise.</p>
<p>I thought I'd fix some local map bugs though osmose. I notice that osmose flags this:</p>
<pre><code>direction = clockwise 
highway = mini_roundabout</code></pre>
<p>with:</p>
<pre><code>Reverse roundabout
Mini roundabout direction in this country is &quot;clockwise&quot; by default, useless direction tag</code></pre>
<p>However, the wiki states that direction should be indicated on mini-roundabouts, as the default is anti-clockwise: <a href="https://wiki.openstreetmap.org/wiki/Tag:junction%3Droundabout">Tag:junction=roundabout</a> (see the examples)</p>
<p>Which is correct?</p>
<ul>
<li>If the direction is needed, osmose needs fixing, where can I file a bug report?</li>
<li>If the direction is not needed, the wiki needs updating in a few places.</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmose" rel="tag" title="see questions tagged &#39;osmose&#39;">osmose</span> <span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '16, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/5d86ce6a7f60ce7f4ae41ff45dee6de5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jack_B&#39;s gravatar image" />
<p><span>Jack_B</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jack_B has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47988" class="comments-container">
<span id="48045"></span>
<div id="comment-48045" class="comment">
<div id="post-48045-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I have now opened an issue on Osmose Github <a href="https://github.com/osm-fr/osmose-backend/issues/95">https://github.com/osm-fr/osmose-backend/issues/95</a></p>
</div>
<div id="comment-48045-info" class="comment-info">
<span class="comment-age">(10 Feb '16, 22:38)</span> <span class="comment-user userinfo">Jack_B</span>
</div>
</div>
</div>
<div id="comment-tools-47988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47988-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="48011"></span>

<div id="answer-container-48011" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48011-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jack_B has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In this case, Osmose and the OSM wiki disagree.</p>
<p>The OSM wiki says:</p>
<blockquote>
<p>Note that the default value for mini-roundabouts is anti-clockwise.</p>
</blockquote>
<p><em><a href="https://wiki.openstreetmap.org/wiki/Key:direction#Clockwise_and_anticlockwise">Key:direction on the wiki</a></em></p>
<p>and specifically on a page about the United Kingdom:</p>
<blockquote>
<p>Add highway=mini_roundabout to the intersection node where the mini roundabout is located. Also add direction=clockwise.</p>
</blockquote>
<p><em><a href="https://wiki.openstreetmap.org/wiki/Road_signs_in_the_United_Kingdom">Road signs in the United_Kingdom</a></em></p>
<p>Osmose, however, seems to use a different rule (from reading <a href="https://raw.githubusercontent.com/osm-fr/osmose-backend/1cb12fc9f796110422ca515bbdbfda2ef1667e63/plugins/TagFix_MultipleTag.py">its source code</a>):</p>
<p><em>Default value: "anti-clockwise" for countries that drive on the right, and "clockwise" for countries that drive on the left.</em></p>
<p><a href="https://github.com/osm-fr/osmose-backend/blob/9149580422d677ce9d4623bd9baf6d1cbc91084f/osmose_config.py">osmose_config.py</a> contains a list of countries with the side they drive on.</p>
<p>While Osmose's rule makes sense, I believe the Wiki should take precedence here. Also, when in doubt, I'd choose the simpler rule, so Wiki wins again.</p>
<p>So I'd advise to ignore Osmose's complaints, and file a bug on GitHub: <a href="https://github.com/osm-fr/osmose-backend">https://github.com/osm-fr/osmose-backend</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '16, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-48011" class="comments-container">
<span id="48012"></span>
<div id="comment-48012" class="comment">
<div id="post-48012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When adding a mini roundabout with potlatch2, in edit mode, the icon shows anti clockwise, but by default the node seems to be unset. when editing an unset ordinary roundabout setting oneway made it default to clockwise. (in GB we drive on left).</p>
</div>
<div id="comment-48012-info" class="comment-info">
<span class="comment-age">(09 Feb '16, 11:18)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-48011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48011-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48043"></span>

<div id="answer-container-48043" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48043-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My personal opinion is that it really doesn't matter whether a UK mini-roundabout is tagged as direction=clockwise or not. I wouldn't add direction=clockwise if the tag was missing or remove it if it was present.</p>
<p>An anti-clockwise mini-roundabout is far more likely to be a tagging error than a genuinely anti-clockwise mini-roundabout. There are currently 2 allegedly anti-clockwise mini-roundabouts in the UK - see <a href="http://overpass-turbo.eu/s/ekM">http://overpass-turbo.eu/s/ekM</a> .</p>
<p>If there were a significant number of genuine exceptions then it might be worth tagging it, but we don't tag "driving_side" throughout the UK just because Savoy Court <a href="https://www.openstreetmap.org/way/4253954">https://www.openstreetmap.org/way/4253954</a> is (famously) an exception to the side of the road we drive on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '16, 21:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-48043" class="comments-container">
<span id="48044"></span>
<div id="comment-48044" class="comment">
<div id="post-48044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a bit of extra info, here's an Overpass Turbo link for driving_side ways which covers most of the UK:</p>
<p><a href="http://overpass-turbo.eu/s/ekN">http://overpass-turbo.eu/s/ekN</a></p>
</div>
<div id="comment-48044-info" class="comment-info">
<span class="comment-age">(10 Feb '16, 21:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48043-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48058"></span>

<div id="answer-container-48058" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48058-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Any competent router should be aware which country the route is being created &amp; have appropriate rules built to suit, making the tagging pointless.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '16, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-48058" class="comments-container">
&#10;</div>
<div id="comment-tools-48058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48058-form-container" class="comment-form-container">
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

