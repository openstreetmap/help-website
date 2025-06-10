+++
type = "question"
title = "Tirex / Mapnik does not find font"
description = '''I am getting the following Tirex error: tirex-backend-mapnik[15024]: no valid fonts could be loaded in FontSet &#x27;fontset-0&#x27; in FontSet at line 17 of &#x27;/etc/mapnik-osm-carto-data/osm.xml&#x27;  The first font in osm.xml is DejaVu Sans Book which is installed: # python -c &quot;from mapnik import FontEngine as e;...'''
date = "2014-06-23T11:57:00Z"
lastmod = "2014-06-23T12:28:00Z"
weight = 34256
keywords = [ "debugging", "tirex", "mapnik" ]
aliases = [ "/questions/34256" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tirex / Mapnik does not find font](/questions/34256/tirex-mapnik-does-not-find-font)

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
<span id="post-34256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34256-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am getting the following Tirex error:</p>
<pre><code>tirex-backend-mapnik[15024]: no valid fonts could be loaded in FontSet &#39;fontset-0&#39; in FontSet at line 17 of &#39;/etc/mapnik-osm-carto-data/osm.xml&#39;</code></pre>
<p>The first font in <code>osm.xml</code> is <code>DejaVu Sans Book</code> which is installed:</p>
<pre><code># python -c &quot;from mapnik import FontEngine as e;print &#39;\n&#39;.join(e.instance().face_names())&quot; | grep &quot;DejaVu Sans Book&quot;
&#10;Output:
DejaVu Sans Book</code></pre>
<p>When rendering via <code>generate_image.py</code> it works.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-debugging" rel="tag" title="see questions tagged &#39;debugging&#39;">debugging</span> <span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jun '14, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/7651f7a3094f0a39b51630214fe9c94d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex_AddisMap&#39;s gravatar image" />
<p><span>Alex_AddisMap</span><br />
<span class="score" title="189 reputation points">189</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex_AddisMap has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jun '14, 12:20</strong> </span></p>
</div>
</div>
<div id="comments-container-34256" class="comments-container">
&#10;</div>
<div id="comment-tools-34256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34256-form-container" class="comment-form-container">
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

<span id="34257"></span>

<div id="answer-container-34257" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34257-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Set</p>
<pre><code>fontdir=/usr/share/fonts/
fontdir_recurse=1</code></pre>
<p>in <code>/etc/tirex/renderer/mapnik.conf</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '14, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/7651f7a3094f0a39b51630214fe9c94d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex_AddisMap&#39;s gravatar image" />
<p><span>Alex_AddisMap</span><br />
<span class="score" title="189 reputation points">189</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex_AddisMap has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34257" class="comments-container">
&#10;</div>
<div id="comment-tools-34257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34257-form-container" class="comment-form-container">
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

