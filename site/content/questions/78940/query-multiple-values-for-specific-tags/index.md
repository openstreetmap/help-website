+++
type = "question"
title = "Query multiple values for specific tags"
description = '''Hello, I&#x27;m trying to query all the &quot;mall&quot; and &quot;department_store&quot; for the key &quot;shop&quot; using the Overpass API and the following query: [out:json]; area[name=&quot;London&quot;]; nwr[&#x27;shop&#x27;=&#x27;department_store&#x27;](area); out center; nwr[&#x27;shop&#x27;=&#x27;mall&#x27;](area); out center;  This however gives me only department_store be...'''
date = "2021-02-19T12:27:00Z"
lastmod = "2021-02-19T15:04:00Z"
weight = 78940
keywords = [ "shop", "overpass", "tags" ]
aliases = [ "/questions/78940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query multiple values for specific tags](/questions/78940/query-multiple-values-for-specific-tags)

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
<span id="post-78940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78940-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to query all the "mall" and "department_store" for the key "shop" using the Overpass API and the following query:</p>
<pre><code>[out:json];
area[name=&quot;London&quot;];
nwr[&#39;shop&#39;=&#39;department_store&#39;](area);
out center;
nwr[&#39;shop&#39;=&#39;mall&#39;](area);
out center;</code></pre>
<p>This however gives me only department_store because I put it first. So, basically it returns only the first shop I ask.</p>
<p>I also tried with the pyrosm package from Python. When I query for all shops it returns around 3330 records, but when I query to get both all shops and some amenities the records are less which doesn't make sense.</p>
<p>Any help please? :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '21, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/78ca4faede71449fd93c1790b87d816d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Katerina_Kourou&#39;s gravatar image" />
<p><span>Katerina_Kourou</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Katerina_Kourou has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '21, 13:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-78940" class="comments-container">
&#10;</div>
<div id="comment-tools-78940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78940-form-container" class="comment-form-container">
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

<span id="78943"></span>

<div id="answer-container-78943" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78943-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-78943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The result of the first shop query is stored in the default set, which the second query is written to use for the search area. Storing the area results to a named set makes it available for multiple queries:</p>
<pre><code>[out:json];
area[name=&quot;London&quot;]-&gt;.search;
nwr[&#39;shop&#39;=&#39;department_store&#39;](area.search);
out center;
nwr[&#39;shop&#39;=&#39;mall&#39;](area.search);
out center;</code></pre>
<p>In general, any statement without a named result set is stored in the default set, and any statement that takes an input (like <code>area</code>) will use the default set if a named set is not specified.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '21, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '21, 13:44</strong> </span></p>
</div>
</div>
<div id="comments-container-78943" class="comments-container">
<span id="78946"></span>
<div id="comment-78946" class="comment">
<div id="post-78946-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This worked! Thanks a lot :)</p>
</div>
<div id="comment-78946-info" class="comment-info">
<span class="comment-age">(19 Feb '21, 15:04)</span> <span class="comment-user userinfo">Katerina_Kourou</span>
</div>
</div>
</div>
<div id="comment-tools-78943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78943-form-container" class="comment-form-container">
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

