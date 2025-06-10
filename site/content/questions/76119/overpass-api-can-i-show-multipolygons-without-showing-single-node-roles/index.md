+++
type = "question"
title = "Overpass API - Can I show multipolygons without showing single-node roles?"
description = '''I am trying to output a map of British Columbia&#x27;s regional districts using the Overpass API. I tried the following code on overpass-turbo.eu, and got a bit of a messy map. [out:json][timeout:90]; ( relation[admin_level=6](area:3600390867); ); out body; &amp;gt;; out skel qt;  What I want to do is hide a...'''
date = "2020-08-15T00:59:00Z"
lastmod = "2020-08-19T04:58:00Z"
weight = 76119
keywords = [ "boundary", "relation", "multipolygon" ]
aliases = [ "/questions/76119" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API - Can I show multipolygons without showing single-node roles?](/questions/76119/overpass-api-can-i-show-multipolygons-without-showing-single-node-roles)

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
<span id="post-76119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76119-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to output a map of British Columbia's regional districts using the Overpass API. I tried the following code on overpass-turbo.eu, and got a bit of a messy map.</p>
<pre><code>[out:json][timeout:90];
(
relation[admin_level=6](area:3600390867);
);
out body;
&gt;;
out skel qt;</code></pre>
<p>What I want to do is hide all of those single nodes that have roles in each of these relations, i.e., I want to see each multipolygon area depicted in yellow, but I want to hide the nodes that have "admin_centre" and "label" roles. I have not figured out a way to do this. Can anyone help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '20, 00:59</strong></p>
<img src="https://secure.gravatar.com/avatar/fd3f710d06987dc73153b9a1e836929a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DENelson83&#39;s gravatar image" />
<p><span>DENelson83</span><br />
<span class="score" title="18 reputation points">18</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DENelson83 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76119" class="comments-container">
&#10;</div>
<div id="comment-tools-76119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76119-form-container" class="comment-form-container">
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

<span id="76201"></span>

<div id="answer-container-76201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76201-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is closer. There's an Overpass Turbo map setting to not show the small areas as nodes, which gets even closer.</p>
<p><a href="http://overpass-turbo.eu/s/XbB">http://overpass-turbo.eu/s/XbB</a></p>
<pre><code>[out:json][timeout:90];
(
relation[admin_level=6](area:3600390867);
);
out body;
way(r);
(._;&gt;;);
out skel qt;
{{style:
area{
  color:#e99;
  width:2;
  opacity:0.8;
  fill-color:#c77;
  fill-opacity:0.3;
}
}}</code></pre>
<p>The OSM data is output in a few pieces here. <code>out body;</code> emits the relation data. Then only the way members of the relations are retrieved by <code>way(r);</code> (as in the other answer). Then the nodes needed to draw those ways are retrieved by <code>(._;&gt;;);</code>. The ways and nodes are then emitted in <code>out skel qt;</code>. Using <code>out skel;</code> doesn't emit tags, so the nodes and ways output in that line are only used to construct the relation geometries, they aren't also interpreted as features in their own right. I put the <code>{{style::...}}</code> directive in there to show it was possible to adjust the display, if you like the default colors, just delete that part.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '20, 01:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '20, 01:58</strong> </span></p>
</div>
</div>
<div id="comments-container-76201" class="comments-container">
<span id="76203"></span>
<div id="comment-76203" class="comment">
<div id="post-76203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow! That is much cleaner. I was unaware that overpass-turbo allows for CSS fine-tuning of its output. Thank you for pointing this out.</p>
</div>
<div id="comment-76203-info" class="comment-info">
<span class="comment-age">(19 Aug '20, 04:58)</span> <span class="comment-user userinfo">DENelson83</span>
</div>
</div>
</div>
<div id="comment-tools-76201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76201-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76157"></span>

<div id="answer-container-76157" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76157-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>rel[admin_level=6](area:3600390867);
way(r);
out geom;</code></pre>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29</a></p>
<p>Tip: to receive more answers add 'overpass' to the the tags list when asking a Q.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '20, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-76157" class="comments-container">
<span id="76175"></span>
<div id="comment-76175" class="comment">
<div id="post-76175-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Except that looks even more hideous when depicted on overpass-turbo.eu, and none of the areas get coloured yellow.</p>
</div>
<div id="comment-76175-info" class="comment-info">
<span class="comment-age">(17 Aug '20, 22:41)</span> <span class="comment-user userinfo">DENelson83</span>
</div>
</div>
<span id="76182"></span>
<div id="comment-76182" class="comment">
<div id="post-76182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry I spoke. You clearly think you know best. You're on you own.</p>
</div>
<div id="comment-76182-info" class="comment-info">
<span class="comment-age">(18 Aug '20, 14:20)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-76157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76157-form-container" class="comment-form-container">
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

