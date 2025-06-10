+++
type = "question"
title = "how can i get all the residential nodes in a specific region in overpass turbo?"
description = '''I&#x27;m new to osm queries and I explore it using overpass turbo so I&#x27;m trying that gets a specific way with a predefine id the code looks like this if anyone would like to test [bbox:40.73112,-73.89061,40.73391,-73.88807]; // gather results (  way(5703091); ); // print results out body; &amp;gt;; out skel ...'''
date = "2020-12-20T16:53:00Z"
lastmod = "2020-12-20T23:07:00Z"
weight = 78017
keywords = [ "openstreetmap", "overpass", "overpass-turbo" ]
aliases = [ "/questions/78017" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how can i get all the residential nodes in a specific region in overpass turbo?](/questions/78017/how-can-i-get-all-the-residential-nodes-in-a-specific-region-in-overpass-turbo)

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
<span id="post-78017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78017-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to osm queries and I explore it using overpass turbo so I'm trying that gets a specific way with a predefine id the code looks like this if anyone would like to test</p>
<pre><code>[bbox:40.73112,-73.89061,40.73391,-73.88807];
// gather results
(
  way(5703091);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>when I did explore the XML file in the data view I saw that this way contain all of these nodes that make the way &lt; way id="5703091"&gt; &lt; nd ref="42839143"/&gt; &lt; nd ref="8219742075"/&gt; &lt; nd ref="42807002"/&gt; &lt; nd ref="42839146"/&gt; &lt; nd ref="42839155"/&gt; &lt; nd ref="42839161"/&gt; &lt; nd ref="42839168"/&gt; &lt; nd ref="2875111804"/&gt; &lt; nd ref="42839172"/&gt;</p>
<p>so is there a way to show these nodes in the map view without assign each one individually with the query i try to use node(5703091); but office didn't work since it is a way</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '20, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/00b20ea2eb5708a716896e0d335050f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabeeqasem&#39;s gravatar image" />
<p><span>rabeeqasem</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabeeqasem has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78017" class="comments-container">
&#10;</div>
<div id="comment-tools-78017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78017-form-container" class="comment-form-container">
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

<span id="78021"></span>

<div id="answer-container-78021" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78021-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rabeeqasem has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Recurse: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29</a></p>
<pre><code>way(5703091);
node(w);
out center;</code></pre>
<p>Will display the nodes.</p>
<p>What's strange is this routine should display all the nodes &amp; way, but only loads the start &amp; end ones:</p>
<pre><code>way(5703091)-&gt;.Way;
node(w.Way);
out center;
.Way out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '20, 23:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-78021" class="comments-container">
<span id="78022"></span>
<div id="comment-78022" class="comment">
<div id="post-78022-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you so much</p>
</div>
<div id="comment-78022-info" class="comment-info">
<span class="comment-age">(20 Dec '20, 23:07)</span> <span class="comment-user userinfo">rabeeqasem</span>
</div>
</div>
</div>
<div id="comment-tools-78021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78021-form-container" class="comment-form-container">
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

