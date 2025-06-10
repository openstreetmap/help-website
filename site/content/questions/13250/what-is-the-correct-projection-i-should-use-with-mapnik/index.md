+++
type = "question"
title = "What is the correct projection I should use with Mapnik?"
description = '''Hello, I&#x27;m trying to render tiles with a very simple stylesheet. For data feed I&#x27;m using OSM file extract from the planet dump. I&#x27;ve read Mapnik can handle OSM XML files with some limitations. There are two problems:  Long ways are not rendered. All ways are distorted or displaced.  You can see the ...'''
date = "2012-06-04T17:45:00Z"
lastmod = "2017-03-29T23:03:00Z"
weight = 13250
keywords = [ "rendering", "tiles", "mapnik" ]
aliases = [ "/questions/13250" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is the correct projection I should use with Mapnik?](/questions/13250/what-is-the-correct-projection-i-should-use-with-mapnik)

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
<span id="post-13250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13250-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to render tiles with a very simple stylesheet. For data feed I'm using OSM file extract from the planet dump. I've read Mapnik can handle OSM XML files with some limitations.</p>
<p>There are two problems:</p>
<ol>
<li>Long ways are not rendered.</li>
<li>All ways are distorted or displaced.</li>
</ol>
<p>You can see the result here: <a href="http://dev.ivanatora.info/roads/">http://dev.ivanatora.info/roads/</a> At least the big roads in these two layers "Roads" and "Roads tiles" should match.</p>
<p>The second one seems like a projection problem and I tried tons of different variants but in vain. Here is my latest stylesheet: <a href="http://dev.ivanatora.info/tests/mapnik_style.xml">http://dev.ivanatora.info/tests/mapnik_style.xml</a> I've tried also simplier things for srs - "+proj=merc +datum=WGS84" and "+proj=latlon +datum=WGS84". I think the data from the planet dump extract is in latlon projection, but something is not right...</p>
<p>I would really appreciate some insight.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '12, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '12, 17:54</strong> </span></p>
</div>
</div>
<div id="comments-container-13250" class="comments-container">
&#10;</div>
<div id="comment-tools-13250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13250-form-container" class="comment-form-container">
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

<span id="13254"></span>

<div id="answer-container-13254" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13254-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-13254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivanatora has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When rendering with Mapnik, you have an input projection and an output projection. The input projection is what your data is in, and has to be given in the <code>&lt;Layer&gt;</code> element. The output projection is what you want your map to be in, and is usually given in the <code>&lt;Map&gt;</code> element (but some client programs e.g. nik2img.py allow you to override that).</p>
<p>You likely want your map in Google Mercator projection so your <code>&lt;Map&gt;</code> element</p>
<pre><code>&lt;Map bgcolor=&quot;transparent&quot; srs=&quot;+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over&quot;&gt;</code></pre>
<p>looks ok (but try writing srs="+init=epsg:3857" which should also work and is clearer).</p>
<p>Your <code>&lt;Layer&gt;</code> elements claims that the source data is in Mercator as well, but it isn't; this will lead to distorted rendering. Your source data, raw latitudes and longitudes from OSM, is in EPSG:4326, so you'll need something like this:</p>
<pre><code>&lt;Layer name=&quot;highways&quot; status=&quot;on&quot; srs=&quot;+init=epsg:4326&quot;&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '12, 18:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '17, 23:03</strong> </span></p>
</div>
</div>
<div id="comments-container-13254" class="comments-container">
<span id="13265"></span>
<div id="comment-13265" class="comment">
<div id="post-13265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, it does make sense in that way and that was the problem. Thank you!</p>
</div>
<div id="comment-13265-info" class="comment-info">
<span class="comment-age">(05 Jun '12, 15:01)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="55343"></span>
<div id="comment-55343" class="comment">
<div id="post-55343-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm"></a><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@frederik</a>-ramm I'm a little late to the party but the code above should be <code>srs="+init=epsg:4326"</code> shouldn't it?</p>
</div>
<div id="comment-55343-info" class="comment-info">
<span class="comment-age">(29 Mar '17, 22:12)</span> <span class="comment-user userinfo">k-nut</span>
</div>
</div>
<span id="55347"></span>
<div id="comment-55347" class="comment">
<div id="post-55347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, I modified the answer. Thanks.</p>
</div>
<div id="comment-55347-info" class="comment-info">
<span class="comment-age">(29 Mar '17, 23:03)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13254-form-container" class="comment-form-container">
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

