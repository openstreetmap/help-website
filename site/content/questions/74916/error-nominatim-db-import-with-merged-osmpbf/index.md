+++
type = "question"
title = "Error Nominatim DB import with merged .osm.pbf"
description = '''Hello, I&#x27;m trying to create a Nominatim DB with data for the US and Europe. I looked around for a merged PBF but couldn&#x27;t find one, so I created a merge myself using osmconvert. I tried two ways of doing this after the import failed with the first, just in case: 1. osmconvert us-latest.osm.pbf --out...'''
date = "2020-05-19T23:58:00Z"
lastmod = "2020-05-20T15:19:00Z"
weight = 74916
keywords = [ "import", "nominatim", "pbf", "merge" ]
aliases = [ "/questions/74916" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Error Nominatim DB import with merged .osm.pbf](/questions/74916/error-nominatim-db-import-with-merged-osmpbf)

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
<span id="post-74916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74916-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to create a Nominatim DB with data for the US and Europe. I looked around for a merged PBF but couldn't find one, so I created a merge myself using <code>osmconvert</code>. I tried two ways of doing this after the import failed with the first, just in case:</p>
<p>1. <code>osmconvert us-latest.osm.pbf --out-o5m | osmconvert - europe-latest.osm.pbf -o=us-europe-merge.pbf</code></p>
<p>2. <code>osmconvert us-latest.osm.pbf -o="us-latest.o5m" osmconvert europe-latest.osm.pbf -o="europe-latest.o5m" osmconvert us-latest.o5m europe-latest.o5m -o="us-europe-merge.o5m" osmconvert us-europe-merge.o5m -o="us-europe-merge.osm.pbf"</code></p>
<p>In both cases, I get the same error: <code>PHP Notice: Undefined variable: aCMDResult in /app/src/lib/setup_functions.php on line 14 ERROR: osm-file "" not readable string(24) "osm-file "" not readable</code></p>
<p>The original .osm.pbf files are downloaded from Geofabrik. I should also note that I've successfully run the import with the same setup using the individual us-latest.osm.pbf file.</p>
<p>Is there something wrong with the merge? Should I create it some other way? Any ideas are welcome.</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '20, 23:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ede0a84ad576e5a6dc3b1b650869aa6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shai&#39;s gravatar image" />
<p><span>Shai</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74916" class="comments-container">
&#10;</div>
<div id="comment-tools-74916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74916-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="74931"></span>

<div id="answer-container-74931" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Shai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(The jQuery javascript library on help.osm.org sometimes doesn't load, it's infuriating. There are already github tickets open about this.)</p>
<p>When I look at <a href="https://github.com/osm-search/Nominatim/blob/master/lib/setup_functions.php">https://github.com/osm-search/Nominatim/blob/master/lib/setup_functions.php</a> it looks more like your file exists, but can't be read due to file permissions? Or maybe it's 0 byte size? The <code>is_readable</code> is standard PHP, similar to <code>test -r</code> in bash.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '20, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74931" class="comments-container">
<span id="74932"></span>
<div id="comment-74932" class="comment">
<div id="post-74932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That was it <a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>! Permissions. The merge was created without read permissions for some reason. Thank you.</p>
</div>
<div id="comment-74932-info" class="comment-info">
<span class="comment-age">(20 May '20, 15:19)</span> <span class="comment-user userinfo">Shai</span>
</div>
</div>
</div>
<div id="comment-tools-74931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74931-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74922"></span>

<div id="answer-container-74922" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74922-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="https://osmcode.org/osmium-tool/">Osmium</a> to <a href="https://docs.osmcode.org/osmium/latest/osmium-merge.html">merge</a> one or more OSM files more easily: <code>osmium merge -o all.osm.pbf file1.osm.pbf file2.osm.pbf ...</code></p>
<p>The important thing to remember with any kind of merging like this is that you <strong>must</strong> have files that come from the exact same point in time. If you have one extract from today and another from yesterday, chances are you get different versions of the same object in the output which Nominatim (or most other programs) will not be able to cope with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '20, 07:58</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-74922" class="comments-container">
<span id="74930"></span>
<div id="comment-74930" class="comment">
<div id="post-74930-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Jochen, I came across Osmium but had trouble installing it on the AWS machine I'm using, so I stuck with osmconvert. I'll try installing it again. As for merging files coming from the exact same point in time, is that even possible when using different extracts like this? Or should I try to use two extracts that are as close to being from the same time as possible? I'd expect it not to matter for regions as disjoint as the US and Europe though.</p>
<p>mtmail, thank you, I'll check out that script. From what I gather, it overall runs the same procedure I did manually, except for the creation of that sequence.state file. Could that be breaking the import?</p>
<p>Sorry by the way, I tried to comment on your individual comments but wasn't able to.</p>
</div>
<div id="comment-74930-info" class="comment-info">
<span class="comment-age">(20 May '20, 14:32)</span> <span class="comment-user userinfo">Shai</span>
</div>
</div>
</div>
<div id="comment-tools-74922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74922-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74925"></span>

<div id="answer-container-74925" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the development branch of Nominatim documentation there's also an update script to deal with multiple countries and how to keep them updated. <a href="http://nominatim.org/release-docs/develop/admin/Advanced-Installations/">http://nominatim.org/release-docs/develop/admin/Advanced-Installations/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '20, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74925" class="comments-container">
&#10;</div>
<div id="comment-tools-74925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74925-form-container" class="comment-form-container">
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

