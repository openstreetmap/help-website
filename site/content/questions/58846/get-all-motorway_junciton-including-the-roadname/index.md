+++
type = "question"
title = "Get all motorway_junciton including the roadname"
description = '''Hello, I would like to get all motorway junctions with their roadnames. At the moment, I&#x27;m using this: [timeout:3600][maxsize:1073741824][bbox:{{bbox}}]; way[highway~&quot;^(motorway)$&quot;]; node(w)[highway=motorway_junction]; (._;&amp;gt;;); out meta;  Which works, but it gives me the following output: {  &quot;typ...'''
date = "2017-08-28T12:22:00Z"
lastmod = "2017-08-28T13:57:00Z"
weight = 58846
keywords = [ "overpass", "api", "name", "road", "highway" ]
aliases = [ "/questions/58846" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get all motorway_junciton including the roadname](/questions/58846/get-all-motorway_junciton-including-the-roadname)

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
<span id="post-58846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58846-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to get all motorway junctions with their roadnames. At the moment, I'm using this:</p>
<pre><code>[timeout:3600][maxsize:1073741824][bbox:{{bbox}}];
way[highway~&quot;^(motorway)$&quot;];
node(w)[highway=motorway_junction];
(._;&gt;;);
out meta;</code></pre>
<p>Which works, but it gives me the following output:</p>
<pre><code>{
  &quot;type&quot;: &quot;Feature&quot;,
  &quot;properties&quot;: {
    &quot;@id&quot;: &quot;node/9200769&quot;,
    &quot;highway&quot;: &quot;motorway_junction&quot;,
    &quot;name&quot;: &quot;Kreuz Rostock&quot;,
    &quot;ref&quot;: &quot;9&quot;,
    &quot;@timestamp&quot;: &quot;2015-04-09T06:46:01Z&quot;,
    &quot;@version&quot;: &quot;10&quot;,
    &quot;@changeset&quot;: &quot;30082198&quot;,
    &quot;@user&quot;: &quot;da-sch&quot;,
    &quot;@uid&quot;: &quot;200139&quot;
  },
  &quot;geometry&quot;: {
    &quot;type&quot;: &quot;Point&quot;,
    &quot;coordinates&quot;: [
      12.1994746,
      54.0327681
    ]
  },
  &quot;id&quot;: &quot;node/9200769&quot;</code></pre>
<p>I can't find any information, which says, on which road this junciton is. I do not mean the destination road. In my example it would be the road(highway) "A20". For testing i'm using overpass turbo.</p>
<p>Could somebody please help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '17, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/fdc1128d8c973d21ccae9fc5bf612091?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_supersonic&#39;s gravatar image" />
<p><span>_supersonic</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_supersonic has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58846" class="comments-container">
<span id="58847"></span>
<div id="comment-58847" class="comment">
<div id="post-58847-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you asking about the data model, or about the overpass syntax?</p>
<p>As to data model, "A 20" is the value of the <code>destination:ref=*</code> tag on the highway=motorway_link road that <a href="https://www.openstreetmap.org/node/9200769">node 9200769</a> is part of. I don't know the overpass syntax for requesting that information.</p>
</div>
<div id="comment-58847-info" class="comment-info">
<span class="comment-age">(28 Aug '17, 12:55)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
</div>
<div id="comment-tools-58846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58846-form-container" class="comment-form-container">
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

<span id="58849"></span>

<div id="answer-container-58849" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58849-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>node(w)</code> here means you are only fetching <code>motorway_junction</code> nodes that are part of a <code>highway=motorway</code> (or <code>motorway_link</code>; this is subtlety different than <em>all</em> <code>motorway_junction</code> nodes).</p>
<pre><code>way[highway~&quot;^(motorway)$&quot;];
node(w)[highway=motorway_junction];</code></pre>
<p>I think there is no way to get Overpass to amend the nodes with information from the parent ways, but you can at least return the ways as part of your Overpass query and then use the node ids to find information about parent ways:</p>
<pre><code>[timeout:3600][maxsize:1073741824][bbox:{{bbox}}];
(
way[highway~&quot;^(motorway)$&quot;];
node(w)[highway=motorway_junction];
);
out meta;</code></pre>
<p>Overpass Turbo might warn that this query is broken because it doesn't return the full geometries of the ways, but if I understand correctly you don't care about the way geometry, so just ignore the warning.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '17, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-58849" class="comments-container">
&#10;</div>
<div id="comment-tools-58849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58849-form-container" class="comment-form-container">
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

