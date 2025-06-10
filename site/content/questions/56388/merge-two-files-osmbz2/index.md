+++
type = "question"
title = "Merge two files .osm.bz2"
description = '''Hello, i installed my own overpass API server. Today i only work with French country data and everything is ok. I would like to add the Canada but i don&#x27;t know how to do that. I tried to merge two .osm files with osmconvert64 but i&#x27;ve got an error : unexpected end of file in france-latest.osm. Do yo...'''
date = "2017-05-31T08:10:00Z"
lastmod = "2017-08-01T18:21:00Z"
weight = 56388
keywords = [ "overpass-api" ]
aliases = [ "/questions/56388" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Merge two files .osm.bz2](/questions/56388/merge-two-files-osmbz2)

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
<span id="post-56388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56388-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, i installed my own overpass API server. Today i only work with French country data and everything is ok. I would like to add the Canada but i don't know how to do that. I tried to merge two .osm files with osmconvert64 but i've got an error : unexpected end of file in france-latest.osm. Do you have a good method to do that ?</p>
<p>Thanks for all</p>
<p>Mathieu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '17, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb03db977326117a75fb9a84b79f3e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdk83&#39;s gravatar image" />
<p><span>mdk83</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdk83 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56388" class="comments-container">
<span id="57416"></span>
<div id="comment-57416" class="comment">
<div id="post-57416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello guys, sorry for my late answer but i couldn't test before. Thank you very much for your answer it works wonderfully !!</p>
<p>thank you for everything !</p>
<p>Mathieu</p>
</div>
<div id="comment-57416-info" class="comment-info">
<span class="comment-age">(01 Aug '17, 18:21)</span> <span class="comment-user userinfo">mdk83</span>
</div>
</div>
</div>
<div id="comment-tools-56388" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56388-form-container" class="comment-form-container">
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

<span id="56398"></span>

<div id="answer-container-56398" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56398-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://osmcode.org/osmium-tool/">Osmium</a> can merge two OSM files: <code>osmium merge file1.osm file2.osm -o merged.osm</code>. Osmium can read and write any OSM file format. I recommend you use PBF format for best performance. Make sure to use files that are extracted from the same planet file (for instance Geofabrik extracts). Do not use files from different points in time, otherwise you might get wierd effects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '17, 06:58</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-56398" class="comments-container">
&#10;</div>
<div id="comment-tools-56398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56398-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56412"></span>

<div id="answer-container-56412" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56412-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In your specific use case, you could also just import one file after another into the same directory, i.e. run</p>
<pre><code>bunzip2 &lt;$FIRST_FILE | $EXEC_DIR/bin/update_database --db-dir=$DB_DIR/ --meta
bunzip2 &lt;$SECOND_FILE | $EXEC_DIR/bin/update_database --db-dir=$DB_DIR/ --meta</code></pre>
<p>If there is conflicting data then the data from the last file wins.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '17, 06:52</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-56412" class="comments-container">
&#10;</div>
<div id="comment-tools-56412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56412-form-container" class="comment-form-container">
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

