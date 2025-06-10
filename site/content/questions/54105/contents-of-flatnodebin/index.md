+++
type = "question"
title = "Contents of flatnode.bin?"
description = '''Hi all, I&#x27;m fairly new to OSM so I was hoping to get some guidance. I&#x27;m looking to speed up the process of the import of planet-latest.osm.pbf. It failed due to disk space but now that I allocated another TB of storage I was looking to speed up the process so I&#x27;m not waiting 2 weeks again. I stumble...'''
date = "2017-01-17T16:24:00Z"
lastmod = "2017-01-17T16:59:00Z"
weight = 54105
keywords = [ "flatnode" ]
aliases = [ "/questions/54105" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Contents of flatnode.bin?](/questions/54105/contents-of-flatnodebin)

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
<span id="post-54105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54105-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm fairly new to OSM so I was hoping to get some guidance.</p>
<p>I'm looking to speed up the process of the import of planet-latest.osm.pbf. It failed due to disk space but now that I allocated another TB of storage I was looking to speed up the process so I'm not waiting 2 weeks again.</p>
<p>I stumbled across the --flat-node flag but I'm unsure what is supposed to go inside the flatnode.bin file. Any guidance would be greatly appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-flatnode" rel="tag" title="see questions tagged &#39;flatnode&#39;">flatnode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '17, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/7e15a6fef91f6e39d22fcd6873a5d835?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jhollingsworth&#39;s gravatar image" />
<p><span>jhollingsworth</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jhollingsworth has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54105" class="comments-container">
<span id="54106"></span>
<div id="comment-54106" class="comment">
<div id="post-54106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At the risk of playing Captain Obvious here - you have got the whole process working end to end with a smaller file already haven't you? It'd be terrible to hit a snag and have to wait 2 weeks again...</p>
</div>
<div id="comment-54106-info" class="comment-info">
<span class="comment-age">(17 Jan '17, 16:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="54107"></span>
<div id="comment-54107" class="comment">
<div id="post-54107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To a point. I ran central America and Australia and all of the render scripts and only Australia would show the borders and actually render. So I was hoping to run planet-latest to just get the whole file rather than the broken up files (if that makes sense).</p>
<p>edit: also Europe and the North America also takes about a week would if I did end up going that route I would still like to get flat-node figured out so I can use it for those two as well :)</p>
</div>
<div id="comment-54107-info" class="comment-info">
<span class="comment-age">(17 Jan '17, 16:32)</span> <span class="comment-user userinfo">jhollingsworth</span>
</div>
</div>
</div>
<div id="comment-tools-54105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54105-form-container" class="comment-form-container">
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

<span id="54113"></span>

<div id="answer-container-54113" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using the flatnode file will give you a performance speedup an almost every case, especially if you don't have SSD storage. It will also save about 80 GB of storage if you load a full planet, however if you do something like "Africa only" you'll likely waste some space. The file contains what would normally be in the <code>planet_osm_nodes</code> database table and the file can be read with the <code>nodecachefilereader</code> utility if desired. It is however not a standard data format, and only used by osm2pgsql. Also note that <a href="https://github.com/openstreetmap/osm2pgsql/pull/668">the format of the file has recently changed.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '17, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54113" class="comments-container">
&#10;</div>
<div id="comment-tools-54113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54113-form-container" class="comment-form-container">
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

