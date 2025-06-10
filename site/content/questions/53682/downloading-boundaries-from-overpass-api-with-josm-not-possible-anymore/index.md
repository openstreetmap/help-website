+++
type = "question"
title = "Downloading Boundaries from Overpass API with  JOSM not possible anymore?"
description = '''Hi, in the past I was able to download only the administrative boundary relations/ways of a country/large area by using JOSM and add this Overpass request: [timeout:180]; ( way[&quot;boundary&quot;=&quot;administrative&quot;]; node(w); rel(bn)-&amp;gt;.x; way(bn); rel(bw); ); out meta;  but now it seems the server is alway...'''
date = "2016-12-23T10:12:00Z"
lastmod = "2016-12-25T02:03:00Z"
weight = 53682
keywords = [ "boundaries", "overpass", "xapi" ]
aliases = [ "/questions/53682" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Downloading Boundaries from Overpass API with JOSM not possible anymore?](/questions/53682/downloading-boundaries-from-overpass-api-with-josm-not-possible-anymore)

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
<span id="post-53682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53682-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, in the past I was able to download only the administrative boundary relations/ways of a country/large area by using JOSM and add this Overpass request:</p>
<pre><code>[timeout:180];
(
way[&quot;boundary&quot;=&quot;administrative&quot;];
node(w);
rel(bn)-&gt;.x;
way(bn);
rel(bw);
);
out meta;</code></pre>
<p>but now it seems the server is always failing contacting the server and it ends up failing. Can anybody help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Dec '16, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/987c49ec23024986ddcb6f907ec58250?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="capiscuas&#39;s gravatar image" />
<p><span>capiscuas</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="capiscuas has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Dec '16, 11:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-53682" class="comments-container">
&#10;</div>
<div id="comment-tools-53682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53682-form-container" class="comment-form-container">
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

<span id="53709"></span>

<div id="answer-container-53709" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53709-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your code doesn't work for me either, but... For Denmark (the country north of Germany) the solution is now as simple as entering "<strong>boundary=administrative &amp; type:relation in Danmark</strong>" in the first field in JOSM's "<em>Download from Overpass API</em>" view, click the "<em>create query</em>" button and then finally the "<em>Download</em>" button.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Dec '16, 02:03</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Dec '16, 11:11</strong> </span></p>
</div>
</div>
<div id="comments-container-53709" class="comments-container">
&#10;</div>
<div id="comment-tools-53709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53709-form-container" class="comment-form-container">
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

