+++
type = "question"
title = "Buildings via overpass-turbo"
description = '''Hi. I am experiencing challenges querying buildings on a campus via overpass with [out:json][timeout:30]; area[name=&#x27;Cape Peninsula University of Technology (Bellville Campus)&#x27;]-&amp;gt;.a; (  (  // I want all buildings  way[building](area.a);   // plus every building:part  way[&quot;building:part&quot;](area.a);...'''
date = "2021-03-22T07:24:00Z"
lastmod = "2021-08-31T16:13:00Z"
weight = 79352
keywords = [ "building", "relation", "overpass-turbo", "multipolygon" ]
aliases = [ "/questions/79352" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Buildings via overpass-turbo](/questions/79352/buildings-via-overpass-turbo)

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
<span id="post-79352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79352-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I am experiencing challenges querying buildings on a campus via overpass with</p>
<pre><code>[out:json][timeout:30];
area[name=&#39;Cape Peninsula University of Technology (Bellville Campus)&#39;]-&gt;.a;
(
  (
    // I want all buildings
    way[building](area.a);
&#10;    // plus every building:part
    way[&quot;building:part&quot;](area.a);
  // and multipolygon relation ¬ to represent buildings with courtyards correctly
    relation[&quot;building&quot;][&quot;type&quot;=&quot;multipolygon&quot;](area.a);
  );
-
  // excluding buildings with relation type=building role=outline ¬ I want to correct form/height of the part
  (
    // for every way in the input set select the relations of which it is an &quot;outline&quot; member
    rel(bw:&quot;outline&quot;)[&quot;type&quot;=&quot;building&quot;];
    // back to the ways with role &quot;outline&quot;
    way(r:&quot;outline&quot;);
  );
);
out body;
&gt;;
out skel qt;</code></pre>
<p>three buildings are not being harvested correctly <a href="https://www.openstreetmap.org/relation/12469713">https://www.openstreetmap.org/relation/12469713</a>, <a href="https://www.openstreetmap.org/relation/12442311">https://www.openstreetmap.org/relation/12442311</a> and <a href="https://www.openstreetmap.org/relation/12445158">https://www.openstreetmap.org/relation/12445158</a> are <code>building:parts</code> with a courtyard (multipolygon relation <code>role=inner</code>) that exist within an <code>outline</code> <code>type=building</code> relation which contain the same courtyard. (i.e.: the courtyard is inside a <code>building:part</code> and the <code>role=outer</code> is coming with the query even though I’ve excluded the <code>outline</code>).</p>
<p>I want the form/shape and height of the <code>building:part</code> and not the outline; while being mindful of every other structure on the campus. How do I exclude the relation <code>type=multipolygon</code> <code>role=outer</code> when <code>type=building</code> <code>role=outline</code> already exists for a structure? Have I created the relations incorrectly? Your help is appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '21, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a235da08f7d6877654b16dfe832aed66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arkriger&#39;s gravatar image" />
<p><span>arkriger</span><br />
<span class="score" title="155 reputation points">155</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arkriger has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79352" class="comments-container">
<span id="81222"></span>
<div id="comment-81222" class="comment">
<div id="post-81222-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is now obvious the fault lies with how I tagged these features.</p>
<p>If we focus on <a href="https://www.openstreetmap.org/relation/12469713">Relation: 12469713</a> I don't know where the relation <code>type=building</code> <code>role=outline goes</code>.</p>
<p>I don't know.</p>
</div>
<div id="comment-81222-info" class="comment-info">
<span class="comment-age">(07 Aug '21, 16:38)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
<span id="81581"></span>
<div id="comment-81581" class="comment">
<div id="post-81581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>building:part multipolygon</code> relations were not accounted for - when a <code>building:part</code> has a courtyard.</p>
<p>adding: <code>relation["building:part"]["type"="multipolygon"](area.a);</code> to the <a href="https://overpass-turbo.eu/">query</a> (line 10) fixes it.</p>
</div>
<div id="comment-81581-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 16:13)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
</div>
<div id="comment-tools-79352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79352-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

