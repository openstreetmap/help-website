+++
type = "question"
title = "Find all junction next to way which has the tag landuse=meadow"
description = '''Hello everybody, I try to create a request to find all junction next to way which has the tag landuse=meadow in a certain radius. // Find nodes up to 1000m around a point node(around:1000,49.0809183333 ,9.2923300000) -&amp;gt;.aroundnodes; way(bn.aroundnodes)[&quot;junction&quot;][&quot;roundabout&quot;][&quot;landuse&quot;=&quot;meadow&quot;...'''
date = "2018-06-26T08:37:00Z"
lastmod = "2018-06-27T06:15:00Z"
weight = 64375
keywords = [ "openstreetmap", "overpass-turbo" ]
aliases = [ "/questions/64375" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find all junction next to way which has the tag landuse=meadow](/questions/64375/find-all-junction-next-to-way-which-has-the-tag-landusemeadow)

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
<span id="post-64375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64375-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody,</p>
<p>I try to create a request to find all junction next to way which has the tag landuse=meadow in a certain radius.</p>
<pre><code>// Find nodes up to 1000m  around a point
node(around:1000,49.0809183333  ,9.2923300000)
-&gt;.aroundnodes;
way(bn.aroundnodes)[&quot;junction&quot;][&quot;roundabout&quot;][&quot;landuse&quot;=&quot;meadow&quot;]-&gt;.allways;
// determine nodes belonging to found ways
    node(w.allways)-&gt;.waynodes;
    ( 
    // determine intersection of all ways&#39; nodes and nodes around center point  
    node.waynodes.aroundnodes;  
    // and return ways (intersection is just a workaround for a bug)  
    way.allways.allways; 
    );
out;</code></pre>
<p>Where is my mistake? Help is much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '18, 08:37</strong></p>
<img src="https://secure.gravatar.com/avatar/dbcc94f4176dd0d253bf83871344cbff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gustav9999&#39;s gravatar image" />
<p><span>Gustav9999</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gustav9999 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64375" class="comments-container">
<span id="64386"></span>
<div id="comment-64386" class="comment">
<div id="post-64386-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also asked in the Forum: <a href="https://forum.openstreetmap.org/viewtopic.php?id=62827">https://forum.openstreetmap.org/viewtopic.php?id=62827</a></p>
</div>
<div id="comment-64386-info" class="comment-info">
<span class="comment-age">(26 Jun '18, 14:55)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="64401"></span>
<div id="comment-64401" class="comment">
<div id="post-64401-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah but I dont receive any help, sugesstions or an answer. What a great admin.</p>
</div>
<div id="comment-64401-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 06:15)</span> <span class="comment-user userinfo">Gustav9999</span>
</div>
</div>
</div>
<div id="comment-tools-64375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64375-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

