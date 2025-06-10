+++
type = "question"
title = "How to easy export osm data in csv"
description = '''For example:  I want to export the position, Street and names of all fire hydrants of my city in a spreadsheet or csv file? How can I do that? Is there an easy web frontend to configure and download the export? Or do I have to code?'''
date = "2018-12-18T08:27:00Z"
lastmod = "2018-12-18T12:52:00Z"
weight = 67260
keywords = [ "data", "csv", "export", "spreadseet" ]
aliases = [ "/questions/67260" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to easy export osm data in csv](/questions/67260/how-to-easy-export-osm-data-in-csv)

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
<span id="post-67260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67260-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example: I want to export the position, Street and names of all fire hydrants of my city in a spreadsheet or csv file? How can I do that? Is there an easy web frontend to configure and download the export? Or do I have to code?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-spreadseet" rel="tag" title="see questions tagged &#39;spreadseet&#39;">spreadseet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '18, 08:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c255fbf9350ffffb0fd8605abb13dc70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vale&#39;s gravatar image" />
<p><span>Vale</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vale has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67260" class="comments-container">
<span id="67261"></span>
<div id="comment-67261" class="comment">
<div id="post-67261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am experimenting with <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> For example I try to get all glass containers in a city.</p>
<p>qith the query I get all recycling related points: // query part for: “recycling” node<a href="area.searchArea">"amenity"="recycling"</a>; way<a href="area.searchArea">"amenity"="recycling"</a>; relation<a href="area.searchArea">"amenity"="recycling"</a>;</p>
<p>How do I get only the glass containers?</p>
</div>
<div id="comment-67261-info" class="comment-info">
<span class="comment-age">(18 Dec '18, 08:52)</span> <span class="comment-user userinfo">Vale</span>
</div>
</div>
</div>
<div id="comment-tools-67260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67260-form-container" class="comment-form-container">
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

<span id="67263"></span>

<div id="answer-container-67263" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67263-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-67263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you've already found out (for not all too large areas) the overpass api or the overpass-turbo frontend is likely the best choice.</p>
<p>If you need to refine your searches you should consult the wiki for information on the objects and how they are tagged (and yes there may be a couple of variants that you will need to consider).</p>
<p>For your example <a href="http://overpass-turbo.eu/s/EC5">http://overpass-turbo.eu/s/EC5</a></p>
<pre><code>/*
This has been generated by the overpass-turbo wizard.
The original search was:
“amenity=recycling and recycling_type=container and &quot;recycling:glass_bottles&quot;=yes”
*/
[out:json][timeout:25];
// gather results
(
  // query part for: “amenity=recycling and recycling_type=container and &quot;recycling:glass_bottles&quot;=yes”
  node[&quot;amenity&quot;=&quot;recycling&quot;][&quot;recycling_type&quot;=&quot;container&quot;][&quot;recycling:glass_bottles&quot;=&quot;yes&quot;]({{bbox}});
  way[&quot;amenity&quot;=&quot;recycling&quot;][&quot;recycling_type&quot;=&quot;container&quot;][&quot;recycling:glass_bottles&quot;=&quot;yes&quot;]({{bbox}});
  relation[&quot;amenity&quot;=&quot;recycling&quot;][&quot;recycling_type&quot;=&quot;container&quot;][&quot;recycling:glass_bottles&quot;=&quot;yes&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>To get CSV output you will need to directly use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">overpass-api</a> and specify that you want CSV output.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '18, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '18, 12:20</strong> </span></p>
</div>
</div>
<div id="comments-container-67263" class="comments-container">
<span id="67265"></span>
<div id="comment-67265" class="comment">
<div id="post-67265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've added the Overpass API query to your answer in case overpass-turbo becomes (temporarily) unavailable.</p>
</div>
<div id="comment-67265-info" class="comment-info">
<span class="comment-age">(18 Dec '18, 11:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="67266"></span>
<div id="comment-67266" class="comment">
<div id="post-67266-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can get csv in overpass turbo, by replaceing [out:json] like this:</p>
<p>[out:csv (::id, ::lat,::lon, "recycling_type","recycling:glass_bottles")]</p>
</div>
<div id="comment-67266-info" class="comment-info">
<span class="comment-age">(18 Dec '18, 12:52)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67263-form-container" class="comment-form-container">
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

