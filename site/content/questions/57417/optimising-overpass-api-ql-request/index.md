+++
type = "question"
title = "optimising overpass API QL request"
description = '''Hello everyone, the query below works. I would have liked to optimize it so as to accelerate the result. Can you help me ? Thank you in advance. Mathieu http://overpass.mydevicexxx.com/api/interpreter?data=[out:json][timeout:25];(node(around:1000,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;amenity&quot;=&quot;parki...'''
date = "2017-08-01T18:24:00Z"
lastmod = "2017-08-01T20:52:00Z"
weight = 57417
keywords = [ "overpass", "optimization", "request", "ql" ]
aliases = [ "/questions/57417" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [optimising overpass API QL request](/questions/57417/optimising-overpass-api-ql-request)

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
<span id="post-57417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone, the query below works. I would have liked to optimize it so as to accelerate the result. Can you help me ? Thank you in advance. Mathieu</p>
<pre><code>http://overpass.mydevicexxx.com/api/interpreter?data=[out:json][timeout:25];(node(around:1000,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;amenity&quot;=&quot;parking&quot;]-&gt;.b;node(around:1000,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;amenity&quot;=&quot;school&quot;]-&gt;.c;node(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;amenity&quot;=&quot;townhall&quot;]-&gt;.d;way(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;amenity&quot;=&quot;townhall&quot;]-&gt;.d;relation(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;amenity&quot;=&quot;townhall&quot;]-&gt;.d;node(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;railway&quot;=&quot;subway_entrance&quot;]-&gt;.f;node(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;railway&quot;=&quot;tram_stop&quot;]-&gt;.g;node(around:1000,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;tourism&quot;=&quot;museum&quot;]-&gt;.h;node(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;highway&quot;=&quot;bus_stop&quot;]-&gt;.j;node(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;leisure&quot;=&quot;park&quot;]-&gt;.k;way(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;leisure&quot;=&quot;park&quot;]-&gt;.k;relation(around:500,48.84203354,2.790979589)[&quot;name&quot;~&quot;.&quot;][&quot;leisure&quot;=&quot;park&quot;]-&gt;.k;);.b out qt tags 1;&gt;;.c out qt tags 1;&gt;;.d out qt tags 1;&gt;;.f out qt tags 1;&gt;;.g out qt tags 1;&gt;;.h out qt tags 1;&gt;;.j out qt tags 1;&gt;;.k out qt tags 1;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-optimization" rel="tag" title="see questions tagged &#39;optimization&#39;">optimization</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-ql" rel="tag" title="see questions tagged &#39;ql&#39;">ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '17, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb03db977326117a75fb9a84b79f3e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdk83&#39;s gravatar image" />
<p><span>mdk83</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdk83 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '17, 07:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-57417" class="comments-container">
<span id="57421"></span>
<div id="comment-57421" class="comment">
<div id="post-57421-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can already simplify your query a bit by using "<code>|</code>" in queries, which acts like "a or b" -&gt; "a|b", and "<code>~</code>" (tilde) instead of "<code>=</code>". For example: <code>["amenity"~"parking|school"]</code> -- Not sure how much that will speed up the process though and what your desired result should look like.</p>
</div>
<div id="comment-57421-info" class="comment-info">
<span class="comment-age">(01 Aug '17, 20:52)</span> <span class="comment-user userinfo">chrki</span>
</div>
</div>
</div>
<div id="comment-tools-57417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57417-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

