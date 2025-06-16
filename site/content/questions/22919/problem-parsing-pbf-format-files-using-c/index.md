+++
type = "question"
title = "Problem parsing PBF format files using C#"
description = '''Hi - I&#x27;m using the code sample here: http://stackoverflow.com/questions/4663298/protobuf-net-deserialize-open-street-maps To parse a sample osm.pbf export. I generated C# classes from the .proto definitions here: https://github.com/scrosby/OSM-binary/blob/master/src/ using the protogen util associat...'''
date = "2013-05-31T15:09:00Z"
lastmod = "2013-08-10T18:11:00Z"
weight = 22919
keywords = [ "c#", "pbf" ]
aliases = [ "/questions/22919" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem parsing PBF format files using C#](/questions/22919/problem-parsing-pbf-format-files-using-c)

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
<span id="post-22919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22919-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi - I'm using the code sample here:</p>
<p><a href="http://stackoverflow.com/questions/4663298/protobuf-net-deserialize-open-street-maps">http://stackoverflow.com/questions/4663298/protobuf-net-deserialize-open-street-maps</a></p>
<p>To parse a sample osm.pbf export. I generated C# classes from the .proto definitions here:</p>
<p><a href="https://github.com/scrosby/OSM-binary/blob/master/src/">https://github.com/scrosby/OSM-binary/blob/master/src/</a></p>
<p>using the protogen util associated with protobuf-net</p>
<p>The code runs and I can see valid looking data in the string table for each PrimitiveBlock instance. However, the PrimitiveGroup list always has a single item which is unpopulated (e.g. no nodes, ways, relations etc.).</p>
<p>I'm using a sample data file from here:</p>
<p><a href="http://download.geofabrik.de/europe.html">http://download.geofabrik.de/europe.html</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '13, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/b3b3625faddae3ba07ac6eda27abac96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simonthorogood&#39;s gravatar image" />
<p><span>simonthorogood</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simonthorogood has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22919" class="comments-container">
<span id="22933"></span>
<div id="comment-22933" class="comment">
<div id="post-22933-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A very developer-y question that might perhaps yield better/more responses if posted to the dev mailing list, see lists.openstreetmap.org.</p>
</div>
<div id="comment-22933-info" class="comment-info">
<span class="comment-age">(31 May '13, 22:20)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22919-form-container" class="comment-form-container">
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

<span id="25172"></span>

<div id="answer-container-25172" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25172-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have found an answer you should post it; this isn't a direct answer, but may contain information which would help others who are trying to read PBF.</p>
<p>I translated the <a href="https://wiki.openstreetmap.org/wiki/PBF">PBF Format</a> into <a href="https://gist.github.com/JesseKPhillips/6051600">D code</a>. I then wrote up a <a href="http://he-the-great.livejournal.com/46498.html">blog series</a> to detail what I went through. I believe that D is clean enough that those familiar with C syntax can easily understand how PBF is laid out (if not, let me know so I can correct that belief). Hope this helps someone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '13, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-25172" class="comments-container">
&#10;</div>
<div id="comment-tools-25172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25172-form-container" class="comment-form-container">
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

