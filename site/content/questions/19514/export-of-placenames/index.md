+++
type = "question"
title = "Export of Placenames?"
description = '''I&#x27;ve done some looking around but can&#x27;t figure out if this is possible: I need a file of placenames in the UK along with their lat/lng. Similar to this: http://wiki.openstreetmap.org/wiki/List_of_London_Underground_stations Does such a thing exist? Chris.'''
date = "2013-02-01T16:15:00Z"
lastmod = "2013-02-04T08:53:00Z"
weight = 19514
keywords = [ "export" ]
aliases = [ "/questions/19514" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Export of Placenames?](/questions/19514/export-of-placenames)

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
<span id="post-19514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19514-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've done some looking around but can't figure out if this is possible:</p>
<p>I need a file of placenames in the UK along with their lat/lng. Similar to this:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/List_of_London_Underground_stations">http://wiki.openstreetmap.org/wiki/List_of_London_Underground_stations</a></p>
<p>Does such a thing exist?</p>
<p>Chris.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '13, 16:15</strong></p>
<img src="https://secure.gravatar.com/avatar/8c74f089c047244a08303867c921a833?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris1970&#39;s gravatar image" />
<p><span>Chris1970</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris1970 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19514" class="comments-container">
&#10;</div>
<div id="comment-tools-19514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19514-form-container" class="comment-form-container">
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

<span id="19568"></span>

<div id="answer-container-19568" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19568-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As an example, here's what I did when I wanted all the railway stations in mainland GB. You'll need to think about what "<code>place=</code>" items you want to keep and amend accordingly. If you want Northern Ireland as well, then you'll need to include some from an Irish extract too - it might be worth asking another question about that.</p>
<pre><code>1) osmconvert great_britain.osm.pbf -o=great_britain.o5m
&#10;2) osmfilter great_britain.o5m --keep=&quot;railway=station&quot; &gt; stations.osm
&#10;3) osmconvert stations.osm --all-to-nodes --csv=&quot;@id @lat @lon railway name&quot; --csv=headline &gt; stations.txt
&#10;4) Open stations.txt in your spreadsheet program of choice, and remove lines that don&#39;t have &quot;station&quot; in column D</code></pre>
<p>Step (1) is needed because osmfilter doesn't understand pbf (protobuf format) files. You could process as a raw .osm file, but it'd be much bigger.</p>
<p>Step (4) is a sanity check to get rid of a few bits and pieces.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '13, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-19568" class="comments-container">
&#10;</div>
<div id="comment-tools-19568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19568-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19567"></span>

<div id="answer-container-19567" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19567-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm afraid this probably doesn't readily exist. But for sure it is possible to generate this, although this require the use of more advanced techniques. I could imagine two different approaches:</p>
<p><strong>Filter the data locally from downloaded data</strong></p>
<p>First you have to get the country extract for the UK e.g. from <a href="http://download.geofabrik.de/openstreetmap/europe/">Geofabrik</a>. Also you have to get <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> and familiarize yourself with the usage. Osmosis allows you to extract all place nodes, use something like <code>--tag-filter accept-nodes place=*</code>. This gives you an XML file containing the information, you will have to reformat it somehow to get the list you're looking for.</p>
<p><strong>Use <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> to get the data</strong></p>
<p>Overpass API allows you to do the filtering directly. Here you'll have to use something like <code>&amp;lt; has-kv k="place" /&amp;gt;</code>. But doing so for all places in the UK might be a bit to large of an request. For an easier interface you could have a look at <a href="http://overpass-turbo.eu/">overpass turbo</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '13, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c79367c8f07471873499bb9e54a3c427?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ohr&#39;s gravatar image" />
<p><span>Ohr</span><br />
<span class="score" title="101 reputation points">101</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ohr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19567" class="comments-container">
&#10;</div>
<div id="comment-tools-19567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19567-form-container" class="comment-form-container">
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

