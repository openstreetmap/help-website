+++
type = "question"
title = "english city name in overpass turbo request"
description = '''hi all,  i have a list of city names in english, i want to export road lengths. using the below syntax, but it doesn&#x27;t give results for cities like Copenhagen since it&#x27;s different than the local name. any advices here? i tried name:en, but didn&#x27;t work.  &quot;Dedicated cycle lanes&quot;: &quot;&quot;&quot; [out:json]; area[...'''
date = "2023-04-27T14:03:00Z"
lastmod = "2023-04-27T14:22:00Z"
weight = 87180
keywords = [ "city", "overpass-turbo", "name", "overpass" ]
aliases = [ "/questions/87180" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [english city name in overpass turbo request](/questions/87180/english-city-name-in-overpass-turbo-request)

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
<span id="post-87180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87180-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi all, i have a list of city names in english, i want to export road lengths. using the below syntax, but it doesn't give results for cities like Copenhagen since it's different than the local name. any advices here? i tried name:en, but didn't work.</p>
<pre><code>&quot;Dedicated cycle lanes&quot;: &quot;&quot;&quot;
[out:json];
area[name=&#39;{city}&#39;]-&gt;.a;
way[highway=cycleway][bicycle=designated](area.a);
(._;&gt;;);
out geom;
&quot;&quot;&quot;,</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '23, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f9c301431095d1df657ac7d9558bef2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ozlem_&#39;s gravatar image" />
<p><span>ozlem_</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ozlem_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '23, 14:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-87180" class="comments-container">
&#10;</div>
<div id="comment-tools-87180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87180-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="87181"></span>

<div id="answer-container-87181" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87181-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try <em>name:en</em> For larger cities this should always be populated, <em>int_name</em> could work too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '23, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-87181" class="comments-container">
&#10;</div>
<div id="comment-tools-87181" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87181-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87182"></span>

<div id="answer-container-87182" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87182-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You would need to use 'name:en' not name:en for hstore tags.</p>
<p>Example:</p>
<pre><code>[out:json];
area[&#39;name:en&#39;=&#39;Rome&#39;]-&gt;.a;
way[highway=cycleway][bicycle=designated](area.a);
(._;&gt;;);
out geom;</code></pre>
<p>Though for Copenhagen, it does not seem to have any bicycle=designated cycleways. Maybe they use different tagging in Copenhagen?</p>
<p>But the above overpass turbo code works for e.g. Rome, Berlin or Munich (Munich example: <a href="http://overpass-turbo.eu/s/1uiK">http://overpass-turbo.eu/s/1uiK</a> ).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '23, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '23, 15:13</strong> </span></p>
</div>
</div>
<div id="comments-container-87182" class="comments-container">
&#10;</div>
<div id="comment-tools-87182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87182-form-container" class="comment-form-container">
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

