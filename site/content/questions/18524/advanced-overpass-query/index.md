+++
type = "question"
title = "Advanced overpass query"
description = '''I have query: &amp;lt; area-query ref=&quot;3600438171&quot; /&amp;gt;  &amp;lt; recurse type=&quot;node-way&quot;/&amp;gt;  &amp;lt; union&amp;gt; &amp;lt;query type=&quot;way&quot;&amp;gt;  &amp;lt; item/&amp;gt;  &amp;lt; has-kv k=&quot;highway&quot; v=&quot;cycleway&quot; /&amp;gt;  &amp;lt; /query&amp;gt;  &amp;lt; recurse type=&quot;way-node&quot;/&amp;gt;  &amp;lt; /union&amp;gt;  &amp;lt; print mode=&quot;meta&quot; /&amp;gt;  I need help...'''
date = "2012-12-17T13:06:00Z"
lastmod = "2012-12-18T12:13:00Z"
weight = 18524
keywords = [ "overpass" ]
aliases = [ "/questions/18524" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Advanced overpass query](/questions/18524/advanced-overpass-query)

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
<span id="post-18524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18524-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have query:</p>
<pre><code>&lt; area-query ref=&quot;3600438171&quot; /&gt; 
&lt; recurse type=&quot;node-way&quot;/&gt; 
&lt; union&gt; &lt;query type=&quot;way&quot;&gt; 
&lt; item/&gt; 
&lt; has-kv k=&quot;highway&quot; v=&quot;cycleway&quot; /&gt; 
&lt; /query&gt; 
&lt; recurse type=&quot;way-node&quot;/&gt; 
&lt; /union&gt; 
&lt; print mode=&quot;meta&quot; /&gt;</code></pre>
<p>I need help with correct:</p>
<ul>
<li>how to get parent relation of way</li>
<li>how to get tag UNION, i.e. result with &lt; has-kv k="highway" v="cycleway" /&gt; OR &lt; has-kv k="cycleway" /&gt;</li>
</ul>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '12, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/66bf6007fa22ce69a29332e9737f0dfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hanoj&#39;s gravatar image" />
<p><span>hanoj</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hanoj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '12, 13:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-18524" class="comments-container">
&#10;</div>
<div id="comment-tools-18524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18524-form-container" class="comment-form-container">
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

<span id="18551"></span>

<div id="answer-container-18551" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18551-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hanoj has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get the union of both "highway=cycleway" and "cycleway", you can use a (nested) "union". Please note that we need a separate variable name "all_ways" in this case to use the found ways twice:</p>
<pre><code>    &lt;area-query ref=&quot;3600438171&quot;/&gt;
    &lt;recurse type=&quot;node-way&quot; into=&quot;all_ways&quot;/&gt;
    &lt;union&gt;
      &lt;union&gt;
        &lt;query type=&quot;way&quot;&gt;
          &lt;item set=&quot;all_ways&quot;/&gt;
          &lt;has-kv k=&quot;highway&quot; v=&quot;cycleway&quot;/&gt;
        &lt;/query&gt; 
        &lt;query type=&quot;way&quot;&gt;
          &lt;item set=&quot;all_ways&quot;/&gt;
          &lt;has-kv k=&quot;cycleway&quot;/&gt;
        &lt;/query&gt; 
      &lt;/union&gt;
      &lt;recurse type=&quot;way-node&quot;/&gt;
    &lt;/union&gt;
    &lt;print mode=&quot;meta&quot;/&gt;</code></pre>
<p>To get the parent relation of the way, please add a further recurse statement. This adds the parent relations only.</p>
<pre><code>    &lt;area-query ref=&quot;3600438171&quot;/&gt;
    &lt;recurse type=&quot;node-way&quot; into=&quot;all_ways&quot;/&gt;
    &lt;union&gt;
      &lt;union into=&quot;selected_ways&quot;&gt;
        &lt;query type=&quot;way&quot;&gt;
          &lt;item set=&quot;all_ways&quot;/&gt;
          &lt;has-kv k=&quot;highway&quot; v=&quot;cycleway&quot;/&gt;
        &lt;/query&gt; 
        &lt;query type=&quot;way&quot;&gt;
          &lt;item set=&quot;all_ways&quot;/&gt;
          &lt;has-kv k=&quot;cycleway&quot;/&gt;
        &lt;/query&gt; 
      &lt;/union&gt;
      &lt;recurse from=&quot;selected_ways&quot; type=&quot;way-relation&quot;/&gt;
      &lt;recurse from=&quot;selected_ways&quot; type=&quot;way-node&quot;/&gt;
    &lt;/union&gt;
    &lt;print mode=&quot;meta&quot;/&gt;</code></pre>
<p>If you want further the child elements of this parent relation, please add yet another recurse. But this can return very much data if you have hit a road network, a national border or another large relation:</p>
<pre><code>    &lt;area-query ref=&quot;3600438171&quot;/&gt;
    &lt;recurse type=&quot;node-way&quot; into=&quot;all_ways&quot;/&gt;
    &lt;union&gt;
      &lt;union into=&quot;selected_ways&quot;&gt;
        &lt;query type=&quot;way&quot;&gt;
          &lt;item set=&quot;all_ways&quot;/&gt;
          &lt;has-kv k=&quot;highway&quot; v=&quot;cycleway&quot;/&gt;
        &lt;/query&gt; 
        &lt;query type=&quot;way&quot;&gt;
          &lt;item set=&quot;all_ways&quot;/&gt;
          &lt;has-kv k=&quot;cycleway&quot;/&gt;
        &lt;/query&gt; 
      &lt;/union&gt;
      &lt;recurse from=&quot;selected_ways&quot; type=&quot;way-relation&quot;/&gt;
      &lt;recurse type=&quot;down&quot;/&gt;
      &lt;recurse from=&quot;selected_ways&quot; type=&quot;way-node&quot;/&gt;
    &lt;/union&gt;
    &lt;print mode=&quot;meta&quot;/&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '12, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-18551" class="comments-container">
<span id="18561"></span>
<div id="comment-18561" class="comment">
<div id="post-18561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanx for you!</p>
</div>
<div id="comment-18561-info" class="comment-info">
<span class="comment-age">(18 Dec '12, 12:13)</span> <span class="comment-user userinfo">hanoj</span>
</div>
</div>
</div>
<div id="comment-tools-18551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18551-form-container" class="comment-form-container">
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

