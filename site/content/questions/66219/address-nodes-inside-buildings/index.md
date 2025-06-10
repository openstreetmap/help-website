+++
type = "question"
title = "Address nodes inside buildings"
description = '''How can I find nodes with &quot;addr:housenumber&quot; inside buildings with Overpass? I&#x27;ve found this snippet, but it doesn&#x27;t work: way[building=yes]  ({{bbox}});  (node(around:0)[&quot;addr:housenumber&quot;~&quot;.&quot;];  node(w);); out meta; '''
date = "2018-10-08T16:40:00Z"
lastmod = "2018-10-09T08:26:00Z"
weight = 66219
keywords = [ "overpass", "address" ]
aliases = [ "/questions/66219" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Address nodes inside buildings](/questions/66219/address-nodes-inside-buildings)

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
<span id="post-66219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66219-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I find nodes with "addr:housenumber" inside buildings with Overpass? I've found this snippet, but it doesn't work:</p>
<pre><code>way[building=yes]
   ({{bbox}});
   (node(around:0)[&quot;addr:housenumber&quot;~&quot;.&quot;];
    node(w););
out meta;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '18, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/6e9f60277459f11b6d1f5ecc386088b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norske&#39;s gravatar image" />
<p><span>Norske</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norske has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66219" class="comments-container">
<span id="66239"></span>
<div id="comment-66239" class="comment">
<div id="post-66239-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just curious, why do you need this query?</p>
</div>
<div id="comment-66239-info" class="comment-info">
<span class="comment-age">(09 Oct '18, 07:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66219-form-container" class="comment-form-container">
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

<span id="66226"></span>

<div id="answer-container-66226" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66226-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, here's a script that will get you <em>some</em> results, but it isn't really correct:</p>
<pre><code>[timeout:30];
way[building]({{bbox}});
( 
  node(around:5)[&quot;addr:housenumber&quot;];
);
out meta;</code></pre>
<p>Some things to note:</p>
<ul>
<li>Rather than just <code>building=yes</code>, I'm just checking if the <code>building</code> tag exists, so it will work with <code>building=school</code>, <code>building=apartments</code>, etc.</li>
<li>Rather than using a regex match on the <code>addr:housenumber</code> tag, I'm again simply checking that the tag exists, which is more efficient.</li>
<li>I've used a value of 5 meters for the <code>around()</code> filter. This will find all address nodes within 5 meters of... something. Truth is, I don't really understand how <code>around()</code> works with ways. It doesn't mean within 5 meters of the interior. If it did, 0 (or at least 1) would work. By trial-and-error, it doesn't seem to mean within 5 meters of the center, either. Nonetheless, if you're dealing with larger buildings, you may have to increase this number to catch the address nodes -- at the risk of false positives, if there are address nodes outside but near the buildings.</li>
</ul>
<p>If there's a way to actually filter whats inside the perimeters of the buildings, rather than using <code>around()</code> to find what's nearby, I'd love to see that script.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '18, 21:24</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '18, 21:30</strong> </span></p>
</div>
</div>
<div id="comments-container-66226" class="comments-container">
<span id="66227"></span>
<div id="comment-66227" class="comment">
<div id="post-66227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But with around I can't really check whether the node is inside or outside: <a href="https://overpass-turbo.eu/s/CBX">https://overpass-turbo.eu/s/CBX</a></p>
</div>
<div id="comment-66227-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 21:52)</span> <span class="comment-user userinfo">Norske</span>
</div>
</div>
<span id="66233"></span>
<div id="comment-66233" class="comment">
<div id="post-66233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's right -- it gives both false positives and false negatives. That's why I said it isn't really correct. I'd like to know the correct answer too, if there is one!</p>
</div>
<div id="comment-66233-info" class="comment-info">
<span class="comment-age">(09 Oct '18, 00:54)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="66242"></span>
<div id="comment-66242" class="comment">
<div id="post-66242-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This enhancement request may be relevant <a href="https://github.com/drolbr/Overpass-API/issues/77">https://github.com/drolbr/Overpass-API/issues/77</a></p>
</div>
<div id="comment-66242-info" class="comment-info">
<span class="comment-age">(09 Oct '18, 08:26)</span> <span class="comment-user userinfo">andrewblack</span>
</div>
</div>
</div>
<div id="comment-tools-66226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66226-form-container" class="comment-form-container">
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

