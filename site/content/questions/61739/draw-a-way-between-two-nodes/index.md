+++
type = "question"
title = "draw a way between two nodes"
description = '''Hello, I&#x27;m new in OSM and I want to create some queries, using overpass turbo. Is it possible to get a connected way between two nodes? For example I want to receive a part of a highway/motorhighway between two motorway junctions. Is this possible?  I only want to make queries on existing OSM data w...'''
date = "2018-01-20T16:40:00Z"
lastmod = "2018-01-27T10:26:00Z"
weight = 61739
keywords = [ "overpass", "nodes", "overpass-turbo", "export", "highway" ]
aliases = [ "/questions/61739" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [draw a way between two nodes](/questions/61739/draw-a-way-between-two-nodes)

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
<span id="post-61739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61739-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,<br />
I'm new in OSM and I want to create some queries, using overpass turbo.<br />
Is it possible to get a connected way between two nodes? For example I want to receive a part of a highway/motorhighway between two motorway junctions.<br />
Is this possible?</p>
<p>I only want to make queries on existing OSM data with overpass turbo.<br />
My first test looks like this:</p>
<pre><code>// select nodes:
(
node[name=&quot;Baiersdorf-Nord&quot;];
node[name=&quot;Erlangen-Nord&quot;];
);
(._;&gt;;);
out meta;
</code></pre>
<p>I would like to draw the highway and export the data between this nodes.<br />
Is this possible?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '18, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/715c13056959e6329a8ecf40ecf4a50e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JarJarDingsBums&#39;s gravatar image" />
<p><span>JarJarDingsBums</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JarJarDingsBums has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '18, 13:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></br></p>
</div>
</div>
<div id="comments-container-61739" class="comments-container">
<span id="61752"></span>
<div id="comment-61752" class="comment">
<div id="post-61752-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>hi, welcome to OSM! Do you want to add new data to OSM (draw) or do you want to make queries to the existing OSM data using overpass turbo? Can you provide an example query?</p>
</div>
<div id="comment-61752-info" class="comment-info">
<span class="comment-age">(20 Jan '18, 23:53)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="61755"></span>
<div id="comment-61755" class="comment">
<div id="post-61755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your reply! <span class="small">[moderator edit: text added to question text]</span></p>
</div>
<div id="comment-61755-info" class="comment-info">
<span class="comment-age">(21 Jan '18, 11:40)</span> <span class="comment-user userinfo">JarJarDingsBums</span>
</div>
</div>
<span id="61843"></span>
<div id="comment-61843" class="comment">
<div id="post-61843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi! Has anybody an idea?</p>
<p>Thanks.</p>
</div>
<div id="comment-61843-info" class="comment-info">
<span class="comment-age">(27 Jan '18, 10:26)</span> <span class="comment-user userinfo">JarJarDingsBums</span>
</div>
</div>
</div>
<div id="comment-tools-61739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61739-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

