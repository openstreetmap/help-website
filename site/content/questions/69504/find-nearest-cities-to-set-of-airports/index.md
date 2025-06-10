+++
type = "question"
title = "Find nearest cities to set of airports"
description = '''I am using the following query to get all the airports in Manitoba that have an IATA or ICAO code associated with them (maybe not the most efficient code, so feel free to suggest something better): [out:json][timeout:25]; area[&quot;name&quot;=&quot;Manitoba&quot;]-&amp;gt;.a;  (  node(area.a)[&quot;aeroway&quot;=&quot;aerodrome&quot;][&quot;iata&quot;...'''
date = "2019-06-06T18:10:00Z"
lastmod = "2020-01-12T16:39:00Z"
weight = 69504
keywords = [ "nearest", "airport", "cities", "overpass" ]
aliases = [ "/questions/69504" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find nearest cities to set of airports](/questions/69504/find-nearest-cities-to-set-of-airports)

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
<span id="post-69504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69504-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using the following query to get all the airports in Manitoba that have an IATA or ICAO code associated with them (maybe not the most efficient code, so feel free to suggest something better):</p>
<pre><code>[out:json][timeout:25];
area[&quot;name&quot;=&quot;Manitoba&quot;]-&gt;.a;
&#10;(
  node(area.a)[&quot;aeroway&quot;=&quot;aerodrome&quot;][&quot;iata&quot;];
  way(area.a)[&quot;aeroway&quot;=&quot;aerodrome&quot;][&quot;iata&quot;];
  relation(area.a)[&quot;aeroway&quot;=&quot;aerodrome&quot;][&quot;iata&quot;];
&#10;  node(area.a)[&quot;aeroway&quot;=&quot;aerodrome&quot;][&quot;icao&quot;];
  way(area.a)[&quot;aeroway&quot;=&quot;aerodrome&quot;][&quot;icao&quot;];
  relation(area.a)[&quot;aeroway&quot;=&quot;aerodrome&quot;][&quot;icao&quot;];
)-&gt;.airports;
&#10;.airports out center;</code></pre>
<p>What I'd like to do now is, for each of those airports, find the nearest city (or town or whatever) to the airport. How can I do that? The end result would ideally be some JSON structure that gave me something like the following:</p>
<pre><code>[
  {
    &quot;id&quot;: 7932149,
    &quot;center&quot;: {
      &quot;lat&quot;: 49.9104284,
      &quot;lon&quot;: -97.2381871
    },
    &quot;iata&quot;: &quot;YWG&quot;,
    &quot;icao&quot;: &quot;CYWG&quot;,
    &quot;name&quot;: &quot;Winnipeg James Armstrong Richardson International Airport&quot;,
    &quot;nearest_city&quot;: {
      &quot;id&quot;: &quot;123456&quot;,
      &quot;name&quot;: &quot;Winnipeg&quot;,
      &quot;center&quot;: {
        &quot;lat&quot;: 49.9,
        &quot;lon&quot;: -97.0,
      },
      &quot;admin_level&quot;: 8,
      &quot;type&quot;: &quot;city&quot;
    }
  },
  ... more entries ...
]</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nearest" rel="tag" title="see questions tagged &#39;nearest&#39;">nearest</span> <span class="post-tag tag-link-airport" rel="tag" title="see questions tagged &#39;airport&#39;">airport</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '19, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/490fceb89fb30e037a4a78fd09d6fd3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cviebrock_ppn&#39;s gravatar image" />
<p><span>cviebrock_ppn</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cviebrock_ppn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69504" class="comments-container">
<span id="70749"></span>
<div id="comment-70749" class="comment">
<div id="post-70749-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you find a solutions for this?</p>
</div>
<div id="comment-70749-info" class="comment-info">
<span class="comment-age">(12 Sep '19, 13:59)</span> <span class="comment-user userinfo">Javisst</span>
</div>
</div>
</div>
<div id="comment-tools-69504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69504-form-container" class="comment-form-container">
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

<span id="72478"></span>

<div id="answer-container-72478" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72478-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This doesn't fully return the nearest, but should get you started:</p>
<pre><code>[out:json];
area[name=Manitoba];
nwr(area)[aeroway=aerodrome][~&quot;iata|icao&quot;~&quot;.&quot;]-&gt;.airports;
&#10;foreach.airports-&gt;.elem(
  nwr(around.elem:100000)[place=city];
  out geom;
);
&#10;.airports out center;
&#10;{{style: 
node [aeroway]{color:green;fill-color:green; symbol-size:5}
node [place]{color:red;fill-color:red; symbol-size:20;fill-opacity:0.5}
way [place]{color:red; opacity:0.5}
relation [place]{color:red; opacity:0.5}
}}</code></pre>
<p><a href="https://overpass-turbo.eu/s/PFZ">https://overpass-turbo.eu/s/PFZ</a></p>
<p>The third line is just a concentration of your routine. It uses regular expressions (~ means 'something like')</p>
<p>It then loops through each airport &amp; finds any city with the specified distance (in metres).</p>
<p>T oget the nearest you'll have to perform some post processing.</p>
<p>PS I'm not convinced the <code>admin</code> ways should have <code>place</code> tags</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '20, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72478" class="comments-container">
&#10;</div>
<div id="comment-tools-72478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72478-form-container" class="comment-form-container">
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

