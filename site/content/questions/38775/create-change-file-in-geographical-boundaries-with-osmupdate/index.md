+++
type = "question"
title = "Create change file in geographical boundaries with osmupdate"
description = '''Hey, is it possible to create a change file in geographical boundaries with osmupdate.  I already tried: osmupdate germany-latest.osm.pbf 2014-11-23T21:22:02Z change_file.osc.gz -B=germany.poly But the Change File always contains the entire globe. regards lakul'''
date = "2014-11-25T11:40:00Z"
lastmod = "2014-11-25T19:29:00Z"
weight = 38775
keywords = [ "changeset", "osmconvert", "regional", "update", "change" ]
aliases = [ "/questions/38775" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Create change file in geographical boundaries with osmupdate](/questions/38775/create-change-file-in-geographical-boundaries-with-osmupdate)

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
<span id="post-38775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38775-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>is it possible to create a change file in geographical boundaries with osmupdate.</p>
<p>I already tried:</p>
<p>osmupdate germany-latest.osm.pbf 2014-11-23T21:22:02Z change_file.osc.gz -B=germany.poly</p>
<p>But the Change File always contains the entire globe.</p>
<p>regards</p>
<p>lakul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-regional" rel="tag" title="see questions tagged &#39;regional&#39;">regional</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-change" rel="tag" title="see questions tagged &#39;change&#39;">change</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '14, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/9b6ed29df9f64447f43439473548aae5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakul83&#39;s gravatar image" />
<p><span>lakul83</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakul83 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '14, 11:55</strong> </span></p>
</div>
</div>
<div id="comments-container-38775" class="comments-container">
&#10;</div>
<div id="comment-tools-38775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38775-form-container" class="comment-form-container">
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

<span id="38777"></span>

<div id="answer-container-38777" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38777-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes it is possible, but it is a bit more complicated.</p>
<p>First you update your extract with osmupdate:</p>
<pre><code>osmupdate germany-latest.osm.pbf germany-updated.osm.pbf -B=germany.poly</code></pre>
<p>Then you calculate the differences with osmconvert:</p>
<pre><code>osmconvert germany-updated.osm.pbf germany-latest.osm.pbf --diff --fake-lonlat --emulate-osmosis -o=diff.osc</code></pre>
<p>This gies you the desired osm change file. After that you probably want to rename <code>germany-updated.osm.pbf</code> to <code>germany-latest.osm.pbf</code> to be able to run the same process again to get the next diff.</p>
<p>It has a slight problem though: you might get incomplete extracts when ways or relations move inside your boundary. This is why I do a slightly more complicated variant for the swiss extract on planet.osm.ch:</p>
<p>use a larger bbox around swizerland:</p>
<pre><code>BBOX=&quot;5,45.3,11.3,48.3&quot;</code></pre>
<p>update this bbox:</p>
<pre><code>osmupdate chbbox_updated.o5m chbbox.o5m --minutely -b=$BBOX</code></pre>
<p>cut out switzerland from this larger region:</p>
<pre><code>osmconvert chbbox_updated.o5m -B=$CHPOLY -o=switzerland_updated.o5m</code></pre>
<p>and create the diff between the old cut out and the new one:</p>
<pre><code>osmconvert switzerland_updated.o5m switzerland.o5m --diff --fake-lonlat --emulate-osmosis -o=diff.osc</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '14, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/0697f0a3c5fdeff1999768f7df9cb2af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="datendelphin&#39;s gravatar image" />
<p><span>datendelphin</span><br />
<span class="score" title="234 reputation points">234</span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="datendelphin has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-38777" class="comments-container">
<span id="38790"></span>
<div id="comment-38790" class="comment">
<div id="post-38790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>many thanks. This idea I had. The update of the file germany-latest.pbf but takes too long. I would like to update my tile server every 5 minutes.</p>
<p>Greetings Lakul</p>
</div>
<div id="comment-38790-info" class="comment-info">
<span class="comment-age">(25 Nov '14, 14:01)</span> <span class="comment-user userinfo">lakul83</span>
</div>
</div>
<span id="38804"></span>
<div id="comment-38804" class="comment">
<div id="post-38804-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is ambitious. If your server is too slow, you will have to rely on other resources or tools. For example overpass offers augmented diffs: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Augmented_Diffs">https://wiki.openstreetmap.org/wiki/Overpass_API/Augmented_Diffs</a> But it only support BBOX for extracting a region. Or let someone with a fast server provide you with the regional diffs.</p>
</div>
<div id="comment-38804-info" class="comment-info">
<span class="comment-age">(25 Nov '14, 19:29)</span> <span class="comment-user userinfo">datendelphin</span>
</div>
</div>
</div>
<div id="comment-tools-38777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38777-form-container" class="comment-form-container">
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

