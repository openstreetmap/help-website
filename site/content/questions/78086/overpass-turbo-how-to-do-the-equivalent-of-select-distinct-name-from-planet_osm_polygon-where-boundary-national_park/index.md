+++
type = "question"
title = "Overpass Turbo: How to do the equivalent of &quot;SELECT distinct name FROM planet_osm_polygon WHERE (boundary = &#x27;national_park&#x27;);&quot;"
description = '''In psql it&#x27;s easy to do a query like &quot;SELECT distinct name FROM planet_osm_polygon WHERE (boundary = &#x27;national_park&#x27;);&quot; to return the names of national parks from a database. What&#x27;s the equivalent in Overpass Turbo? Various area selection methods exist such as &quot;geocodeArea:Great Britain}}-&amp;gt;.searc...'''
date = "2020-12-28T17:17:00Z"
lastmod = "2021-01-05T13:42:00Z"
weight = 78086
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/78086" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Turbo: How to do the equivalent of "SELECT distinct name FROM planet_osm_polygon WHERE (boundary = 'national_park');"](/questions/78086/overpass-turbo-how-to-do-the-equivalent-of-select-distinct-name-from-planet_osm_polygon-where-boundary-national_park)

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
<span id="post-78086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In psql it's easy to do a query like "<code>SELECT distinct name FROM planet_osm_polygon WHERE (boundary = 'national_park');</code>" to return the names of national parks from a database. What's the equivalent in Overpass Turbo?</p>
<p>Various area selection methods exist such as "geocodeArea:Great Britain}}-&gt;.searchArea" followed by adding "(area.searchArea)" before the semicolon, but let's assume for now that a simple "<code>({{bbox}})</code>" query would work.</p>
<p>The link from taginfo, once I've commented out nodes and ways and added "<code>({{bbox}})</code>" gets me to <a href="https://overpass-turbo.eu/s/11DZ">https://overpass-turbo.eu/s/11DZ</a> , but that's a visual query - I don't want the constituent ways, I don't want a map and I want a list of unique names (actually, to start with, just the number of items in the list).</p>
<p>There are some pages linked from <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">https://wiki.openstreetmap.org/wiki/Overpass_turbo</a> , but a search suggests there's nothing directly useful to me there.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '20, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-78086" class="comments-container">
&#10;</div>
<div id="comment-tools-78086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78086-form-container" class="comment-form-container">
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

<span id="78088"></span>

<div id="answer-container-78088" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78088-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This might not cover the DISTINCT bit, but change the top of your query from [out:json] to something like the example below?</p>
<pre><code>[out:csv(&quot;name&quot;)][timeout:25];
// gather results
(
  // query part for: “protect_class=5”
  //node[&quot;protect_class&quot;=&quot;5&quot;]({{bbox}});
  //way[&quot;protect_class&quot;=&quot;5&quot;]({{bbox}});
  relation[&quot;protect_class&quot;=&quot;5&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '20, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-78088" class="comments-container">
<span id="78089"></span>
<div id="comment-78089" class="comment">
<div id="post-78089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually it's good enough, because very few AONBs have separate outer polygons - of the ones in the rendering database, just the Forest of Bowland I think.</p>
<p>I'll work through the list of discrepancies to see if there are any obvious relation issues with the "missing" ones.</p>
</div>
<div id="comment-78089-info" class="comment-info">
<span class="comment-age">(28 Dec '20, 19:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="78114"></span>
<div id="comment-78114" class="comment">
<div id="post-78114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Over at <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/395232#comment48986">https://www.openstreetmap.org/user/SomeoneElse/diary/395232#comment48986</a> <a href="https://www.openstreetmap.org/user/mmd">https://www.openstreetmap.org/user/mmd</a> has suggested <a href="https://overpass-turbo.eu/s/11In">https://overpass-turbo.eu/s/11In</a> .</p>
</div>
<div id="comment-78114-info" class="comment-info">
<span class="comment-age">(29 Dec '20, 20:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78088-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78230"></span>

<div id="answer-container-78230" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78230-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is what I use:</p>
<pre><code>// CSV list of National Parks 
[out:csv(::id, &quot;name&quot;,::count; false; &quot;,&quot;)];
area(id:3600058447,3600058437,3600058446); //EWS
rel(area)[boundary=protected_area][designation=national_park];
out;
out count;</code></pre>
<p>Note the value change of the boundary tag from national_park to protected_area.</p>
<p>Also, ISO3166-1"="GB" would return data from Northern Island, if there were any, which is why I specify the ids for England, Wales &amp; Scotland.</p>
<p>PS {{geocodeArea:Great Britain}}, for some reason, excludes GB's islands such as Sky, Isle of Wight &amp; Sheppy; something I mean to bring up on Talk-GB.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '21, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '21, 13:53</strong> </span></p>
</div>
</div>
<div id="comments-container-78230" class="comments-container">
&#10;</div>
<div id="comment-tools-78230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78230-form-container" class="comment-form-container">
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

