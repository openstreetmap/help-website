+++
type = "question"
title = "Buildings from multiple campuses with the same operator"
description = '''Hi; I am experiencing challenges harvesting building from a university with many campuses. The campuses are linked with a relation type=site and tagged amenity=university and the sites themselves are named uniquely while the operator= is the same.  [out:json];  area[name=&quot;Western Cape&quot;]-&amp;gt;.b; way(...'''
date = "2021-02-25T15:58:00Z"
lastmod = "2022-04-02T14:22:00Z"
weight = 79032
keywords = [ "building", "operator", "university", "relation", "overpass-turbo" ]
aliases = [ "/questions/79032" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Buildings from multiple campuses with the same operator](/questions/79032/buildings-from-multiple-campuses-with-the-same-operator)

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
<span id="post-79032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79032-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi; I am experiencing challenges harvesting <code>building</code> from a university with many campuses. The campuses are linked with a relation <code>type=site</code> and tagged <code>amenity=university</code> and the sites themselves are named uniquely while the <code>operator=</code> is the same.</p>
<pre><code>[out:json];
&#10;area[name=&quot;Western Cape&quot;]-&gt;.b;
way(area.b)[operator=&#39;Cape Peninsula University of Technology&#39;];
map_to_area -&gt; .a;
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>Executes correctly and returns the sites but</p>
<pre><code>[out:json];
&#10;area[name=&quot;Western Cape&quot;]-&gt;.b;
way(area.b)[operator=&#39;Cape Peninsula University of Technology&#39;];
map_to_area -&gt; .a;
&#10;way[&quot;building&quot;](area.a);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>does not return isolated buildings. Only buildings that are enclosed within <code>University Grounds</code> are returned and buildings not on <em>"traditional"</em> grounds are excluded - this is even though isolated buildings are <code>University Grounds</code>. How must the query change to accommodate isolated buildings not on <em>"traditional"</em> <code>University Grounds</code>? Are the <code>Tags</code> effective or should these change? Must <code>University Grounds</code> be a separate area bigger than features - such as <code>building</code> - it contains?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-operator" rel="tag" title="see questions tagged &#39;operator&#39;">operator</span> <span class="post-tag tag-link-university" rel="tag" title="see questions tagged &#39;university&#39;">university</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '21, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a235da08f7d6877654b16dfe832aed66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arkriger&#39;s gravatar image" />
<p><span>arkriger</span><br />
<span class="score" title="155 reputation points">155</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arkriger has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '21, 11:20</strong> </span></p>
</div>
</div>
<div id="comments-container-79032" class="comments-container">
<span id="84068"></span>
<div id="comment-84068" class="comment">
<div id="post-84068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please advise if I should open a separate question:</p>
<p>I believe the 'amenity=university' on each campus including the <a href="https://www.openstreetmap.org/relation/12344662">site relation</a> is unnecessary. I should delete the 'amenity=university' on each campus and leave only the 'amenity=university' on the relation.</p>
<p>Is this correct?</p>
</div>
<div id="comment-84068-info" class="comment-info">
<span class="comment-age">(02 Apr '22, 09:19)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
<span id="84083"></span>
<div id="comment-84083" class="comment">
<div id="post-84083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No I would not do that site relations are relatively uncommon &amp; therefore not often consumed (for instance I don't believe the main Carto-OSM render consumes them, in which case all labelling of Western Cape sites would cease).</p>
</div>
<div id="comment-84083-info" class="comment-info">
<span class="comment-age">(02 Apr '22, 13:17)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79032-form-container" class="comment-form-container">
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

<span id="84084"></span>

<div id="answer-container-84084" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84084-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="arkriger has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many of the buildings are mapped as multipolygons so you need to <a href="https://overpass-turbo.eu/s/1hl7">include</a> <code>relation(area.a)["building"]</code> too. I'm seeing isolated buildings mapped as ways, such as <a href="https://www.openstreetmap.org/way/253456002">253456002</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '22, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-84084" class="comments-container">
<span id="84085"></span>
<div id="comment-84085" class="comment">
<div id="post-84085-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<pre><code>[out:json][timeout:30];
&#10;(area[name=&quot;Western Cape&quot;] -&gt;.b;
way(area.b)[operator=&quot;Cape Peninsula University of Technology&quot;];
map_to_area -&gt; .a;
 way[&#39;building&#39;](area.a);
 relation[&quot;building&quot;][&quot;type&quot;=&quot;multipolygon&quot;](area.a);
);
out body;
&gt;;
out skel qt;</code></pre>
<p>might do the necessary. I'll confirm at a later date. Thank you.</p>
</div>
<div id="comment-84085-info" class="comment-info">
<span class="comment-age">(02 Apr '22, 14:22)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
</div>
<div id="comment-tools-84084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84084-form-container" class="comment-form-container">
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

