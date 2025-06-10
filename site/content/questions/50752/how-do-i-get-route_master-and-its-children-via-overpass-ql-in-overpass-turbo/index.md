+++
type = "question"
title = "How do I get route_master (and its children) via Overpass QL in overpass-turbo?"
description = '''Hi, I am new to OSM and trying to understand Overpass QL so editing of public Transport data in JOSM will be easier in the future. My Question is, why this Overpass QL query won&#x27;t give me any data, not even the data I just added myself? [out:json]; (  relation[&quot;type&quot;=&quot;route_master&quot;][&quot;route_master&quot;=&quot;...'''
date = "2016-07-09T11:14:00Z"
lastmod = "2016-08-17T12:00:00Z"
weight = 50752
keywords = [ "route_master", "bus", "route", "relations", "overpass-ql" ]
aliases = [ "/questions/50752" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I get route_master (and its children) via Overpass QL in overpass-turbo?](/questions/50752/how-do-i-get-route_master-and-its-children-via-overpass-ql-in-overpass-turbo)

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
<span id="post-50752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50752-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am new to OSM and trying to understand Overpass QL so editing of public Transport data in JOSM will be easier in the future.</p>
<p>My Question is, why this Overpass QL query won't give me any data, not even <a href="https://www.openstreetmap.org/relation/1729861">the data I just added myself</a>?</p>
<pre><code>[out:json];
(
  relation[&quot;type&quot;=&quot;route_master&quot;][&quot;route_master&quot;=&quot;bus&quot;](51.3649215, 9.2642212, 51.7134161, 9.810791);
);
rel(r);
way(r);
out meta qt;</code></pre>
<p>As far as I think, this query works this way:</p>
<ol>
<li>I ask for json-data (but xml won't work, either)</li>
<li>I like to get all relations in the bounding box which carry the tags type=route_master and route_master=bus</li>
<li>from that I recursively ask for all child-relations</li>
<li>and from that for child ways</li>
<li>(and even if I ask for child nodes, I won't get any data)</li>
<li>and then I print the result (with all data there is, geographically ordered (whatever this means) )</li>
</ol>
<p>So whats wrong with that query (or the data I added previously). Could anybody explain it to me?</p>
<p>P.S.: I just had to type this once again, because the wait for email-validation (after creating a new account) didn't seem to keep this question pending, but instead deleted it. P.P.S.: It is denglish I am writing. If there is a native english speaker here who cares for educating his or hers language: I am listening.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route_master" rel="tag" title="see questions tagged &#39;route_master&#39;">route_master</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '16, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/9783c8591af9a852805e5d69c461e828?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jannefleischer&#39;s gravatar image" />
<p><span>jannefleischer</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jannefleischer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50752" class="comments-container">
&#10;</div>
<div id="comment-tools-50752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50752-form-container" class="comment-form-container">
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

<span id="50753"></span>

<div id="answer-container-50753" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50753-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-50753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jannefleischer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tricky question ... :)</p>
<p>Master relations don't have any geometry on their own. That's why your query won't find anything for a given bounding box in step 2 already. I'm not sure if that's a bug or not, at least it doesn't work right now (<a href="https://github.com/drolbr/Overpass-API/issues/293">Github issue opened</a>).</p>
<p>I have changed that part of your query to include the network "NVV" and effectively turned it into a global scale query for route_master relations. That's purely a performance tweak to reduce the number of relevant master relations from 21862 down to 64.</p>
<p>Now, instead of applying the bounding box filter to the master relation, I'm using the individual bus routes via <code>(rel(r){{bbox}})</code> for that purpose. As those bus routes all have their proper geometry information, using the bounding box as a filter shouldn't be an issue anymore.</p>
<p><a href="http://overpass-turbo.eu/s/hdA">overpass turbo link</a></p>
<pre><code>[out:json];
relation[&quot;type&quot;=&quot;route_master&quot;][&quot;route_master&quot;=&quot;bus&quot;][network=&quot;NVV&quot;];
(rel(r)({{bbox}});&gt;;);
out meta;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '16, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '16, 12:26</strong> </span></p>
</div>
</div>
<div id="comments-container-50753" class="comments-container">
<span id="50755"></span>
<div id="comment-50755" class="comment">
<div id="post-50755-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks for your immediate response. I had my problems with the first revision of your answer, but now I think I understood. The problem is, that, since the relation master_route do not contain any geometries, I can't filter it with a bounding box. So I first have to get the sub-routes (tag: route) and use the bounding-box filter over those.</p>
<p>Thanks for pointing this out to me. It wasn't that trivial as I expected it to be, after all. :)</p>
<p>The wizard provides a template called (in german) „Hauptroute" which does it wrong, too. Reported it: <a href="https://github.com/tyrasd/overpass-turbo/issues/254">https://github.com/tyrasd/overpass-turbo/issues/254</a></p>
</div>
<div id="comment-50755-info" class="comment-info">
<span class="comment-age">(09 Jul '16, 12:28)</span> <span class="comment-user userinfo">jannefleischer</span>
</div>
</div>
<span id="51476"></span>
<div id="comment-51476" class="comment">
<div id="post-51476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just a note: this answer helped me create a query to render a relation and it's subrelations (queried by master relation ID): <a href="http://overpass-turbo.eu/s/hTR">http://overpass-turbo.eu/s/hTR</a></p>
</div>
<div id="comment-51476-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 10:20)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="51481"></span>
<div id="comment-51481" class="comment">
<div id="post-51481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10142/joost-schouppe">@joost schouppe</a>: <code>(relation(2099432);&gt;&gt;;);out body;</code> would be the usual approach, as you already have a relation id.</p>
</div>
<div id="comment-51481-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 11:53)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="51482"></span>
<div id="comment-51482" class="comment">
<div id="post-51482-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I noticed it does make a small difference: it also returns the tagged nodes that are members of the ways of the relations, whereas the other approach just returns member relations.</p>
</div>
<div id="comment-51482-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 12:00)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-50753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50753-form-container" class="comment-form-container">
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

