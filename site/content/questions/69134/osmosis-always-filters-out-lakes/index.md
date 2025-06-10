+++
type = "question"
title = "Osmosis always filters out lakes"
description = '''Hi, I&#x27;m trying to create a .pbf file with only water (Coastlines, rivers, streams, lakes). I&#x27;m using the following with perfect results except none of the lakes come through: osmosis --rbf file.osm.pbf outPipe.0=1 --wkv keyValueList=natural.coastline,natural.water,waterway.river,waterway.riverbank,w...'''
date = "2019-05-08T22:02:00Z"
lastmod = "2019-05-09T17:54:00Z"
weight = 69134
keywords = [ "water", "natural", "lakes", "osmosis", "wkv" ]
aliases = [ "/questions/69134" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis always filters out lakes](/questions/69134/osmosis-always-filters-out-lakes)

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
<span id="post-69134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69134-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm trying to create a .pbf file with only water (Coastlines, rivers, streams, lakes). I'm using the following with perfect results except none of the lakes come through:</p>
<p>osmosis --rbf file.osm.pbf outPipe.0=1 --wkv keyValueList=natural.coastline,natural.water,waterway.river,waterway.riverbank,waterway.stream,water.lake inPipe.0=1 outPipe.0=2 --tf reject-relations inPipe.0=2 outPipe.0=3 --used-nodes inPipe.0=3 outPipe.0=4 --wb file=filewater.osm.pbf inPipe.0=4</p>
<p>I'm running Osmosis version 0.47 on Windows 10 with Java 8 (update 211). I've tried many variation on the keyValueList and no matter what I try, the lakes won't pass through. I've been working on this for days and haven't been able to figure things out; any help would be greatly appreciated. btw, the file I'm starting with has the lakes in it, with natural=water, and water=lake in the keyValues tags.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-natural" rel="tag" title="see questions tagged &#39;natural&#39;">natural</span> <span class="post-tag tag-link-lakes" rel="tag" title="see questions tagged &#39;lakes&#39;">lakes</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-wkv" rel="tag" title="see questions tagged &#39;wkv&#39;">wkv</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '19, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/f0727be5ba3a840fbc2c2f4edaa7ae8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmoore45&#39;s gravatar image" />
<p><span>dmoore45</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmoore45 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 May '19, 22:05</strong> </span></p>
</div>
</div>
<div id="comments-container-69134" class="comments-container">
<span id="69141"></span>
<div id="comment-69141" class="comment">
<div id="post-69141-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You are rejecting relations: most larger waterbodies will be mapped as such. I would suggest perhaps using osmfilter which provides a less complicated way of doing this.</p>
</div>
<div id="comment-69141-info" class="comment-info">
<span class="comment-age">(09 May '19, 13:33)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="69146"></span>
<div id="comment-69146" class="comment">
<div id="post-69146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>SK53, I have run the same command with --tf accept-relations, and also leaving accept/reject out altogether. I get the same result: lakes are gone.</p>
<p>Thanks for the suggestion on osmfilter. I'll play with that to see if I can get it to work. I appreciate your help!</p>
</div>
<div id="comment-69146-info" class="comment-info">
<span class="comment-age">(09 May '19, 17:54)</span> <span class="comment-user userinfo">dmoore45</span>
</div>
</div>
</div>
<div id="comment-tools-69134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69134-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

