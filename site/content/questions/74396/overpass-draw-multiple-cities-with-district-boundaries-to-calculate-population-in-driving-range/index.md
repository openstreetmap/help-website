+++
type = "question"
title = "overpass draw multiple cities with district boundaries, to calculate population in driving range"
description = '''Hi there, I want to draw the city(including district) boundaries on Overpass, including district and Xian boundaries.  I want to draw the city, district, and County(Xian in China) level boundaries of those cities: Shanghai, Suzhou, Wuxi, Changzhou, Huzhou, Jiaxing, Hangzhou, Shaoxing and Ningbo. Ple...'''
date = "2020-04-27T07:01:00Z"
lastmod = "2020-04-27T07:01:00Z"
weight = 74396
keywords = [ "boundaries", "overpass", "china", "population" ]
aliases = [ "/questions/74396" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [overpass draw multiple cities with district boundaries, to calculate population in driving range](/questions/74396/overpass-draw-multiple-cities-with-district-boundaries-to-calculate-population-in-driving-range)

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
<span id="post-74396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74396-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, I want to draw the city(including district) boundaries on Overpass, including district and Xian boundaries.</p>
<p>I want to draw the city, district, and County(Xian in China) level boundaries of those cities: Shanghai, Suzhou, Wuxi, Changzhou, Huzhou, Jiaxing, Hangzhou, Shaoxing and Ningbo. Please help. please</p>
<p>I have tried this code for each province, JS, SH, ZJ</p>
<pre><code>[out:xml][timeout:45];
area[&quot;ISO3166-2&quot;=&quot;CN-AH&quot;]-&gt;.a;
(relation(area.a)[&quot;admin_level&quot;=6][boundary=&quot;administrative&quot;];);
out meta;
&gt;;
out meta qt;</code></pre>
<p>But what I really want is more detailed district level boundaries of several cities: Shanghai, Suzhou, Wuxi, Changzhou, Huzhou, Jiaxing, Hangzhou, Shaoxing and Ningbo. and Xuancheng</p>
<p>And using that data with the year population data, I think I can calculate the population of a 2 hour driving range which cuts those district boundaries.</p>
<p>Please help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-china" rel="tag" title="see questions tagged &#39;china&#39;">china</span> <span class="post-tag tag-link-population" rel="tag" title="see questions tagged &#39;population&#39;">population</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '20, 07:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1e1ce4fc4e5cfdefa2e6c481eeee176b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CliffHU&#39;s gravatar image" />
<p><span>CliffHU</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CliffHU has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '20, 07:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-74396" class="comments-container">
&#10;</div>
<div id="comment-tools-74396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74396-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

