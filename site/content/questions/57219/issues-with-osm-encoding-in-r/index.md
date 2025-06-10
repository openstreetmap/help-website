+++
type = "question"
title = "Issues with OSM encoding in r"
description = '''I am having troubles with the encoding of the osm data in R. Here is a reproducible example using the osmar package: osmData &amp;lt;- osmar::get_osm(osmar::center_bbox(23.334360, 42.693180, 100, 100)) osmData$nodes$tags[80:100, ] #the output is not UTF-8  I have also downloaded a planet file from https...'''
date = "2017-07-21T09:10:00Z"
lastmod = "2017-07-24T08:54:00Z"
weight = 57219
keywords = [ "osmar", "r", "encoding" ]
aliases = [ "/questions/57219" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Issues with OSM encoding in r](/questions/57219/issues-with-osm-encoding-in-r)

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
<span id="post-57219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57219-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am having troubles with the encoding of the osm data in R. Here is a reproducible example using the osmar package:</p>
<pre><code>osmData &lt;- osmar::get_osm(osmar::center_bbox(23.334360, 42.693180, 100, 100))
osmData$nodes$tags[80:100, ] #the output is not UTF-8</code></pre>
<p>I have also downloaded a planet file from <a href="https://download.geofabrik.de/europe/.">https://download.geofabrik.de/europe/.</a> The filename is "bulgaria-latest.osm.bz2".</p>
<p>After unzipping it, installing osmosis, and reading the file with <em>osmar::get_osm(source = osmsource_osmosis(fileName))</em> I still have the same issue. The cyrilics letters are not readable.</p>
<p>I am using a 64bit Windows 10 with R version 3.3.3. My default encoding is Bulgarian, but I have also tried English encoding in R with no help.</p>
<p>Any ideas how can I counter this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmar" rel="tag" title="see questions tagged &#39;osmar&#39;">osmar</span> <span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span> <span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '17, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/15590012de284a8b83ca707eff81f212?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deann88&#39;s gravatar image" />
<p><span>deann88</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deann88 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-57219" class="comments-container">
<span id="57220"></span>
<div id="comment-57220" class="comment">
<div id="post-57220-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>crossposted: <a href="https://stackoverflow.com/questions/45215553/issues-with-osm-encoding">https://stackoverflow.com/questions/45215553/issues-with-osm-encoding</a> + <a href="https://gis.stackexchange.com/questions/248440/issues-with-osm-encoding">https://gis.stackexchange.com/questions/248440/issues-with-osm-encoding</a></p>
</div>
<div id="comment-57220-info" class="comment-info">
<span class="comment-age">(21 Jul '17, 10:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="57223"></span>
<div id="comment-57223" class="comment">
<div id="post-57223-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect this is an issue you need to raise with the osmar package owner or R forums rather than here.</p>
</div>
<div id="comment-57223-info" class="comment-info">
<span class="comment-age">(21 Jul '17, 13:18)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="57224"></span>
<div id="comment-57224" class="comment">
<div id="post-57224-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have raised it to several places where people have worked with OSM as <a href="https://help.openstreetmap.org/users/158/scai">@scai</a> pointed out. It is not package specific issue as I have tried it and it works in ubuntu. It is something connected with Windows locale and I am looking for a solution.</p>
</div>
<div id="comment-57224-info" class="comment-info">
<span class="comment-age">(21 Jul '17, 13:22)</span> <span class="comment-user userinfo">deann88</span>
</div>
</div>
<span id="57227"></span>
<div id="comment-57227" class="comment">
<div id="post-57227-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's likely the issue is in the R console you are using. You could isolate whether it has anything to do with OSM and/or osmar by creating a simple test file and loading it with read.table.</p>
<p>Something like</p>
<pre><code>col1, col2
Стадион, Левски</code></pre>
<p>should be sufficient.</p>
</div>
<div id="comment-57227-info" class="comment-info">
<span class="comment-age">(21 Jul '17, 15:35)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-57219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57219-form-container" class="comment-form-container">
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

<span id="57241"></span>

<div id="answer-container-57241" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57241-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ok, Answering my own question:</p>
<p>I ran the above code in linux and understood that the issue was with the windows locale. The workaround I found was to use iconv with <em>from</em> and <em>to</em> parameters set to <em>"UTF-8"</em>.</p>
<pre><code>iconv(osmData$nodes$tags[80:100,3][11], from=&quot;UTF-8&quot;, to=&quot;UTF-8&quot;)</code></pre>
<p>This works and could be applied to all columns.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '17, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/15590012de284a8b83ca707eff81f212?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deann88&#39;s gravatar image" />
<p><span>deann88</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deann88 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-57241" class="comments-container">
&#10;</div>
<div id="comment-tools-57241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57241-form-container" class="comment-form-container">
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

