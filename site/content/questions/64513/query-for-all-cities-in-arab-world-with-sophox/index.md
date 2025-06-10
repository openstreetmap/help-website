+++
type = "question"
title = "Query for all cities in Arab world with Sophox"
description = '''I&#x27;ve just discovered this new Sophox API. I would to get all cities (place=city) in the Arab World. I assume that it would be much easier to query for this using Wikidata than filtering the global dump. The arab countries have the following Wikidata IDs: Q79 Q262 Q1049 Q796 Q1028 Q851 Q805 Q858 Q104...'''
date = "2018-07-03T20:14:00Z"
lastmod = "2018-11-28T18:58:00Z"
weight = 64513
keywords = [ "sophox", "wikidata", "query" ]
aliases = [ "/questions/64513" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query for all cities in Arab world with Sophox](/questions/64513/query-for-all-cities-in-arab-world-with-sophox)

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
<span id="post-64513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64513-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've just discovered this new Sophox API.</p>
<p>I would to get all cities (place=city) in the Arab World. I assume that it would be much easier to query for this using Wikidata than filtering the global dump.</p>
<p>The arab countries have the following Wikidata IDs: Q79 Q262 Q1049 Q796 Q1028 Q851 Q805 Q858 Q1045 Q948 Q878 Q810 Q1016 Q1176995 Q822 Q842 Q817 Q1025 Q846 Q398 Q977 Q970</p>
<p>Is this possible and how would it look like? Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sophox" rel="tag" title="see questions tagged &#39;sophox&#39;">sophox</span> <span class="post-tag tag-link-wikidata" rel="tag" title="see questions tagged &#39;wikidata&#39;">wikidata</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '18, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/b081ac1f1126c32011d2c9cf57c2b430?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nehaj&#39;s gravatar image" />
<p><span>Nehaj</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nehaj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64513" class="comments-container">
<span id="66976"></span>
<div id="comment-66976" class="comment">
<div id="post-66976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>updated my reply with an example</p>
</div>
<div id="comment-66976-info" class="comment-info">
<span class="comment-age">(28 Nov '18, 18:58)</span> <span class="comment-user userinfo">nyuriks</span>
</div>
</div>
</div>
<div id="comment-tools-64513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64513-form-container" class="comment-form-container">
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

<span id="64544"></span>

<div id="answer-container-64544" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64544-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nehaj, updating my reply. Sophox is back up. Here's a sample query, but unfortunately it is very slow - I suspect it needs some <a href="https://wiki.blazegraph.com/wiki/index.php/FederatedQuery">federated query optimizations</a>:</p>
<pre><code>PREFIX wdt: &lt;http://www.wikidata.org/prop/direct/&gt;
PREFIX wd: &lt;http://www.wikidata.org/entity/&gt;
&#10;SELECT * WHERE {
  VALUES ?countries { wd:Q79 wd:Q262 wd:Q1049 wd:Q796 wd:Q1028 wd:Q851 wd:Q805 wd:Q858 wd:Q1045 wd:Q948 wd:Q878 wd:Q810 wd:Q1016 wd:Q1176995 wd:Q822 wd:Q842 wd:Q817 wd:Q1025 wd:Q846 wd:Q398 wd:Q977 wd:Q970 }
&#10;  ?osmid osmt:place &quot;city&quot; ;
         osmt:wikidata ?wd .
&#10;  SERVICE &lt;https://query.wikidata.org/sparql&gt; {
    ?wd wdt:P17 ?countries .
  }
&#10;} limit 10</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '18, 07:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d46d9a8875ccdaa0b3b39bf485df3ead?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyuriks&#39;s gravatar image" />
<p><span>nyuriks</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyuriks has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '18, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-64544" class="comments-container">
&#10;</div>
<div id="comment-tools-64544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64544-form-container" class="comment-form-container">
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

