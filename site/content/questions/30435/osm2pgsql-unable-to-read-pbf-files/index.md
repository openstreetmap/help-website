+++
type = "question"
title = "OSM2PGSQL unable to read .pbf files"
description = '''Hi, I have installed osm2pgsql with all required dependencies (according to https://wiki.openstreetmap.org/wiki/Osm2pgsql), but when reading a .pbf file, I&#x27;m getting this message: ERROR: PBF support has not been compiled into this version of osm2pgsql, please either compile it with pbf support or use...'''
date = "2014-02-04T10:10:00Z"
lastmod = "2014-12-08T01:06:00Z"
weight = 30435
keywords = [ "pbf", "osm2pgsql" ]
aliases = [ "/questions/30435" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM2PGSQL unable to read .pbf files](/questions/30435/osm2pgsql-unable-to-read-pbf-files)

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
<span id="post-30435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30435-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have installed osm2pgsql with all required dependencies (according to <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql),">https://wiki.openstreetmap.org/wiki/Osm2pgsql),</a> but when reading a .pbf file, I'm getting this message:</p>
<pre><code>ERROR: PBF support has not been compiled into this version of osm2pgsql, please either compile it with pbf support or use one of the other input formats</code></pre>
<p>My version of osm2pgsql is 0.85.0, so I think it's supposed to read .pbf. Is there anything I can do about it?</p>
<p>EDIT: OK, already solved - I've made some reinstalls, I've also tried some older versions, so I don't know what exactly caused this issue, but now everything, works fine.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '14, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/6a96ed96e98be951c872daa097cc1c26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Speeder1612&#39;s gravatar image" />
<p><span>Speeder1612</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Speeder1612 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '14, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-30435" class="comments-container">
<span id="39128"></span>
<div id="comment-39128" class="comment">
<div id="post-39128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi can you tell me where did you get the older version of osm2pgsql? My osm2pgsql is 0.87.0 and it doesn't work either. Thank you!</p>
</div>
<div id="comment-39128-info" class="comment-info">
<span class="comment-age">(08 Dec '14, 01:06)</span> <span class="comment-user userinfo">studiousdavid</span>
</div>
</div>
</div>
<div id="comment-tools-30435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30435-form-container" class="comment-form-container">
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

<span id="30436"></span>

<div id="answer-container-30436" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30436-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you read the part of the instructions where it says:</p>
<pre><code>If you want PBF read support, you will also need libprotobuf-c0-dev and protobuf-c-compiler:
sudo apt-get install libprotobuf-c0-dev protobuf-c-compiler</code></pre>
<p>osm2pgsql will compile if the protobuf dependencies are not met, and simply issue a warning that is overlooked easily. The result is an osm2pgsql binary without PBF support.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '14, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30436" class="comments-container">
<span id="30437"></span>
<div id="comment-30437" class="comment">
<div id="post-30437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I have - this is why I don't understand why it doesn't work.</p>
</div>
<div id="comment-30437-info" class="comment-info">
<span class="comment-age">(04 Feb '14, 10:33)</span> <span class="comment-user userinfo">Speeder1612</span>
</div>
</div>
<span id="30439"></span>
<div id="comment-30439" class="comment">
<div id="post-30439-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Then take a look at the output of <code>./configure</code> which is run via the <code>autogen.sh</code> script.</p>
</div>
<div id="comment-30439-info" class="comment-info">
<span class="comment-age">(04 Feb '14, 11:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30436-form-container" class="comment-form-container">
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

