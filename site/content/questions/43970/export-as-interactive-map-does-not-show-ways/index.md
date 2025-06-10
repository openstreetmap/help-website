+++
type = "question"
title = "Export as interactive map does not show ways"
description = '''Hello when I do this request in overpass, I can see node and ways highlighted: node[&quot;name&quot;=&quot;Bures-sur-Yvette&quot;]; ( way  (around:5000)  [&quot;leisure&quot;=&quot;playground&quot;]; node  (around:5000)  [&quot;leisure&quot;=&quot;playground&quot;];  ); (._;&amp;gt;;); out;   but when I do export as interactive map, only nodes are highlighted wi...'''
date = "2015-07-04T08:38:00Z"
lastmod = "2015-07-04T09:48:00Z"
weight = 43970
keywords = [ "map", "export", "overpass-turbo", "interactive" ]
aliases = [ "/questions/43970" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export as interactive map does not show ways](/questions/43970/export-as-interactive-map-does-not-show-ways)

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
<span id="post-43970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43970-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello when I do this request in overpass, I can see node and ways highlighted:</p>
<pre><code>node[&quot;name&quot;=&quot;Bures-sur-Yvette&quot;];
(
way
  (around:5000)
  [&quot;leisure&quot;=&quot;playground&quot;];
node
  (around:5000)
  [&quot;leisure&quot;=&quot;playground&quot;];
  );
(._;&gt;;);
out;</code></pre>
<p><img src="http://snag.gy/AnuEj.jpg" alt="alt text" /></p>
<p>but when I do export as interactive map, only nodes are highlighted with a litlle circle, ways have no more circle on top of them</p>
<p><img src="http://snag.gy/PL2mc.jpg" alt="alt text" /></p>
<p>what's wrong ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-interactive" rel="tag" title="see questions tagged &#39;interactive&#39;">interactive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '15, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/475f485ebcd73adde35434f45410b449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bodtx&#39;s gravatar image" />
<p><span>bodtx</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bodtx has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '15, 08:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</img>
</div>
</div>
<div id="comments-container-43970" class="comments-container">
&#10;</div>
<div id="comment-tools-43970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43970-form-container" class="comment-form-container">
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

<span id="43973"></span>

<div id="answer-container-43973" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43973-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-43973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately, this is one of the features which are not yet implemented on the "interactive map" export option. See the following ticket on github: <a href="https://github.com/tyrasd/overpass-turbo/issues/23">https://github.com/tyrasd/overpass-turbo/issues/23</a></p>
<p>As a <a href="https://github.com/tyrasd/overpass-turbo/issues/169#issuecomment-103836754">workaround</a> you can try using the <code>out center</code> output mode of overpass API: <a href="http://overpass-turbo.eu/s/afT">http://overpass-turbo.eu/s/afT</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '15, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-43973" class="comments-container">
&#10;</div>
<div id="comment-tools-43973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43973-form-container" class="comment-form-container">
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

