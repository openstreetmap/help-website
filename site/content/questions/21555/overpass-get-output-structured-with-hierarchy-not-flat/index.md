+++
type = "question"
title = "Overpass get output structured (with hierarchy, not flat ?)"
description = '''I have the following script working so that in the resulting file I get a list of all districts and their ways and their nodes and the nodes themselves (but in the file it&#x27;s in reverse order and with a flat hierarchy) &amp;lt;osm-script&amp;gt;  &amp;lt;query type=&quot;relation&quot;&amp;gt;  &amp;lt;has-kv k=&quot;admin_level&quot; v=&quot;9...'''
date = "2013-04-15T20:45:00Z"
lastmod = "2013-04-16T17:14:00Z"
weight = 21555
keywords = [ "hierarchy", "overpass", "structured", "output" ]
aliases = [ "/questions/21555" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass get output structured (with hierarchy, not flat ?)](/questions/21555/overpass-get-output-structured-with-hierarchy-not-flat)

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
<span id="post-21555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21555-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the following script working so that in the resulting file I get a list of all districts and their ways and their nodes and the nodes themselves (but in the file it's in reverse order and with a flat hierarchy)</p>
<pre><code>&lt;osm-script&gt;
  &lt;query type=&quot;relation&quot;&gt;
    &lt;has-kv k=&quot;admin_level&quot; v=&quot;9&quot;/&gt;
    &lt;bbox-query e=&quot;1&quot; n=&quot;2&quot; s=&quot;3&quot; w=&quot;4&quot;/&gt;
  &lt;/query&gt;
  &lt;union&gt;
    &lt;item /&gt;
    &lt;recurse type=&quot;relation-way&quot;/&gt;
  &lt;/union&gt;
  &lt;union&gt;
    &lt;item /&gt;
    &lt;recurse type=&quot;way-node&quot;/&gt;
  &lt;/union&gt;
  &lt;print /&gt;
&lt;/osm-script&gt;</code></pre>
<p>Now I can't figure out how to get this structured, so that in the end it's not flat but so that the relation nodes have their member nodes (type="way"), and so that the member nodes themselves have long-lat nodes (all structured)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-structured" rel="tag" title="see questions tagged &#39;structured&#39;">structured</span> <span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '13, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/889a2f870eec6bc61e706e0de1645b6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeWo&#39;s gravatar image" />
<p><span>SeWo</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeWo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '13, 21:02</strong> </span></p>
</div>
</div>
<div id="comments-container-21555" class="comments-container">
&#10;</div>
<div id="comment-tools-21555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21555-form-container" class="comment-form-container">
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

<span id="21568"></span>

<div id="answer-container-21568" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21568-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suggest</p>
<pre><code>&lt;osm-script&gt;
  &lt;query type=&quot;relation&quot;&gt;
    &lt;has-kv k=&quot;admin_level&quot; v=&quot;9&quot;/&gt;
    &lt;bbox-query e=&quot;1&quot; n=&quot;2&quot; s=&quot;3&quot; w=&quot;4&quot;/&gt;
  &lt;/query&gt;
  &lt;foreach&gt;
    &lt;print /&gt;
    &lt;recurse type=&quot;relation-way&quot;/&gt;
    &lt;union&gt;
      &lt;item /&gt;
      &lt;recurse type=&quot;way-node&quot;/&gt;
    &lt;/union&gt;
    &lt;print /&gt;
  &lt;/foreach&gt;
&lt;/osm-script&gt;</code></pre>
<p>This prints for each relation first the relation and then the ways and nodes belonging to this relation. Ways and nodes that belong to more than one relation are repeated to appear after each relation where they belong to.</p>
<p>You can even do the same thing with the ways:</p>
<pre><code>&lt;osm-script&gt;
  &lt;query type=&quot;relation&quot;&gt;
    &lt;has-kv k=&quot;admin_level&quot; v=&quot;9&quot;/&gt;
    &lt;bbox-query e=&quot;1&quot; n=&quot;2&quot; s=&quot;3&quot; w=&quot;4&quot;/&gt;
  &lt;/query&gt;
  &lt;foreach&gt;
    &lt;print /&gt;
    &lt;recurse type=&quot;relation-way&quot;/&gt;
    &lt;foreach&gt;
      &lt;print /&gt;
      &lt;recurse type=&quot;way-node&quot;/&gt;
      &lt;print /&gt;
    &lt;/foreach&gt;
    &lt;print /&gt;
  &lt;/foreach&gt;
&lt;/osm-script&gt;</code></pre>
<p>Or let the ways and relations appear after their members:</p>
<pre><code>&lt;osm-script&gt;
  &lt;query type=&quot;relation&quot;&gt;
    &lt;has-kv k=&quot;admin_level&quot; v=&quot;9&quot;/&gt;
    &lt;bbox-query e=&quot;1&quot; n=&quot;2&quot; s=&quot;3&quot; w=&quot;4&quot;/&gt;
  &lt;/query&gt;
  &lt;foreach&gt;
    &lt;recurse type=&quot;relation-way&quot; into=&quot;ways&quot;/&gt;
    &lt;foreach from=&quot;ways&quot; into=&quot;way&quot;&gt;
      &lt;recurse type=&quot;way-node&quot; from=&quot;way&quot; into=&quot;nodes&quot;/&gt;
      &lt;print from=&quot;nodes&quot;/&gt;
      &lt;print from=&quot;way&quot;/&gt;
    &lt;/foreach&gt;
    &lt;print from=&quot;ways&quot;/&gt;
    &lt;print /&gt;
  &lt;/foreach&gt;
&lt;/osm-script&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '13, 06:20</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-21568" class="comments-container">
<span id="21576"></span>
<div id="comment-21576" class="comment">
<div id="post-21576-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Again, note that as a way can belong to multiple relations and nodes can belong to multiple ways and relations, the resulting file will likely be bigger (and take longer to generate) than the flat version.</p>
<p>The hierarchy you're looking for doesn't exist in that form in OSM; depending on what you do, it might be less error-prone to embrace the OSM data structure directly.</p>
</div>
<div id="comment-21576-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 09:23)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="21601"></span>
<div id="comment-21601" class="comment">
<div id="post-21601-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well it really builds some structures, but it's not what I wanted... I guess I'll build a script that parses all the data, builds a data-structure itself and then writes my kml file which is what I need in the end</p>
</div>
<div id="comment-21601-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 17:14)</span> <span class="comment-user userinfo">SeWo</span>
</div>
</div>
<span id="21602"></span>
<div id="comment-21602" class="comment">
<div id="post-21602-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks anyway ;)</p>
</div>
<div id="comment-21602-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 17:14)</span> <span class="comment-user userinfo">SeWo</span>
</div>
</div>
</div>
<div id="comment-tools-21568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21568-form-container" class="comment-form-container">
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

