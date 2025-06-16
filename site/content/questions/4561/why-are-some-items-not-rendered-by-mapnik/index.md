+++
type = "question"
title = "Why are some items not rendered by Mapnik?"
description = '''While designing a fantasy map, I got some strange unconsistent behaviors with my OSM file when processing it with mapnik (not from a database, from the .osm file in command line) I made some parts with the &quot;natural&quot;=&quot;fell&quot; tag. One is made of 39 nodes, an other one is 70 nodes and a third one is 6 n...'''
date = "2011-04-16T22:00:00Z"
lastmod = "2011-04-21T19:51:00Z"
weight = 4561
keywords = [ "mapnik" ]
aliases = [ "/questions/4561" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why are some items not rendered by Mapnik?](/questions/4561/why-are-some-items-not-rendered-by-mapnik)

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
<span id="post-4561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4561-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While designing a fantasy map, I got some strange unconsistent behaviors with my OSM file when processing it with mapnik (not from a database, from the .osm file in command line)</p>
<p>I made some parts with the "natural"="fell" tag. One is made of 39 nodes, an other one is 70 nodes and a third one is 6 nodes. Only the first "fell" is displayed. When I move a single node in the third fell, making it slightly more pointy, then it is displayed like the first one.</p>
<p>I tried to alter the scaledenominator (also to remove them), but it was useless. The rule is quite simple:</p>
<pre><code>&lt;Filter&gt;[landuse] = &#39;fell&#39; or [natural] = &#39;fell&#39;&lt;/Filter&gt; 
      &lt;MaxScaleDenominator&gt;20000000&lt;/MaxScaleDenominator&gt;
      &lt;MinScaleDenominator&gt;0&lt;/MinScaleDenominator&gt;
      &lt;PolygonSymbolizer&gt;
        &lt;CssParameter name=&quot;fill&quot;&gt;#8dc56c&lt;/CssParameter&gt;
     &lt;/PolygonSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[landuse] = &#39;fell&#39; or [natural] = &#39;fell&#39;&lt;/Filter&gt;
      &lt;MaxScaleDenominator&gt;20000000&lt;/MaxScaleDenominator&gt;
      &lt;MinScaleDenominator&gt;0&lt;/MinScaleDenominator&gt;
      &lt;PolygonPatternSymbolizer file= &quot;/temp/mapnik/symbols/forest.png&quot; type=&quot;png&quot; width=&quot;21&quot; height=&quot;24&quot;/&gt;
    &lt;/Rule&gt;</code></pre>
<p>What can it be?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '11, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/71d339cacc167d5b3fef9344badd74e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="otto&#39;s gravatar image" />
<p><span>otto</span><br />
<span class="score" title="251 reputation points">251</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="otto has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4561" class="comments-container">
&#10;</div>
<div id="comment-tools-4561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4561-form-container" class="comment-form-container">
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

<span id="4676"></span>

<div id="answer-container-4676" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4676-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The osm plugin in mapnik is not a drop in replacement for a proper postgis db. I read it's also missing (parts of) relation handling.</p>
<p>Also, the osm.xml stylesheet is not maintained with the osm plugin in mind, and this can also lead to strange behaviours, dropped items and other assorted rendering quirks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '11, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/90263d23dc3f15a98d14d91e889b9d25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lennard&#39;s gravatar image" />
<p><span>Lennard</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lennard has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4676" class="comments-container">
<span id="4712"></span>
<div id="comment-4712" class="comment">
<div id="post-4712-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for telling me about those problems. I hadn't read there was limitations, but I find it now: <a href="https://wiki.openstreetmap.org/wiki/Mapnik:_Rendering_OSM_XML_data_directly#Limitations">https://wiki.openstreetmap.org/wiki/Mapnik:_Rendering_OSM_XML_data_directly#Limitations</a> I've tried to separate my elements into different layers, but it seems it's not much better, only one element is shown according to the order it is called. If you're curious or willing to help, here is the archive of my tests so far: <a href="http://dl.free.fr/hAVI7ezre">http://dl.free.fr/hAVI7ezre</a></p>
</div>
<div id="comment-4712-info" class="comment-info">
<span class="comment-age">(21 Apr '11, 19:51)</span> <span class="comment-user userinfo">otto</span>
</div>
</div>
</div>
<div id="comment-tools-4676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4676-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4576"></span>

<div id="answer-container-4576" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4576-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know about the stylesheet part, but I would double check if these areas are correctly drawn (first and last node of the way is the same node)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '11, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4576" class="comments-container">
<span id="4578"></span>
<div id="comment-4578" class="comment">
<div id="post-4578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It can't be, because for the same shape, one time it's rendered, another time, when I move a single node a few miles away, it's not.</p>
<p>After some investigations, I noticed some elements are preventing the others to render, for example I have a "natural=peak" above a "fell" which prevents another fell to be displayed (except if I make it bigger).</p>
<p>When I remove all the other elements, the 3 "fells" are correctly displayed.</p>
</div>
<div id="comment-4578-info" class="comment-info">
<span class="comment-age">(17 Apr '11, 22:40)</span> <span class="comment-user userinfo">otto</span>
</div>
</div>
</div>
<div id="comment-tools-4576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4576-form-container" class="comment-form-container">
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

