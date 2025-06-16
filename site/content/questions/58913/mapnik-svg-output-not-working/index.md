+++
type = "question"
title = "Mapnik: SVG output not working"
description = '''I want to generate SVG maps in Python using Mapnik 3.0.13 (built from source). I&#x27;m using version 3.0.13 of the Python bindings as well, built with PYCAIRO. My code: f = open(&#x27;/tmp/test.svg&#x27;, &#x27;w&#x27;) surface = cairo.SVGSurface(f.name, map.width, map.height) mapnik.render(map, surface) surface.finish()  ...'''
date = "2017-09-01T17:44:00Z"
lastmod = "2019-02-11T23:41:00Z"
weight = 58913
keywords = [ "python", "svg", "mapnik" ]
aliases = [ "/questions/58913" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik: SVG output not working](/questions/58913/mapnik-svg-output-not-working)

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
<span id="post-58913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58913-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to generate SVG maps in Python using Mapnik 3.0.13 (built from source). I'm using version 3.0.13 of the Python bindings as well, built with PYCAIRO. My code:</p>
<pre><code>f = open(&#39;/tmp/test.svg&#39;, &#39;w&#39;)
surface = cairo.SVGSurface(f.name, map.width, map.height)
mapnik.render(map, surface)
surface.finish()</code></pre>
<p>The output SVG file looks like this:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;svg xmlns=&quot;http://www.w3.org/2000/svg&quot; xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot; width=&quot;4961pt&quot; height=&quot;3508pt&quot; viewBox=&quot;0 0 4961 3508&quot; version=&quot;1.1&quot;&gt;
&lt;defs&gt;
&lt;image id=&quot;image3198&quot; width=&quot;20671&quot; height=&quot;14617&quot; xlink:href=&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAUL8A ...</code></pre>
<p>Followed by ~200 MB of base64-encoded PNG garbage.</p>
<p>I tried recompiling my library and bindings to use the native svg_renderer instead of Cairo, but got the same result.</p>
<p>How do I get a "real" SVG? This is just a PNG file wrapped inside an SVG (in an extremely inefficient way).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '17, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/2380c889f144fa299eccba2983a60826?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="derkartograf&#39;s gravatar image" />
<p><span>derkartograf</span><br />
<span class="score" title="81 reputation points">81</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="derkartograf has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '17, 17:51</strong> </span></p>
</div>
</div>
<div id="comments-container-58913" class="comments-container">
<span id="58978"></span>
<div id="comment-58978" class="comment">
<div id="post-58978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the same issue. PDF export works properly though (outputs a vector PDF)</p>
</div>
<div id="comment-58978-info" class="comment-info">
<span class="comment-age">(05 Sep '17, 10:48)</span> <span class="comment-user userinfo">knowname</span>
</div>
</div>
<span id="58979"></span>
<div id="comment-58979" class="comment">
<div id="post-58979-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See <a href="https://github.com/mapnik/python-mapnik/issues/137">https://github.com/mapnik/python-mapnik/issues/137</a> - this appears to be a Mapnik issue.</p>
</div>
<div id="comment-58979-info" class="comment-info">
<span class="comment-age">(05 Sep '17, 11:08)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58913-form-container" class="comment-form-container">
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

<span id="58980"></span>

<div id="answer-container-58980" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58980-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I created a Mapnik issue for this: <a href="https://github.com/mapnik/mapnik/issues/3749">https://github.com/mapnik/mapnik/issues/3749</a></p>
<p>Turns out this happens when your style uses compositing operations like <code>comp-op="multiply"</code>. These lead to rasterization of the map.</p>
<p>Removing all <code>comp-op</code> filters produces a "real" SVG. Alternatively, PDF output works as mentioned by <a href="https://help.openstreetmap.org/users/14170/knowname">@knowname</a> above.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '17, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/2380c889f144fa299eccba2983a60826?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="derkartograf&#39;s gravatar image" />
<p><span>derkartograf</span><br />
<span class="score" title="81 reputation points">81</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="derkartograf has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-58980" class="comments-container">
<span id="58990"></span>
<div id="comment-58990" class="comment">
<div id="post-58990-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've accepted your answer here - hope that's OK!</p>
</div>
<div id="comment-58990-info" class="comment-info">
<span class="comment-age">(05 Sep '17, 13:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58980-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67970"></span>

<div id="answer-container-67970" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67970-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem has been found to be something with SVG version support. You can build Mapnik with this patch applied:</p>
<p><a href="https://github.com/mapnik/mapnik/pull/4029#issue-251451960">https://github.com/mapnik/mapnik/pull/4029#issue-251451960</a></p>
<p>or just use python-cairo with a code like:</p>
<p><code>surface.restrict_to_version(cairo.SVG_VERSION_1_2)</code></p>
<p>See also <a href="/questions/65497/is-there-any-change-in-svg-exports/67940">https://help.openstreetmap.org/questions/65497/is-there-any-change-in-svg-exports/67940</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '19, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-67970" class="comments-container">
&#10;</div>
<div id="comment-tools-67970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67970-form-container" class="comment-form-container">
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

