+++
type = "question"
title = "How can I import the color of the marker with input csv file?"
description = '''I have a csv file holding coordinates, I am able to import it correctly into umap. I managed to also have the marker name imported through an additional column named &#x27;name&#x27;. However, I would like to import the color of the marker. Here is an example of input file: lon;lat;name;color 2.2908106734441;...'''
date = "2021-10-27T13:55:00Z"
lastmod = "2021-10-29T13:44:00Z"
weight = 82388
keywords = [ "umap", "csv", "import" ]
aliases = [ "/questions/82388" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I import the color of the marker with input csv file?](/questions/82388/how-can-i-import-the-color-of-the-marker-with-input-csv-file)

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
<span id="post-82388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82388-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a csv file holding coordinates, I am able to import it correctly into umap. I managed to also have the marker name imported through an additional column named 'name'. However, I would like to import the color of the marker.</p>
<p>Here is an example of input file:</p>
<pre><code>lon;lat;name;color
2.2908106734441;48.8421565600018;aaa;green
2.40580700033425;48.8756657433978;bbb;red
2.33270615799049;48.8661396641722;ccc;blue
2.34734689771536;48.8668886093452;ddd;yellow</code></pre>
<p>This does not work. I also tried using HTML/CSS colors (i.e. replacing 'red' with #ff0000). This does not work either. What I don't understand is that is is stated here: <a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_files">https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_files</a></p>
<blockquote>
<p>csv: [...] All other columns will be imported as properties.</p>
</blockquote>
<p>Did I misunderstand something?</p>
<p>If this is not possible with csv, is it possible with other file formats?</p>
<p>Thanks for all suggestions.</p>
<p><strong>Edit</strong>: the real file is about 5000 markers, so I can't edit them one by one...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '21, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/15eec8ac7932edc5e9e5f8bbd76d0884?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sebkramm&#39;s gravatar image" />
<p><span>sebkramm</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sebkramm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '21, 14:34</strong> </span></p>
</div>
</div>
<div id="comments-container-82388" class="comments-container">
&#10;</div>
<div id="comment-tools-82388" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82388-form-container" class="comment-form-container">
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

<span id="82391"></span>

<div id="answer-container-82391" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82391-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In <a href="https://github.com/umap-project/umap/issues/494">umap Github there is a description</a> how this can be achieved using GeoJSON. Maybe that is a way for you to do it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '21, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-82391" class="comments-container">
<span id="82394"></span>
<div id="comment-82394" class="comment">
<div id="post-82394-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll have a look, but I have to check how can I convert my csv file to geoJSON.</p>
</div>
<div id="comment-82394-info" class="comment-info">
<span class="comment-age">(27 Oct '21, 21:40)</span> <span class="comment-user userinfo">sebkramm</span>
</div>
</div>
<span id="82395"></span>
<div id="comment-82395" class="comment">
<div id="post-82395-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can also try if _umap_options can be passed as a csv column somehow.</p>
</div>
<div id="comment-82395-info" class="comment-info">
<span class="comment-age">(28 Oct '21, 07:36)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="82410"></span>
<div id="comment-82410" class="comment">
<div id="post-82410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for you suggestion. Tried this: <a href="https://pastebin.com/WezLpauz">https://pastebin.com/WezLpauz</a> =&gt; no result...</p>
</div>
<div id="comment-82410-info" class="comment-info">
<span class="comment-age">(29 Oct '21, 13:44)</span> <span class="comment-user userinfo">sebkramm</span>
</div>
</div>
</div>
<div id="comment-tools-82391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82391-form-container" class="comment-form-container">
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

