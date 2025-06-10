+++
type = "question"
title = "Solution to use OFFLINE maps with JOSM"
description = '''I have found a way to use downloaded maps from http://download.geofabrik.de/ and then split them up with SPLITTER.jar from http://www.mkgmap.org.uk/download/splitter.html I use this PC COMMAND: java -Xmx1024m -Xms1024m -ea -jar &#92;MKGMAP&#92;splitter-r429&#92;splitter.jar --max-nodes=1400000 -- handle-element...'''
date = "2016-03-02T17:00:00Z"
lastmod = "2016-03-03T07:57:00Z"
weight = 48457
keywords = [ "josm", "offline", "maps" ]
aliases = [ "/questions/48457" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Solution to use OFFLINE maps with JOSM](/questions/48457/solution-to-use-offline-maps-with-josm)

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
<span id="post-48457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48457-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have found a way to use downloaded maps from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> and then split them up with SPLITTER.jar from <a href="http://www.mkgmap.org.uk/download/splitter.html">http://www.mkgmap.org.uk/download/splitter.html</a></p>
<p>I use this PC COMMAND:</p>
<p>java -Xmx1024m -Xms1024m -ea -jar \MKGMAP\splitter-r429\splitter.jar --max-nodes=1400000 -- handle-element-version=keep --mapid="12340000" --geonames-file=\MKGMAP\cities15000.zip --description=mymap --max-areas="255" --no-trim --status-freq="600" michigan-latest.osm.pbf</p>
<p>This makes several smaller .osm.pbf maps about 11MB each. You can use these to open in JOSM and do you work and then upload your changes to OSM when you are back online.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '16, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/aaf8869d4cd5c92ca9831ebf99b07eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregcrago&#39;s gravatar image" />
<p><span>gregcrago</span><br />
<span class="score" title="69 reputation points">69</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregcrago has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48457" class="comments-container">
<span id="48463"></span>
<div id="comment-48463" class="comment">
<div id="post-48463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is your question?</p>
</div>
<div id="comment-48463-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 17:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48464"></span>
<div id="comment-48464" class="comment">
<div id="post-48464-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I would personally avoid uploading anything from a splitter-created file unless you first synchronize the file with the online database. Splitter will chop ways and relations at tile boundaries, and those changes probably shouldn't be uploaded.</p>
</div>
<div id="comment-48464-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 18:59)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-48457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48457-form-container" class="comment-form-container">
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

<span id="48470"></span>

<div id="answer-container-48470" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48470-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree alester, splitter will chop ways and relations at boundaries, but this is a good way to work off line and have relatively new maps to work on Interior objects. If you need to work at the 'edges', then this might cause a problem.</p>
<p>I agree that this IS NOT A QUESTION. Where do you INFORM other JOSM users of new techniques that might be able to help out other users in similar situitations? (Wanting to work off line with OSM maps?)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '16, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/aaf8869d4cd5c92ca9831ebf99b07eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregcrago&#39;s gravatar image" />
<p><span>gregcrago</span><br />
<span class="score" title="69 reputation points">69</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregcrago has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48470" class="comments-container">
<span id="48471"></span>
<div id="comment-48471" class="comment">
<div id="post-48471-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If it's an answer to one of your previous questions, you could always add it there. You won't be able to accept your own answer, but if you say something like "I found the answer and it's this..." a moderator might come along and mark it as an accepted answer.</p>
</div>
<div id="comment-48471-info" class="comment-info">
<span class="comment-age">(02 Mar '16, 21:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48473"></span>
<div id="comment-48473" class="comment">
<div id="post-48473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is perfectly fine to ask a question and answer it yourself.</p>
</div>
<div id="comment-48473-info" class="comment-info">
<span class="comment-age">(03 Mar '16, 07:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48470-form-container" class="comment-form-container">
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

