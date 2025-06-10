+++
type = "question"
title = "Right way of setting minimum and maximum zoom level for OSMdroid"
description = '''I have tried setting this in my codes to set the minimum and maximum zoom levels for viewing on the android platform: MyTileSource myTiles = new MyTileSource( &quot;&quot; + tID, null, 14, 16, 256, &quot;.png&quot;);  This is an example of what I&#x27;ve done to try and limit the zoom levels between 14 and 16. From this que...'''
date = "2013-01-31T15:56:00Z"
lastmod = "2013-01-31T15:56:00Z"
weight = 19496
keywords = [ "zoomlevel", "osmdroid", "zoom" ]
aliases = [ "/questions/19496" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Right way of setting minimum and maximum zoom level for OSMdroid](/questions/19496/right-way-of-setting-minimum-and-maximum-zoom-level-for-osmdroid)

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
<span id="post-19496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19496-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have tried setting this in my codes to set the minimum and maximum zoom levels for viewing on the android platform:</p>
<pre><code>MyTileSource myTiles = new MyTileSource( &quot;&quot; + tID, null, 14, 16, 256, &quot;.png&quot;);</code></pre>
<p>This is an example of what I've done to try and limit the zoom levels between 14 and 16.</p>
<p>From this <a href="http://stackoverflow.com/questions/6773480/android-osm-droid-set-max-zoom-level">question</a>, I understand that there is a work around which is to manually edit the files in the package.</p>
<p>However, I currently have 2 different MapView activities catered for different viewing, thus I am unable to define a global settings in the library package file. What should be the right way to get the above codes to work in setting the minimum/maximum zoom?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '13, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/8e2f3652fadd1fc58cbd9780977ab5d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lyk&#39;s gravatar image" />
<p><span>lyk</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lyk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19496" class="comments-container">
&#10;</div>
<div id="comment-tools-19496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19496-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

