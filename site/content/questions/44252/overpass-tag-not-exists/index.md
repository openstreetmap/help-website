+++
type = "question"
title = "Overpass tag not exists"
description = '''I&#x27;m trying to get the addresses that do not have a postal code but have the address information the code still selects ways/relations that have the postal code set already, but I want to select those that don&#x27;t exist/aren&#x27;t set. [out:json][timeout:2500]; {{geocodeArea:Gatineau}}-&amp;gt;.searchArea; // ...'''
date = "2015-07-18T12:20:00Z"
lastmod = "2015-07-19T20:00:00Z"
weight = 44252
keywords = [ "ways", "overpass", "relations", "empty" ]
aliases = [ "/questions/44252" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass tag not exists](/questions/44252/overpass-tag-not-exists)

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
<span id="post-44252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44252-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get the addresses that do not have a postal code but have the address information the code still selects ways/relations that have the postal code set already, but I want to select those that don't exist/aren't set.</p>
<pre><code>[out:json][timeout:2500];
{{geocodeArea:Gatineau}}-&gt;.searchArea;
// gather results
(
  // query part for: “&quot;addr:housenumber&quot;=*”
&#10;  (way[&quot;addr:housenumber&quot;](area.searchArea);relation[&quot;addr:housenumber&quot;](area.searchArea))-&gt;.a;
  way.a[&quot;addr:postcode&quot;~&quot;^$&quot;]({{bbox}});
  relation.a[&quot;addr:postcode&quot;~&quot;^$&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '15, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/55b745b283e8f1a78cd942c72b6021f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LogicalViolinist&#39;s gravatar image" />
<p><span>LogicalVioli...</span><br />
<span class="score" title="246 reputation points">246</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LogicalViolinist has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-44252" class="comments-container">
<span id="44271"></span>
<div id="comment-44271" class="comment">
<div id="post-44271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A bit off topic, but please do not add the postal code information to individual addresses in e.g. Flanders, Belgium. We have a complete set of postal code boundaries and that information has to be used to get a complete address. I think the same holds e.g. for Germany.</p>
</div>
<div id="comment-44271-info" class="comment-info">
<span class="comment-age">(19 Jul '15, 14:49)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="44276"></span>
<div id="comment-44276" class="comment">
<div id="post-44276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That may be well for europe, but in Canada, canada post wants to copyright postal codes and has sued geocder.ca for building a database against it. The lawsuit was eventually dropped, but what I wanted to get at is untill we have a full data population for a street I cannot trace said polygon as it can change midway through the street</p>
</div>
<div id="comment-44276-info" class="comment-info">
<span class="comment-age">(19 Jul '15, 20:00)</span> <span class="comment-user userinfo">LogicalVioli...</span>
</div>
</div>
</div>
<div id="comment-tools-44252" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44252-form-container" class="comment-form-container">
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

<span id="44265"></span>

<div id="answer-container-44265" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44265-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LogicalViolinist has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you're using the wizard in overpass turbo already, simply copy the following expression to the wizard popup:</p>
<pre><code>(&quot;addr:housenumber&quot;=* and &quot;addr:postcode&quot; is null) in Gatineau</code></pre>
<p>overpass turbo link: <a href="http://overpass-turbo.eu/s/auT">http://overpass-turbo.eu/s/auT</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '15, 08:50</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '15, 08:50</strong> </span></p>
</div>
</div>
<div id="comments-container-44265" class="comments-container">
&#10;</div>
<div id="comment-tools-44265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44265-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44260"></span>

<div id="answer-container-44260" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44260-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe this example can be helpful:</p>
<p>has-kv k="addr:city"</p>
<p>has-kv k="addr:postcode" modv="not" regv="."</p>
<p>This is looking for elements with addr_city=xxx and without addr:postcode.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '15, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-44260" class="comments-container">
&#10;</div>
<div id="comment-tools-44260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44260-form-container" class="comment-form-container">
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

