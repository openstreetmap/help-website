+++
type = "question"
title = "Is the Overpass API not returning a full result set or is my query flawed?"
description = '''I&#x27;m using the Overpass API to pull data from OpenStreetMap. The web version that I use to verify queries before running through my process against the API is Overpass Turbo. This is the query I&#x27;m using to collect all places that are Admin Level 8 within California: [out:json]; area[&#x27;admin_level&#x27;=&#x27;4&#x27;...'''
date = "2015-10-25T20:26:00Z"
lastmod = "2015-10-25T21:53:00Z"
weight = 46111
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/46111" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is the Overpass API not returning a full result set or is my query flawed?](/questions/46111/is-the-overpass-api-not-returning-a-full-result-set-or-is-my-query-flawed)

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
<span id="post-46111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46111-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using the Overpass API to pull data from OpenStreetMap. The web version that I use to verify queries before running through my process against the API is <a href="http://overpass-turbo.eu/">Overpass Turbo</a>.</p>
<p>This is the query I'm using to collect all places that are Admin Level 8 within California:</p>
<p><code>[out:json]; area['admin_level'='4']['name'='California']; (relation['admin_level'='8'](area);); out;</code></p>
<p>That doesn't return all items, though. For example, <a href="https://nominatim.openstreetmap.org/details.php?place_id=63317338">Pacifica</a> is not included.</p>
<p>Is that a problem with Overpass, or is there something wrong with my query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '15, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-46111" class="comments-container">
&#10;</div>
<div id="comment-tools-46111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46111-form-container" class="comment-form-container">
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

<span id="46112"></span>

<div id="answer-container-46112" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46112-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JamesChevalier has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Pacifica is a way. So you need to also have a way query (or just use an area query).</p>
<pre><code>[out:json];
area[&#39;admin_level&#39;=&#39;4&#39;][&#39;name&#39;=&#39;California&#39;]-&gt;.ca;
(
 relation[&#39;admin_level&#39;=&#39;8&#39;](area.ca);
 way[&#39;admin_level&#39;=&#39;8&#39;](area.ca);
);
out geom;</code></pre>
<p>or the mostly equivalent (mmd points out in a comment that this won't work as it is not implemented):</p>
<pre><code>(
  area[&#39;admin_level&#39;=&#39;8&#39;](area);
);</code></pre>
<p>I guess the area query will probably be cleaner, as it will only return closed polygons (depending on what's in the data, there might be a bunch of ways that aren't closed areas).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '15, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '15, 21:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-46112" class="comments-container">
<span id="46116"></span>
<div id="comment-46116" class="comment">
<div id="post-46116-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><code>area['admin_level'='8'](area);</code> looks correct, but unfortunately it is <em>not implemented</em> and doesn't work as you would expect: it just returns areas matching admin_level = 8, without taking the <code>(area)</code> part into consideration. Also, you will not get any error message whatsoever, but simply a 60MB response with admin_level=8 areas from all over the world.</p>
<p>Bottom line: you have to stick to rel...(area) / way...(area) for the time being.</p>
</div>
<div id="comment-46116-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 21:05)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="46119"></span>
<div id="comment-46119" class="comment">
<div id="post-46119-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The biggest issue is that it will probably return ways that are parts of the relations (but with any luck you will be able to discard those by checking for things like 'name').</p>
</div>
<div id="comment-46119-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 21:14)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="46121"></span>
<div id="comment-46121" class="comment">
<div id="post-46121-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>: I had to adopt your initial proposal, as it also didn't work as expected: you need to store the area in an inputset (here it is called <code>.ca</code>) and use that for both relation and way. Otherwise, the relation query will silently remove the California area, and way (area) will not find anything, as there's no more area to work on.</p>
</div>
<div id="comment-46121-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 21:21)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="46122"></span>
<div id="comment-46122" class="comment">
<div id="post-46122-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you! Thank you! Thank you! You both just helped me out <em>so much</em>. In case it's at all useful to anyone, I've been storing the individual cities that I'm using in my project in github: <a href="https://github.com/JamesChevalier/cities">https://github.com/JamesChevalier/cities</a></p>
</div>
<div id="comment-46122-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 21:32)</span> <span class="comment-user userinfo">JamesChevalier</span>
</div>
</div>
<span id="46123"></span>
<div id="comment-46123" class="comment">
<div id="post-46123-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh wow, I just realized how critical that last <code>geom</code> you added is! Thanks.</p>
</div>
<div id="comment-46123-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 21:53)</span> <span class="comment-user userinfo">JamesChevalier</span>
</div>
</div>
</div>
<div id="comment-tools-46112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46112-form-container" class="comment-form-container">
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

