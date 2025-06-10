+++
type = "question"
title = "getting a list of the location of all the Tesco supermarkets in the UK – many are misssing?!"
description = '''Hi I&#x27;d like to get a list of the location of all the Tesco supermarkets in the UK into excel. I&#x27;m running a query through Overpass Turbo but I&#x27;m not getting a full list of results. I shows ~600 nodes but I know there are over 3000 Tesco&#x27;s in the UK. Here is my query &amp;lt;osm-script output=&quot;xml&quot; timeo...'''
date = "2014-08-27T11:13:00Z"
lastmod = "2014-08-27T16:27:00Z"
weight = 36260
keywords = [ "overpass", "tesco", "supermarket", "uk" ]
aliases = [ "/questions/36260" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [getting a list of the location of all the Tesco supermarkets in the UK – many are misssing?!](/questions/36260/getting-a-list-of-the-location-of-all-the-tesco-supermarkets-in-the-uk-many-are-misssing)

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
<span id="post-36260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36260-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I'd like to get a list of the location of all the Tesco supermarkets in the UK into excel. I'm running a query through Overpass Turbo but I'm not getting a full list of results. I shows ~600 nodes but I know there are over 3000 Tesco's in the UK. Here is my query</p>
<pre><code>&lt;osm-script output=&quot;xml&quot; timeout=&quot;100000&quot;&gt;
  &lt;!-- gather results --&gt;
  &lt;union&gt;
    &lt;query type=&quot;way&quot;&gt;
      &lt;has-kv k=&quot;name&quot; v=&quot;Tesco&quot;/&gt;
      &lt;bbox-query {{bbox}}/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;!-- print results --&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot; order=&quot;quadtile&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>Am I missing something? Also - can I use a wildcard for the name search? It only returns stores with the exact name "Tesco" rather than "Tesco Express".</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-tesco" rel="tag" title="see questions tagged &#39;tesco&#39;">tesco</span> <span class="post-tag tag-link-supermarket" rel="tag" title="see questions tagged &#39;supermarket&#39;">supermarket</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '14, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/528cb6df0d6f29def77a43ff65d213e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dotman&#39;s gravatar image" />
<p><span>dotman</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dotman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '14, 12:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-36260" class="comments-container">
<span id="36263"></span>
<div id="comment-36263" class="comment">
<div id="post-36263-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Don't forget to include in your query type=node as well. Most of the smaller shops I tag are only nodes.</p>
</div>
<div id="comment-36263-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 11:49)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="36264"></span>
<div id="comment-36264" class="comment">
<div id="post-36264-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Added that. Results look much better now. Thanks</p>
</div>
<div id="comment-36264-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 11:59)</span> <span class="comment-user userinfo">dotman</span>
</div>
</div>
<span id="36289"></span>
<div id="comment-36289" class="comment">
<div id="post-36289-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you update your question or add an answer? Showing your new query will help other users having the same problem.</p>
</div>
<div id="comment-36289-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 16:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36260-form-container" class="comment-form-container">
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

<span id="36262"></span>

<div id="answer-container-36262" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36262-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-36262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Non-exact_names">wiki page</a> suggests you can get names that start Tesco by changing <code>v=</code> to <code>regv=</code> if I've understood correctly.</p>
<p>Also, it looks like you are only querying named ways, rather than also checking node POIs and relations.</p>
<p>Finally, I doubt all Tesco stores are mapped. <a href="http://taginfo.openstreetmap.org.uk/search?q=Tesco#values">Taginfo</a> can perhaps show you how many to expect</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '14, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '14, 11:50</strong> </span></p>
</div>
</div>
<div id="comments-container-36262" class="comments-container">
<span id="36286"></span>
<div id="comment-36286" class="comment">
<div id="post-36286-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Given that I added one yesterday, I also doubt that it was the last one to be mapped! <a href="http://www.openstreetmap.org/node/3043305147">http://www.openstreetmap.org/node/3043305147</a></p>
</div>
<div id="comment-36286-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 16:06)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-36262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36262-form-container" class="comment-form-container">
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

