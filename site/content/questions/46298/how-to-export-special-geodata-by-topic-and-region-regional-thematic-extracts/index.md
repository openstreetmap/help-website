+++
type = "question"
title = "how to export special geodata by topic and region / regional thematic extracts?"
description = '''Hello there, I want to export special geodata such as international Airports, railway stations or motorway entrances in Germany from OSM. Is this at all possible without downloading the complete Germany map? Best regards and thanks once before, Carsten (German) Hallo,  ich möchte spezielle Geodaten ...'''
date = "2015-11-02T12:07:00Z"
lastmod = "2015-11-03T14:03:00Z"
weight = 46298
keywords = [ "thematic", "export" ]
aliases = [ "/questions/46298" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to export special geodata by topic and region / regional thematic extracts?](/questions/46298/how-to-export-special-geodata-by-topic-and-region-regional-thematic-extracts)

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
<span id="post-46298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46298-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello there,</p>
<p>I want to export special geodata such as international Airports, railway stations or motorway entrances in Germany from OSM. Is this at all possible without downloading the complete Germany map?</p>
<p>Best regards and thanks once before, Carsten</p>
<p><span class="small">(German) Hallo,<br />
ich möchte spezielle Geodaten wie z.B. Flughäfen, Bahnhöfe oder Autobahnauffahrten in ganz Deutschland aus OSM exportieren. Ist dies irgendwie möglich ohne sich die komplette Deutschland-Karte herunterzuladen?<br />
Beste Grüße und schon einmal vielen Dank, Carsten</span></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-thematic" rel="tag" title="see questions tagged &#39;thematic&#39;">thematic</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '15, 12:07</strong></p>
<img src="https://secure.gravatar.com/avatar/8325c6b0b249be9494fac3818b572f79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c_schroeder&#39;s gravatar image" />
<p><span>c_schroeder</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c_schroeder has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Nov '15, 18:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46298" class="comments-container">
&#10;</div>
<div id="comment-tools-46298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46298-form-container" class="comment-form-container">
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

<span id="46299"></span>

<div id="answer-container-46299" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46299-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-46299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> might be a good place to start. I used it to get a list of all Points tagged "railway:station" in Switzerland, and it worked beautifully. The language is kind of weird, but there's a Wizard where I simply typed "railway stations in switzerland", and I had a piece of code that gave me almost what I wanted. Here's something to get you started:</p>
<pre><code>// Output as JSON and account for my shitty connection
[out:json][timeout:300];
&#10;// Limit to DE
{{geocodeArea:Germany}}-&gt;.searchArea;
(
    // Get all nodes with the aeroway:aerodrome tag
    node[&quot;aeroway&quot;=&quot;aerodrome&quot;](area.searchArea);
);
// Print the results
out body;
&gt;; // &lt;- No idea what the hell that is
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '15, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/2b6b4a775e6134adeb9c2d7fb0f3e5c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="balducien&#39;s gravatar image" />
<p><span>balducien</span><br />
<span class="score" title="131 reputation points">131</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="balducien has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46299" class="comments-container">
<span id="46303"></span>
<div id="comment-46303" class="comment">
<div id="post-46303-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>… and docs are there (mind the links): <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">https://wiki.openstreetmap.org/wiki/Overpass_turbo</a></p>
</div>
<div id="comment-46303-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 18:51)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46311"></span>
<div id="comment-46311" class="comment">
<div id="post-46311-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><code>&gt;;</code> would be needed to also fetch all nodes for a way. But as your example fetches nodes only, this is probably a bit of an overkill here. As always, things are modeled in very different ways in OSM, sometimes as nodes, but also quite often as way or even relation. The default statement created by the overpass turbo wizard includes all the 3 of them. Might be a good starting point to get all relevant data...</p>
</div>
<div id="comment-46311-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 20:47)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="46314"></span>
<div id="comment-46314" class="comment">
<div id="post-46314-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Upvoted purely for</p>
<pre><code>&gt;; // &lt;- No idea what the hell that is</code></pre>
</div>
<div id="comment-46314-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 23:35)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="46315"></span>
<div id="comment-46315" class="comment">
<div id="post-46315-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A completely off topic note: to get stuff in Switzerland you can use both our overpass api and turbo instances: <a href="http://osm.ch/">http://osm.ch/</a></p>
</div>
<div id="comment-46315-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 23:43)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="46367"></span>
<div id="comment-46367" class="comment">
<div id="post-46367-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>: even more off topic: do you know if there are some specs available of this Swiss Overpass API instance? Would be great to add them to <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">this wiki page</a>.</p>
</div>
<div id="comment-46367-info" class="comment-info">
<span class="comment-age">(03 Nov '15, 14:03)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-46299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46299-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46306"></span>

<div id="answer-container-46306" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46306-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Even if downloading a ~4gb file isn't what you want, imho it would be better to just download it. It is avaiable at <a href="http://download.geofabrik.de/europe/germany.html">geofabrik.de</a>. Afterwards you can use <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> to reduce the data to what is really needed. For experimenting with osmfilter i would also download a small destrict, maybe Hessen, to get results of your osmfilter command within minutes instead of possibly hours. Those are the times i experienced doing something comparable without an SSD. So using an SSD might be a good idea, if possible.</p>
<p>The advantage over the overpass api is, that you won't have to experiment with timeout values, which you probably would probably have to. Also you would have the result as an .osm file, which can be used for further osm related works, like populating a sql database with <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">Osm2pgsql</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '15, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/991a1daf7de47d3dcc3d94933c70ce2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EinFreierNick&#39;s gravatar image" />
<p><span>EinFreierNick</span><br />
<span class="score" title="121 reputation points">121</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EinFreierNick has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Nov '15, 20:10</strong> </span></p>
</div>
</div>
<div id="comments-container-46306" class="comments-container">
<span id="46310"></span>
<div id="comment-46310" class="comment">
<div id="post-46310-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Did you know: Overpass API can produce several output formats, amongst them OSM XML format. You just need to replace <code>[out:json]</code> by <code>[out:xml]</code> (=default), as well as <code>out body; &gt;; out skel qt;</code> by <code>out meta; &gt;; out meta;</code> to fetch all the details - or just export it to JOSM from overpass turbo, which has the same effect.</p>
</div>
<div id="comment-46310-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 20:45)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-46306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46306-form-container" class="comment-form-container">
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

