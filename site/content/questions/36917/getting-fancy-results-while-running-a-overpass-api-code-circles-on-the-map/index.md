+++
type = "question"
title = "getting fancy results while running a overpass-api code: circles on the map"
description = '''if i run this following code - in http://overpass-turbo.eu/ i have interesting results in the map -  some circles are shown  &amp;lt;!-- This query looks for nodes, ways and relations with the given key. Choose your region and hit the Run button above! --&amp;gt; &amp;lt;osm-script output=&quot;json&quot; timeout=&quot;25&quot;&amp;gt...'''
date = "2014-09-18T22:27:00Z"
lastmod = "2014-09-22T04:23:00Z"
weight = 36917
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/36917" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [getting fancy results while running a overpass-api code: circles on the map](/questions/36917/getting-fancy-results-while-running-a-overpass-api-code-circles-on-the-map)

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
<span id="post-36917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36917-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>if i run this following code - in <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> i have interesting results in the map -</p>
<p>some circles are shown</p>
<pre><code>&lt;!-- This query looks for nodes, ways and relations  with the given key. Choose your region and hit the Run button above!
--&gt; &lt;osm-script output=&quot;json&quot; timeout=&quot;25&quot;&gt;   &lt;!-- gather results
--&gt;   &lt;union&gt;
    &lt;!-- query part for: “school=*” --&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;school&quot;/&gt;
      &lt;bbox-query s=&quot;-57.13623931917743&quot; w=&quot;-82.6171875&quot; n=&quot;15.114552871944102&quot; e=&quot;-33.57421875&quot;/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;way&quot;&gt;
      &lt;has-kv k=&quot;school&quot;/&gt;
      &lt;bbox-query s=&quot;-57.13623931917743&quot; w=&quot;-82.6171875&quot; n=&quot;15.114552871944102&quot; e=&quot;-33.57421875&quot;/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;relation&quot;&gt;
      &lt;has-kv k=&quot;school&quot;/&gt;
      &lt;bbox-query s=&quot;-57.13623931917743&quot; w=&quot;-82.6171875&quot; n=&quot;15.114552871944102&quot; e=&quot;-33.57421875&quot;/&gt;
    &lt;/query&gt;   &lt;/union&gt;   &lt;!-- print results --&gt;   &lt;print mode=&quot;body&quot;/&gt;   &lt;recurse type=&quot;down&quot;/&gt;   &lt;print mode=&quot;skeleton&quot; order=&quot;quadtile&quot;/&gt; &lt;/osm-script&gt;</code></pre>
<p>see the circles -</p>
<p>what are these circles good for. i love to hear from you</p>
<p>greetings</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '14, 22:27</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '14, 01:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-36917" class="comments-container">
&#10;</div>
<div id="comment-tools-36917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36917-form-container" class="comment-form-container">
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

<span id="36919"></span>

<div id="answer-container-36919" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36919-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-36919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As mentioned in <a href="https://help.openstreetmap.org/questions/36295/results-in-overpass-turbo-api-interesting-data-tells-us-more-things">this previous question</a>, see <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">our wiki page</a> about it, specifically the "Map key" section of that page which explains what the different circle colours mean.</p>
<p>Below this picture</p>
<p><img src="https://wiki.openstreetmap.org/w/images/c/c1/Overpass_turbo_map_key.png" alt="Overpass turbo symbols as displayed in wiki page" /></p>
<p>is a description that says what they mean:</p>
<pre><code>objects:
    (1,2) POIs (nodes with tags) are shown as circles with a yellow filling and a thin blue outline,
    (2,3,4) ways as bold blue lines and
    (5,6,7) areas as yellow polygons with a thin blue outline.
(2,5,8) Pink lines and outlines mean that an object is part of at least one relation.
(4,7) Dashed lines mean that a line or area has an incomplete geometry (most likely because some of its nodes have not been loaded).
(9) Circles with a red filling represent ways or polygons that are too small to be displayed normally (to switch this off and show the small feature instead: Settings → Map → &quot;Don&#39;t display small features as POIs.&quot;).</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '14, 23:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-36919" class="comments-container">
<span id="36925"></span>
<div id="comment-36925" class="comment">
<div id="post-36925-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>So basically, the circles represent (part of) the answer, i.e. the location of the things you were looking for.</p>
</div>
<div id="comment-36925-info" class="comment-info">
<span class="comment-age">(19 Sep '14, 07:30)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="36939"></span>
<div id="comment-36939" class="comment">
<div id="post-36939-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello and good day - hello somoneElse and escada - thx for the info. BTW - can i export the data of the map - i.e. to use it in a wordpress-plugin? is this possible.?</p>
</div>
<div id="comment-36939-info" class="comment-info">
<span class="comment-age">(20 Sep '14, 09:36)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="36940"></span>
<div id="comment-36940" class="comment">
<div id="post-36940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No idea about wordpress, but at the top right there's a "data" button - press that.</p>
</div>
<div id="comment-36940-info" class="comment-info">
<span class="comment-age">(20 Sep '14, 09:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36919-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36961"></span>

<div id="answer-container-36961" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36961-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>and on the left there is en export button. you'll see that there are kml, geojson, etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '14, 04:23</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-36961" class="comments-container">
&#10;</div>
<div id="comment-tools-36961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36961-form-container" class="comment-form-container">
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

