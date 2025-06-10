+++
type = "question"
title = "Overpass: count size of set"
description = '''Hi I&#x27;m selecting railway=station then searching 20m around them for any building that are not train_station. If there are none then I output the railway=station entity. How do I check if the .build set to see if it has no members?  Is there even a simpler way to achieve this? In this example:   Tott...'''
date = "2018-06-26T17:17:00Z"
lastmod = "2018-06-27T17:14:00Z"
weight = 64391
keywords = [ "count", "overpass", "set" ]
aliases = [ "/questions/64391" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: count size of set](/questions/64391/overpass-count-size-of-set)

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
<span id="post-64391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64391-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I'm selecting <code>railway=station</code> then searching 20m <code>around</code> them for any <code>building</code> that are not <code>train_station</code>. If there are none then I output the <code>railway=station</code> entity.</p>
<p>How do I check if the <code>.build</code> set to see if it has no members? Is there even a simpler way to achieve this?</p>
<p>In this example:</p>
<ul>
<li>Tottenham Court Road shouldn't display as it has no adjacent <code>building=train_station</code>.</li>
<li>Russell Square should display as it does.</li>
<li>Goodge Street should as it's both <code>building=train_station</code> and <code>railway=station</code>.</li>
</ul>
<p><a href="http://overpass-turbo.eu/s/zRH">http://overpass-turbo.eu/s/zRH</a></p>
<pre><code>[bbox:{{bbox}}];
nwr[railway=station]-&gt;.TStats;
foreach .TStats
(
 way(around:20)[building];
 way._[building!=train_station]-&gt;.build;
 if (.build.count(ways) == 0) 
  (.TStats out geom;)
);</code></pre>
<p>Edit: I spotted an error I my code, now rectified, but it doesn't help with the solution.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-set" rel="tag" title="see questions tagged &#39;set&#39;">set</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '18, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '18, 17:49</strong> </span></p>
</div>
</div>
<div id="comments-container-64391" class="comments-container">
<span id="64399"></span>
<div id="comment-64399" class="comment">
<div id="post-64399-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>(.TStats out geom;)</code> will output all members of the .TStats set, so the script will currently output the whole set for each one that matches the test.</p>
</div>
<div id="comment-64399-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 02:29)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="64403"></span>
<div id="comment-64403" class="comment">
<div id="post-64403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see. So is there a way to get the individual element of .TStats being processed by the foreach loop?</p>
</div>
<div id="comment-64403-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 11:33)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="64404"></span>
<div id="comment-64404" class="comment">
<div id="post-64404-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, take a look at <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#For-each_loop_.28foreach.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#For-each_loop_.28foreach.29</a> it shows how to name the loop variable.</p>
<p>I experimented a bit, the current test doesn't work with the variable fixed.</p>
</div>
<div id="comment-64404-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 12:20)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="64411"></span>
<div id="comment-64411" class="comment">
<div id="post-64411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><strong><em>Note I've updated the OP routine</em></strong> To test, I simplified the routine a bit: <a href="http://overpass-turbo.eu/s/zSZ">http://overpass-turbo.eu/s/zSZ</a> I've made it more verbose than it needs to be, to hopefully make it clearer. if you look on the data tab Tottenham shouldn't be displaying as the way count is 0. It seems to me the <code>if:count(ways)</code> line isn't filtering, but I'm unsure why. I took it from : <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Isolated_Buildings.">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Isolated_Buildings.</a> ----- Sorry, which variable shouldn't be fixed?</p>
</div>
<div id="comment-64411-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 16:54)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="64413"></span>
<div id="comment-64413" class="comment">
<div id="post-64413-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By variable fixed I meant I experimented with the initial script after correcting the issue with the looping variable.</p>
</div>
<div id="comment-64413-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 17:14)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-64391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64391-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

